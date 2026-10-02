# VMC-QF — Vacuum Microcavity Quantum Foam

> **A manifold-free quantum substrate: microcavity networks, discrete cadence time, and topological solitons on a five-around-one geometric frustration.**
>
> VMC-QF is a self-contained theoretical vault: it builds emergent spacetime structure — metric, causality, particles — from a discrete graph of finite-dimensional quantum cavities with intrinsic cadence time, without assuming any background manifold.

**Author:** Adel Gachkar (ORCID: [0009-0006-7713-6004](https://orcid.org/0009-0006-7713-6004) · adelgachkar@gmail.com)
**License:** MIT · **Status:** revised-draft / candidate (see per-note frontmatter) · **Language:** English

---

## Architecture (reading order)

> **Start here:** [00_MOC/Index](00_MOC/Index.md) — the full map of content (14 notes, statuses, data map, and three suggested paths through the vault).

| Layer | Note | Content |
|---|---|---|
| **00 MOC** | [00_MOC/Index](00_MOC/Index.md) Index | navigation, per-note statuses, data map, falsification chain | 
| **00 Core Axioms** | [A01](00_CORE_AXIOMS/A01_Manifold_Free_Substrate.md) Manifold-Free Substrate | graph substrate, finite local Hilbert space, coupling budget, cadence time, metric emergence |
| | [A02](00_CORE_AXIOMS/A02_Microcavity_Quantization.md) Microcavity Quantization | truncated oscillator, Pegg–Barnett phase, phase debt, reactive energy |
| | [A03](00_CORE_AXIOMS/A03_Balance_Principle.md) Balance Principle | edge-flux accounting law, regional conservation, saturation control |
| | [A04](00_CORE_AXIOMS/A04_Cadence_Phase_Leak.md) Cadence & Phase Leak | memory kernel, bottleneck, reconstruction, effective cadence leak |
| **02 Geometry** | [G01](02_GEOMETRY_TOPOLOGY/G01_Five_Around_One_Deficit.md) Five-Around-One Deficit | angular deficit δθ = 7.356103°, loop holonomy, frustration potential, topological charge |
| **03 Dynamics** | [D01](03_DYNAMICS_SOLITON/D01_Cavity_Network_Hamiltonian.md) Network Hamiltonian | graph-local generator, CPTP/Lindblad/memory regimes, U(1) gauge structure |
| | [D02](03_DYNAMICS_SOLITON/D02_Causal_Bounds_and_Lieb_Robinson.md) Causal Bounds | Lieb–Robinson velocity, causal/entanglement wedges, graph Shapiro delay |
| | [D03](03_DYNAMICS_SOLITON/D03_Topological_Soliton_Formation.md) Soliton Formation | four-fold soliton definition, three stabilization mechanisms, nucleation/fusion/decay |
| | [D04](03_DYNAMICS_SOLITON/D04_Minimal_Simulatable_Soliton_Model.md) Minimal Model | 6-node qubit cluster, discrete-step CPTP circuit, twist injection |
| | [D05](03_DYNAMICS_SOLITON/D05_Cluster_Simulation_and_Validation.md) Simulation & Validation | open-channel protocol, experiment matrix S-01/02/03, falsification criteria |
| **04 Scale Transition** | [S01](04_SCALE_TRANSITION/S01_Scale_Bridge_Definitions.md) Scale Bridge | coarse-graining order parameters, conditional charge Q_eff |
| | [S02](04_SCALE_TRANSITION/S02_Effective_Dynamics_and_Causality.md) Effective Dynamics | mesoscopic Lindblad equation, effective Lieb–Robinson bound |
| | [S03](04_SCALE_TRANSITION/S03_Topological_and_Memory_Scaling.md) Topological Scaling | defect percolation, memory scaling law, phase hydrodynamics |
| | [S04](04_SCALE_TRANSITION/S04_Metrics_Criteria_and_Falsification.md) Metrics & Falsification | R_τ, v_ratio, S_Q indices; four scale-level falsification criteria |

Data: `_data/03_DYNAMICS_SOLITON/D05/` — exact CPTP trajectories and sweeps (S-01/S-02/S-04 + two γ-sweeps) + `simulate_D05_cptp.py` (exact engine, verification battery included). The earlier phenomenological script `simulate_D05.py` is retained as a historical record.

## Epistemic status (read first)

- **No empirical cosmological or experimental claim is made.** All quantitative results are model-level outputs of explicitly labeled simulation protocols (see the Execution Register in D05).
- The registered constants are **derived structural inputs of the five-around-one packing**: δθ = 2π − 5·arccos(1/3) = 7.356103° ≈ 0.1284 rad (complete tetrahedral derivation and machine verification in G01 §3); per-cell fractional charge δθ/2π = 0.0204336 (family label 0.02044). Used consistently across G01–S04.
- The D05 **exact CPTP execution (Record VMC-QF-Vault-11, 2026-09-30) confirms the "defect at least doubles the coherence lifetime" acceptance criterion at γ = 0.1** for both registered defect implementations: site detuning ratio 2.042, D04 edge-phase flux ratio 2.083 (verified block==full to ~10⁻¹³). The **relative-stability map (Record Vault-12)** then bounded the claim honestly: R(γ) erodes monotonically from ≈2.1 (weak-γ plateau) to ≈1.65 (γ = 0.5); the ×2 criterion survives to γ ≈ 0.3 and fails gradually beyond — no universal constant ratio is claimed. The **scale-feedback battery (Record Vault-14)** closed the last open criterion: with the D01 §8 saturation operator switched on, R_τ > 1 is dt-robust and genuine macro protection requires χ ≥ 2.0 J, while the dt crosscheck exposed that the Vault-13 baseline R_τ(β=0) = 0.965 was an engine-convention artifact (dt-converged value ≈ 2.06; E4 qualifier registered, history not erased). The **joint (γ, χ) map (Record Vault-15)** then bounded criterion 2 in the plane: the R_τ > 1 region is a narrow low-γ pocket (γ ≈ 0.02–0.10); above γ ≈ 0.10 the map is flat at R_τ ≈ 0.97–1.00 across the whole χ axis — feedback cannot buy macro advantage once dephasing exceeds the beat-revival scale — and all boundary curves are reported under both dt contracts (χ* and χ_gen are convention-sensitive; χ_gen = 2.0 at the reference point is not). The **beat-scale test (Record Vault-15q)** then measured the named mechanism: the pocket edge sits where Γ_env·τ_beat crosses 1 (0.709 → 0.966 → 1.795 across γ = 0.08/0.10/0.15, dt = 0.1 contract), with the twist-state beat period measured (3.288, ×4 the naive spectral bound — labeled) and the mechanism upgraded from named hypothesis to measured consistency with contract scope. The earlier negative reference run (section 8) and the phenomenological record (Vault-10) are retained as historical records. All in-silico, model-level — no experimental claim.
- Every layer carries its own explicit falsification criteria.

## Registered constants

| Constant | Value | Registered in |
|---|---|---|
| Angular deficit δθ | **2π − 5·arccos(1/3)** = 7.356103° = 0.1284 rad (derived, machine-verified) | G01 §3 |
| Per-cell fractional charge | δθ/2π = 0.0204336 (family label 0.02044) | G01 §4.3 |
| Coherence cutoff ε_cut | 10⁻³ | S01, D05, S04 |
| Defect percolation threshold ρ_c | ≈ 0.4075 (measured, L=64; supersedes untraceable 0.382) | S03, Vault-13 |
| Feedback strength for genuine macro gain χ_gen | **2.0 J** (dt-robust; near-threshold gain is denominator-driven, micro collapse at χ_collapse = 0.14) | S04, Vault-14 |
| dt-converged baseline R_τ(β=0) | ≈ **2.06** (the Vault-13 row 0.965 carries a beat-revival engine-convention qualifier) | S04, Vault-14 |
| Joint (γ, χ) stability pocket | R_τ > 1 confined to **γ ≈ 0.02–0.10**; flat R_τ ≈ 0.97–1.00 for γ ≥ 0.10 across the whole χ axis; boundary curves convention-sensitive (both dt contracts reported) | S04, Vault-15 |
| Beat-scale closure of the pocket edge | Γ_env·τ_beat = **0.709 → 0.966 → 1.795** across γ = 0.08/0.10/0.15 (dt = 0.1 contract); τ_beat = 3.288 measured (×4 the naive π/W bound — labeled); mechanism measured, contract-labeled | S04, Vault-15q |
| Critical scaling exponent α | ≈ 1.42 (model-level) | S03 |

## Citation

See [CITATION.cff](CITATION.cff). If you use this framework, please cite the Zenodo record (DOI badge above once published).

## Related family repositories

VMC-QF shares intellectual lineage — discrete substrates, cadence time, phase leak, and the 5-around-1 geometry — with the SDF family:

- [LIMEN-VACUI](https://github.com/adelgachkar/LIMEN-VACUI) — the Aligned Protocol (constraint × silence × event), canonical protocol home
- [SPUMA-VACUI](https://github.com/adelgachkar/SPUMA-VACUI) — vacuum-foam emergence of polarized cavities via dual boundary constraints
- [Emergence-SDF-Vault](https://github.com/adelgachkar/Emergence-SDF-Vault) — the master vault (30+ notes, full family register)
- [CADENCE-SDF](https://github.com/adelgachkar/CADENCE-SDF) — the canonical formalism edition (v3.5+)

*(VMC-QF itself is self-contained and readable without the family.)*

---

*This repository makes no acceptance, endorsement, or empirical claims; all statuses are logged exactly as registered in the notes' frontmatter.*
