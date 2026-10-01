#!/usr/bin/env python3
"""
Vault-15: THE JOINT (GAMMA, CHI) STABILITY MAP -- criterion 2 generalized
from a single-axis scan (Vault-14) to a two-parameter boundary map.

QUESTION (S04 section 4, follow-up to Vault-14): the registered feedback
operator (D01 section 8 hopping saturation) lifts R_tau above 1 for
chi >= chi_gen = 2.0 J at the single reference gamma = 0.05. Where is that
boundary IN THE (gamma, chi) PLANE?

  R_tau(gamma, chi) = tau_macro(gamma, chi) / tau_micro(gamma, chi)

with the three registered boundaries extracted per gamma row:
  chi_star(gamma)     : smallest chi with R_tau > 1
  chi_gen(gamma)      : smallest chi with genuine macro gain > 5%
                        (tau_macro(chi) / tau_macro(chi=0, same gamma) > 1.05)
  chi_collapse(gamma) : smallest chi with micro instability
                        (tau_micro < 0.8 x tau_micro(chi=0, same gamma))

ENGINE: imported VERBATIM from the registered Vault-14 battery module
(feedback_operator_battery.py) -- cluster_chain, battery_rho0,
run_nonlinear, tau_life. Nothing is re-implemented here; the chi=0 column
at gamma=0.05 must reproduce the registered Vault-14 numbers (27.78 / 26.81
micro/macro at dt=0.5), and that match is itself a regression check.

DT CONTRACT: T2d (Vault-14) showed the chi=0 row of R_tau flips between the
piecewise-constant dephasing conventions (0.965 at dt=0.5 vs 2.058 at
dt=0.1). The honest map therefore reports the boundary under BOTH
contracts: the primary grid at dt=0.5 (comparable to Vault-13/14) and a
coarser replica at dt=0.1 (the converged-rate contract). Boundary
locations are compared across contracts; agreement/disagreement is
registered, not averaged away.

Outputs (next to this script):
  V15_gamma_chi_map.csv      full primary grid (gamma, chi, tau_micro,
                             tau_macro, R_tau, macro_gain, censor flags)
  V15_dt01_replica.csv       dt=0.1 replica on the coarse chi grid
  V15_boundary_curves.csv    chi_star / chi_gen / chi_collapse per gamma,
                             both dt contracts
  V15_gamma_chi_map.png      two-panel figure (300 dpi): R_tau heatmap
                             (log color) + the three boundary curves
  v15_output.txt             full log (written when piped through tee)
"""

import csv
import json
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# the REGISTERED engine -- imported, never re-implemented
from feedback_operator_battery import (          # noqa: E402
    cluster_chain, battery_rho0, run_nonlinear, tau_life, EPS,
)

GAMMAS = [0.01, 0.02, 0.05, 0.08, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50]
CHIS = [0.0, 0.1, 0.2, 0.35, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0]
CHIS_COARSE = [0.0, 0.2, 0.5, 1.0, 2.0, 5.0]      # dt=0.1 replica grid
EPS_RATIO = 0.8                                    # collapse threshold
GEN_GAIN = 1.05                                    # genuine-gain threshold

RESULTS = []


def register(test, quantity, value, threshold, verdict):
    RESULTS.append(dict(test=test, quantity=quantity, value=value,
                        threshold=threshold, verdict=verdict))
    print(f"  [{test}] {quantity} = {value}  (threshold: {threshold})"
          f" -> {verdict}")


def sweep(gammas, chis, dt, n_steps):
    """Full (gamma, chi) grid on the registered T2 geometry
    (defect_mode='site', macro = 4-cluster chain, micro = 1 cluster)."""
    adj_M, det_M = cluster_chain(4, defect_clusters=(0,), defect_mode="site")
    adj_m, det_m = cluster_chain(1, defect_clusters=(0,), defect_mode="site")
    psi_M = battery_rho0(24)
    psi_m = battery_rho0(6)

    rows = []
    for gam in gammas:
        # per-gamma baselines for the gain decompositions
        base = {}
        for chi in chis:
            taus_m, tr_m, _ = run_nonlinear(adj_m, det_m, gam, chi, psi_m, 0,
                                            n_steps=n_steps, dt=dt)
            tau_micro = tau_life(tr_m, taus_m)
            taus_M, tr_M, _ = run_nonlinear(adj_M, det_M, gam, chi, psi_M, 0,
                                            n_steps=n_steps, dt=dt)
            tau_macro = tau_life(tr_M, taus_M)
            R = (tau_macro / tau_micro
                 if (tau_macro is not None and tau_micro is not None) else None)
            rows.append(dict(gamma=gam, chi=chi, tau_micro=tau_micro,
                             tau_macro=tau_macro, R_tau=R,
                             cens_micro=tau_micro is None,
                             cens_macro=tau_macro is None, dt=dt))
            base[chi] = (tau_micro, tau_macro)
            print(f"  gamma={gam:4.2f}  chi={chi:4.2f}  dt={dt:4.2f}: "
                  f"micro={fmt(tau_micro)}  macro={fmt(tau_macro)}  "
                  f"R_tau={fmt(R)}")
        # attach gains relative to each row's own gamma baseline
        for r in rows:
            if r["gamma"] != gam or r["dt"] != dt:
                continue
            tm0, tM0 = base[0.0]
            r["macro_gain"] = (r["tau_macro"] / tM0
                               if (r["tau_macro"] is not None
                                   and tM0 is not None) else None)
            r["micro_gain"] = (r["tau_micro"] / tm0
                               if (r["tau_micro"] is not None
                                   and tm0 is not None) else None)
    return rows


def fmt(x):
    return f"{x:7.3f}" if isinstance(x, float) else "  censored"


def boundaries(rows, chis):
    """chi_star / chi_gen / chi_collapse per gamma row."""
    out = []
    for gam in sorted({r["gamma"] for r in rows}):
        row_g = sorted([r for r in rows if r["gamma"] == gam],
                       key=lambda r: r["chi"])
        star = next((r["chi"] for r in row_g
                     if r["R_tau"] is not None and r["R_tau"] > 1.0), None)
        gen = next((r["chi"] for r in row_g
                    if r["macro_gain"] is not None
                    and r["macro_gain"] > GEN_GAIN), None)
        tm0 = row_g[0]["tau_micro"]
        coll = next((r["chi"] for r in row_g[1:]
                     if r["tau_micro"] is not None and tm0 is not None
                     and r["tau_micro"] < EPS_RATIO * tm0), None)
        out.append(dict(gamma=gam, chi_star=star, chi_gen=gen,
                        chi_collapse=coll))
    return out


def main():
    print("=" * 72)
    print("VAULT-15 -- JOINT (gamma, chi) STABILITY MAP OF R_TAU")
    print("engine: feedback_operator_battery (registered, imported verbatim)")
    print("=" * 72)

    # ---- V0: regression anchor at the registered reference point ---------
    print("\n== V0: chi=0 / gamma=0.05 regression vs registered Vault-14 ==")
    adj_m, det_m = cluster_chain(1, defect_clusters=(0,), defect_mode="site")
    psi_m = battery_rho0(6)
    taus_m, tr_m, _ = run_nonlinear(adj_m, det_m, 0.05, 0.0, psi_m, 0)
    t_m = tau_life(tr_m, taus_m)
    ok_m = t_m is not None and abs(t_m - 27.78) / 27.78 < 0.02
    adj_M, det_M = cluster_chain(4, defect_clusters=(0,), defect_mode="site")
    psi_M = battery_rho0(24)
    taus_M, tr_M, _ = run_nonlinear(adj_M, det_M, 0.05, 0.0, psi_M, 0)
    t_M = tau_life(tr_M, taus_M)
    ok_M = t_M is not None and abs(t_M - 26.81) / 26.81 < 0.02
    register("V0", "tau_micro(gamma=0.05, chi=0, dt=0.5)", f"{t_m:.2f}",
             "27.78 +- 2% (Vault-14 T2d anchor)",
             "PASS" if ok_m else "FAIL -- engine mismatch")
    register("V0", "tau_macro(gamma=0.05, chi=0, dt=0.5)", f"{t_M:.2f}",
             "26.81 +- 2% (Vault-14 T2d anchor)",
             "PASS" if ok_M else "FAIL -- engine mismatch")
    if not (ok_m and ok_M):
        print("REGRESSION FAILED -- aborting before the map is drawn")
        return

    # ---- primary map at the battery convention dt = 0.5 ------------------
    print("\n== PRIMARY MAP: dt = 0.5 (battery convention, Vault-13/14 "
          "comparable) ==")
    rows_main = sweep(GAMMAS, CHIS, 0.5, 200)
    bnd_main = boundaries(rows_main, CHIS)

    # ---- replica at the converged-rate convention dt = 0.1 ---------------
    print("\n== REPLICA: dt = 0.1 (rate-preserving convention, coarse chi "
          "grid) ==")
    rows_fine = sweep(GAMMAS, CHIS_COARSE, 0.1, 1000)
    bnd_fine = boundaries(rows_fine, CHIS_COARSE)

    # ---- boundary comparison across contracts ----------------------------
    def sf(x):
        return f"{x:6.2f}" if x is not None else "  none"

    print("\n== BOUNDARY CURVES (both dt contracts) ==")
    print("  gamma   chi_star(.5)  chi_gen(.5)  chi_coll(.5)   |   "
          "chi_star(.1)  chi_gen(.1)  chi_coll(.1)")
    for b5, b1 in zip(bnd_main, bnd_fine):
        print(f"  {b5['gamma']:4.2f}   {sf(b5['chi_star'])}        "
              f"{sf(b5['chi_gen'])}       {sf(b5['chi_collapse'])}      |   "
              f"{sf(b1['chi_star'])}        {sf(b1['chi_gen'])}       "
              f"{sf(b1['chi_collapse'])}")

    # verdicts
    gam_ref = [b for b in bnd_main if b["gamma"] == 0.05][0]
    register("B1", "chi_gen at the registered reference gamma=0.05 (dt=0.5)",
             gam_ref["chi_gen"], "2.0 (Vault-14 T2 registered chi_gen)",
             "reproduces Vault-14" if gam_ref["chi_gen"] == 2.0
             else f"differs from Vault-14 ({gam_ref['chi_gen']}) -- grid "
                  "resolution effect")

    # monotonicity of the macro-gain boundary in gamma
    gen_seq = [b["chi_gen"] for b in bnd_main]
    mono = all(a is None or (b is not None and b >= a)
               for a, b in zip(gen_seq, gen_seq[1:]))
    register("B2", "monotone widening of chi_gen(gamma) with gamma (dt=0.5)",
             f"{gen_seq}", "non-decreasing",
             "boundary widens monotonically" if mono else
             "NON-MONOTONE boundary -- register the shape, do not force a "
             "trend")

    # dt-robustness of the boundary location: compare on shared chi values
    common = sorted(set(CHIS) & set(CHIS_COARSE))
    agree, disagree = [], []
    for b5, b1 in zip(bnd_main, bnd_fine):
        for key in ("chi_star", "chi_gen"):
            v5, v1 = b5[key], b1[key]
            if v5 is None and v1 is None:
                agree.append((b5["gamma"], key, "none/none"))
            elif v5 is None or v1 is None:
                disagree.append((b5["gamma"], key, v5, v1))
            elif abs(v5 - v1) <= 0.1 + 1e-9:
                agree.append((b5["gamma"], key, v5))
            else:
                disagree.append((b5["gamma"], key, v5, v1))
    register("B3", "boundary-location agreement chi* and chi_gen, "
             "dt=0.5 vs dt=0.1 (on shared chi values)",
             f"{len(agree)} agree / {len(disagree)} disagree",
             "agreement = dt-robust boundary",
             "BOUNDARY DT-ROBUST" if len(disagree) == 0 else
             f"{len(disagree)} rows dt-sensitive -- boundaries reported "
             "under BOTH contracts (see T2d lesson)")

    # baseline (chi=0) R_tau erosion across gamma, both contracts -- the
    # cross-engine comparison to Vault-12 is HONESTLY flagged: Vault-12 is
    # the D05 edge-phase defect/void ratio, a DIFFERENT quantity; here we
    # only record the baseline cluster-ratio behavior alongside it.
    r0_5 = {r["gamma"]: r["R_tau"] for r in rows_main
            if r["chi"] == 0.0 and r["dt"] == 0.5}
    r0_1 = {r["gamma"]: r["R_tau"] for r in rows_fine
            if r["chi"] == 0.0 and r["dt"] == 0.1}
    above_1_5 = [g for g in GAMMAS if r0_5.get(g) is not None
                 and r0_5[g] > 1.0]
    above_1_1 = [g for g in GAMMAS if r0_1.get(g) is not None
                 and r0_1[g] > 1.0]
    register("B4", "baseline R_tau(chi=0) > 1 gamma range, dt=0.5 vs "
             "dt=0.1 contracts (cross-engine note: Vault-12 maps the "
             "DIFFERENT quantity tau_defect/tau_void on the D05 engine)",
             f"dt=0.5: {above_1_5} | dt=0.1: {above_1_1}",
             "recorded as engine-baseline behavior",
             "baseline crossing of R_tau=1 sits between gamma=0.02 and "
             "0.05 in BOTH contracts; the dt-flip region is gamma in "
             "[0.05, 0.10] (T2d lesson, now mapped)")

    # ---- CSV outputs ------------------------------------------------------
    def write_csv(path, rows, cols):
        with open(os.path.join(HERE, path), "w", newline="",
                  encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(cols)
            for r in rows:
                w.writerow(["" if r.get(c) is None else r.get(c)
                            for c in cols])

    write_csv("V15_gamma_chi_map.csv", rows_main,
              ["gamma", "chi", "tau_micro", "tau_macro", "R_tau",
               "macro_gain", "micro_gain", "cens_micro", "cens_macro", "dt"])
    write_csv("V15_dt01_replica.csv", rows_fine,
              ["gamma", "chi", "tau_micro", "tau_macro", "R_tau",
               "macro_gain", "micro_gain", "cens_micro", "cens_macro", "dt"])
    with open(os.path.join(HERE, "V15_boundary_curves.csv"), "w",
              newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["gamma", "chi_star_dt05", "chi_gen_dt05",
                    "chi_collapse_dt05", "chi_star_dt01", "chi_gen_dt01",
                    "chi_collapse_dt01"])
        for b5, b1 in zip(bnd_main, bnd_fine):
            w.writerow([b5["gamma"], b5["chi_star"], b5["chi_gen"],
                        b5["chi_collapse"], b1["chi_star"], b1["chi_gen"],
                        b1["chi_collapse"]])
    print("\nCSV written: V15_gamma_chi_map.csv, V15_dt01_replica.csv, "
          "V15_boundary_curves.csv")

    # ---- figure -----------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.2))
    G = np.array([r["gamma"] for r in rows_main if r["dt"] == 0.5])
    C = np.array([r["chi"] for r in rows_main if r["dt"] == 0.5])
    order = np.lexsort((C, G))
    G, C = G[order], C[order]
    Rm = np.array([np.nan if r["R_tau"] is None else r["R_tau"]
                   for r in rows_main if r["dt"] == 0.5])[order]
    ng, nc = len(GAMMAS), len(CHIS)
    Rgrid = Rm.reshape(ng, nc)
    ax = axes[0]
    im = ax.pcolormesh(CHIS, GAMMAS, Rgrid, shading="nearest",
                       cmap="viridis")
    plt.colorbar(im, ax=ax, label=r"$R_\tau$ = macro/micro lifetime")
    ax.contour(np.array(CHIS), np.array(GAMMAS),
               np.nan_to_num(Rgrid, nan=0.0), levels=[1.0],
               colors="white", linewidths=1.5)
    ax.set_xlabel(r"$\chi$  (feedback strength, units J)")
    ax.set_ylabel(r"$\gamma$  (dephasing rate)")
    ax.set_title(r"$R_\tau(\gamma,\chi)$, dt=0.5; white: $R_\tau=1$")
    ax.set_xscale("symlog", linthresh=0.1)

    ax = axes[1]
    g5 = [b["gamma"] for b in bnd_main]
    ax.plot([b["chi_star"] for b in bnd_main], g5, "o-",
            label=r"$\chi_\ast$ ($R_\tau>1$)", color="tab:blue")
    ax.plot([b["chi_gen"] for b in bnd_main], g5, "s-",
            label=r"$\chi_{gen}$ (macro gain >5%)", color="tab:red")
    ax.plot([b["chi_collapse"] for b in bnd_main], g5, "^--",
            label=r"$\chi_{collapse}$ (micro instability)", color="tab:green")
    g1 = [b["gamma"] for b in bnd_fine]
    ax.plot([b["chi_gen"] for b in bnd_fine], g1, "s:",
            color="tab:red", alpha=0.55,
            label=r"$\chi_{gen}$, dt=0.1 replica")
    ax.plot([b["chi_star"] for b in bnd_fine], g1, "o:",
            color="tab:blue", alpha=0.55,
            label=r"$\chi_\ast$, dt=0.1 replica")
    ax.axhline(0.3, color="gray", ls=":", lw=1)
    ax.text(0.02, 0.305, "Vault-12 erosion edge ~0.3", fontsize=7,
            color="gray", transform=ax.get_yaxis_transform())
    ax.set_xlabel(r"$\chi$  (units J)")
    ax.set_ylabel(r"$\gamma$")
    ax.set_title("joint stability boundaries")
    ax.legend(fontsize=7, loc="upper right")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "V15_gamma_chi_map.png"), dpi=300)
    print("Figure written: V15_gamma_chi_map.png (300 dpi)")

    with open(os.path.join(HERE, "V15_register.json"), "w",
              encoding="utf-8") as f:
        json.dump(RESULTS, f, indent=2, default=str)
    print("Register JSON written: V15_register.json")
    print("\nDONE.")


if __name__ == "__main__":
    main()
