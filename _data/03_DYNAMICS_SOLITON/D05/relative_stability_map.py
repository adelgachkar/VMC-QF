#!/usr/bin/env python3
"""
Relative-stability map: defect/null coherence-lifetime ratio as a function of gamma.

Question (D05 Record Vault-11, qualification (i)): the "defect at least doubles
the lifetime" criterion was confirmed at the single reference gamma = 0.1. How
does R(gamma) = tau_life(defect)/tau_life(null) behave across the full sweep
range gamma in [0.01, 0.50]?

Lifetime definition (registered battery): first tau at which mean link coherence
crosses below EPS = 1e-3; right-censored at tau = 100 if no crossing (rows
flagged, excluded from ratio fits).

GRID-LIMITATION REMOVAL: the cadence grid is tau = 0.5, so raw crossing taus
are coarse multiples of 0.5 and R becomes a quotient of two coarse integers
(visible as banding in the raw map). Two sub-grid estimators are added:
  * Linear  : linear interpolation of the coherence trace to the exact EPS
              crossing; primary estimator.
  * Loglinear: linear interpolation of log(coherence) (exponential-locally
              assumption); secondary cross-check.
All three estimators are registered side by side; conclusions must survive the
estimator choice.

Engines: the exact closed 6x6 block engine of simulate_D05_cptp
(block==full verified to ~1e-13). Null-engine equivalence of the site and
edge-phase defects on the S-01 initial state is asserted numerically at
gamma = 0.1 and 0.25.

Outputs (next to this script):
  D05_relative_stability_map.csv        raw + interpolated rows for all three
                                        estimators
  D05_relative_stability_map.png        two-panel figure (raw + interpolated)
  relative_stability_output.txt         full log
"""
import csv
import importlib
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

m = importlib.import_module("simulate_D05_cptp")

GAMMAS = m.GAMMA_SWEEP
EPS = m.EPS
DT = m.DT
TAU_MAX = 100.0


def life_raw(rows):
    for r in rows:
        if r["mean_edge_coherence"] < EPS:
            return r["tau"]
    return None


def _interp_to_eps(vals, taus, mode):
    """Find the tau where the trace crosses EPS between the bracketing samples."""
    for k in range(1, len(vals)):
        a, b = vals[k - 1], vals[k]
        if a >= EPS > b:
            if mode == "linear":
                frac = (a - EPS) / (a - b)
            else:  # loglinear
                la, lb = math.log(a), math.log(b)
                frac = (la - math.log(EPS)) / (la - lb)
            return taus[k - 1] + frac * (taus[k] - taus[k - 1])
    return None


def life_interp(rows, mode):
    taus = [r["tau"] for r in rows]
    vals = [r["mean_edge_coherence"] for r in rows]
    t = _interp_to_eps(vals, taus, mode)
    return t


def main():
    # ---- null-engine equivalence check ----
    for g in (0.1, 0.25):
        base = life_raw(m.run(False, g, defect="site", n_steps=200))
        alt1 = life_raw(m.run(False, g, defect="edge-phase", n_steps=200))
        print(f"[check] null engine equivalence at gamma={g}: "
              f"site={base} edge-phase={alt1}")
        assert base == alt1

    # ---- three sweeps (run once, evaluate all estimators) ----
    sweeps = {"null": [], "site": [], "edge": []}
    for name, (topo, defect) in {
            "null": (False, "site"), "site": (True, "site"),
            "edge": (True, "edge-phase")}.items():
        print(f"\n== sweep {name} ==")
        for g in GAMMAS:
            sweeps[name].append(m.run(topo, float(g), defect=defect,
                                      n_steps=200))

    # ---- assemble rows: raw + two interpolated estimators ----
    rows = []
    for i, g in enumerate(GAMMAS):
        tn_raw = life_raw(sweeps["null"][i])
        ts_raw = life_raw(sweeps["site"][i])
        te_raw = life_raw(sweeps["edge"][i])
        tn_l = life_interp(sweeps["null"][i], "linear")
        ts_l = life_interp(sweeps["site"][i], "linear")
        te_l = life_interp(sweeps["edge"][i], "linear")
        tn_g = life_interp(sweeps["null"][i], "loglinear")
        ts_g = life_interp(sweeps["site"][i], "loglinear")
        te_g = life_interp(sweeps["edge"][i], "loglinear")

        def ratio(a, b):
            return ("" if (a is None or b is None) else round(a / b, 6))

        rows.append(dict(
            gamma=float(g),
            tau_life_null_raw=("censored>=100" if tn_raw is None else tn_raw),
            tau_life_site_raw=("censored>=100" if ts_raw is None else ts_raw),
            tau_life_edge_raw=("censored>=100" if te_raw is None else te_raw),
            R_site_raw=("" if tn_raw is None or ts_raw is None
                        else round(ts_raw / tn_raw, 6)),
            R_edge_raw=("" if tn_raw is None or te_raw is None
                        else round(te_raw / tn_raw, 6)),
            tau_life_null_lin=(f"{tn_l:.4f}" if tn_l is not None else ""),
            tau_life_site_lin=(f"{ts_l:.4f}" if ts_l is not None else ""),
            tau_life_edge_lin=(f"{te_l:.4f}" if te_l is not None else ""),
            R_site_lin=ratio(ts_l, tn_l), R_edge_lin=ratio(te_l, tn_l),
            tau_life_null_log=(f"{tn_g:.4f}" if tn_g is not None else ""),
            tau_life_site_log=(f"{ts_g:.4f}" if ts_g is not None else ""),
            tau_life_edge_log=(f"{te_g:.4f}" if te_g is not None else ""),
            R_site_log=ratio(ts_g, tn_g), R_edge_log=ratio(te_g, tn_g),
            null_censored=(tn_raw is None),
        ))

    # ---- per-estimator summary: mean ratio in the common uncensored window,
    #      crossing-gamma of the 2.0 line, endpoint contrast (weak vs strong) ----
    def summarize(suffix):
        rs = [(r["gamma"], r[f"R_site_{suffix}"]) for r in rows
              if r[f"R_site_{suffix}"] != ""]
        re = [(r["gamma"], r[f"R_edge_{suffix}"]) for r in rows
              if r[f"R_edge_{suffix}"] != ""]
        s_vals = [v for _, v in rs]
        e_vals = [v for _, v in re]

        def cross(pairs, thr=2.0):
            above = [g for g, v in pairs if v >= thr]
            return above[-1] if above else None

        return dict(
            mean_s=float(np.mean(s_vals)), sd_s=float(np.std(s_vals, ddof=1)),
            mean_e=float(np.mean(e_vals)), sd_e=float(np.std(e_vals, ddof=1)),
            cross_s=cross(rs), cross_e=cross(re),
            w_s=s_vals[:12], w_e=e_vals[:12], s_s=s_vals[-12:], s_e=e_vals[-12:],
            n=len(rs))

    S_lin = summarize("lin")
    S_log = summarize("log")
    S_raw = summarize("raw")

    def mean(x):
        return float(np.mean(x))

    print("\n== estimator comparison (uncensored window, n=%d) ==" % S_lin["n"])
    for tag, S in (("raw  ", S_raw), ("linear", S_lin), ("loglin", S_log)):
        print(f"  {tag}: R_site = {S['mean_s']:.3f} +- {S['sd_s']:.3f} | "
              f"R_edge = {S['mean_e']:.3f} +- {S['sd_e']:.3f} | "
              f"R>=2 up to gamma = {S['cross_s']} / {S['cross_e']}")
    print(f"  endpoint contrast (mean of weakest 12 vs strongest 12 gammas):")
    print(f"    linear : weak {mean(S_lin['w_s']):.3f}/{mean(S_lin['w_e']):.3f}"
          f"   strong {mean(S_lin['s_s']):.3f}/{mean(S_lin['s_e']):.3f}")
    print(f"    loglin : weak {mean(S_log['w_s']):.3f}/{mean(S_log['w_e']):.3f}"
          f"   strong {mean(S_log['s_s']):.3f}/{mean(S_log['s_e']):.3f}")

    # ---- CSV ----
    cols = list(rows[0].keys())
    with open(os.path.join(HERE, "D05_relative_stability_map.csv"), "w",
              newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print("\nCSV written: D05_relative_stability_map.csv")

    # ---- figure ----
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    g = np.array([r["gamma"] for r in rows])

    def arr(suffix, which):
        return np.array([np.nan if r[f"R_{which}_{suffix}"] == ""
                         else float(r[f"R_{which}_{suffix}"]) for r in rows])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 4.8))

    ax1.plot(g, arr("raw", "site"), "s", ms=4, color="tab:blue", alpha=0.45,
             label="site raw (coarse grid)")
    ax1.plot(g, arr("raw", "edge"), "^", ms=4, color="tab:red", alpha=0.45,
             label="edge raw (coarse grid)")
    ax1.plot(g, arr("lin", "site"), "s-", ms=3, color="tab:blue",
             label=r"site, interpolated")
    ax1.plot(g, arr("lin", "edge"), "^-", ms=3, color="tab:red",
             label=r"edge, interpolated")
    ax1.axhline(2.0, color="k", ls="--", lw=1)
    ax1.axhspan(S_lin["mean_s"] - S_lin["sd_s"], S_lin["mean_s"] + S_lin["sd_s"],
                color="tab:blue", alpha=0.10)
    ax1.axhspan(S_lin["mean_e"] - S_lin["sd_e"], S_lin["mean_e"] + S_lin["sd_e"],
                color="tab:red", alpha=0.10)
    ax1.set_ylim(1.2, 2.4)
    ax1.set_xlabel(r"cadence leak $\gamma$")
    ax1.set_ylabel(r"$R(\gamma)$")
    ax1.set_title("Relative-stability map (raw vs interpolated)")
    ax1.legend(fontsize=7)
    ax1.grid(alpha=0.3)

    tn = np.array([np.nan if r["tau_life_null_lin"] == ""
                   else float(r["tau_life_null_lin"]) for r in rows])
    ts = np.array([np.nan if r["tau_life_site_lin"] == ""
                   else float(r["tau_life_site_lin"]) for r in rows])
    te = np.array([np.nan if r["tau_life_edge_lin"] == ""
                   else float(r["tau_life_edge_lin"]) for r in rows])
    ax2.plot(g, tn, "o-", ms=3, color="0.35", label="S-01 null")
    ax2.plot(g, ts, "s-", ms=3, color="tab:blue", label="S-02 site detuning")
    ax2.plot(g, te, "^-", ms=3, color="tab:red", label="S-04 edge-phase flux")
    ax2.set_yscale("log")
    ax2.set_xlabel(r"cadence leak $\gamma$")
    ax2.set_ylabel(r"$\tau_{\rm life}$ (interpolated, Linear)")
    ax2.set_title("Coherence lifetimes")
    ax2.legend(fontsize=7)
    ax2.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "D05_relative_stability_map.png"), dpi=300)
    print("figure written: D05_relative_stability_map.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
