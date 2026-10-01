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
| 1 | [A01 — Manifold-Free Substrate](../00_CORE_AXIOMS/A01_Manifold_Free_Substrate.md) | revised-draft | graph substrate, finite local Hilbert space, coupling budget, cadence time, metric-emergence protocol |
| 2 | [A02 — Microcavity Quantization](../00_CORE_AXIOMS/A02_Microcavity_Quantization.md) | revised-draft | truncated oscillator, Pegg–Barnett phase, phase debt, reactive energy |
| 3 | [A03 — Balance Principle](../00_CORE_AXIOMS/A03_Balance_Principle.md) | revised-draft | edge-flux accounting law, regional conservation, saturation control |
| 4 | [A04 — Cadence & Phase Leak](../00_CORE_AXIOMS/A04_Cadence_Phase_Leak.md) | revised-draft | memory kernel, bottleneck, reconstruction, effective cadence leak γ |

### Layer 02 — Geometry & Topology (the seed)

| # | Note | Status | What it registers |
|---|---|---|---|
| 5 | [G01 — Five-Around-One Deficit](../02_GEOMETRY_TOPOLOGY/G01_Five_Around_One_Deficit.md) | audited | complete derivation δθ = 2π − 5·arccos(1/3) = 7.356103° = 0.1284 rad (§3, machine-verified); per-cell fractional charge 0.0204336; loop holonomy gauge invariance + sector quantization; frustration potential; self-induced chirality |

### Layer 03 — Dynamics & Soliton (the carrier)

| # | Note | Status | What it registers |
|---|---|---|---|
| 6 | [D01 — Network Hamiltonian](../03_DYNAMICS_SOLITON/D01_Cavity_Network_Hamiltonian.md) | revised-draft | graph-local generator, CPTP/Lindblad/memory regimes, U(1) gauge structure |
| 7 | [D02 — Causal Bounds](../03_DYNAMICS_SOLITON/D02_Causal_Bounds_and_Lieb_Robinson.md) | audited | Lieb–Robinson velocity, causal/entanglement wedges, graph Shapiro delay |
| 8 | [D03 — Soliton Formation](../03_DYNAMICS_SOLITON/D03_Topological_Soliton_Formation.md) | audited | four-fold soliton definition, three stabilization mechanisms, nucleation/fusion/decay |
| 9 | [D04 — Minimal Model](../03_DYNAMICS_SOLITON/D04_Minimal_Simulatable_Soliton_Model.md) | audited | 6-node qubit cluster, discrete-step CPTP circuit, twist injection, edge-phase defect |
| 10 | [D05 — Simulation & Validation](../03_DYNAMICS_SOLITON/D05_Cluster_Simulation_and_Validation.md) | candidate | open-channel protocol, experiment matrix S-01…S-04, acceptance criteria, Execution Register (Records Vault-10, Vault-11) |

### Layer 04 — Scale Transition (the exit)

| # | Note | Status | What it registers |
|---|---|---|---|
| 11 | [S01 — Scale Bridge](../04_SCALE_TRANSITION/S01_Scale_Bridge_Definitions.md) | candidate | coarse-graining order parameters, ε_cut = 10⁻³, conditional charge Q_eff |
| 12 | [S02 — Effective Dynamics](../04_SCALE_TRANSITION/S02_Effective_Dynamics_and_Causality.md) | ratified | mesoscopic Lindblad equation, effective Lieb–Robinson bound |
| 13 | [S03 — Topological Scaling](../04_SCALE_TRANSITION/S03_Topological_and_Memory_Scaling.md) | audited | defect percolation ρ_c ≈ 0.4075 (measured, Vault-13), memory scaling law, phase hydrodynamics |
| 14 | [S04 — Metrics & Falsification](../04_SCALE_TRANSITION/S04_Metrics_Criteria_and_Falsification.md) | audited | four scale criteria executed: Vault-13 (causality ✓, balance ✓, percolation ✓ with ρ_c corrected) + Vault-14 (criterion 2 closed: R_τ > 1 with the D01 §8 feedback operator, genuine macro gain at χ ≥ 2.0; Vault-13 R_τ(β=0) = 0.965 carries a dt-convention qualifier — dt-converged baseline ≈ 2.06) + Vault-15 (joint (γ, χ) map: R_τ > 1 is a low-γ pocket γ ≈ 0.02–0.10, flat map for γ ≥ 0.10, boundaries under both dt contracts) + Vault-15q (beat-scale test: the pocket edge γ ≈ 0.10 sits where Γ_env·τ_beat crosses 1 under the dt=0.1 contract — finding 1's mechanism measured, contract-labeled) |

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
| `feedback_operator_battery.py` | **Record Vault-14 engine** — the D01 §8 nonlinear saturation operator applied to criterion 2 (χ scan, fine-grid collapse transition, dt crosscheck, S03 pin-well probe with gauge control) |
| `V14_feedback_scan.csv` | R_τ(χ) with macro/micro decomposition |
| `V14_dt_crosscheck.csv` | the same grid at dt = 0.1 — dt-robustness of the verdict + the R_τ(χ=0) FLIP row |
| `V14_pin_probe.csv` | S03 pin-well placements (no well / uniform control / site / edge) |
| `V14_feedback_scan.png` | three-panel figure: R_τ decomposition, lifetimes vs χ, pin-well bars |
| `v14_output.txt` | full Vault-14 run log (2026-09-30) |
| `feedback_gamma_chi_sweep.py` | **Record Vault-15 engine host** — two-parameter (γ, χ) sweep on the imported Vault-14 engine (no re-implementation), boundary extraction χ*/χ_gen/χ_collapse per γ, dt=0.1 replica |
| `V15_gamma_chi_map.csv` | primary 10×11 grid (γ, χ, τ_micro, τ_macro, R_τ, gains, censor flags) |
| `V15_dt01_replica.csv` | dt=0.1 replica on the coarse χ grid |
| `V15_boundary_curves.csv` | χ*/χ_gen/χ_collapse per γ under both dt contracts |
| `V15_gamma_chi_map.png` | two-panel figure: R_τ heatmap with R_τ=1 contour + the three boundary curves |
| `v15_output.txt` | full Vault-15 run log (2026-09-30) |
| `beat_scale_test.py` | **Record Vault-15q engine host** — beat-scale test of the pocket's upper edge (contrast-envelope decay vs the measured beat period, both dt contracts) |
| `V15q_beatscale.csv` | per-γ table: τ_beat, Γ_env (both contracts), the dimensionless group Γ_env·τ_beat, registered R_τ |
| `V15q_beatscale.png` | two-panel figure: Γ_env·τ_beat vs γ with the pocket shaded, next to the registered baseline R_τ |
| `v15q_output.txt` | full Vault-15q run log (2026-10-01) |
| `D05_key_times_comparison.csv` | side-by-side key rows (S-01/S-02/S-04) |
| `D05_scenario_summary.csv` | per-scenario summary at final τ |
| `simulate_D05.py` | historical phenomenological script (retained, superseded) |

Current headline (Record VMC-QF-Vault-11 + Vault-12): lifetime ratio vs S-01 = **2.042** (site detuning) and **2.083** (edge-phase flux) at γ = 0.1 — the "defect at least doubles the coherence lifetime" criterion is confirmed in-silico, and the Vault-12 map bounds it honestly: R(γ) erodes from ≈2.1 to ≈1.65 across the sweep, with the ×2 criterion surviving to γ ≈ 0.3; see D05 §Execution Register for the verdicts and qualifications.

---

## The falsification chain (how the layers bind)

1. **Axiom/geometry-level:** A01–A04 state what would refute the substrate postulates (coupling-budget violation, balance-law break, cadence-leak scaling failure); G01 adds the arithmetic criterion — an independent recomputation must reproduce δθ = 2π − 5·arccos(1/3) (`_data/02_GEOMETRY_TOPOLOGY/G01/verify_G01_deficit.py`).
2. **Simulation-level:** D05 §6 — if the five-fold defect played no pinning role (Φ_ℓ decays as in the flat cluster), the minimal-model hypothesis is refuted. Current status: criterion confirmed at the reference γ (Vault-11) and mapped across the sweep range (Vault-12: R ≈ 2.1 → 1.65, ×2 surviving to γ ≈ 0.3).
3. **Scale-level:** S04 — four explicit criteria (R_τ, v_ratio, S_Q, percolation) that the bridge to mesoscopics must pass. **Executed 2026-09-30 (Vault-13 + Vault-14):** causality (v_ratio = 0.40 ≤ 1) ✓ and A03 balance (residue within δ_tol) ✓; percolation ✓ with ρ_c corrected to 0.4075; the lifetime-enhancement criterion is **closed by Vault-14**: with the D01 §8 saturation operator switched on, R_τ > 1 holds in both dt conventions and **genuine macro protection requires χ ≥ 2.0** (dt-robust) — near threshold the gain is denominator-driven (micro instability at χ_collapse = 0.14), and the dt-converged baseline is R_τ(β=0) ≈ 2.06 (the Vault-13 value 0.965 was beat-revival-inflated by the coarse dephasing reconstruction; E4 qualifier registered, history not erased); **bounded in the plane by Vault-15**: the R_τ > 1 region is a narrow low-γ pocket (γ ≈ 0.02–0.10), the map is flat for γ ≥ 0.10, and the boundary curves are convention-sensitive (reported under both dt contracts). The chain is closed for the linear engine and for the engine + registered feedback operator: every criterion now has a measured value under a stated engine convention, with its region of validity mapped.

---

## Three ways through the vault

- **Axiom-first (builder's path):** A01 → A02 → A03 → A04 → G01 → D01 → … → S04.
- **Simulation-first (checker's path):** D04 → D05 (protocol §3–6, Record Vault-11) → run `simulate_D05_cptp.py --verify` → S04 criteria.
- **Scale-first (physicist's path):** S01 → S02 → S03 → S04, then descend into D01–D03 for the microscopic justification.

---

## Root documents

- [README](../README.md) — architecture table, epistemic status, registered constants, family links
- `CITATION.cff` / `.zenodo.json` — citation and Zenodo metadata
- Family: [LIMEN-VACUI](https://github.com/adelgachkar/LIMEN-VACUI) · [SPUMA-VACUI](https://github.com/adelgachkar/SPUMA-VACUI) · [Emergence-SDF-Vault](https://github.com/adelgachkar/Emergence-SDF-Vault) · [CADENCE-SDF](https://github.com/adelgachkar/CADENCE-SDF)
