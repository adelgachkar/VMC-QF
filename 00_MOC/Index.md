---
id: INDEX
title: VMC-QF Vault Index — Map of Content
vault: VMC-QF_Vault
layer: 00_MOC
tags:
  - index
  - moc
  - navigation
status: canonical
created: 2026-09-30
language: en
---

# VMC-QF Index — Map of Content

**What this vault is (one paragraph):** VMC-QF (Vacuum Microcavity Quantum Foam) builds emergent spacetime structure — metric, causality, particles — from a manifold-free substrate: a discrete graph of finite-dimensional quantum microcavities with intrinsic cadence time. The geometric seed is the five-around-one packing frustration (angular deficit δθ = 7.356103°); the dynamical carrier is a topological soliton on the 6-node cluster; the exit is a scale bridge to mesoscopic hydrodynamics. No empirical claim is made anywhere; every layer registers its own falsification criteria.

**Vault contents:** 14 notes in 4 layers · 1 data directory (7 CSV + 2 scripts + 2 logs) · README + CITATION.cff + .zenodo.json at the root.

---

## Status legend (per-note frontmatter)

| status | meaning |
|---|---|
| `revised-draft` | content complete after revision; not yet independently audited |
| `audited` | content independently checked (derivations and conventions) |
| `candidate` | protocol or result registered but awaiting confirmation/scaling |
| `ratified` | stabilized after audit; treated as the working canon of the vault |

---

## Reading order (14 notes)

### Layer 00 — Core Axioms (substrate)

| # | Note | Status | What it registers |
|---|---|---|---|
| 1 | [[A01_Manifold_Free_Substrate\|A01 — Manifold-Free Substrate]] | revised-draft | graph substrate, finite local Hilbert space, coupling budget, cadence time, metric-emergence protocol |
| 2 | [[A02_Microcavity_Quantization\|A02 — Microcavity Quantization]] | revised-draft | truncated oscillator, Pegg–Barnett phase, phase debt, reactive energy |
| 3 | [[A03_Balance_Principle\|A03 — Balance Principle]] | revised-draft | edge-flux accounting law, regional conservation, saturation control |
| 4 | [[A04_Cadence_Phase_Leak\|A04 — Cadence & Phase Leak]] | revised-draft | memory kernel, bottleneck, reconstruction, effective cadence leak γ |

### Layer 02 — Geometry & Topology (the seed)

| # | Note | Status | What it registers |
|---|---|---|---|
| 5 | [[G01_Five_Around_One_Deficit\|G01 — Five-Around-One Deficit]] | audited | complete derivation δθ = 2π − 5·arccos(1/3) = 7.356103° = 0.1284 rad (§3, machine-verified); per-cell fractional charge 0.0204336; loop holonomy gauge invariance + sector quantization; frustration potential; self-induced chirality |

### Layer 03 — Dynamics & Soliton (the carrier)

| # | Note | Status | What it registers |
|---|---|---|---|
| 6 | [[D01_Cavity_Network_Hamiltonian\|D01 — Network Hamiltonian]] | revised-draft | graph-local generator, CPTP/Lindblad/memory regimes, U(1) gauge structure |
| 7 | [[D02_Causal_Bounds_and_Lieb_Robinson\|D02 — Causal Bounds]] | audited | Lieb–Robinson velocity, causal/entanglement wedges, graph Shapiro delay |
| 8 | [[D03_Topological_Soliton_Formation\|D03 — Soliton Formation]] | audited | four-fold soliton definition, three stabilization mechanisms, nucleation/fusion/decay |
| 9 | [[D04_Minimal_Simulatable_Soliton_Model\|D04 — Minimal Model]] | audited | 6-node qubit cluster, discrete-step CPTP circuit, twist injection, edge-phase defect |
| 10 | [[D05_Cluster_Simulation_and_Validation\|D05 — Simulation & Validation]] | candidate | open-channel protocol, experiment matrix S-01…S-04, acceptance criteria, Execution Register (Records Vault-10, Vault-11) |

### Layer 04 — Scale Transition (the exit)

| # | Note | Status | What it registers |
|---|---|---|---|
| 11 | [[S01_Scale_Bridge_Definitions\|S01 — Scale Bridge]] | candidate | coarse-graining order parameters, ε_cut = 10⁻³, conditional charge Q_eff |
| 12 | [[S02_Effective_Dynamics_and_Causality\|S02 — Effective Dynamics]] | ratified | mesoscopic Lindblad equation, effective Lieb–Robinson bound |
| 13 | [[S03_Topological_and_Memory_Scaling\|S03 — Topological Scaling]] | audited | defect percolation ρ_c ≈ 0.4075 (measured, Vault-13), memory scaling law, phase hydrodynamics |
| 14 | [[S04_Metrics_Criteria_and_Falsification\|S04 — Metrics & Falsification]] | audited | four scale criteria executed (Vault-13): causality ✓, balance ✓, lifetime-enhancement open (feedback operator missing), percolation ✓ with ρ_c corrected |

---

## Data & tools map (`_data/03_DYNAMICS_SOLITON/D05/`)

| file | what it is |
|---|---|
| `simulate_D05_cptp.py` | **exact CPTP engine** (64-dim reference engine + exact 6×6 production block; verification battery built in; `--verify` flag) |
| `verify_output.txt` / `run_output.txt` | verification-battery log / full production-run log |
| `D05_S01_trajectory.csv` | S-01 (no defect), γ = 0.1, 201 rows |
| `D05_S02_trajectory.csv` | S-02 (site detuning 0.1284), γ = 0.1 |
| `D05_S04_edge_phase_trajectory.csv` | S-04 (D04 edge-phase Peierls flux), γ = 0.1 |
| `D05_S03_gamma_sweep.csv` | S-03 sweep, γ = 0.01–0.50 |
| `D05_S04_gamma_sweep.csv` | S-04 sweep, γ = 0.01–0.50 |
| `D05_relative_stability_map.csv` / `.png` | Record Vault-12: R(γ) = τ_life(defect)/τ_life(null) map with sub-grid estimators (`relative_stability_map.py`) |

## Data & tools map (`_data/04_SCALE_TRANSITION/S04/`)

| file | what it is |
|---|---|
| `s04_scale_battery.py` | **Record Vault-13 engine** — four falsification criteria as executable tests (LR causality, lifetime enhancement, A03 balance residue, percolation + pinning) |
| `S04_battery_results.csv` | all registered measurements (7 tests, verdicts) |
| `S04_battery.png` | four-panel figure: causality, R_τ(β), balance residue convergence, percolation curve + pinning bars |
| `s04_battery_output.txt` | full run log (2026-09-30) |
| `D05_key_times_comparison.csv` | side-by-side key rows (S-01/S-02/S-04) |
| `D05_scenario_summary.csv` | per-scenario summary at final τ |
| `simulate_D05.py` | historical phenomenological script (retained, superseded) |

Current headline (Record VMC-QF-Vault-11 + Vault-12): lifetime ratio vs S-01 = **2.042** (site detuning) and **2.083** (edge-phase flux) at γ = 0.1 — the "defect at least doubles the coherence lifetime" criterion is confirmed in-silico, and the Vault-12 map bounds it honestly: R(γ) erodes from ≈2.1 to ≈1.65 across the sweep, with the ×2 criterion surviving to γ ≈ 0.3; see D05 §Execution Register for the verdicts and qualifications.

---

## The falsification chain (how the layers bind)

1. **Axiom/geometry-level:** A01–A04 state what would refute the substrate postulates (coupling-budget violation, balance-law break, cadence-leak scaling failure); G01 adds the arithmetic criterion — an independent recomputation must reproduce δθ = 2π − 5·arccos(1/3) (`_data/02_GEOMETRY_TOPOLOGY/G01/verify_G01_deficit.py`).
2. **Simulation-level:** D05 §6 — if the five-fold defect played no pinning role (Φ_ℓ decays as in the flat cluster), the minimal-model hypothesis is refuted. Current status: criterion confirmed at the reference γ (Vault-11) and mapped across the sweep range (Vault-12: R ≈ 2.1 → 1.65, ×2 surviving to γ ≈ 0.3).
3. **Scale-level:** S04 — four explicit criteria (R_τ, v_ratio, S_Q, percolation) that the bridge to mesoscopics must pass. **Executed 2026-09-30 (Vault-13):** causality (v_ratio = 0.40 ≤ 1) ✓ and A03 balance (residue within δ_tol) ✓; percolation ✓ with ρ_c corrected to 0.4075; the lifetime-enhancement criterion is **open-pending-feedback-operator** (R_τ = 0.965 flat — the vault currently registers no mechanism producing the scale-up enhancement, recorded as an honest negative). The chain is thereby closed for the linear-excitation engine: every criterion now has a measured value or an explicitly named missing mechanism.

---

## Three ways through the vault

- **Axiom-first (builder's path):** A01 → A02 → A03 → A04 → G01 → D01 → … → S04.
- **Simulation-first (checker's path):** D04 → D05 (protocol §3–6, Record Vault-11) → run `simulate_D05_cptp.py --verify` → S04 criteria.
- **Scale-first (physicist's path):** S01 → S02 → S03 → S04, then descend into D01–D03 for the microscopic justification.

---

## Root documents

- [[../README|README]] — architecture table, epistemic status, registered constants, family links
- `CITATION.cff` / `.zenodo.json` — citation and Zenodo metadata
- Family: [LIMEN-VACUI](https://github.com/adelgachkar/LIMEN-VACUI) · [SPUMA-VACUI](https://github.com/adelgachkar/SPUMA-VACUI) · [Emergence-SDF-Vault](https://github.com/adelgachkar/Emergence-SDF-Vault) · [CADENCE-SDF](https://github.com/adelgachkar/CADENCE-SDF)
