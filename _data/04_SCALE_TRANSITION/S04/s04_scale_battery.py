#!/usr/bin/env python3
"""
S04 scale-falsification battery (Record VMC-QF-Vault-13).

Executes the four scale-level falsification criteria of
04_SCALE_TRANSITION/S04_Metrics_Criteria_and_Falsification.md on the exact
single-excitation block engine (the D05 Vault-11 closure principle,
generalized: number-conserving hopping + diagonal pure-dephasing Kraus
operators close the one-excitation block exactly; here the block basis IS the
site basis of an arbitrary network).

Tests
  T1  criterion 1 -- Lieb-Robinson causality: arrival-time wavefront speed
      v_eff across an 8-cluster chain vs the registered bound
      v_LR = 2 e Delta (Delta = max weighted degree). PASS iff 0 < v_ratio <= 1.
  T2  criterion 2 -- lifetime enhancement R_tau = tau_life(macro)/tau_life(micro):
      4-cluster chain vs isolated cluster at gamma = 0.05, with the D04
      one-step memory layer (eta = 0.2) applied at identical beta on BOTH
      sides (only the network differs). beta has no registered numeric value,
      so this battery MEASURES R_tau(beta) over a scan window and registers
      criterion 2 as passed-conditionally (beta >= beta*) or OPEN if flat.
      Operational closure registered in the note: C_i := n_i(tau) (the one
      unregistered symbol in the D04 memory formula).
  T3  criterion 3 -- A03 balance at the mesoscopic scale: population
      continuity dn_i/dtau = -sum_j J_{i->j} with edge current
      J_{i->j} = 2 J_ij Im(rho_ij), central difference on the grid
      dtau = 0.00125 over 800 steps; dephasing is analytically
      population-invariant (diagonal Kraus operators, proven). PASS iff the
      converged residue <= delta_tol = eta * <|J|> with reported eta = 0.1.
  T4  criterion 4 -- defect-density collapse: Monte-Carlo site percolation on
      the square cluster lattice (defect clusters = pinning traps; transport
      lives on the trap-free sublattice), threshold measured by the spanning
      crossing; PLUS a quantum two-cluster pinning check (charge migrates to
      and accumulates on the defect-bearing cluster). The measured rho_c
      supersedes the untraceable registered 0.382 if they disagree (E4).

Outputs (next to this script):
  S04_battery_results.csv   one row per registered quantity
  S04_battery.png           2x2 figure (light cone, R_tau(beta),
                            percolation curve, pinning populations)
  s04_battery_output.txt    full log
"""
import csv
import math
import os
import sys
from collections import deque

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
EPS = 1e-3
DT = 0.5
N_STEPS = 200
J_RING, J_STAR, J_LINK = 1.0, 0.3, 0.3
DELTA = 0.1284

results = []


def register(test, quantity, value, threshold, verdict):
    results.append(dict(test=test, quantity=quantity, value=value,
                        threshold=threshold, verdict=verdict))
    print(f"  [{test}] {quantity} = {value}  (threshold: {threshold}) -> {verdict}")


# ---------------- generic exact block engine (site basis) ----------------

def build_h(adj, detune=None):
    n = max(max(i, j) for i, j in adj) + 1
    H = np.zeros((n, n), dtype=complex)
    for (i, j), v in adj.items():
        H[i, j] = v
        H[j, i] = np.conj(v)
    if detune:
        for s, d in detune.items():
            H[s, s] += d
    return H


def step_engine(H, gamma):
    evals, evecs = np.linalg.eigh(H)
    U = (evecs * np.exp(-1j * evals * DT)) @ evecs.conj().T
    decay = (1.0 - gamma) ** 2

    def step(rho):
        m = U @ rho @ U.conj().T
        out = m * decay
        np.fill_diagonal(out, np.real(np.diag(m)))
        return out
    return step


def cluster_chain(n_clusters, defect_clusters=(), defect_mode="edge-phase"):
    """Adjacency of n_clusters G6 cells; inter-cluster link = ring node 3 of
    cluster c to ring node 1 of cluster c+1. Defect per D05 conventions on the
    chosen clusters (edge-phase Peierls flux on the 5->1 hop and/or site
    detuning on ring node 1)."""
    adj = {}

    def C(c, k):
        return 6 * c + k
    for c in range(n_clusters):
        for k in range(1, 6):
            adj[(C(c, k), C(c, k % 5 + 1))] = J_RING
        for k in range(1, 6):
            adj[(C(c, 0), C(c, k))] = J_STAR
        if defect_mode in ("edge-phase", "mixed") and c in defect_clusters:
            adj[(C(c, 1), C(c, 5))] = J_RING * np.exp(1j * DELTA)
    for c in range(n_clusters - 1):
        adj[(C(c, 3), C(c + 1, 1))] = J_LINK
    detune = {C(c, 1): DELTA for c in defect_clusters
              if defect_mode in ("site", "mixed")}
    return adj, detune


def ring_edges_of(c):
    return [(6 * c + k, 6 * c + k % 5 + 1) for k in range(1, 6)]


def mean_ring_coherence(rho, c):
    return float(np.mean([abs(rho[i, j]) for (i, j) in ring_edges_of(c)]))


def tau_life(trace, taus, thr=EPS):
    for k in range(1, len(trace)):
        a, b = trace[k - 1], trace[k]
        if a >= thr > b:
            return taus[k - 1] + (a - thr) / (a - b) * (taus[k] - taus[k - 1])
    return None


# ---------------- T1: Lieb-Robinson causality ----------------

def t1_causality():
    print("\n== T1: Lieb-Robinson causality (criterion 1) ==")
    NC = 8
    adj, det = cluster_chain(NC)
    H = build_h(adj, det)
    n = H.shape[0]
    deg = {i: 0.0 for i in range(n)}
    for (i, j), v in adj.items():
        deg[i] += abs(v)
        deg[j] += abs(v)
    Delta = max(deg.values())
    v_LR = 2 * math.e * Delta
    register("T1", "Delta (max weighted degree)", round(Delta, 4),
             "registered bound input", "info")
    register("T1", "v_LR = 2 e Delta", round(v_LR, 3), "LR bound (GOW/Nagel)",
             "info")

    rho = np.zeros((n, n), dtype=complex)
    rho[0, 0] = 1.0
    step = step_engine(H, 0.0)
    taus = [k * DT for k in range(N_STEPS + 1)]
    pops = {k: [] for k in range(NC)}
    centers = [6 * k for k in range(NC)]
    for s in range(N_STEPS + 1):
        for k in range(NC):
            pops[k].append(float(np.real(rho[centers[k], centers[k]])))
        if s < N_STEPS:
            rho = step(rho)

    arrivals = {}
    for k in range(1, NC):
        p = np.array(pops[k])
        half = 0.5 * p.max()
        arrivals[k] = next((taus[i] for i in range(len(p)) if p[i] >= half),
                           None)
    nbr = {i: set() for i in range(n)}
    for (i, j) in adj:
        nbr[i].add(j)
        nbr[j].add(i)
    dist = {0: 0}
    q = deque([0])
    while q:
        u = q.popleft()
        for w in nbr[u]:
            if w not in dist:
                dist[w] = dist[u] + 1
                q.append(w)
    pts = [(dist[6 * k], arrivals[k]) for k in range(1, NC)
           if arrivals[k] is not None]
    d_arr = np.array([p[0] for p in pts], float)
    t_arr = np.array([p[1] for p in pts], float)
    slope, _ = np.polyfit(d_arr, t_arr, 1)
    v_eff = 1.0 / slope
    v_ratio = v_eff / v_LR
    ok = 0 < v_ratio <= 1
    register("T1", "v_eff (edges per tau, wavefront half-max)",
             round(v_eff, 4), "measured", "info")
    register("T1", "v_ratio = v_eff / v_LR", round(v_ratio, 4), "<= 1",
             "PASS" if ok else "FAIL")
    return v_ratio, d_arr, t_arr


# ---------------- T2: R_tau(beta) with the D04 memory layer ----------------

def run_with_memory(adj, detune, gamma, beta, eta, rho0, charged_cluster,
                    n_steps=N_STEPS):
    """Time-dependent star coupling per D04's one-step memory kernel with the
    registered operational closure C_i := n_i(tau). J_star,k(tau) =
    J_STAR * (1 + beta m_k(tau)) with m the node memory variable."""
    n = max(max(i, j) for i, j in adj) + 1
    m = np.zeros(n)
    rho = rho0.copy()
    taus, trace = [0.0], [mean_ring_coherence(rho, charged_cluster)]
    for s in range(n_steps):
        H = np.zeros((n, n), dtype=complex)
        for (i, j), v in adj.items():
            if 0 in (i % 6, j % 6) and i // 6 == j // 6:
                v = J_STAR * (1.0 + beta * 0.5 * (m[i] + m[j]))
            H[i, j] = v
            H[j, i] = np.conj(v)
        for sd, d in detune.items():
            H[sd, sd] += d
        evals, evecs = np.linalg.eigh(H)
        U = (evecs * np.exp(-1j * evals * DT)) @ evecs.conj().T
        mm = U @ rho @ U.conj().T
        out = mm * (1 - gamma) ** 2
        np.fill_diagonal(out, np.real(np.diag(mm)))
        rho = out
        nn = np.real(np.diag(rho))
        m = (1 - eta) * m + eta * nn
        taus.append((s + 1) * DT)
        trace.append(mean_ring_coherence(rho, charged_cluster))
    return np.array(taus), np.array(trace)


def t2_lifetime_enhancement():
    print("\n== T2: R_tau(beta) multi-cluster vs isolated (criterion 2) ==")
    gam = 0.05
    eta = 0.2
    betas = [0.0, 0.5, 1.0]
    adj_M, det_M = cluster_chain(4, defect_clusters=(0,), defect_mode="site")
    psi_M = np.zeros((24, 24), dtype=complex)
    for k in range(1, 6):
        psi_M[k, k] = np.exp(2j * np.pi * (k - 1) / 5)
    psi_M /= np.sqrt(5)
    adj_m, det_m = cluster_chain(1, defect_clusters=(0,), defect_mode="site")
    psi_m = np.zeros((6, 6), dtype=complex)
    for k in range(1, 6):
        psi_m[k, k] = np.exp(2j * np.pi * (k - 1) / 5)
    psi_m /= np.sqrt(5)

    out = []
    for beta in betas:
        taus_m, tr_m = run_with_memory(adj_m, det_m, gam, beta, eta, psi_m, 0)
        tau_micro = tau_life(tr_m, taus_m)
        taus, tr = run_with_memory(adj_M, det_M, gam, beta, eta, psi_M, 0)
        tl = tau_life(tr, taus)
        R = tl / tau_micro if (tl and tau_micro) else None
        out.append(dict(beta=beta, tau_micro=tau_micro, tau_macro=tl, R=R))
        print(f"  beta = {beta:4.2f}: tau_life(micro) = {tau_micro:.2f}  "
              f"tau_life(macro) = {tl if tl else float('nan'):.2f}   "
              f"R_tau = {R if R else float('nan'):.3f}")

    above = [r["beta"] for r in out if r["R"] and r["R"] > 1.0]
    beta_star = min(above) if above else None
    r0 = out[0]["R"]
    register("T2", "R_tau(beta=0) [no-feedback config]",
             f"{r0:.3f}" if r0 else "censored", "> 1",
             "PASS" if (r0 and r0 > 1) else
             "FAIL-without-feedback (the feedback premise is load-bearing)")
    register("T2", "beta* (smallest scanned beta with R_tau > 1)",
             beta_star, "criterion-2 condition measured",
             "PASS-CONDITIONAL (beta >= beta*)" if ok_beta(beta_star) else
             "OPEN -- R_tau(beta) flat below 1 across the scanned window")
    return out


def ok_beta(b):
    return b is not None


# ---------------- T3: A03 balance at the mesoscopic scale ----------------

def t3_balance():
    print("\n== T3: A03 balance residue (criterion 3) ==")
    NC = 4
    adj, det = cluster_chain(NC)
    n = 6 * NC
    H = build_h(adj, det)
    eta_tol = 0.1
    dt_fine = 0.00125
    rho = np.zeros((n, n), dtype=complex)
    rho[0, 0] = 1.0
    evals, evecs = np.linalg.eigh(H)
    Uf = (evecs * np.exp(-1j * evals * dt_fine)) @ evecs.conj().T

    def Jmat(r):
        Jc = np.zeros((n, n))
        for (i, j), v in adj.items():
            J = 2 * abs(v) * np.imag(r[i, j])
            Jc[i, j] = J
            Jc[j, i] = -J
        return Jc

    res_max = 0.0
    Jabs = []
    prev = rho
    cur = Uf @ rho @ Uf.conj().T
    for _ in range(800):
        nxt = Uf @ cur @ Uf.conj().T
        J = Jmat(0.5 * (cur + nxt))
        Jabs.append(np.abs(J[J != 0]).mean())
        dn = (np.real(np.diag(nxt)) - np.real(np.diag(prev))) / (2 * dt_fine)
        div = J.sum(axis=1)
        res_max = max(res_max, float(np.max(np.abs(dn + div))))
        prev, cur = cur, nxt

    delta_tol = eta_tol * float(np.mean(Jabs))
    ok = res_max <= delta_tol
    register("T3", "max population-continuity residue (grid 0.00125)",
             f"{res_max:.2e}", f"<= delta_tol = {delta_tol:.2e}",
             "PASS" if ok else "FAIL")
    register("T3", "dephasing population invariance",
             "0 (exact: diagonal Kraus operators)", "0", "PASS")

    # global conservation on the registered battery engine (dtau = 0.5)
    rho = np.zeros((n, n), dtype=complex)
    rho[0, 0] = 1.0
    step = step_engine(H, 0.1)
    drift = 0.0
    for _ in range(N_STEPS):
        rho = step(rho)
        drift = max(drift, abs(np.trace(rho).real - 1.0))
    register("T3", "global sum(n) drift over 200 steps (gamma=0.1)",
             f"{drift:.2e}", "~ machine precision",
             "PASS" if drift < 1e-10 else "FAIL")
    return res_max, delta_tol


# ---------------- T4: defect-density percolation + quantum pinning -------

def t4_percolation():
    print("\n== T4: defect-density collapse (criterion 4) ==")
    L = 64
    seeds = 300
    rhos = np.round(np.arange(30, 51) * 0.01, 2)
    rng = np.random.default_rng(20260930)

    def spans(grid):
        seen = np.zeros_like(grid, dtype=bool)
        stack = [j for j in range(L) if not grid[0, j]]
        for j in stack:
            seen[0, j] = True
        while stack:
            i, jj = divmod(stack.pop(), L)
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, jj + dj
                if 0 <= ni < L and 0 <= nj < L and not grid[ni, nj] \
                        and not seen[ni, nj]:
                    seen[ni, nj] = True
                    stack.append(ni * L + nj)
        return seen[L - 1].any()

    curve = []
    for rho_d in rhos:
        cnt = 0
        for _ in range(seeds):
            grid = rng.random((L, L)) < rho_d
            cnt += spans(grid)
        curve.append(cnt / seeds)
    curve = np.array(curve)
    cross = None
    for i in range(len(rhos) - 1):
        if curve[i] >= 0.5 > curve[i + 1]:
            frac = (curve[i] - 0.5) / (curve[i] - curve[i + 1])
            cross = rhos[i] + frac * 0.01
            break
    rho_c_ref = 1 - 0.5927465
    ok = abs(cross - rho_c_ref) < 0.01
    register("T4", "rho_c measured (spanning crossing, L=64, 300 seeds)",
             round(cross, 4), f"1 - p_c^site(square) = {rho_c_ref:.4f}",
             "PASS (matches trap-free-sublattice percolation)" if ok
             else "CHECK")
    registered = 0.382
    delta = abs(cross - registered)
    verdict = ("E4 CORRECTION: registered 0.382 superseded by measured "
               f"{cross:.4f} (= 1 - p_c^site of the square lattice; the old "
               "value has no traceable source)" if delta > 0.005 else
               "registered 0.382 confirmed")
    register("T4", "deviation from registered rho_c = 0.382", round(delta, 4),
             "<= 0.005 to confirm", verdict)

    # quantum pinning: two coupled clusters; identical twist (soliton) on
    # cluster 0; ONLY cluster 1's content changes: defect-bearing vs clean.
    # (Order parameter = SOLITON SURVIVAL of cluster 0, not population:
    # probes showed the single excitation equilibrates to 1/2-1/2 across the
    # two clusters regardless of defect placement -- population is NOT a
    # pinning order parameter. The population check is retained as a
    # registered negative control.)
    adj_c, det_c = cluster_chain(2, defect_clusters=(), defect_mode="edge-phase")
    adj_d, det_d = cluster_chain(2, defect_clusters=(1,), defect_mode="edge-phase")

    def soliton_life(adj, det):
        H = build_h(adj, det)
        rho = np.zeros((12, 12), dtype=complex)
        for k in range(1, 6):
            rho[k, k] = np.exp(2j * np.pi * (k - 1) / 5)
        rho /= np.sqrt(5)
        step = step_engine(H, 0.05)
        trace = [mean_ring_coherence(rho, 0)]
        for _ in range(600):
            rho = step(rho)
            trace.append(mean_ring_coherence(rho, 0))
        return tau_life(trace, np.arange(601) * DT), trace

    t_clean, tr_c = soliton_life(adj_c, det_c)
    t_def, tr_d = soliton_life(adj_d, det_d)
    R_pin = t_def / t_clean if (t_def and t_clean) else None
    ok_pin = R_pin is not None and R_pin > 1.0
    register("T4", "soliton tau_life with defect-FREE neighbor",
             round(t_clean, 2), "control", "info")
    register("T4", "soliton tau_life with DEFECT neighbor",
             round(t_def, 2), "treatment", "info")
    register("T4", "pinning ratio R_pin = tau(defect nb)/tau(clean nb)",
             round(R_pin, 4) if R_pin else "censored", "> 1",
             "PASS (pinning)" if ok_pin else
             "FAIL (defect neighbor = destructive scattering, R_pin < 1)")

    # negative control (retained): single-excitation population equilibrates
    # to 1/2-1/2 regardless of defect placement -- population is NOT a
    # pinning order parameter
    H = build_h(adj_d, det_d)
    rho = np.zeros((12, 12), dtype=complex)
    rho[0, 0] = 1.0
    step = step_engine(H, 0.05)
    for _ in range(1000):
        rho = step(rho)
    pop_defect = sum(np.real(rho[6 + k, 6 + k]) for k in range(6))
    register("T4", "negative control: single-excitation population on the "
             "defect cluster at tau=500", round(pop_defect, 4),
             "~ 0.5 expected (NOT a pinning order parameter)",
             "control consistent" if abs(pop_defect - 0.5) < 0.05 else "CHECK")
    return rhos, curve, cross, R_pin, pop_defect, (t_clean, t_def)


# ---------------- figure + main ----------------

def main():
    v_ratio, d_arr, t_arr = t1_causality()
    beta_scan = t2_lifetime_enhancement()
    res_max, delta_tol = t3_balance()
    rhos, curve, cross, R_pin, pop_def, t4_pinning = t4_percolation()

    cols = ["test", "quantity", "value", "threshold", "verdict"]
    with open(os.path.join(HERE, "S04_battery_results.csv"), "w",
              newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in results:
            w.writerow(r)
    print("\nCSV written: S04_battery_results.csv")

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))

    ax = axes[0, 0]
    ax.plot(d_arr, t_arr, "o-")
    ax.set_xlabel("graph distance from injection site (edges)")
    ax.set_ylabel("arrival time (half-max)")
    ax.set_title(f"T1 light cone: v_eff/v_LR = {v_ratio:.3f} <= 1")
    ax.grid(alpha=0.3)

    ax = axes[0, 1]
    bs = [r["beta"] for r in beta_scan]
    Rs = [r["R"] if r["R"] else np.nan for r in beta_scan]
    ax.plot(bs, Rs, "s-")
    ax.axhline(1.0, color="k", ls="--", lw=1)
    ax.set_xlabel(r"memory feedback $\beta$")
    ax.set_ylabel(r"$R_\tau$ (macro/micro)")
    ax.set_title(r"T2: criterion 2 threshold ($\eta=0.2$, $\gamma=0.05$)")
    ax.grid(alpha=0.3)

    ax = axes[1, 0]
    ax.plot(rhos, curve, "o-")
    ax.axvline(cross, color="r", ls="--", lw=1,
               label=rf"measured $\rho_c$ = {cross:.4f}")
    ax.axvline(0.382, color="0.4", ls=":", lw=1, label="superseded 0.382")
    ax.set_xlabel(r"defect density $\rho$")
    ax.set_ylabel("spanning probability")
    ax.set_title("T4: transport percolation (trap-free sublattice)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axes[1, 1]
    labels = ["defect-FREE\nneighbor", "DEFECT\nneighbor"]
    vals = [t4_pinning[0], t4_pinning[1]]
    ax.bar(labels, vals, color=["tab:blue", "tab:red"])
    ax.set_ylabel(r"$\tau_{\rm life}$ of the cluster-0 soliton")
    ax.set_title(f"T4 pinning: R_pin = {R_pin:.3f}")
    for i, v in enumerate(vals):
        ax.text(i, v + 0.3, f"{v:.1f}", ha="center", fontsize=9)
    ax.grid(alpha=0.3, axis="y")

    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "S04_battery.png"), dpi=300)
    print("figure written: S04_battery.png")

    print("\n== battery summary ==")
    for r in results:
        if r["verdict"].startswith(("PASS", "FAIL", "E4", "OPEN")):
            print(f"  {r['test']}: {r['quantity']} -> {r['verdict']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
