#!/usr/bin/env python3
"""
D05 CPTP reference simulation -- full 64-dimensional density matrix (exact).

Implements the D05 protocol literally (vault note: D05_Cluster_Simulation_and_Validation):

    rho(tau+1) = E_leak . U_graph (rho(tau))

with (memory feedback off, beta = 0, since D05 assigns no numeric beta):

    U_graph = exp(-i H dt)
    H       = J_ring * sum_{ring edges (i,j)} (sp_i sm_j + sm_i sp_j)
            + J_star * sum_{k=1..5} (sp_0 sm_k + sm_0 sp_k)
            + sum_{k=1..5} delta_k sz_k
    E_leak  = product over the six sites of the single-qubit pure-dephasing
              channel D_gamma (sequential composition; sites commute, so this
              is exact and trace-preserving at every step)

Node/site index convention (fixed throughout):
    site 0 = center node 0
    site q = ring node q   (q = 1..5)
so ring edges connect sites (1,2),(2,3),(3,4),(4,5),(5,1) and star edges
connect site 0 to sites 1..5.

Basis-state convention: the computational basis index of the 6-qubit space
is i = sum_q b_q 2^(5-q) (site 0 = most significant bit, matching the
left-to-right kron ordering of op()); the single-excitation state with the
excitation on site q has index 2**(5-q). The one-excitation sector
(indices 1,2,4,8,16,32)
is invariant under H and under pure dephasing, so the 6x6 block reduction
is exact -- verified below at machine precision against the full matrix.

Exact block closure (used by run(), verified against the full space):
Phase damping is diagonal in the computational basis, so it maps the
one-excitation block (indices 1,2,4,8,16,32) into itself and leaves every
diagonal element untouched. A coherence |i><j| between distinct one-excitation
basis states differs in exactly two qubits, so it decays by exactly (1-gamma)^2
per step. Hence the 6x6 block obeys the closed recursion
    rb <- (1-gamma)^2 * offdiag(Ub rb Ub^dag)      (diagonal kept)
and every recorded observable (populations, local purities C_i, edge
coherences chi_ij and their phases, topological charge Q) is a functional of
the block alone. The full 64x64 engine is retained for verification.

Defect implementation: S-02/S-03 use site detuning delta_1 = 0.1284 rad
(G01 angular deficit) on the sigma^z of ring site 1; S-01 has all deltas = 0
and starts from the uniform ring wave (phase 0 on every node, per the
Vault-10 record convention, so the S-01/S-02 comparison is like-for-like).
S-04 implements the D04 edge-phase defect -- a hermitian Peierls flux
exp(+i delta_theta) on the oriented ring hop (5 -> 1) -- which the D05
reconciliation note flags as the pending decisive protocol; this execution
closes it.

Outputs (written next to this script, replacing the phenomenological CSVs):
    D05_S01_trajectory.csv             gamma = 0.1, uniform ring wave, no defect
    D05_S02_trajectory.csv             gamma = 0.1, site-detuning defect
    D05_S04_edge_phase_trajectory.csv  gamma = 0.1, D04 edge-phase defect
    D05_S03_gamma_sweep.csv            S-02 sweep, gamma = 0.01 .. 0.5
    D05_S04_gamma_sweep.csv            S-04 sweep, gamma = 0.01 .. 0.5
    D05_key_times_comparison.csv       side-by-side key rows (S-01/S-02/S-04)
    D05_scenario_summary.csv           per-scenario summary at the final tau
Verification printout (stdout):
    H hermiticity, excitation-number conservation, trace preservation,
    positivity, and the exactness of the 6x6 block reduction.
"""
import numpy as np
import math, os, csv, sys

DT = 0.5
N_STEPS = 200                                  # tau = 0 .. 100
TAUS = np.round(np.arange(N_STEPS + 1) * DT, 10)
EPS = 1e-3
J_RING = 1.0
J_STAR = 0.3
DELTA_DEF = 0.1284                             # G01 angular deficit (rad)
GAMMA_TRAJ = 0.1
GAMMA_SWEEP = np.round(np.arange(1, 51) * 0.01, 4)
KEY_TAUS = (0, 10, 20, 40, 80, 100)

HERE = os.path.dirname(os.path.abspath(__file__))

I2 = np.eye(2, dtype=complex)
SM = np.array([[0, 1], [0, 0]], dtype=complex)   # sigma^- = |0><1|
SP = SM.conj().T                                 # sigma^+ = |1><0|
SZ = np.array([[1, 0], [0, -1]], dtype=complex)  # |0> = +1

def op(site_ops):
    """Tensor-product operator on 6 qubits; site_ops = {site: 2x2 matrix}."""
    m = np.array([[1.0 + 0j]])
    for q in range(6):
        m = np.kron(m, site_ops.get(q, I2))
    return m

SP_F = [op({q: SP}) for q in range(6)]
SM_F = [op({q: SM}) for q in range(6)]
SZ_F = [op({q: SZ}) for q in range(6)]
N_F = [SP_F[q] @ SM_F[q] for q in range(6)]
N_TOT = sum(N_F)

RING_EDGES = [(k + 1, (k + 1) % 5 + 1) for k in range(5)]   # node labels 1..5
STAR_EDGES = [(0, k) for k in range(1, 6)]                  # center 0 -> node k

def build_h(delta_vec, edge_phase=None):
    """H with optional uniform-per-edge complex phase on the ring hopping
    (D04 edge-phase defect variant). delta_vec is indexed by ring site 1..5:
    delta_vec[0] is ignored; use a length-6 list with entry 0 unused."""
    H = np.zeros((64, 64), dtype=complex)
    for (i, j) in RING_EDGES:
        if edge_phase is not None and (i, j) == (5, 1):
            ph = np.exp(1j * edge_phase)
            # hermitian Peierls substitution: +phase on 5->1, -phase on 1->5
            H += J_RING * (ph * (SP_F[i] @ SM_F[j])
                           + np.conj(ph) * (SP_F[j] @ SM_F[i]))
        else:
            H += J_RING * (SP_F[i] @ SM_F[j] + SP_F[j] @ SM_F[i])
    for (i, j) in STAR_EDGES:
        H += J_STAR * (SP_F[i] @ SM_F[j] + SP_F[j] @ SM_F[i])
    for k in range(1, 6):
        if delta_vec[k] != 0.0:
            H += delta_vec[k] * SZ_F[k]
    return H

def basis_index(site):
    """Computational-basis index of 'site q excited' (big-endian, op() order)."""
    return 1 << (5 - site)

def initial_rho(topological):
    """T1 protocol: single excitation delocalized over the ring, center empty.
    S-01 (null, Vault-10 convention): uniform ring wave, phase 0 on every node
        -> no twist, Q_winding(0) = 0.
    S-02: twist quench e^{i 2pi (k-1)/5} on the ring -> Q_winding(0) = 1."""
    psi = np.zeros(64, dtype=complex)
    for q in range(1, 6):
        psi[basis_index(q)] = (np.exp(2j * np.pi * (q - 1) / 5) if topological
                               else 1.0) / np.sqrt(5)
    return np.outer(psi, psi.conj())

def apply_dephasing(rho, gamma):
    """E_leak: sequential composition of the six single-qubit dephasing
    channels. Exact and trace-preserving."""
    if gamma == 0.0:
        return rho
    k0c, k1c = math.sqrt(1 - gamma / 2), math.sqrt(gamma / 2)
    out = rho
    for q in range(6):
        K0 = k0c * op({q: I2})
        K1 = k1c * op({q: SZ})
        out = K0 @ out @ K0.conj().T + K1 @ out @ K1.conj().T
    return out

def local_purities(rho):
    """C_i = Tr(rho_i^2) - 1/2 for the six single-site reductions.
    Uses einsum with explicit index lists: bra indices 0..5, ket 6..11;
    every pair except site q is contracted diagonally."""
    r6 = rho.reshape([2] * 12)
    C = []
    for q in range(6):
        spec = [0] * 12
        spec[q] = 40            # kept bra index (unique label)
        spec[6 + q] = 41        # kept ket index (unique label)
        label = 0
        for i in range(6):
            if i != q:
                spec[i] = label
                spec[6 + i] = label
                label += 1
        red = np.einsum(r6, spec, [40, 41])
        C.append(float(np.real(np.trace(red @ red)) - 0.5))
    return C

def edge_chis(rho, edge_phase_ref=None):
    """chi_{i,j} = Tr(rho sp_i sm_j) for the five ring edges (node labels)."""
    out = []
    for (i, j) in RING_EDGES:
        M = SP_F[i] @ SM_F[j]
        out.append(complex(np.trace(rho @ M)))
    return out

def unwrapped_winding(phases):
    """Oriented wrapped winding on the 5-cycle from the five link phases."""
    d = [(phases[(k + 1) % 5] - phases[k] + math.pi) % (2 * math.pi) - math.pi for k in range(5)]
    return sum(d) / (2 * math.pi)

BLOCK_IDX = [basis_index(q) for q in range(6)]   # block position == site label
RING_LOCAL = list(RING_EDGES)                     # positions are site labels now

def run(topological, gamma, defect="site", n_steps=N_STEPS, record_every=1,
        engine="block"):
    delta_vec = [0.0] * 6
    edge_phase = None
    if topological and defect == "site":
        delta_vec[1] = DELTA_DEF
    if topological and defect == "edge-phase":
        edge_phase = DELTA_DEF
    rho = initial_rho(topological)
    H = build_h(delta_vec, edge_phase)
    decay = (1.0 - gamma) ** 2
    if engine == "block":
        Hb = H[np.ix_(BLOCK_IDX, BLOCK_IDX)]
        evb, evecb = np.linalg.eigh(Hb)
        Ub = (evecb * np.exp(-1j * evb * DT)) @ evecb.conj().T
        rb = rho[np.ix_(BLOCK_IDX, BLOCK_IDX)].astype(complex)
        rho = rb  # block engine works on the 6x6 one-excitation block only

        def step(r):
            m = Ub @ r @ Ub.conj().T
            out = m * decay
            np.fill_diagonal(out, np.real(np.diag(m)))
            return out

        def obs(r):
            diag = np.real(np.diag(r))
            ring_pop = float(sum(diag[q] for q in range(1, 6)))
            core_pop = float(diag[0])
            # local purities from the block. PROVEN exact: every off-diagonal
            # element of the single-site reduction rho_q connects different
            # excitation-number sectors (bra N = |rest|+1 vs ket N = |rest|);
            # U is N-conserving and the dephasing Kraus operators are diagonal,
            # so these elements stay zero for all time. Hence Tr(rho_q^2) is
            # purely diagonal: C_q = P^2 + (1-P)^2 - 1/2 = 2 (P - 1/2)^2.
            C = []
            for q in range(6):
                P = diag[q]
                C.append(float(P * P + (1 - P) ** 2 - 0.5))
            chi = [complex(r[l_j, l_i]) for (l_i, l_j) in RING_LOCAL]
            return ring_pop, core_pop, C, chi
    else:
        evals, evecs = np.linalg.eigh(H)
        U = (evecs * np.exp(-1j * evals * DT)) @ evecs.conj().T

        def step(r):
            return apply_dephasing(U @ r @ U.conj().T, gamma)

        def obs(r):
            n_diag = np.real(np.diag(r))
            ring_pop = float(sum(n_diag[basis_index(q)] for q in range(1, 6)))
            core_pop = float(n_diag[basis_index(0)])
            C = local_purities(r)
            chi = edge_chis(r)
            return ring_pop, core_pop, C, chi

    rows = []
    for step_n in range(n_steps + 1):
        tau = round(step_n * DT, 10)
        if step_n > 0:
            rho = step(rho)
        if step_n % record_every == 0 or step_n == n_steps:
            ring_pop, core_pop, C, chi = obs(rho)
            mags = [abs(c) for c in chi]
            ph = [math.atan2(c.imag, c.real) for c in chi]
            mean_abs_chi = sum(mags) / 5
            valid = min(mags) >= EPS
            Q_wind = sum(ph) / (2 * math.pi) if valid else 0.0
            Q_wrap = unwrapped_winding(ph) if valid else 0.0
            rows.append(dict(
                tau=tau, gamma=gamma,
                mean_edge_coherence=mean_abs_chi,
                min_edge_coherence=min(mags),
                Q_winding=Q_wind, Q_wrapped=Q_wrap,
                ring_population=ring_pop, center_population=core_pop,
                mean_ring_C=sum(C[1:]) / 5,
                C0=C[0], C1=C[1], C2=C[2], C3=C[3], C4=C[4], C5=C[5],
                **{f"phase_{k}": ph[k - 1] for k in range(1, 6)},
            ))
    return rows

# ------------------------- verification -------------------------

def verify():
    ok = True
    H = build_h([0.0] * 6)
    herm = np.allclose(H, H.conj().T)
    print(f"[verify] H hermitian (no defect): {herm}")
    ok &= herm
    H2 = build_h([0.0, 0.1284, 0, 0, 0, 0])
    herm2 = np.allclose(H2, H2.conj().T)
    print(f"[verify] H hermitian (site defect): {herm2}")
    ok &= herm2
    rho0 = initial_rho(True)
    evals, evecs = np.linalg.eigh(H)
    U = (evecs * np.exp(-1j * evals * DT)) @ evecs.conj().T
    r1 = U @ rho0 @ U.conj().T
    n_cons = abs(np.trace((r1 - rho0) @ N_TOT)) < 1e-12
    print(f"[verify] excitation number conserved by U: {n_cons}")
    ok &= n_cons
    rd = apply_dephasing(r1, 0.1)
    tr = abs(np.trace(rd).real - 1) < 1e-12
    diag_ok = np.allclose(np.diag(rd).real, np.diag(r1).real)
    herm_ok = np.allclose(rd, rd.conj().T)
    print(f"[verify] dephasing: trace preserved {tr}, diagonal preserved {diag_ok}, hermitian {herm_ok}")
    ok &= (tr and diag_ok and herm_ok)
    r = rho0
    min_eig = 1.0
    for _ in range(50):
        r = apply_dephasing(U @ r @ U.conj().T, 0.1)
        min_eig = min(min_eig, np.linalg.eigvalsh((r + r.conj().T) / 2).min())
    pos = min_eig > -1e-12
    print(f"[verify] 50 CPTP steps: min eigenvalue >= {min_eig:.2e} (positivity {pos})")
    ok &= pos
    # exactness of the 6x6 block reduction (unitary step, S-02 initial state)
    idx = [1, 2, 4, 8, 16, 32]
    Hb = H[np.ix_(idx, idx)]
    evb, evecb = np.linalg.eigh(Hb)
    Ub = (evecb * np.exp(-1j * evb * DT)) @ evecb.conj().T
    rb = Ub @ rho0[np.ix_(idx, idx)] @ Ub.conj().T
    rf = U @ rho0 @ U.conj().T
    block_diff = np.abs(rf[np.ix_(idx, idx)] - rb).max()
    print(f"[verify] block==full max diff (unitary step): {block_diff:.2e}")
    ok &= block_diff < 1e-12
    # edge-phase hermiticity (Peierls substitution)
    H3 = build_h([0.0] * 6, edge_phase=DELTA_DEF)
    herm3 = np.allclose(H3, H3.conj().T)
    print(f"[verify] H hermitian (edge-phase defect): {herm3}")
    ok &= herm3
    # initial-state conventions: topological charge, link coherence, local purities
    # (populations use the big-endian map: site q excited <-> basis_index(q))
    r02, r01 = initial_rho(True), initial_rho(False)
    for tag, r0 in (("S-02", r02), ("S-01", r01)):
        d0 = np.real(np.diag(r0))
        rp = sum(d0[basis_index(q)] for q in range(1, 6))
        cp = d0[basis_index(0)]
        print(f"[verify] {tag} t=0 populations: ring={rp:.6f} center={cp:.6f} "
              f"(expect 1 / 0)")
        ok &= (abs(rp - 1) < 1e-12 and abs(cp) < 1e-12)
    c02 = local_purities(r02)
    ch02 = edge_chis(r02)
    q02 = sum(math.atan2(c.imag, c.real) for c in ch02) / (2 * math.pi)
    ch01 = edge_chis(r01)
    q01 = sum(math.atan2(c.imag, c.real) for c in ch01) / (2 * math.pi)
    print(f"[verify] S-02 t=0: Q_winding={q02:.12f} (expect 1), "
          f"C0={c02[0]:.6f} (expect 0.5), "
          f"mean|chi|={sum(abs(c) for c in ch02) / 5:.6f} (expect 0.2)")
    ok &= (abs(q02 - 1.0) < 1e-12 and abs(c02[0] - 0.5) < 1e-12
           and abs(sum(abs(c) for c in ch02) / 5 - 0.2) < 1e-12)
    print(f"[verify] S-01 t=0: Q_winding={q01:.12f} (expect 0), "
          f"mean|chi|={sum(abs(c) for c in ch01) / 5:.6f} (expect 0.2)")
    ok &= (abs(q01) < 1e-12
           and abs(sum(abs(c) for c in ch01) / 5 - 0.2) < 1e-12)
    # block engine == full-space engine over 300 steps (both scenarios, gamma=0.1)
    for scen in (False, True):
        rb = run(scen, 0.1, defect="site", n_steps=300, engine="block")
        rf = run(scen, 0.1, defect="site", n_steps=300, engine="full")
        keys = ["mean_edge_coherence", "Q_winding", "Q_wrapped", "ring_population",
                "center_population", "mean_ring_C", "C0", "C3"]
        diff = max(abs(a[k] - b[k]) for a, b in zip(rb, rf) for k in keys)
        print(f"[verify] block==full over 300 steps ({'S-02' if scen else 'S-01'}): "
              f"max diff = {diff:.2e}")
        ok &= diff < 1e-10
    print(f"[verify] ALL CHECKS PASSED: {ok}")
    return ok

# ------------------------- output -------------------------

TRAJ_COLS = ["tau", "gamma", "Q_winding", "Q_wrapped", "ring_population", "center_population",
             "mean_ring_C", "C0", "C1", "C2", "C3", "C4", "C5",
             "mean_edge_coherence", "min_edge_coherence",
             "phase_1", "phase_2", "phase_3", "phase_4", "phase_5"]

def write_csv(fname, cols, rows):
    with open(os.path.join(HERE, fname), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})

def main():
    ok = verify()
    if not ok:
        print("VERIFICATION FAILED -- aborting, no CSV written.")
        sys.exit(1)
    print("\n== reference trajectories (gamma = 0.1) ==")
    s01 = run(False, GAMMA_TRAJ, defect="site")
    s02 = run(True, GAMMA_TRAJ, defect="site")
    s04 = run(True, GAMMA_TRAJ, defect="edge-phase")
    write_csv("D05_S01_trajectory.csv", TRAJ_COLS, s01)
    write_csv("D05_S02_trajectory.csv", TRAJ_COLS, s02)
    write_csv("D05_S04_edge_phase_trajectory.csv", TRAJ_COLS, s04)
    print("  S-01 / S-02 / S-04 trajectories written.")

    def sweep(defect, fname, label):
        print(f"== gamma sweep ({label}) ==")
        rows = []
        for g in GAMMA_SWEEP:
            r = run(True, float(g), defect=defect)
            below_mean = next((x["tau"] for x in r if x["mean_edge_coherence"] < EPS), "")
            below_min = next((x["tau"] for x in r if x["min_edge_coherence"] < EPS), "")
            valid_taus = [x["tau"] for x in r if x["min_edge_coherence"] >= EPS]
            tail = [x for x in r if x["tau"] > 20]
            rows.append(dict(
                gamma=float(g),
                first_tau_mean_edge_coherence_below_1e_3=below_mean,
                first_tau_min_edge_coherence_below_1e_3=below_min,
                last_tau_valid_Q=valid_taus[-1] if valid_taus else "",
                tail_mean_ring_population_tau_gt20=sum(x["ring_population"] for x in tail) / len(tail),
                tail_mean_ring_C_tau_gt20=sum(x["mean_ring_C"] for x in tail) / len(tail),
                Q_winding_tau10=min(r, key=lambda x: abs(x["tau"] - 10))["Q_winding"],
                Q_winding_tau20=min(r, key=lambda x: abs(x["tau"] - 20))["Q_winding"],
                Q_winding_tau100=r[-1]["Q_winding"],
            ))
        write_csv(fname,
                  ["gamma", "first_tau_mean_edge_coherence_below_1e_3",
                   "first_tau_min_edge_coherence_below_1e_3", "last_tau_valid_Q",
                   "tail_mean_ring_population_tau_gt20", "tail_mean_ring_C_tau_gt20",
                   "Q_winding_tau10", "Q_winding_tau20", "Q_winding_tau100"], rows)
        print("  written:", fname)

    sweep("site", "D05_S03_gamma_sweep.csv", "S-03, site defect")
    sweep("edge-phase", "D05_S04_gamma_sweep.csv", "S-04, edge-phase defect")

    kt = []
    for name, rows in (("S-01", s01), ("S-02", s02), ("S-04", s04)):
        for t in KEY_TAUS:
            match = min(rows, key=lambda r: abs(r["tau"] - t))
            kt.append(dict(scenario=name, **{c: match[c] for c in TRAJ_COLS if c != "gamma"}))
    write_csv("D05_key_times_comparison.csv", ["scenario"] + TRAJ_COLS, kt)
    print("  key-times written.")

    summ = []
    for name, rows, defect in (("S-01", s01, "none"),
                               ("S-02", s02, "site-detuning 0.1284"),
                               ("S-04", s04, "edge-phase flux 0.1284")):
        r20 = min(rows, key=lambda r: abs(r["tau"] - 20))
        below = next((r["tau"] for r in rows if r["min_edge_coherence"] < EPS), "")
        summ.append(dict(scenario=name, gamma=GAMMA_TRAJ, defect=defect,
                         Q_wrapped_tau0=rows[0]["Q_wrapped"],
                         Q_wrapped_final=rows[-1]["Q_wrapped"],
                         ring_population_final=rows[-1]["ring_population"],
                         center_population_final=rows[-1]["center_population"],
                         mean_edge_coherence_tau20=r20["mean_edge_coherence"],
                         first_tau_below_1e_3=below,
                         mean_edge_coherence_final=rows[-1]["mean_edge_coherence"]))
    write_csv("D05_scenario_summary.csv",
              ["scenario", "gamma", "defect", "Q_wrapped_tau0", "Q_wrapped_final",
               "ring_population_final", "center_population_final",
               "mean_edge_coherence_tau20", "first_tau_below_1e_3",
               "mean_edge_coherence_final"], summ)
    print("  summary written.")

    print("\n== headline numbers ==")
    lives = {}
    for name, rows in (("S-01", s01), ("S-02", s02), ("S-04", s04)):
        below = next((r["tau"] for r in rows if r["mean_edge_coherence"] < EPS), None)
        lives[name] = below if below is not None else rows[-1]["tau"]
        qv = next((r["tau"] for r in rows if r["min_edge_coherence"] < EPS), None)
        print(f"  {name}: mean-link coherence lifetime (first crossing of 1e-3) = {lives[name]}"
              f" ; Q validity ends at tau = {qv}")
    print(f"  lifetime ratio S-02/S-01 = {lives['S-02'] / lives['S-01']:.4f}"
          f"  (acceptance criterion: > 2)")
    print(f"  lifetime ratio S-04/S-01 = {lives['S-04'] / lives['S-01']:.4f}"
          f"  (decisive D04 edge-phase protocol)")
    print("done.")

if __name__ == "__main__":
    if "--verify" in sys.argv:
        sys.exit(0 if verify() else 1)
    main()
