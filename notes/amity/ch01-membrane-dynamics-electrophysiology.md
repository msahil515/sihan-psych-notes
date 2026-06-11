---
date: 2026-06-11
book: "Amity Entrance: Master Syllabus (RCI / NIMHANS pattern)"
subject: "Amity Prep"
chapter: 1
tags: [amity, RCI, clinical-psychology, NIMHANS-pattern, entrance, MET2026]
---

# Ch 1: Membrane Dynamics & Electrophysiology

This chapter builds the electrical foundation of the nervous system from first principles: how a neuron at rest holds a stable voltage across its membrane, how that voltage is suddenly inverted and propagated as an action potential, and how myelin makes that signal fast. Entrance papers on the NIMHANS pattern love the precise numbers (the threshold, the equilibrium potentials, the 3:2 pump ratio) and the named mechanisms (Nernst, Goldman, saltatory conduction), so every figure here is exam-load-bearing.

## The Resting Membrane Potential

Every neuron at rest maintains a **resting membrane potential (RMP)** of roughly **-70 mV** (the inside is negative relative to the outside; values of -65 to -70 mV are commonly quoted). This voltage exists because charged particles (ions) are distributed unevenly across the membrane and the membrane is **selectively permeable**, meaning it lets some ions cross far more easily than others.

### The four key players and their gradients

Four ionic species set up the resting state. Two forces act on each ion: the **chemical (concentration) gradient**, which pushes an ion from where it is concentrated to where it is dilute, and the **electrical gradient**, which pulls an ion toward the oppositely charged side. Together these are the **electrochemical gradient**.

| Ion | Higher concentration | Tends to move | Resting permeability |
|-----|---------------------|---------------|----------------------|
| **Sodium (Na+)** | Outside the cell | Inward (chemical) and inward (electrical, attracted to the negative interior) | Very low at rest |
| **Potassium (K+)** | Inside the cell | Outward (chemical) but held back inward (electrical) | High at rest |
| **Chloride (Cl-)** | Outside the cell | Inward (chemical) but pushed out (electrical) | Moderate |
| **Large anions (A-)** | Inside the cell | Cannot cross (proteins, phosphates) | Effectively zero |

The large intracellular **anions (A-)**, mostly negatively charged proteins and organic phosphates, are trapped inside because they are too big to cross the membrane. They are a fixed source of negative charge that anchors the interior at a negative voltage. **Sodium (Na+)** is concentrated outside (about 145 mM out vs 15 mM in) and **potassium (K+)** is concentrated inside (about 140 mM in vs 5 mM out). At rest the membrane is roughly 25 to 40 times more permeable to K+ than to Na+, so the RMP sits close to (but not exactly at) the potassium equilibrium potential.

### Equilibrium potential and the Nernst equation

The **equilibrium potential (E_ion)** for a single ion is the membrane voltage at which the chemical gradient pushing that ion one way is exactly balanced by the electrical gradient pushing it the other way, so there is no net flow. It is calculated by the **Nernst equation**:

E_ion = (RT / zF) × ln([ion]outside / [ion]inside)

Here R is the gas constant, T is absolute temperature, z is the ion's valence (charge), and F is the Faraday constant. At body temperature, converting to log base 10, this simplifies to roughly:

E_ion = (61 / z) × log10([out] / [in]) millivolts

The standard exam values are **E_K of about -90 mV**, **E_Na of about +60 mV** (some texts say +55 to +65 mV), and **E_Cl of about -70 mV**. Notice that because the resting membrane is dominated by K+ permeability, the RMP (-70 mV) lies very near E_K but is pulled slightly more positive by the small but real Na+ leak. The gap between the actual membrane voltage and an ion's equilibrium potential is the **electrochemical driving force** on that ion: the larger the gap, the harder that ion is being pushed to move when its channels open. At rest, Na+ has a huge driving force (membrane at -70 mV is very far from E_Na of +60 mV), which is exactly why Na+ rushes in so violently the instant its channels open during an action potential.

## The Na+/K+ ATPase (Sodium-Potassium Pump)

The concentration gradients would slowly run down as ions leak across the membrane, so they must be actively maintained. The **sodium-potassium pump (Na+/K+ ATPase)** is a transmembrane protein that uses the energy of **ATP hydrolysis** to push ions against their gradients. With each cycle it pumps **3 Na+ ions out** of the cell and **2 K+ ions in**, splitting one molecule of ATP to do so.

Because it moves three positive charges out for every two it brings in, there is a net export of one positive charge per cycle, making the pump **electrogenic**: it directly contributes a small amount (a few millivolts) of negativity to the interior on top of its main job of preserving the gradients. The pump is the single largest consumer of energy in the brain, which is why neural tissue is so metabolically demanding. Exam point: the ratio is **3 out : 2 in**, it is **primary active transport** (it uses ATP directly), and it is **electrogenic**.

## The Goldman-Hodgkin-Katz (GHK) Equation

The Nernst equation predicts the voltage for one ion in isolation. But the real membrane is permeable to several ions at once, so the resting potential is a weighted average that depends on how permeable the membrane is to each. The **Goldman-Hodgkin-Katz (GHK) equation** (also called the Goldman equation) calculates the actual membrane potential given the relative permeabilities and concentrations of Na+, K+, and Cl-:

Vm = 61 × log10( (P_K[K+]out + P_Na[Na+]out + P_Cl[Cl-]in) / (P_K[K+]in + P_Na[Na+]in + P_Cl[Cl-]out) )

The crucial concept here is **relative permeability (P)**. Whichever ion the membrane is most permeable to dominates the equation and pulls Vm toward that ion's equilibrium potential. At rest **P_K is much greater than P_Na**, so Vm sits near E_K (negative). The genius of the action potential is that for about a millisecond the membrane flips this so that **P_Na becomes much greater than P_K**, and Vm therefore swings toward E_Na (positive). Note that Cl- appears with its concentrations inverted relative to the cations, because it carries a negative charge. The GHK equation is the bridge between the static Nernst picture and the dynamic firing of the cell.

## The Action Potential

An **action potential (AP)** is a brief, all-or-none, self-regenerating reversal of membrane polarity that travels down the axon. "All-or-none" means that once threshold is reached the spike fires at full amplitude regardless of how strong the trigger was; a stronger stimulus produces more frequent spikes, not bigger ones.

### Threshold and the voltage-gated channels

The key proteins are **voltage-gated sodium channels** and **voltage-gated (delayed-rectifier) potassium channels**, which open and close in response to membrane voltage. The voltage-gated Na+ channel famously has **two gates**:

- The **activation gate (m-gate)** is closed at rest and opens fast when the membrane depolarizes.
- The **inactivation gate (h-gate)** is open at rest and closes slowly after depolarization, plugging the channel.

This two-gate design is what makes the spike transient and what produces the refractory period (see below). The delayed-rectifier K+ channel has a single slow activation gate often called the **n-gate**.

### The phases of the action potential

When a stimulus depolarizes the membrane to the **threshold of about -55 mV**, a positive-feedback explosion begins. Walk through the phases:

| Phase | What happens | Voltage |
|-------|--------------|---------|
| **Resting state** | m-gate closed, h-gate open, n-gate closed | about -70 mV |
| **Threshold** | Enough depolarization to trigger mass Na+ channel opening | about -55 mV |
| **Depolarization (rising phase)** | m-gates fly open, Na+ floods in, interior becomes positive | racing toward +30 mV |
| **Overshoot** | Membrane briefly reverses to positive interior | peak about +30 to +40 mV |
| **Repolarization** | Na+ h-gates close (Na+ inactivation) AND slow K+ n-gates open, K+ exits | falling back toward rest |
| **Hyperpolarization (undershoot)** | K+ channels close slowly, so too much K+ leaves and the membrane briefly dips below rest | about -75 to -80 mV |
| **Return to rest** | K+ channels fully close, pump and leak restore RMP | back to about -70 mV |

During the **rising phase**, Na+ entry depolarizes the cell, which opens more Na+ channels, which lets in more Na+: a positive-feedback loop (the "Hodgkin cycle") that drives the membrane explosively toward E_Na. The **overshoot** is the portion where the interior is actually positive. **Repolarization** is driven by two events happening together: the Na+ channel h-gates slam shut (inactivation), cutting off the inward current, while the slow voltage-gated K+ channels finally open and let K+ rush out, restoring negativity. Because those K+ channels are slow to close, the membrane temporarily overshoots in the negative direction, producing the **hyperpolarizing undershoot (after-hyperpolarization)**.

### Absolute vs relative refractory period

After firing, the neuron cannot immediately fire again. This is the **refractory period**, and it has two parts:

- The **absolute refractory period** is the interval during which no stimulus, however strong, can trigger a second action potential. It corresponds to the time when the Na+ channel **h-gates are inactivated (closed)**. Until these reset to the open position (which only happens once the membrane has repolarized), the Na+ channels physically cannot reopen. This is what sets the maximum firing rate of a neuron and what forces the action potential to travel in one direction only (the region behind the spike is refractory and cannot be re-excited).
- The **relative refractory period** follows it. Here the h-gates have mostly reset, but the membrane is still hyperpolarized (because K+ channels are still open) and/or some Na+ channels are still recovering. A second action potential is possible but only if a **stronger than normal stimulus** is applied to overcome the lingering hyperpolarization.

Exam framing: absolute = "impossible at any intensity, h-gate inactivated"; relative = "possible but needs a bigger stimulus, membrane hyperpolarized."

## Passive Cable Properties

Before and between active spikes, voltage changes also spread **passively** (electrotonically) along the neuron, like current leaking down a slightly leaky wire. Two constants describe how far and how fast a passive signal travels.

### Length constant (lambda) and space spread

The **length constant (lambda, λ)** is the distance over which a passive (subthreshold) voltage change decays to about **37 percent (1/e)** of its original amplitude. A larger lambda means the signal travels farther before fading. Lambda depends on the ratio of **membrane resistance (Rm)** to **axial (internal/longitudinal) resistance (Ri or Ra)**:

λ = square root of (Rm / Ri)

A high membrane resistance (a "well-insulated" membrane that does not leak current out) and a low axial resistance (a fat axon whose cytoplasm conducts current easily down its core) both increase lambda. This is precisely why **wider axons conduct faster** and why **myelin** (which dramatically raises Rm) lets signals spread far enough to jump between gaps. Length constant governs **spatial summation**: how far a synaptic potential can travel toward the axon hillock before dying out.

### Time constant (tau) and temporal spread

The **time constant (tau, τ)** describes how quickly the membrane voltage responds to a change in current; specifically it is the time for the voltage to reach about **63 percent of its final value** (or to decay to 37 percent). It equals the product of membrane resistance and **membrane capacitance (Cm)**:

τ = Rm × Cm

A short time constant means the membrane responds and recovers quickly, which favors fast signaling and limits how long two inputs can be "added together" in time. Tau therefore governs **temporal summation**: two inputs arriving close together in time will sum if the first has not yet decayed.

### Axial vs membrane resistance

- **Axial (internal) resistance (Ri)** is the resistance to current flowing lengthwise down the inside of the axon. It falls as the axon gets wider (more cytoplasm in parallel), which is why the squid giant axon conducts so fast.
- **Membrane resistance (Rm)** is the resistance to current leaking out sideways across the membrane. It rises with myelination. High Rm keeps current inside the cable so it travels farther.

## Myelination and Saltatory Conduction

**Myelin** is a fatty (lipid-rich) insulating sheath wrapped in many layers around the axon. By drastically increasing membrane resistance and decreasing membrane capacitance, it lets the action potential travel far faster and with less energy cost.

### Two myelinating cell types

The cell that makes myelin differs by location, a classic exam distinction:

| Feature | **Oligodendrocytes** | **Schwann cells** |
|---------|----------------------|-------------------|
| Location | Central nervous system (CNS) | Peripheral nervous system (PNS) |
| Axons myelinated per cell | Many (one oligodendrocyte myelinates several axons) | One (each Schwann cell wraps a single internode of one axon) |
| Regeneration support | Poor (limited CNS regrowth) | Good (aids PNS nerve repair) |
| Disease example | Multiple sclerosis (CNS demyelination) | Guillain-Barré syndrome (PNS demyelination) |

### Nodes of Ranvier and saltatory conduction

Myelin is not continuous. It is interrupted at regular gaps called the **Nodes of Ranvier**, which are bare patches of axonal membrane densely packed with **voltage-gated Na+ channels**. The insulated, myelin-covered stretches between nodes are the **internodes**, where the membrane is essentially sealed off and the action potential cannot be regenerated.

Because current cannot leak out across the high-resistance internode, the depolarization spreads passively (and almost instantly) from one node straight to the next, where the dense Na+ channels regenerate a full-amplitude spike. The action potential therefore appears to **jump** from node to node rather than crawling continuously along the membrane. This is **saltatory conduction** (from the Latin *saltare*, "to leap"). It makes conduction both **much faster** (myelinated fibers conduct at up to roughly 100 to 120 m/s versus about 1 m/s in small unmyelinated fibers) and **more energy-efficient** (Na+/K+ pumping is only needed at the nodes, not along the entire length). Demyelinating diseases such as multiple sclerosis slow or block conduction precisely because, with the insulation stripped, current leaks out of the internodes and the signal can no longer reliably jump between nodes.

## High-Yield Recap

- **RMP about -70 mV**; interior negative; set by selective permeability and trapped intracellular anions (A-).
- **Equilibrium potentials**: E_K about -90 mV, E_Na about +60 mV, E_Cl about -70 mV. RMP sits near E_K because P_K >> P_Na at rest.
- **Nernst equation** gives one ion's equilibrium potential: E = (61/z) log10([out]/[in]) at body temperature.
- **GHK (Goldman) equation** gives actual Vm using relative permeabilities P_K, P_Na, P_Cl; whichever P dominates pulls Vm toward that ion's E.
- **Electrochemical driving force** = gap between Vm and E_ion; Na+ has a huge inward driving force at rest.
- **Na+/K+ ATPase**: pumps 3 Na+ out, 2 K+ in per ATP; primary active transport; electrogenic (net +1 charge out per cycle).
- **Threshold about -55 mV**; AP is all-or-none; **overshoot peak about +30 to +40 mV**.
- Na+ channel has **m-gate (fast activation)** and **h-gate (slow inactivation)**; K+ delayed rectifier has the **n-gate**.
- **Depolarization** = Na+ in (m-gates open); **repolarization** = Na+ inactivation (h-gates close) + K+ out (n-gates open); **hyperpolarizing undershoot** = slow K+ channel closure.
- **Absolute refractory period** = h-gates inactivated, no spike at any strength; **relative refractory period** = membrane hyperpolarized, spike possible only with stronger stimulus.
- **Length constant λ = √(Rm/Ri)**: distance to decay to 37% (1/e); governs spatial summation; bigger with high Rm (myelin) and low Ri (fat axon).
- **Time constant τ = Rm × Cm**: time to reach 63% of final voltage; governs temporal summation.
- **Myelin**: oligodendrocytes in CNS (many axons each), Schwann cells in PNS (one internode each).
- **Nodes of Ranvier** = bare gaps packed with voltage-gated Na+ channels; AP leaps node to node = **saltatory conduction** (faster, up to ~120 m/s, and energy-efficient).
- Demyelination: multiple sclerosis (CNS), Guillain-Barré syndrome (PNS).
