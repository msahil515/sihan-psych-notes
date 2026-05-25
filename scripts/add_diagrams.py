#!/usr/bin/env python3
"""Insert clean, self-contained inline-SVG diagrams into the biopsychology notes.

Diagrams are schematic (built for understanding/MCQ recall, not photographic) and
themed for the dark reader. Each is a single <div class="fig"> ... </div> block with
NO internal blank lines, so python-markdown passes it through as raw HTML untouched.
Idempotent: skips a file if its diagrams are already present.
"""
import pathlib, sys

PINEL = pathlib.Path(__file__).resolve().parent.parent / "notes" / "pinel-biopsychology"

# ---- palette (matches reader dark theme; biopsych accent = amber) ----
INK, MUT, FAINT = "#e8ebf2", "#c2c8d6", "#5b6376"
AMBER, BLUE, TEAL, PURP, RED = "#fbbf72", "#5b9cff", "#2dd4bf", "#a78bfa", "#f08a8a"

def fig(svg, cap):
    """One contiguous raw-HTML block (no blank lines) -> survives markdown."""
    svg = "\n".join(l for l in svg.strip().splitlines() if l.strip() != "")
    return '<div class="fig">\n' + svg + '\n<p class="cap">' + cap + '</p>\n</div>'

# ======================================================================
# 1. NEURON STRUCTURE  (ch03, External Anatomy of neurons)
# ======================================================================
NEURON = fig(f'''
<svg viewBox="0 0 560 240" role="img" aria-label="Structure of a neuron">
<line x1="150" y1="120" x2="478" y2="120" stroke="#cdd3e0" stroke-width="5"/>
<g fill="#22314c" stroke="{BLUE}" stroke-width="2">
<rect x="190" y="110" width="58" height="20" rx="10"/>
<rect x="266" y="110" width="58" height="20" rx="10"/>
<rect x="342" y="110" width="58" height="20" rx="10"/>
</g>
<g stroke="{AMBER}" stroke-width="2.6" fill="none" stroke-linecap="round">
<path d="M96 116 L60 78 M72 86 L46 66 M72 86 L50 100"/>
<path d="M96 128 L58 162 M70 152 L46 170 M70 152 L52 182"/>
<path d="M92 104 L66 58"/>
</g>
<ellipse cx="116" cy="121" rx="30" ry="27" fill="#3a2f1e" stroke="{AMBER}" stroke-width="2.6"/>
<circle cx="116" cy="121" r="11" fill="{AMBER}" opacity="0.9"/>
<path d="M146 108 L162 121 L146 134 Z" fill="{AMBER}" opacity="0.55"/>
<line x1="478" y1="120" x2="498" y2="104" stroke="#cdd3e0" stroke-width="3" stroke-linecap="round"/>
<line x1="478" y1="120" x2="504" y2="120" stroke="#cdd3e0" stroke-width="3" stroke-linecap="round"/>
<line x1="478" y1="120" x2="494" y2="136" stroke="#cdd3e0" stroke-width="3" stroke-linecap="round"/>
<g fill="{AMBER}"><circle cx="500" cy="100" r="8"/><circle cx="508" cy="120" r="8"/><circle cx="500" cy="140" r="8"/></g>
<g font-size="13" fill="{MUT}">
<text x="40" y="40">Dendrites</text>
<line x1="58" y1="46" x2="72" y2="70" stroke="{FAINT}"/>
<text x="116" y="200" text-anchor="middle">Cell body (soma)</text>
<text x="116" y="218" text-anchor="middle" fill="{AMBER}" font-size="11.5">nucleus inside</text>
<text x="170" y="92" text-anchor="middle">Axon hillock</text>
<line x1="170" y1="98" x2="158" y2="114" stroke="{FAINT}"/>
<text x="277" y="92" text-anchor="middle" fill="{BLUE}">Myelin sheath</text>
<line x1="277" y1="98" x2="277" y2="108" stroke="{FAINT}"/>
<text x="333" y="160" text-anchor="middle">Node of Ranvier</text>
<line x1="333" y1="148" x2="333" y2="130" stroke="{FAINT}"/>
<text x="496" y="172" text-anchor="middle">Terminal buttons</text>
<line x1="500" y1="158" x2="504" y2="148" stroke="{FAINT}"/>
<text x="300" y="103" text-anchor="middle" fill="{INK}" font-size="11.5">Axon</text>
</g>
</svg>
''', "<b>Structure of a neuron.</b> Signals flow one way: dendrites receive, the soma integrates, the axon carries the action potential (jumping node to node between myelin segments), and terminal buttons release neurotransmitter onto the next cell.")

# ======================================================================
# 2. NERVOUS SYSTEM ORGANISATION  (ch03, 3.1 General Layout)
# ======================================================================
def box(x, y, w, h, label, sub, col, fs=13.5):
    cx = x + w / 2
    t = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="#161b27" stroke="{col}" stroke-width="2"/>'
    t += f'<text x="{cx}" y="{y + (h/2+5 if not sub else 20)}" text-anchor="middle" fill="{INK}" font-size="{fs}" font-weight="700">{label}</text>'
    if sub:
        t += f'<text x="{cx}" y="{y+36}" text-anchor="middle" fill="{MUT}" font-size="10.5">{sub}</text>'
    return t

NS_TREE = fig(f'''
<svg viewBox="0 0 560 320" role="img" aria-label="Organisation of the nervous system">
<g stroke="{FAINT}" stroke-width="1.6" fill="none">
<path d="M280 52 V74 M135 74 H425 M135 74 V96 M425 74 V96"/>
<path d="M425 138 V156 M296 156 H467 M296 156 V176 M467 156 V176"/>
<path d="M467 218 V236 M381 236 H500 M381 236 V256 M500 236 V256"/>
</g>
{box(180, 18, 200, 34, "Nervous system", "", AMBER)}
{box(60, 96, 150, 42, "CNS", "brain + spinal cord", BLUE)}
{box(350, 96, 150, 42, "PNS", "outside the CNS", BLUE)}
{box(232, 176, 128, 42, "Somatic (SNS)", "external world", TEAL)}
{box(392, 176, 150, 42, "Autonomic (ANS)", "internal organs", TEAL)}
{box(330, 256, 102, 46, "Sympathetic", "fight-or-flight", PURP, 12)}
{box(442, 256, 116, 46, "Parasympathetic", "rest-and-digest", PURP, 12)}
</svg>
''', "<b>A system of twos.</b> The nervous system splits into CNS and PNS; the PNS into somatic and autonomic; and the autonomic into the opposing sympathetic (arousal) and parasympathetic (calming) branches.")

# ======================================================================
# 3. ACTION POTENTIAL  (ch04, 4.4 Conduction of Action Potentials)
# ======================================================================
# plot area x:64..524, y:46..286 ; +40mV -> y58, -90mV -> y286
def mv(v):  # mV -> y
    return 58 + (40 - v) * (228 / 130)
AP = fig(f'''
<svg viewBox="0 0 560 330" role="img" aria-label="The action potential">
<line x1="64" y1="40" x2="64" y2="292" stroke="{FAINT}" stroke-width="1.6"/>
<line x1="64" y1="292" x2="528" y2="292" stroke="{FAINT}" stroke-width="1.6"/>
<line x1="64" y1="{mv(-65):.0f}" x2="528" y2="{mv(-65):.0f}" stroke="{TEAL}" stroke-width="1.3" stroke-dasharray="5 4"/>
<line x1="64" y1="{mv(-70):.0f}" x2="528" y2="{mv(-70):.0f}" stroke="{MUT}" stroke-width="1.3" stroke-dasharray="5 4"/>
<polyline fill="none" stroke="{AMBER}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"
 points="74,{mv(-70):.0f} 150,{mv(-70):.0f} 170,{mv(-65):.0f} 196,{mv(40):.0f} 210,{mv(35):.0f} 244,{mv(-70):.0f} 262,{mv(-82):.0f} 300,{mv(-72):.0f} 360,{mv(-70):.0f} 520,{mv(-70):.0f}"/>
<g font-size="12" fill="{MUT}">
<text x="58" y="{mv(40)+4:.0f}" text-anchor="end">+40</text>
<text x="58" y="{mv(0)+4:.0f}" text-anchor="end">0</text>
<text x="58" y="{mv(-65)+4:.0f}" text-anchor="end" fill="{TEAL}">-65</text>
<text x="58" y="{mv(-70)+13:.0f}" text-anchor="end">-70</text>
<text x="14" y="160" font-size="12" fill="{MUT}" transform="rotate(-90 14 160)">membrane potential (mV)</text>
<text x="300" y="320" text-anchor="middle">time (~1 ms per spike)</text>
</g>
<g font-size="11.5" fill="{TEAL}"><text x="520" y="{mv(-65)-7:.0f}" text-anchor="end">threshold</text></g>
<g font-size="11.5" fill="{INK}">
<text x="118" y="{mv(-70)-10:.0f}" text-anchor="middle">resting</text>
<text x="205" y="44" text-anchor="middle" fill="{RED}">depolarization</text>
<text x="205" y="60" text-anchor="middle" fill="{RED}" font-size="10.5">Na+ rushes IN</text>
<text x="300" y="{mv(20):.0f}" fill="{BLUE}">repolarization</text>
<text x="300" y="{mv(20)+15:.0f}" fill="{BLUE}" font-size="10.5">K+ flows OUT</text>
<text x="360" y="{mv(-78):.0f}" text-anchor="middle" font-size="10.5">hyperpolarization</text>
<line x1="318" y1="{mv(-80):.0f}" x2="272" y2="{mv(-83):.0f}" stroke="{FAINT}"/>
</g>
</svg>
''', "<b>The action potential is all-or-none.</b> Once a stimulus pushes the membrane past threshold (-65 mV), Na+ floods in and the inside shoots to about +40 mV; K+ then flows out to repolarize, overshooting into a brief hyperpolarization before settling back to the -70 mV resting potential.")

# ======================================================================
# 4. THE SYNAPSE  (ch04, 4.5 Synaptic Transmission)
# ======================================================================
SYNAPSE = fig(f'''
<svg viewBox="0 0 520 320" role="img" aria-label="Chemical synapse">
<path d="M150 20 Q120 70 130 120 L390 120 Q400 70 370 20 Z" fill="#3a2f1e" stroke="{AMBER}" stroke-width="2.4"/>
<g fill="none" stroke="{AMBER}" stroke-width="2"><circle cx="200" cy="70" r="13"/><circle cx="250" cy="92" r="13"/><circle cx="300" cy="64" r="13"/><circle cx="335" cy="96" r="13"/></g>
<g fill="{AMBER}"><circle cx="200" cy="70" r="3.5"/><circle cx="250" cy="92" r="3.5"/><circle cx="300" cy="64" r="3.5"/><circle cx="335" cy="96" r="3.5"/></g>
<rect x="110" y="200" width="300" height="80" rx="8" fill="#1c2740" stroke="{BLUE}" stroke-width="2.4"/>
<g fill="{TEAL}"><rect x="170" y="186" width="26" height="16" rx="5"/><rect x="247" y="186" width="26" height="16" rx="5"/><rect x="324" y="186" width="26" height="16" rx="5"/></g>
<g fill="{AMBER}"><circle cx="225" cy="150" r="4"/><circle cx="205" cy="165" r="4"/><circle cx="260" cy="160" r="4"/><circle cx="300" cy="150" r="4"/><circle cx="335" cy="166" r="4"/><circle cx="183" cy="178" r="4"/><circle cx="337" cy="178" r="4"/></g>
<path d="M150 140 q-22 18 -4 36" fill="none" stroke="{MUT}" stroke-width="1.8" marker-end="url(#ah)"/>
<defs><marker id="ah" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto"><path d="M0 0 L7 4 L0 8 z" fill="{MUT}"/></marker></defs>
<g font-size="13" fill="{MUT}">
<text x="260" y="40" text-anchor="middle" fill="{INK}">Presynaptic terminal button</text>
<text x="200" y="70" text-anchor="middle" dy="-18" font-size="11" fill="{AMBER}">vesicles (NT)</text>
<text x="438" y="160" text-anchor="middle">synaptic</text><text x="438" y="175" text-anchor="middle">cleft</text>
<line x1="408" y1="158" x2="380" y2="140" stroke="{FAINT}"/>
<text x="260" y="245" text-anchor="middle" fill="{INK}">Postsynaptic membrane</text>
<text x="385" y="196" font-size="11" fill="{TEAL}">receptors</text>
<text x="120" y="150" font-size="11">reuptake</text>
</g>
</svg>
''', "<b>Chemical synapse.</b> An arriving action potential triggers vesicles to dump neurotransmitter into the synaptic cleft; the molecules diffuse across and bind receptors on the postsynaptic membrane (causing an EPSP or IPSP), then are cleared by reuptake or enzymes.")

# ======================================================================
# 5. BRAIN: LATERAL VIEW + FOUR LOBES  (ch03, 3.10 Telencephalon)
# ======================================================================
BRAIN = fig(f'''
<svg viewBox="0 0 560 350" role="img" aria-label="Lateral view of the brain and its four lobes">
<defs>
<clipPath id="cx"><path d="M90 195 C70 150 80 100 140 80 C210 55 320 55 400 75 C450 90 488 130 478 175 C470 218 440 242 380 242 C300 247 175 247 130 236 C106 229 96 213 90 195 Z"/></clipPath>
</defs>
<g clip-path="url(#cx)">
<rect x="0" y="0" width="560" height="350" fill="#11151f"/>
<path d="M0 0 L255 40 L304 197 L0 150 Z" fill="{BLUE}" fill-opacity="0.50"/>
<path d="M255 40 L400 45 L430 210 L380 205 L304 197 Z" fill="{PURP}" fill-opacity="0.50"/>
<path d="M400 45 L560 0 L560 350 L425 350 L430 210 Z" fill="{AMBER}" fill-opacity="0.44"/>
<path d="M0 150 L304 197 L380 205 L430 211 L427 350 L0 350 Z" fill="{TEAL}" fill-opacity="0.48"/>
</g>
<path d="M404 232 Q416 280 408 320 Q402 334 392 322 Q380 280 388 234 Z" fill="#222a3a" stroke="{INK}" stroke-width="2"/>
<path d="M420 236 Q502 232 500 276 Q498 312 438 310 Q414 308 414 280 Q414 254 420 236 Z" fill="#15302b" stroke="{TEAL}" stroke-width="2.2"/>
<g stroke="{TEAL}" stroke-width="1.3" opacity="0.7"><path d="M420 252 H494"/><path d="M416 268 H498"/><path d="M418 284 H492"/><path d="M426 298 H480"/></g>
<path d="M90 195 C70 150 80 100 140 80 C210 55 320 55 400 75 C450 90 488 130 478 175 C470 218 440 242 380 242 C300 247 175 247 130 236 C106 229 96 213 90 195 Z" fill="none" stroke="{INK}" stroke-width="2.4"/>
<path d="M252 66 L300 192" stroke="{INK}" stroke-width="2" fill="none" stroke-dasharray="2 5" opacity="0.85"/>
<path d="M120 165 Q250 188 372 205" stroke="{INK}" stroke-width="2" fill="none" stroke-dasharray="2 5" opacity="0.85"/>
<g font-size="14.5" font-weight="700">
<text x="165" y="120" fill="{BLUE}">Frontal</text>
<text x="318" y="95" text-anchor="middle" fill="{PURP}">Parietal</text>
<text x="445" y="135" text-anchor="middle" fill="{AMBER}">Occipital</text>
<text x="235" y="218" fill="{TEAL}">Temporal</text>
</g>
<g font-size="11.5" fill="{MUT}">
<text x="262" y="52" text-anchor="middle">central sulcus</text>
<line x1="262" y1="58" x2="270" y2="74" stroke="{FAINT}"/>
<text x="104" y="150" text-anchor="end">lateral</text><text x="104" y="163" text-anchor="end">sulcus</text>
<line x1="108" y1="158" x2="124" y2="166" stroke="{FAINT}"/>
<text x="470" y="344" text-anchor="middle" fill="{TEAL}">cerebellum</text>
<line x1="466" y1="330" x2="460" y2="312" stroke="{FAINT}"/>
<text x="360" y="340" text-anchor="middle">brain stem</text>
<line x1="374" y1="328" x2="398" y2="312" stroke="{FAINT}"/>
</g>
</svg>
''', "<b>The cerebral cortex, side view.</b> The central sulcus and lateral sulcus split each hemisphere into four lobes: frontal (movement, planning), parietal (body sensation), temporal (hearing, memory), occipital (vision). The cerebellum (movement coordination) and brain stem sit below and behind.")

# ======================================================================
# 6. VISUAL PATHWAY  (ch06, 6.3 From Retina to Primary Visual Cortex)
# ======================================================================
VISUAL = fig(f'''
<svg viewBox="0 0 560 330" role="img" aria-label="The visual pathway from eyes to primary visual cortex">
<text x="280" y="22" text-anchor="middle" font-size="12" fill="{MUT}">left visual field <tspan fill="{BLUE}">&#9632;</tspan>   right visual field <tspan fill="{AMBER}">&#9632;</tspan></text>
<g stroke="{INK}" stroke-width="2"><circle cx="70" cy="95" r="30" fill="#161b27"/><circle cx="70" cy="235" r="30" fill="#161b27"/></g>
<path d="M70 65 A30 30 0 0 1 70 125" fill="{AMBER}" opacity="0.55"/>
<path d="M70 125 A30 30 0 0 1 70 65" fill="{BLUE}" opacity="0.55"/>
<path d="M70 205 A30 30 0 0 1 70 265" fill="{AMBER}" opacity="0.55"/>
<path d="M70 265 A30 30 0 0 1 70 205" fill="{BLUE}" opacity="0.55"/>
<g fill="none" stroke-width="3.4" stroke-linecap="round">
<path d="M100 88 L210 150" stroke="{BLUE}"/>
<path d="M100 102 L210 165" stroke="{AMBER}"/>
<path d="M100 228 L210 165" stroke="{BLUE}"/>
<path d="M100 242 L210 150" stroke="{AMBER}"/>
</g>
<ellipse cx="210" cy="157" rx="16" ry="26" fill="#3a2f1e" stroke="{INK}" stroke-width="2"/>
<g fill="none" stroke-width="3.4" stroke-linecap="round">
<path d="M226 150 L330 120" stroke="{AMBER}"/>
<path d="M226 165 L330 232" stroke="{BLUE}"/>
</g>
<rect x="330" y="100" width="46" height="40" rx="8" fill="#1c2740" stroke="{AMBER}" stroke-width="2"/>
<rect x="330" y="212" width="46" height="40" rx="8" fill="#22314c" stroke="{BLUE}" stroke-width="2"/>
<g fill="none" stroke-width="3.4" stroke-linecap="round">
<path d="M376 120 Q450 130 470 165" stroke="{AMBER}"/>
<path d="M376 232 Q450 222 470 191" stroke="{BLUE}"/>
</g>
<path d="M470 120 Q520 178 470 236 Q500 178 470 120 Z" fill="#2a2238" stroke="{PURP}" stroke-width="2.2"/>
<g font-size="12.5" fill="{MUT}">
<text x="70" y="290" text-anchor="middle" fill="{INK}">eyes (retinas)</text>
<text x="70" y="306" text-anchor="middle" font-size="10.5">nasal | temporal halves</text>
<text x="155" y="120" text-anchor="middle">optic nerve</text>
<text x="210" y="205" text-anchor="middle">optic chiasm</text>
<text x="210" y="220" text-anchor="middle" font-size="10.5">nasal fibers cross</text>
<text x="300" y="95" text-anchor="middle">optic tract</text>
<text x="353" y="92" text-anchor="middle" fill="{INK}">LGN</text>
<text x="353" y="270" text-anchor="middle" font-size="10.5">(thalamus)</text>
<text x="445" y="150" text-anchor="middle" font-size="11">optic</text><text x="445" y="163" text-anchor="middle" font-size="11">radiation</text>
<text x="498" y="178" text-anchor="middle" fill="{PURP}">V1</text>
<text x="498" y="290" text-anchor="middle" font-size="10.5">primary</text>
<text x="498" y="303" text-anchor="middle" font-size="10.5">visual cortex</text>
</g>
</svg>
''', "<b>Retina to cortex.</b> Each eye splits into a nasal and temporal half-retina. At the optic chiasm the nasal fibers cross, so everything from the <b>left</b> visual field ends up in the <b>right</b> primary visual cortex (and vice-versa), relayed through the LGN of the thalamus.")

# ======================================================================
# insertion: anchor text -> figure block, inserted BEFORE the anchor line
# ======================================================================
PATCHES = {
    "ch03-chapter-3-anatomy-of-the-nervous-system.md": [
        ("### Cranial Nerves", NS_TREE),
        ("### Internal Anatomy", NEURON),
        ("- **Lobes are NOT functional units**", BRAIN),
    ],
    "ch04-chapter-4-neural-conduction-and-synaptic-transmiss.md": [
        ("- Ion movement per AP is tiny", AP),
        ("| Synapse Type | Description |", SYNAPSE),
    ],
    "ch06-chapter-6-the-visual-system.md": [
        ("### Retinotopic Organization", VISUAL),
    ],
}

def main():
    for fname, patches in PATCHES.items():
        f = PINEL / fname
        text = f.read_text()
        if 'class="fig"' in text:
            print(f"SKIP {fname} (already has diagrams)")
            continue
        lines = text.splitlines(keepends=True)
        for anchor, block in patches:
            idx = next((i for i, l in enumerate(lines) if l.strip() == anchor.strip()
                        or l.startswith(anchor)), None)
            if idx is None:
                print(f"!! anchor not found in {fname}: {anchor!r}")
                sys.exit(1)
            lines.insert(idx, block + "\n\n")
        f.write_text("".join(lines))
        print(f"patched {fname}: +{len(patches)} diagrams")

if __name__ == "__main__":
    main()
