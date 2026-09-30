---
id: A02
title: Microcavity Quantization and Finite Phase Capacity
vault: VMC-QF_Vault
layer: 00_CORE_AXIOMS
tags:
  - foundational
  - microcavity
  - quantization
  - phase_capacity
  - reactive_energy
status: revised-draft
created: 2026-09-28
language: en
cross_references:
  - "[A01_Manifold_Free_Substrate](A01_Manifold_Free_Substrate.md)"
  - "[A03_Balance_Principle](A03_Balance_Principle.md)"
  - "[A04_Cadence_Phase_Leak](A04_Cadence_Phase_Leak.md)"
  - "[D01_Cavity_Network_Hamiltonian](../03_DYNAMICS_SOLITON/D01_Cavity_Network_Hamiltonian.md)"
---

# A02 — Microcavity Quantization and Finite Phase Capacity

---

### 1. Motivation and role in the theory (Role in VMC-QF)
Following axiom [A01_Manifold_Free_Substrate](A01_Manifold_Free_Substrate.md), every node $v_i \in V$ of the network is a resonant, discrete physical entity called a **microcavity**. Microcavities have three fundamental properties:
1. **Finite-dimensional local state space:** unbounded continuity of degrees of freedom inside a node is not allowed.
2. **Finite storage and exchange capacity:** local phase and reactive energy are bounded, and their exchange through structural edges is subject to the coupling budget.
3. **Non-instantaneous response (cadence):** due to frequency selectivity and limited bandwidth, every node has delayed/memory-keeping behavior.

---

### 2. Axiom: finite local Hilbert space

> **Axiom 2:** every microcavity $v_i$ has a local Hilbert space of finite dimension:
> $$ \dim(\mathcal{H}_i) = d_i < \infty $$
> This dimension bound expresses the finite capacity of the system to distinguish energy states, store phase, and accumulate reactive energy.

---

### 3. Minimal model: truncated oscillator
For operational description, a minimal representation built on the occupation basis is chosen:
- **Truncated photonic basis:**
  $$\mathcal{H}_i = \operatorname{span}\{|n\rangle_i\}_{n=0}^{d_i-1}$$
- **Local number operator:**
  $$\hat{n}_i |n\rangle_i = n |n\rangle_i$$
- **Truncated ladder operators:**
  $$
  \hat{a}_i = \sum_{n=1}^{d_i-1} \sqrt{n}\, |n-1\rangle_i \langle n|_i, \qquad
  \hat{a}_i^\dagger = \sum_{n=0}^{d_i-2} \sqrt{n+1}\, |n+1\rangle_i \langle n|_i
  $$
  *(Note: at the upper edge $n = d_i - 1$ these operators break the canonical commutation relation of the infinite oscillator, which expresses the nonlinear saturation effect).*

---

### 4. Separation of closed dynamics and dissipation (Local Hamiltonian & Dissipation)
The local dynamics of a microcavity consists of two distinct parts: a unitary Hamiltonian part and incoherent leakage/decay channels:

#### 4.1) Local Hamiltonian (closed part)
$$
\hat{H}_i = \hbar\omega_i \hat{n}_i + \frac{U_i}{2} \hat{n}_i(\hat{n}_i - 1)
$$
- $\omega_i$: the local resonance frequency of the microcavity.
- $U_i$: the self-Kerr nonlinear coefficient (cost of occupying higher levels), which amplifies local saturation.

#### 4.2) Open channel and phase leak (non-unitary evolution)
Decay, cadence leak, and decoherence are not placed inside the Hamiltonian operator; rather, the local density operator $\rho_i$ evolves through a Lindblad-form or local CPTP map:
$$
\frac{d\rho_i}{d\tau} = -\frac{i}{\hbar}[\hat{H}_i, \rho_i] + \mathcal{D}_{\text{leak}}[\rho_i]
$$
where the details of the jump operators and cadence damping are defined in [A04_Cadence_Phase_Leak](A04_Cadence_Phase_Leak.md).

---

### 5. Definition of phase debt and local reactive energy (Phase Debt & Reactive Energy)

#### 5.1) Phase operator in finite space (Pegg–Barnett framework)
In the finite $d_i$-dimensional space, the Pegg–Barnett phaseor operator is built from angular phase bases:
$$
|\theta_m\rangle_i \equiv \frac{1}{\sqrt{d_i}} \sum_{n=0}^{d_i-1} \exp\left(i \frac{2\pi m n}{d_i}\right) |n\rangle_i, \quad m = 0, \dots, d_i - 1
$$
The effective local phaseor operator is formulated as $\widehat{E^{i\phi}_i} \equiv \sum_{m} e^{i\theta_m} |\theta_m\rangle\langle\theta_m|$.

#### 5.2) Phase-debt index ($\Pi_i$)
The local phase debt is defined as the incoherent fraction of the angular phase coherence:
$$
\Pi_i \equiv 1 - \left| \operatorname{Tr}\left(\rho_i \widehat{E^{i\phi}_i}\right) \right|
$$
- If the state is a fully coherent phase state: $\Pi_i \to 0$.
- If the state has no phase coherence, or is a random-occupation / maximally mixed density matrix: $\Pi_i \to 1$.

#### 5.3) Phase-capacity and reactive-energy bound
Because of the finite dimension $d_i$ and the nonlinear interaction, accumulating asymmetric phase requires storing energy. The local reactive energy is modeled as an increasing function of the phase debt:
$$
E_{\text{react}, i} \approx \chi_i \Pi_i^\alpha \quad (\alpha \ge 1)
$$
governed by the physical maximum bound $\Pi_{\max}(d_i) \le 1$.

---

### 6. Cadence, bandwidth, and memory kernel (Bandwidth–Q–Cadence Structure)

1. **Quality factor and time scale:**
   For every microcavity with linewidth $\Delta\omega_i$, the effective quality factor is $Q_i = \omega_i / \Delta\omega_i$. The stable local response time, following [A04_Cadence_Phase_Leak](A04_Cadence_Phase_Leak.md), scales as $\tau_{c,i} \sim 1/\Delta\omega_i$.
2. **Continuum approximation of the response kernel:**
   At time scales larger than the fundamental discrete steps, the delayed response kernel is formulated causally:
   $$
   K_i(\Delta\tau) = \Theta(\Delta\tau) A_i e^{-\gamma_i \Delta\tau} \cos(\omega_i \Delta\tau)
   $$
   where $\Theta$ is the Heaviside step function and $\gamma_i$ is the effective local damping width.

---

### 7. Exchange-budget bound on network edges
The finiteness of the local Hilbert space ($d_i$) and the bounded phase absorption/accumulation power prevent a node from interacting with an unlimited number of nodes at arbitrary strength:
$$
\sum_{j \in \mathcal{N}(i)} |\kappa_{ij}|^2 \le \kappa_{\max}^2(d_i) < \infty
$$
This consistency constraint is the bridge between the local cavity capacity (this document) and the structural coupling bound in [A01_Manifold_Free_Substrate](A01_Manifold_Free_Substrate.md).

---

### 8. Falsification criteria
This axiom loses its degree of validity upon any of the following events:
1. **Necessity of infinite dimension:** a proof that $d_i = \infty$ is absolutely required to reproduce stable soliton properties or the continuum limit.
2. **Coherence collapse below the stability threshold:** the inability of the phaseor operator to maintain quasi-classical behavior at conventional dimensions $d_i$.
3. **Empirical/computational violation of the coupling budget:** dynamic-structure instability when the bound $\kappa_{\max}(d_i)$ is not enforced.
