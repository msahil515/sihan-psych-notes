#!/usr/bin/env python3
"""Insert the real Pinel & Barnes textbook figures into the biopsychology notes.

These are the actual figures cropped from Pinel & Barnes, Biopsychology (11th ed.),
NOT schematic redraws. Each is one contiguous <div class="fig"> ... </div> block with
NO internal blank lines, so python-markdown passes it through as raw HTML untouched.
Image files live in docs/figs/ (served by Pages, precached by the service worker).

Idempotent: strips any existing <div class="fig"> blocks first, then re-inserts, so
re-running (or running over the old inline-SVG diagrams) yields the same clean result.
"""
import pathlib, re, sys

PINEL = pathlib.Path(__file__).resolve().parent.parent / "notes" / "pinel-biopsychology"
ATTRIB = "Pinel &amp; Barnes, 11th ed."


def block(fig, title, alt):
    """One contiguous raw-HTML figure block (no blank lines) -> survives markdown."""
    num = fig.replace("f_", "").replace(".jpg", "").replace("_", ".")
    return (
        '<div class="fig">\n'
        f'<a class="figzoom" href="figs/{fig}" target="_blank" rel="noopener">'
        f'<img src="figs/{fig}" loading="lazy" alt="{alt}"></a>\n'
        f'<p class="cap"><b>{title}</b> {ATTRIB} &middot; Fig {num}</p>\n'
        '</div>'
    )


# chapter file -> list of (anchor heading, [figure blocks to insert before it])
PLAN = {
    "ch03-chapter-3-anatomy-of-the-nervous-system.md": [
        ("### Major Divisions", [
            ("f_3_2.jpg", "The major divisions of the nervous system.",
             "Pinel Fig 3.2: the major divisions of the nervous system")]),
        ("### External Anatomy", [
            ("f_3_5.jpg", "External features of a neuron.",
             "Pinel Fig 3.5: external features of a neuron")]),
        ("### Internal Anatomy", [
            ("f_3_6.jpg", "Internal features of a neuron.",
             "Pinel Fig 3.6: internal features of a neuron")]),
        ("### Classes of Neurons (by processes)", [
            ("f_3_8.jpg", "Unipolar, bipolar &amp; multipolar neurons and an interneuron.",
             "Pinel Fig 3.8: unipolar, bipolar and multipolar neurons and an interneuron")]),
        ("### Oligodendrocytes vs. Schwann Cells", [
            ("f_3_9.jpg", "Myelination: an oligodendrocyte (CNS) vs a Schwann cell (PNS).",
             "Pinel Fig 3.9: myelination by an oligodendrocyte versus a Schwann cell")]),
        ("### Planes of Section", [
            ("f_3_16.jpg", "Horizontal, frontal (coronal) and sagittal planes.",
             "Pinel Fig 3.16: horizontal, frontal and sagittal planes")]),
        ("## 3.9 Five Major Divisions of the Brain", [
            ("f_3_19.jpg", "The five divisions of the adult human brain.",
             "Pinel Fig 3.19: the five divisions of the adult human brain")]),
        ("#### Cerebral Cortex", [
            ("f_3_25.jpg", "The lobes of the cerebral hemisphere.",
             "Pinel Fig 3.25: the lobes of the cerebral hemisphere")]),
        ("### Limbic System", [
            ("f_3_27.jpg", "The limbic system.",
             "Pinel Fig 3.27: the limbic system")]),
        ("### Basal Ganglia", [
            ("f_3_28.jpg", "The basal ganglia.",
             "Pinel Fig 3.28: the basal ganglia")]),
    ],
    "ch04-chapter-4-neural-conduction-and-synaptic-transmiss.md": [
        ("### Refractory Periods", [
            ("f_4_5.jpg", "Na⁺ and K⁺ channels across the three phases of the action potential.",
             "Pinel Fig 4.5: sodium and potassium channels across the action potential")]),
        ("### Synthesis, Packaging, Transport", [
            ("f_4_7.jpg", "Anatomy of a typical synapse.",
             "Pinel Fig 4.7: anatomy of a typical synapse")]),
        ("### Amino Acid Neurotransmitters", [
            ("f_4_16.jpg", "The classes of neurotransmitters.",
             "Pinel Fig 4.16: the classes of neurotransmitters")]),
    ],
    "ch06-chapter-6-the-visual-system.md": [
        ("### Inside-Out Arrangement", [
            ("f_6_5.jpg", "The cellular structure of the retina.",
             "Pinel Fig 6.5: the cellular structure of the retina")]),
        ("### Retinotopic Organization", [
            ("f_6_13.jpg", "The retina-geniculate-striate pathway.",
             "Pinel Fig 6.13: the retina-geniculate-striate pathway")]),
    ],
    "ch07-chapter-7-mechanisms-of-perception-hearing-touch-s.md": [
        ("### From Ear to Primary Auditory Cortex", [
            ("f_7_4.jpg", "Anatomy of the ear.",
             "Pinel Fig 7.4: anatomy of the ear")]),
        ("### Cortical Areas of Somatosensation", [
            ("f_7_10.jpg", "The dorsal-column medial-lemniscus system.",
             "Pinel Fig 7.10: the dorsal-column medial-lemniscus system"),
            ("f_7_11.jpg", "The anterolateral system.",
             "Pinel Fig 7.11: the anterolateral system")]),
    ],
    "ch08-chapter-8-the-sensorimotor-system.md": [
        ("### General Model (Figure 8.1)", [
            ("f_8_1.jpg", "The sensorimotor system as a hierarchy.",
             "Pinel Fig 8.1: the sensorimotor system as a hierarchy")]),
        ("### Conventional View", [
            ("f_8_6.jpg", "The motor homunculus.",
             "Pinel Fig 8.6: the motor homunculus")]),
    ],
    "ch11-chapter-11-learning-memory-and-amnesia.md": [
        ("### Gradients of Retrograde Amnesia and Consolidation", [
            ("f_11_5.jpg", "Retrograde vs anterograde amnesia after a closed-head TBI.",
             "Pinel Fig 11.5: retrograde versus anterograde amnesia after a closed-head injury")]),
        ("### Spatial Tasks", [
            ("f_11_4.jpg", "The major components of the hippocampus.",
             "Pinel Fig 11.4: the major components of the hippocampus")]),
    ],
}


def main():
    for fname, anchors in PLAN.items():
        f = PINEL / fname
        text = f.read_text()
        # strip any existing fig blocks (old inline-SVG doodles or a previous run)
        text = re.sub(r'<div class="fig">.*?</div>\n*', '', text, flags=re.S)
        lines = text.splitlines(keepends=True)
        inserts = []
        for anchor, figs in anchors:
            idx = next((i for i, l in enumerate(lines)
                        if l.strip() == anchor or l.startswith(anchor)), None)
            if idx is None:
                print(f"!! anchor not found in {fname}: {anchor!r}")
                sys.exit(1)
            inserts.append((idx, figs))
        # insert from the bottom up so earlier line indices stay valid
        for idx, figs in sorted(inserts, reverse=True):
            blob = "".join(block(*fg) + "\n\n" for fg in figs)
            lines.insert(idx, blob)
        f.write_text("".join(lines))
        n = sum(len(figs) for _, figs in anchors)
        print(f"patched {fname}: +{n} real figures")


if __name__ == "__main__":
    main()
