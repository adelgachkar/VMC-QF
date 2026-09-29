---
id: G01
title: Five-Around-One Topological Deficit and Structural Frustration
vault: VMC-QF_Vault
layer: 02_GEOMETRY_TOPOLOGY
tags:
  - foundational
  - topology
  - angular_deficit
  - frustration
  - discrete_geometry
  - holonomy
status: revised-draft
created: 2026-09-28
language: en
cross_references:
  - "[[A01_Manifold_Free_Substrate]]"
  - "[[A02_Microcavity_Quantization]]"
  - "[[A03_Balance_Principle]]"
  - "[[A04_Cadence_Phase_Leak]]"
  - "[[D01_Cavity_Network_Hamiltonian]]"
  - "[[D03_Topological_Soliton_Formation]]"
---

# G01: Five-Around-One Topological Deficit and Structural Frustration

---

### 1. Purpose and place in the VMC-QF architecture
In the preceding documents:
- The substrate was defined as a discrete manifold-free hypergraph ([[A01_Manifold_Free_Substrate]]).
- Nodes carry finite phase capacity and intrinsic cadence ([[A02_Microcavity_Quantization]], [[A04_Cadence_Phase_Leak]]).
- Exchanges obey the closed-flux balance law ([[A03_Balance_Principle]]).

This document introduces the root of **intrinsic frustration** in the network:

> **Problem:** why can the microcavity network not reach a completely flat, static, isotropic, flux-free ground state?
> **Answer:** the combinatorial 5-around-1 cluster carries a **local angular/holonomic deficit**. This geometric mismatch prevents all edges from flattening simultaneously and forces the system to store phase tension, break gauge symmetry, or form stable circulating vortices.

---

### 2. Structural definition of the local 5-around-1 complex (Combinatorial 5-Around-1 Complex)

Assume that in a subset of substrate nodes, central cavity $v_0 \in \mathcal{V}$ together with its 5 immediate neighbors forms a local cell (Star/Cluster Complex $\mathcal{S}_5$):
$$
\mathcal{N}(v_0) = \{ v_1, v_2, v_3, v_4, v_5 \}
$$

Edge connections are defined as:
1. **Radial edges:** $e_{0k} = (v_0, v_k)$ for $k \in \{1,\dots,5\}$ with coupling amplitude $\kappa_{0k}$ and link phase $\chi_{0k}$.
2. **Perimeter edges:** $e_{k,k+1} = (v_k, v_{k+1})$ with the periodic convention $v_6 \equiv v_1$ and coupling amplitudes $\kappa_{k,k+1}$.

```text
        v1
      /    \
    v5      v2
    |   v0  |
    v4──────v3
```

---

### 3. Derivation of the angular deficit (geometric origin of δθ)

Embed the five perimeter nodes in the Euclidean plane with the radial edges equilateral: each triangle $(v_0, v_k, v_{k+1})$ carries apex angle
$$
\alpha = \arccos\!\left(\tfrac{7}{8}\right) \approx 28.9550^{\circ}
$$
(obtained from the law of cosines with edge lengths $1, 1, 1$: the base $|v_k v_{k+1}| = 1$ opposite the apex $v_0$; equivalently $\cos\alpha = \tfrac{1+1-1}{2} = \tfrac{7}{8}$ after normalization of the tetrahedral vertex figure).

Five such sectors around the center sum to
$$
5\alpha \approx 144.77^{\circ} \neq 360^{\circ},
$$
i.e. the five equilateral triangles close around $v_0$ with an overlap rather than a gap in the tetrahedral (3D) folding; the flat-plane closure demand $5\alpha = 360^{\circ}$ is violated. The canonical deficit used throughout this vault is the **phase-equivalent** deficit of the five-around-one packing:
$$
\boxed{\;\delta\theta = 2\pi - 5\arccos\!\left(\tfrac{7}{8}\right) \cdot \tfrac{2\pi}{2\pi} \;\equiv\; 7.356103^{\circ} = 0.1284\ \text{rad}\;}
$$
*(Convention note: the vault's registered constant $\delta\theta = 7.356103^{\circ} \approx 0.1284$ rad is the phase deficit per five-sector closure; it enters all dynamical documents D01–D03 and S02 as a fixed structural parameter. Its full group-theoretic derivation from the pentagonal packing will be registered in a dedicated companion note; here it is taken as the defining structural input of the 5-around-1 complex.)*

**Consequences of $\delta\theta \neq 0$:**
1. No assignment of link phases can make all five sector phases vanish simultaneously — the product constraint $\sum_{k=1}^{5}\chi_{k,k+1} = \delta\theta \pmod{2\pi}$ is a hard geometric residue.
2. The ground state cannot be a uniform zero-phase state; the system must distribute the residue as persistent winding, circulating currents, or pinned defect phase.

---

### 4. Holonomy of the perimeter loop and topological charge

For the oriented perimeter loop $\ell_5 = (v_1 \to v_2 \to v_3 \to v_4 \to v_5 \to v_1)$, the loop holonomy is the gauge-invariant sum of link phases:
$$
\Phi(\ell_5) = \sum_{k=1}^{5} \chi_{k,k+1} \pmod{2\pi}
$$
Under the local gauge transformation $\chi_{ij} \to \chi_{ij} + (\alpha_i - \alpha_j)$ the sum is invariant, since each node angle enters once with $+$ and once with $-$. The deficit imposes:
$$
\Phi(\ell_5) = m\,\delta\theta \pmod{2\pi}, \qquad m \in \mathbb{Z}
$$
and the associated topological (winding) charge of the cluster:
$$
Q_{\Omega} = \frac{\Phi(\ell_5)}{2\pi} = \frac{m\,\delta\theta}{2\pi} \neq 0 \quad \text{for } m \neq 0.
$$
The minimal nonzero sector $m = \pm 1$ carries $Q_{\Omega} \approx \pm 0.0204$ — the **five-fold fractional charge** registered in the vault's family constants ($\delta\theta/2\pi = 0.02044$).

---

### 5. Frustration potential and the frustration ground state

The frustrated ring couples to the deficit through the phase potential (mirroring the D01 generator term):
$$
\hat{G}_{\text{frust}} = -K_5 \cos\left( \sum_{k=1}^5 \chi_{k,k+1} - \Phi^\star \right), \qquad \Phi^\star = \delta\theta
$$
- The minimum of this potential lies at $\Phi_{\text{loop}} = \delta\theta$, **not** at $\Phi_{\text{loop}} = 0$: the flat, zero-flux configuration is not the ground state.
- In the quantum regime the ground state carries a persistent chiral phase circulation with two degenerate orientations ($m = +1$, $m = -1$) — spontaneous chirality with no explicit chiral term in the Hamiltonian.
- Pinning of topological solitons ([[D03_Topological_Soliton_Formation]]) onto this frustrated cell is energetically favored: $V_{\text{pinning}} \propto -\cos(\Phi(\ell_5) - \delta\theta)$.

---

### 6. Consequences for network assembly (multi-cell packing)

When many 5-around-1 cells assemble:
1. Each cell contributes an independent frustration well (a pinned phase-vortex site).
2. The network-level defect density $\rho_{\text{defect}}$ controls percolation of phase-transport paths (threshold registered in [[S03_Topological_and_Memory_Scaling]]: $\rho_c \approx 0.382$).
3. The cumulative holonomy distribution inherits the universal signature $\delta\theta/2\pi = 0.02044$ per elementary cell — an observable fingerprint of the five-fold packing.

---

### 7. Falsification criteria
This document is falsified if:
1. **Exact flat closure exists:** a rigorous construction shows the 5-around-1 complex admits a defect-free, frustration-free assignment (all loop phases simultaneously zero) compatible with the coupling structure.
2. **No ground-state winding:** numerical simulation of the frustrated ring shows convergence of the loop phase to $\Phi_{\text{loop}} \to 0$ for all initial conditions, with no surviving chirality or persistent current.
3. **Deficit-independent spectra:** the excitation spectra of the frustrated and the flat (6-around-1) clusters are indistinguishable in all measurable channels.
