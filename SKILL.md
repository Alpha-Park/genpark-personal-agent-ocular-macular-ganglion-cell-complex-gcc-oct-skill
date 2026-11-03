---
name: genpark-personal-agent-ocular-macular-ganglion-cell-complex-gcc-oct-skill
description: Evaluates macular Ganglion Cell Complex (GCC / GCIPL) thickness, vertical hemifield asymmetry, and focal/global loss volumes (FLV%/GLV%) from SD-OCT scans for early glaucoma detection.
---

# Ocular Macular Ganglion Cell Complex (GCC / GCIPL) Skill

This skill computes structural neuroretinal parameters from optical coherence tomography (OCT) macular scans to detect pre-perimetric glaucoma, focal neuroretinal rim breaches, and neurodegenerative axonal loss according to ISGEO ophthalmic standards.

## Core Capabilities
- Evaluates Average GCC / GCIPL Thickness ($\mu m$, normal $\ge 78.0\ \mu m$).
- Computes Superior vs Inferior Vertical Hemifield Asymmetry ($\mu m$, normal $\le 5.0\ \mu m$).
- Calculates Focal Loss Volume ($FLV\%$, normal $< 1.0\%$) and Global Loss Volume ($GLV\%$, normal $< 4.0\%$).
- Detects occult pre-perimetric glaucomatous damage before standard visual field defects manifest.

## Zero-Mock Architecture
Standard Python standard library only with zero external dependencies.
