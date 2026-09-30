---
id: S03
title: Topological and Memory Scaling
vault: VMC-QF_Vault
layer: 04_SCALE_TRANSITION
status: ratified
language: en
tags:
  - topological_transport
  - memory_scaling
  - defect_network
  - phase_hydrodynamics
cross_references:
  - "[G01_Five_Around_One_Deficit](../02_GEOMETRY_TOPOLOGY/G01_Five_Around_One_Deficit.md)"
  - "[D03_Topological_Soliton_Formation](../03_DYNAMICS_SOLITON/D03_Topological_Soliton_Formation.md)"
  - "[D04_Minimal_Simulatable_Soliton_Model](../03_DYNAMICS_SOLITON/D04_Minimal_Simulatable_Soliton_Model.md)"
  - "[D05_Cluster_Simulation_and_Validation](../03_DYNAMICS_SOLITON/D05_Cluster_Simulation_and_Validation.md)"
  - "[S01_Scale_Bridge_Definitions](S01_Scale_Bridge_Definitions.md)"
  - "[S02_Effective_Dynamics_and_Causality](S02_Effective_Dynamics_and_Causality.md)"
---

# S03: Topological and Memory Scaling

## 1. Topological-charge transport and stability at the multi-cluster scale
- The localized phase solitons introduced in [D03_Topological_Soliton_Formation](../03_DYNAMICS_SOLITON/D03_Topological_Soliton_Formation.md) act as carriers of continuous topological charge ($Q_{\text{eff}}$) between clusters:
  $$Q_{\text{eff}} = \frac{1}{2\pi} \oint_{\mathcal{C}} \nabla \theta \cdot d\mathbf{r} \in \mathbb{Z}$$
- **Memory scaling law:** the candidate-model simulation in [D05_Cluster_Simulation_and_Validation](../03_DYNAMICS_SOLITON/D05_Cluster_Simulation_and_Validation.md) showed that linear interactions without cadence feedback suffer instability at step 32. With self-consistent Kerr feedback ($\chi_{\text{eff}}$) and cadence feedback $\beta$, the stability time of the topological charge follows a power-law scale:
  $$\tau_{\text{life}}(N, \beta) = \tau_0 \cdot N^{\alpha} \exp\left( \frac{\beta}{\beta_c} \right)$$
  where $N$ is the number of active clusters, $\alpha \approx 1.42$ the critical scaling exponent, and $\beta_c$ the error-correction activation threshold. *(Status: model-level scaling hypothesis derived from the candidate run; not yet validated by the full CPTP protocol.)*

---

## 2. Pinning dynamics on the defect network (Defect Pinning & Percolation)
- Per the angular-defect geometry of [G01_Five_Around_One_Deficit](../02_GEOMETRY_TOPOLOGY/G01_Five_Around_One_Deficit.md) with deficit $\delta = 0.1284 \ \text{rad}$, each defect vertex produces a potential well for a soliton with winding number $W=1$:
  $$U_{\text{pin}}(\delta) = \hbar \kappa_{\max} (1 - \cos\delta) \approx \frac{1}{2} \hbar \kappa_{\max} \delta^2$$
- This potential prevents free migration and dissipation of the soliton at open network edges.
- **Defect-network percolation threshold ($\rho_c$):** in a random multi-cluster network, the condition for forming continuous phase-transport paths and avoiding excessive trapping (localization) is set by the critical surface density of defect-bearing nodes:
  $$\rho_{\text{defect}} < \rho_c \approx 0.4075$$
  If $\rho > \rho_c$, the network collapses into the isolated phase (cluster fragmentation) and the topological charge becomes trapped (confirming index 4 of [S04_Metrics_Criteria_and_Falsification](S04_Metrics_Criteria_and_Falsification.md)).
  *(E4 correction, 2026-09-30, battery-caught: the previously registered $\rho_c \approx 0.382$ had no traceable source and is superseded by the measured spanning-crossing value 0.4075 — L=64, 300 seeds, matching $1 - p_c^{\text{site}}$ of the square lattice = 0.4073. See Record VMC-QF-Vault-13 in [S04_Metrics_Criteria_and_Falsification](S04_Metrics_Criteria_and_Falsification.md).)*

---

## 3. Transition to causal phase hydrodynamics (Continuum Phase Hydrodynamics)
In the continuum limit, averaging over time scales much larger than the cadence clock ($\tau \gg \tau_0$), the discrete phase variables $\theta_i$ and field amplitude $|\psi_i|^2$ convert into the charge density $\rho_\theta(\mathbf{r}, t)$ and the phase-velocity field $\mathbf{v}_\theta(\mathbf{r}, t) = \frac{\hbar}{m_{\text{eff}}} \nabla \theta$.

### 3.1. Phase-charge density conservation equation
$$\frac{\partial \rho_\theta}{\partial t} + \nabla \cdot \mathbf{j}_\theta = -\Gamma_{\text{leak}} (\mathbf{r}) \, \rho_\theta$$
where $\mathbf{j}_\theta = \rho_\theta \mathbf{v}_\theta$ is the phase-current density and $\Gamma_{\text{leak}}$ the source/sink term from radiative leakage at open environment boundaries.

### 3.2. Hydrodynamic momentum equation (dissipative Euler–Madelung)
The evolution of the phase velocity under defect-pinning potentials and the self-consistent nonlinear force converges to:
$$\frac{\partial \mathbf{v}_\theta}{\partial t} + (\mathbf{v}_\theta \cdot \nabla) \mathbf{v}_\theta = -\frac{1}{m_{\text{eff}}} \nabla \left[ U_{\text{pin}}(\mathbf{r}) + g_{\text{eff}} \rho_\theta - \frac{\hbar^2}{2 m_{\text{eff}}} \frac{\nabla^2 \sqrt{\rho_\theta}}{\sqrt{\rho_\theta}} \right] + \nu_{\text{eff}} \nabla^2 \mathbf{v}_\theta$$
where:
- $m_{\text{eff}} = \frac{\hbar}{2 \kappa_{\max} a_0^2}$ is the effective inertial mass of the phase soliton.
- The bracketed terms are, in order: the Shapiro-delay pinning potential, the Kerr self-interaction pressure term, and the Bohm quantum potential.
- $\nu_{\text{eff}}$ is the effective kinematic viscosity, damping instabilities at velocities above $v_{\text{LR}}$.
