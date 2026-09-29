---
id: D02
title: Causal Bounds, Lieb-Robinson Velocity, and Tensor Causal Wedges
vault: VMC-QF_Vault
layer: 03_DYNAMICS_SOLITON
tags:
  - causality
  - lieb-robinson
  - causal-wedge
  - entanglement-entropy
  - tensor-networks
  - graph-speed-of-light
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
---

# D02: Causal Bounds, Lieb–Robinson Velocity, and Tensor Causal Wedges

---

## 1. Motivation and the emergent-causality principle (Pre-Geometric Causality)
In quantum field theory in continuous spacetime, microcausality is defined by the vanishing of commutators at spacelike separation:
$$
[\hat{\mathcal{O}}(x), \hat{\mathcal{O}}(y)] = 0 \quad \forall (x-y)^2 < 0
$$
In the **VMC-QF** framework:
1. **No background manifold (per A01):** there is no a priori metric $\eta_{\mu\nu}$ and no conventional light cone.
2. **Space as a graph:** the interaction substrate is a countable graph $\mathcal{G}=(\mathcal{V},\mathcal{E})$ of microcavities.
3. **Cadence time:** evolution is measured in the local rhythm $\tau$ of the cavities.

**Problem:** how does a universal speed cap for information transfer (the analogue of the speed of light $c$) and a pseudo-Lorentzian causal structure emerge from purely local graph dynamics?

---

## 2. Graph distance and the network metric
For any two subsystems or nodes $X, Y \subset \mathcal{V}$, the fundamental metric distance is the minimum length of connecting paths:
$$
d_{\mathcal{G}}(X, Y) \equiv \min_{x \in X, y \in Y} \mathrm{dist}_{\mathcal{G}}(x, y)
$$
where $\mathrm{dist}_{\mathcal{G}}(x, y)$, given the weighted edge structure $\kappa_{ij}$, is computed as:
$$
\mathrm{dist}_{\mathcal{G}}(x, y) = \min_{\gamma \in \mathcal{P}(x, y)} \sum_{e=(u,v) \in \gamma} \frac{\kappa_0}{\kappa_{uv}}
$$
- $\mathcal{P}(x, y)$: the class of all possible paths between $x$ and $y$ on the graph.
- $\kappa_0$: the standard reference coupling.
In the simplest homogeneous case, $\mathrm{dist}_{\mathcal{G}}(x, y)$ is simply the minimum number of edge hops between the two nodes.

---

## 3. The Lieb–Robinson bound on the cavity network
Assume the system evolves under a local dynamical generator or network Hamiltonian $\hat{H}$ (derived in D01):
$$
\hat{H} = \sum_{x \in \mathcal{V}} \hat{h}_x + \sum_{\langle x, y \rangle \in \mathcal{E}} \hat{h}_{xy}
$$
where the edge-coupling potential has finite range and a bounded norm:
$$
\|\hat{h}_{xy}\| \le \kappa_{\max}
$$

### 3.1. Commutator bound in the Heisenberg picture
For two local operators $\hat{\mathcal{O}}_A$ (supported on $A \subset \mathcal{V}$) and $\hat{\mathcal{O}}_B$ (supported on $B \subset \mathcal{V}$):
$$
\left\| [\hat{\mathcal{O}}_A(\tau), \hat{\mathcal{O}}_B(0)] \right\| \;\le\; 2 \, \|\hat{\mathcal{O}}_A\| \, \|\hat{\mathcal{O}}_B\| \, C_0 \sum_{x \in A, y \in B} \exp\left( -\frac{d_{\mathcal{G}}(x, y) - v_{\mathrm{LR}} |\tau|}{\xi} \right)
$$
where:
- $\xi > 0$: the network correlation length (of order 1 graph step).
- $C_0$: a dimensionless structural constant.
- $v_{\mathrm{LR}}$: the **graph Lieb–Robinson velocity** (graph steps per unit cadence time).

---

## 4. Explicit derivation of the effective speed of light ($v_{\mathrm{LR}}$)
The maximum information-propagation rate is extracted from the maximum interaction power of a node with its neighbors:
$$
s \equiv \sup_{i \in \mathcal{V}} \sum_{j \in \mathcal{N}(i)} \|\hat{h}_{ij}\| \le z_{\max} \, \kappa_{\max}
$$
where $z_{\max}$ is the maximum local coordination number (node degree) in the graph.

The maximum linear speed of information propagation on the manifold-free graph is:
$$
v_{\mathrm{LR}} = 2 \, e \, \xi \, s = 2 \, e \, \xi \, z_{\max} \, \kappa_{\max} \quad [\text{hops} / \tau_c]
$$
If a physical emerged length scale $a_0$ is assigned to each graph step in the dense-chain limit, the effective physical speed of light follows:
$$
c_{\mathrm{eff}} \equiv v_{\mathrm{LR}} \cdot a_0 = 2 \, e \, z_{\max} \, \kappa_{\max} \, a_0
$$
- For symmetric 5-around-1 clusters ($z = 5$ per G01):
$$
c_{\mathrm{eff}}^{(5)} \approx 10 \, e \, \kappa_{\max} \, a_0 \approx 27.18 \, \kappa_{\max} \, a_0
$$

> **Emergent-causality principle:** no physical signal, entropic evolution, or state change can influence distances $d_{\mathcal{G}} > v_{\mathrm{LR}} \tau$ with a rate exceeding the Lieb–Robinson exponential tail. The causal structure therefore needs no aether or a priori manifold; the speed of light is the saturation cap of edge interaction.

---

## 5. Causal and entanglement wedges of tensors

### 5.1. Graph causal cone (Causal Cone)
For any region $\Omega \subset \mathcal{V}$, the forward causal cone $\mathcal{C}^+(\Omega, \tau)$ is partitioned using the quantum accuracy threshold $\epsilon \ll 1$:
$$
\mathcal{C}^+(\Omega, \tau) \equiv \left\{ j \in \mathcal{V} \;\middle|\; d_{\mathcal{G}}(j, \Omega) \le v_{\mathrm{LR}} \tau + \xi \ln\left(\frac{1}{\epsilon}\right) \right\}
$$
For any local operator $\hat{\mathcal{T}}_k$ at node $k \notin \mathcal{C}^+(\Omega, \tau)$:
$$
\| [\hat{\mathcal{T}}_k(\tau), \hat{\mathcal{O}}_\Omega(0)] \| \le \mathcal{O}(\epsilon) \approx 0 \quad \Longrightarrow \quad \text{No-Signaling}
$$

### 5.2. Causal wedge versus entanglement wedge
Defining the balance entropy on the basis of axiom A03:
$$
\mathcal{B}_i \equiv S(\hat{\rho}_i) = -\mathrm{Tr}(\hat{\rho}_i \ln \hat{\rho}_i)
$$
1. **Causal wedge ($\mathcal{W}_{\mathrm{causal}}(A)$):** the region swept by the boundary rays of the Lieb–Robinson velocity:
   $$
   \mathcal{W}_{\mathrm{causal}}(A) = \mathcal{C}^-(A) \cap \mathcal{C}^+(A)
   $$
2. **Entanglement wedge ($\mathcal{W}_{\mathrm{ent}}(A)$):** the region whose boundary is set by the minimum entanglement flux of edges under a minimal cut (Minimal Cut / RT surface):
   $$
   S(A) = \min_{\gamma_A} \sum_{e \in \gamma_A} \mathcal{C}_e
   $$
   where $\mathcal{C}_e$ is the entanglement capacity of edge $e$.
3. **Causal inclusion theorem:**
   $$
   \mathcal{W}_{\mathrm{causal}}(A) \subseteq \mathcal{W}_{\mathrm{ent}}(A)
   $$
   This asymmetry guarantees that operator reconstruction inside the causal wedge is always uniquely possible through the boundary density matrix in the entanglement wedge.

---

## 6. Emergence of the stress tensor $T_{\mu\nu}$ from cadence balancing
The stress-energy tensor $T_{\mu\nu}$ is not a primary entity; it is a representation of the balance flux across the boundary of the causal wedge:
1. **Balance flux on the causal boundary:**
   $$
   \frac{d S_{\mathrm{ent}}}{d\tau} = \sum_{e \in \partial \mathcal{C}(\Omega)} \mathcal{J}_e^{\mathrm{info}}
   $$
2. **Cadence–entropy relation (Jacobson-like Equilibrium):**
   with the local cadence temperature $T_{\mathrm{cad}} \equiv \frac{\hbar}{\tau_c}$:
   $$
   \delta \mathcal{Q}_{\mathrm{cad}} = T_{\mathrm{cad}} \, dS_{\mathrm{ent}}
   $$
3. **Tensorial matching in the continuum-chain limit:**
   mapping the cadence-advance vector to the local null vector $k^\mu$:
   $$
   \sum_{e \in \partial \mathcal{C}} \mathcal{J}_e^{\mathrm{info}} \;\xrightarrow{\text{Continuum}}\; \frac{1}{\hbar} \int_{\partial \Omega} T_{\mu\nu} k^\mu d\Sigma^\nu
   $$
   Thus the energy-momentum tensor is an abstract component of the information-current density and residue phases.

---

## 7. Effect of the 5-around-1 frustration on causal coverage and the Shapiro delay
Based on the phase-defect structure of G01, the presence of a five-fold cluster with angular deficit $\delta\theta \approx 7.356^{\circ}$ modifies the causal propagation structure:
1. **Phase-residue modulation of the coupling:**
   the effective edge coupling in the frustrated cycle is reduced by destructive interference:
   $$
   \kappa_{\mathrm{eff}} = \kappa_0 \cos\left(\frac{\delta\theta}{2}\right)
   $$
2. **Local reduction of the Lieb–Robinson velocity:**
   $$
   v_{\mathrm{LR}}^{\mathrm{defect}} = 2 \, e \, z \, \kappa_{\mathrm{eff}} \, a_0 < v_{\mathrm{LR}}^{\mathrm{flat}}
   $$
3. **Emergence of the graph Shapiro delay:**
   any phaseor wave packet or informational signal passing near a five-fold defect requires additional cadence time:
   $$
   \Delta \tau_{\mathrm{delay}} = \int_{\text{path}} \left( \frac{1}{v_{\mathrm{LR}}(x)} - \frac{1}{v_{\mathrm{LR}}^{(0)}} \right) dx > 0
   $$
   This local slowing is the primary manifestation of **gravitational curvature** in a manifold-free space.

---

## 8. Falsification criteria
The D02 model and assumptions are falsified if:
1. **Commutator-bound violation:** interaction or informational leak is observed at $d_{\mathcal{G}} > v_{\mathrm{LR}} \tau$ with a strength exceeding the exponential tail.
2. **Speed–degree non-compliance:** the propagation speed of the causal wavefront is independent of the node degree $z$ or the cavity coupling $\kappa$.
3. **No Shapiro delay in the five-fold cluster:** numerical simulation of the model shows that the phaseor-residue cycle ($\delta\theta$) does not slow signal propagation.
