---
id: A01
title: Manifold-Free Quantum Substrate
vault: VMC-QF_Vault
layer: 00_CORE_AXIOMS
tags:
  - axiom
  - substrate
  - graph-state
  - discrete-cadence
  - metric-emergence
status: revised-draft
created: 2026-09-28
language: en
cross_references:
  - "[[A02_Microcavity_Quantization]]"
  - "[[A03_Balance_Principle]]"
  - "[[A04_Cadence_Phase_Leak]]"
  - "[[G01_Five_Around_One_Deficit]]"
---

# A01 — Manifold-Free Quantum Substrate

## 1) Axiomatic non-continuous substrate
The fundamental substrate of physics carries no background spacetime, no differentiable manifold, and no pre-defined metric. The fundamental structure is described solely by a countable quantum network given as a labeled graph $G = (V, E)$:
- $V = \{v_i\}_{i \in \mathbb{N}}$: a finite or countable set of nodes (microcavities).
- $E \subset V \times V$: the set of local interaction coupling edges.

### 1.1) System Hilbert space
For every finite subset of nodes $\Lambda \subset V$, the state space is the tensor product of finite-dimensional local spaces:
$$
\mathcal{H}_\Lambda = \bigotimes_{i \in \Lambda} \mathcal{H}_i, \quad \dim(\mathcal{H}_i) = d_i < \infty
$$
The state space of the full substrate is defined through the local $C^*$-algebra or an inductively built local structure (Inductive Limit / Quasi-local Algebra), avoiding the naive infinite tensor-product assumption that lacks well-defined topological properties.

---

## 2) Local interaction principles and the coupling budget
To guarantee structural locality and avoid unphysical action at a distance, two independent conditions are imposed:

1. **Locally finite topology:**
   The number of direct neighbors of each node is bounded by a structural cap:
   $$
   \operatorname{deg}(v_i) \le d_{\max} < \infty \quad \forall v_i \in V
   $$
2. **Finite coupling budget:**
   If $\kappa_{ij}$ is the amplitude or strength of direct coupling between two nodes, the interaction power of each node is bounded:
   $$
   \sum_{j \in \mathcal{N}(i)} |\kappa_{ij}|^2 \le \mathcal{K}_{\max} < \infty
   $$
   *(Note: this condition replaces continuum energy assumptions and directly sets up the validity of Lieb–Robinson bounds.)*

---

## 3) Intrinsic cadence instead of continuous time
Time is not an external independent parameter $t \in \mathbb{R}$; it is a discrete ordering of events or cadence steps ($\tau \in \mathbb{N}_0$) internal to the network.
- State evolution is applied on the substrate through a discrete completely positive trace-preserving (CPTP) map:
  $$
  \rho(\tau + 1) = \mathcal{E}(\rho(\tau))
  $$
- Any local time variable is an emergent quantity derived from counting the cycles of local phaseors in each microcavity:
  $$
  \Delta \tau_i \propto \frac{2\pi}{\omega_i}
  $$

---

## 4) Emergence of distance and the effective metric
Distance is not fundamental; it is a secondary structure that follows from local correlation or operator coupling:
1. **Informational / correlation distance:**
   For every pair of nodes $(v_i, v_j)$, the local graph distance is defined from coupling resistance or operator-level signaling:
   $$
   d_{\text{eff}}(i, j) \equiv -\ln \left( \frac{|\kappa_{ij}|}{\max_{k} |\kappa_{ik}|} \right) \quad (\text{for neighbors})
   $$
   and for farther nodes it is obtained as the shortest geodesic path on the resulting weighted graph.
2. **Passage to the continuum metric limit:**
   The emergence of a Riemannian metric $g_{\mu\nu}$ is possible only as a macroscopic (coarse-grained) approximation at scales much larger than the lattice cell scale ($L \gg \ell_{\text{sub}}$), and conditional on statistical homogeneity and local symmetry — not as a fundamental property of the substrate.

---

## 5) Compact geometric structure and the angular deficit (the 5-around-1 hypothesis)
- In a substrate with uniform connection degree, if the local edge arrangement forms a 5-fold cyclic symmetry around a central core, the network acquires a geometric coupling deficit relative to flat symmetric networks (such as the 6-fold honeycomb).
- This geometric deficit produces an incomplete phase and holonomic deviation, which will be the basis of topological charge storage in the cluster (detailed derivation in [[G01_Five_Around_One_Deficit]]).
