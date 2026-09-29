---
id: D03
title: Topological Soliton Formation in a Microcavity Hypergraph
vault: VMC-QF_Vault
layer: 03_DYNAMICS_SOLITON
tags:
  - soliton
  - topological-defect
  - phase-winding
  - chirality
  - memory-kernel
  - lieb-robinson
  - localization
  - emergent-particle
status: audited
created: 2026-09-27
audited: 2026-09-28
language: en
cross_references:
  - "[[A01_Manifold_Free_Substrate]]"
  - "[[A02_Microcavity_Quantization]]"
  - "[[A03_Balance_Principle]]"
  - "[[A04_Cadence_Phase_Leak]]"
  - "[[G01_Five_Around_One_Deficit]]"
  - "[[D01_Cavity_Network_Hamiltonian]]"
  - "[[D02_Causal_Bounds_and_Lieb_Robinson]]"
---

# D03: Topological Soliton Formation in a Microcavity Hypergraph

---

## 0. Motivation and the pre-geometric approach (Pre-Geometric Soliton)
In conventional quantum field theory, material particles (fermions/bosons) are defined as local excitations or topological solitons (such as skyrmions or monopoles) on a continuous manifold with differential structure.
In the **VMC-QF** framework:
- **No continuous spacetime (A01):** there is no a priori manifold, continuous Lagrangian, or spatial vector $x^\mu$.
- **Particle as an emergent structure:** a particle is a **stable informational-topological soliton**; a pattern of phase locking and coherence on a cluster of microcavities, characterized by a low-flux boundary, self-feedback memory, and holonomic defect.

---

## 1. Operational definition of a soliton on the graph
A configuration on a finite subset of nodes $\Omega_\Sigma \subset \mathcal{V}$ is called a **topological soliton $\Sigma$** if and only if the following four conditions hold:

1. **Finite support:**
   its spatial support is confined within a graph partition of finite radius $R_\Sigma$ around the soliton center $c_\Sigma$:
   $$
   c_\Sigma \equiv \arg\min_{i \in \Omega_\Sigma} \sum_{j \in \Omega_\Sigma} d_{\mathcal{G}}(i, j), \quad R_\Sigma \equiv \max_{j \in \Omega_\Sigma} d_{\mathcal{G}}(c_\Sigma, j) < \infty
   $$
2. **Cadence-attractor stability (Attractor Dynamics):**
   under local dynamical evolution (D01), the system state converges to an attractor subspace:
   $$
   \lim_{\tau \to \infty} \left\| \hat{\rho}_{\Omega_\Sigma}(\tau) - \hat{\rho}_{\Sigma}^\star \right\|_1 \le \varepsilon_{\text{fluct}}
   $$
3. **Dynamic isolation and boundary flux suppression:**
   the exchange rate of information and the entropy balance across the soliton boundary $\partial \Omega_\Sigma$ is suppressed to the minimum:
   $$
   \left| \sum_{e \in \partial \Omega_\Sigma} \mathcal{J}_e(\tau) \right| \le \varepsilon_\Sigma \ll \kappa_{\max}
   $$
4. **Nonzero invariant topological charge ($Q_\Omega \neq 0$):**
   it carries an irreducible phase-winding or loop holonomy number.

---

## 2. Edge holonomy and topological-charge quantization

### 2.1. Edge phase and loop holonomy (Loop Holonomy)
For every oriented edge $e=(i \to j)$ with complex coupling amplitude $\kappa_{ij} \in \mathbb{C}$, the link phase is:
$$
\phi_{ij} \equiv \arg(\kappa_{ij})
$$
For every oriented closed loop $\ell = (i_0 \to i_1 \to \dots \to i_n = i_0)$ in the first graph homology $H_1(\mathcal{G}, \mathbb{Z})$, the cadence holonomy is defined as:
$$
\Phi(\ell) \equiv \sum_{m=0}^{n-1} \phi_{i_m i_{m+1}} \pmod{2\pi}
$$
This phase is independent of local node-phaseor gauge transformations ($\hat{a}_i \to \hat{a}_i e^{i \theta_i}$) and constitutes the network's local gauge invariant.

### 2.2. Cluster topological charge ($Q_{\Omega}$)
For the cluster region $\Omega_\Sigma$ containing a basis of independent fundamental cycles $\{\ell_k\}_{k=1}^K \in H_1(\Omega_\Sigma, \mathbb{Z})$:
$$
Q_{\Omega} \equiv \frac{1}{2\pi} \sum_{k=1}^K m_k \, \Phi(\ell_k) \in \mathbb{Z}
$$
where the integer coefficients $m_k \in \{-1, +1\}$ are set by the chiral orientation of the loops. As long as the stability gap holds, $Q_\Omega$ is not a continuous number but the system's discrete invariant charge.

---

## 3. The three stability and formation mechanisms

### Mechanism A: confinement through neutralizing vortex currents (Flux Suppression & Circulating Currents)
Given the balance equation A03:
$$
\frac{d\mathcal{B}_i}{d\tau} = \sum_{j \in \mathcal{N}(i)} \left( \mathcal{J}_{j \to i} - \mathcal{J}_{i \to j} \right) + \mathcal{S}_i - \mathcal{L}_i + \mathcal{M}_i
$$
in the soliton core, instead of free leakage outward, the informational and phaseor fluxes organize into a closed loop (Chiral Loop Currents):
$$
\sum_{e \in \ell} \mathcal{J}_e \neq 0, \quad \text{but} \quad \sum_{e \in \partial \Omega_\Sigma} \mathcal{J}_e \approx 0
$$
This configuration confines the flux inside the cycle without requiring any classical attractive force.

### Mechanism B: self-stabilization through cadence memory locking (Memory-Locked Core)
Based on the memory kernel introduced in axiom A04:
$$
\mathcal{M}_i(\tau) = \int_0^\tau K_i(\tau - \tau') \, \Xi_i(\tau') \, d\tau'
$$
if the memory function $K_i(t)$ has a resonance at the intrinsic rhythm frequency of the soliton ($\omega_\Sigma \sim 1/\tau_c$), the causal kernel produces a negative phaseor feedback that suppresses local wave scattering and locks the wave packet in the discrete substrate.

### Mechanism C: pinning on the 5-around-1 geometric frustration (G01 Defect Pinning)
Per G01, the closed loop of five peripheral cavities faces a flat angular deficit:
$$
\delta\theta \approx 7.356^{\circ} \neq 0
$$
This frustration creates a local "phase-residue well." The soliton, by sitting on this cluster, ties its topological charge to the geometric frustration and minimizes the local free energy:
$$
V_{\mathrm{pinning}}(\Omega) \propto -\cos\left(\Phi(\ell_5) - \delta\theta\right)
$$
The structural frustration of G01 thus acts as the mass-generating and stabilizing nucleus.

---

## 4. Stability and causal-survival criteria

1. **Intra-cluster balance stability:**
   $$
   \left| \frac{d}{d\tau} \sum_{i \in \Omega_\Sigma} \mathcal{B}_i(\tau) \right| \le \varepsilon_1 \ll \kappa_0
   $$
2. **Effective spectral gap of the local dynamics ($\Delta_\Sigma$):**
   the Liouvillian/Hamiltonian superoperator of the local soliton evolution $\hat{\mathcal{L}}_\Sigma$ must have a positive spectral gap above the solitonic ground state:
   $$
   \Delta_\Sigma \equiv \mathrm{Re}(\lambda_1 - \lambda_0) \ge \Delta_{\min} > 0
   $$
   This gap prevents thermal fluctuations and the destruction of the soliton by weak background interactions.
3. **Compatibility with the Lieb–Robinson bound (D02):**
   any excitation or signal from the soliton at distances $d_{\mathcal{G}} > v_{\mathrm{LR}} \tau$ remains exponentially bounded and does not violate the emergent-causality principle:
   $$
   \| [ \hat{\mathcal{O}}_{\Omega_\Sigma}(\tau), \hat{\mathcal{O}}_B(0)] \| \le C \exp\left( -\frac{d_{\mathcal{G}}(\Omega_\Sigma, B) - v_{\mathrm{LR}} \tau}{\xi} \right)
   $$

---

## 5. Soliton interaction dynamics: nucleation, fusion, decay

1. **Nucleation:**
   occurs when the local flux or phase gradient reaches the critical threshold:
   $$
   |\Phi(\ell)| \ge \Phi_\star \equiv \pi
   $$
   At this point the excitation converts into a stable holonomic configuration with charge $Q = \pm 1$.
2. **Fusion and scattering (Fusion & Scattering):**
   upon collision of two solitons $\Sigma_1$ and $\Sigma_2$ within a shared causal cone:
   $$
   Q_{\mathrm{total}} = Q_1 + Q_2
   $$
   if $Q_1 + Q_2 = 0$, recombination and decay into cadence radiation waves with high boundary leakage is possible (annihilation).
3. **Decay:**
   soliton decay is possible only under the following conditions:
   - strong dominance of random phase leakage over memory feedback ($\mathcal{L}_i \gg \mathcal{M}_i$);
   - destruction or topological rearrangement of the underlying pinning defect in the graph.

---

## 6. Explicit falsification criteria
The D03 structural model and assumptions are falsified if:
1. **Instability of $Q_\Omega$:** under local-dynamics simulation, the loop holonomy decays rapidly and the charge $Q_\Omega$ vanishes without interaction with an opposite charge.
2. **Non-compliance with G01 frustration:** soliton stability on defect-free (flat) clusters is greater than or equal to that on five-fold clusters (negating the catalytic role of frustration).
3. **Violation of the D02 causal bound:** solitonic interaction could transfer information faster than the Lieb–Robinson bound.
