# VMC-QF — Vacuum Microcavity Quantum Foam

> **A manifold-free quantum substrate: microcavity networks, discrete cadence time, and topological solitons on a five-around-one geometric frustration.**
>
> VMC-QF is a self-contained theoretical vault: it builds emergent spacetime structure — metric, causality, particles — from a discrete graph of finite-dimensional quantum cavities with intrinsic cadence time, without assuming any background manifold.

**Author:** Adel Gachkar (ORCID: [0009-0006-7713-6004](https://orcid.org/0009-0006-7713-6004))
**License:** MIT · **Status:** revised-draft / candidate (see per-note frontmatter) · **Language:** English

---

## Architecture (reading order)

> **Start here:** [[00_MOC/Index]] — the full map of content (14 notes, statuses, data map, and three suggested paths through the vault).

| Layer | Note | Content |
|---|---|---|
| **00 MOC** | [[00_MOC/Index]] Index | navigation, per-note statuses, data map, falsification chain | 
| **00 Core Axioms** | [[A01]] Manifold-Free Substrate | graph substrate, finite local Hilbert space, coupling budget, cadence time, metric emergence |
| | [[A02]] Microcavity Quantization | truncated oscillator, Pegg–Barnett phase, phase debt, reactive energy |
| | [[A03]] Balance Principle | edge-flux accounting law, regional conservation, saturation control |
| | [[A04]] Cadence & Phase Leak | memory kernel, bottleneck, reconstruction, effective cadence leak |
| **02 Geometry** | [[G01]] Five-Around-One Deficit | angular deficit δθ = 7.356103°, loop holonomy, frustration potential, topological charge |
| **03 Dynamics** | [[D01]] Network Hamiltonian | graph-local generator, CPTP/Lindblad/memory regimes, U(1) gauge structure |
| | [[D02]] Causal Bounds | Lieb–Robinson velocity, causal/entanglement wedges, graph Shapiro delay |
| | [[D03]] Soliton Formation | four-fold soliton definition, three stabilization mechanisms, nucleation/fusion/decay |
| | [[D04]] Minimal Model | 6-node qubit cluster, discrete-step CPTP circuit, twist injection |
| | [[D05]] Simulation & Validation | open-channel protocol, experiment matrix S-01/02/03, falsification criteria |
| **04 Scale Transition** | [[S01]] Scale Bridge | coarse-graining order parameters, conditional charge Q_eff |
| | [[S02]] Effective Dynamics | mesoscopic Lindblad equation, effective Lieb–Robinson bound |
| | [[S03]] Topological Scaling | defect percolation, memory scaling law, phase hydrodynamics |
| | [[S04]] Metrics & Falsification | R_τ, v_ratio, S_Q indices; four scale-level falsification criteria |

Data: `_data/03_DYNAMICS_SOLITON/D05/` — exact CPTP trajectories and sweeps (S-01/S-02/S-04 + two γ-sweeps) + `simulate_D05_cptp.py` (exact engine, verification battery included). The earlier phenomenological script `simulate_D05.py` is retained as a historical record.

## Epistemic status (read first)

- **No empirical cosmological or experimental claim is made.** All quantitative results are model-level outputs of explicitly labeled simulation protocols (see the Execution Register in D05).
- The registered constants (δθ = 7.356103° ≈ 0.1284 rad; per-cell fractional charge δθ/2π ≈ 0.02044) are **structural inputs of the five-around-one packing**, used consistently across G01–S04.
- The D05 **exact CPTP execution (Record VMC-QF-Vault-11, 2026-09-30) confirms the "defect at least doubles the coherence lifetime" acceptance criterion at γ = 0.1** for both registered defect implementations: site detuning ratio 2.042, D04 edge-phase flux ratio 2.083 (verified block==full to ~10⁻¹³). The earlier negative reference run (section 8) and the phenomenological record (Vault-10) are retained as historical records. This remains an in-silico, model-level result — no experimental claim.
- Every layer carries its own explicit falsification criteria.

## Registered constants

| Constant | Value | Registered in |
|---|---|---|
| Angular deficit δθ | 7.356103° = 0.1284 rad | G01, D01, D02, D03, S02 |
| Per-cell fractional charge | δθ/2π ≈ 0.02044 | G01 |
| Coherence cutoff ε_cut | 10⁻³ | S01, D05, S04 |
| Defect percolation threshold ρ_c | ≈ 0.382 | S03 |
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
