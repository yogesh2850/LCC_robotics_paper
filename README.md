# LCC robotics paper — ICRA draft

`root.tex` + `refs.bib` on the IEEE conference class (`ieeeconf.cls`, from
ras.papercept.net; the untouched template is kept as `template_root.tex`). Compile on
Overleaf with pdfLaTeX + BibTeX (no TeX installation on the workstation, so the draft has not
been compiled locally — expect a few layout fixes on the first Overleaf build).

Status: working draft, **simulation results only**, originally written 2026-09-16 from the runs in
`Grasp_direct/agronomist_robotiq/outputs` (rq17, rq22, rq26, rq30, rq33, rq34, rq35 and the
`softleaf_E*` settling checks). Figures in `figs/` are frames from those runs.

Red `TODO` marks in the PDF: affiliation / co-authors / funding, and real-robot experiments.

## 2026-09-18 research and evidence revision

The main manuscript is now **Holding Is Not Presenting: Evaluating Contact and Deformation
in Robotic Leaf Inspection**. The plant and both working robot projects were left untouched.
The paper's broader novelty claims were narrowed against recent primary literature,
including ICRA 2025 safe leaf manipulation and the September 2026 RoMu4o preprint.

- `RESEARCH_DIRECTION.md`: recommended contribution, literature boundaries, reviewer risks,
  and a frozen-plant matched evaluation plan.
- `proposed_method.tex`: separately compilable, explicitly **unimplemented/unevaluated**
  response-aware probing, presentation and regrasping method. Do not include it as measured
  work or use its candidate title as a claim of validated results yet.
- `scripts/audit_interaction.py`: reanalysis of archived `iaR*` / `iaS*` outputs only.
- `results/interaction_audit.md` / `.csv`: per-attempt provenance and corrected cell counts.
- `scripts/check_paper.py`: static LaTeX/reference/figure checks and input-hash verification.

Important corrections: the Robotiq mid-blade soft 4 N baseline is 2/3, not the mixed-force
8/9; recorded blade angles are terminal rather than peak/synchronized roll response;
none of the 89 archived interaction attempts contains a sensor-swing value. Five painted
shades map to four chart classes, and the colour matrix has 3,800 rows (3,555 valid),
19 recorded conditions including the default. Original historical reports in `results/`
are retained as provenance even when their labels/aggregation are superseded by the audit.

```bash
cd /home/yogesh/Grasp_direct/LCC_robotics_paper
/home/yogesh/anaconda3/bin/python scripts/audit_interaction.py
/home/yogesh/anaconda3/bin/python scripts/check_paper.py
```

This revision does not establish a new controller's performance or ICRA readiness.
The decisive next experiment is a matched comparison of fixed sweep, visual feedback,
heuristic regrasp, and response-aware control on the unchanged plant. TeX is not installed
locally; neither revised document has been PDF-compiled or checked against a page limit.
