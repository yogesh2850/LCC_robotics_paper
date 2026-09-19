# Research direction: response-aware leaf presentation

Literature checked 2026-09-18. This is a research recommendation, not a novelty guarantee
or a claim that the proposed controller has already been implemented.

## Recommendation

Make the main question **when and how an attached leaf can be presented through a given
contact**, not whether a robot can read a colour chart. The strongest candidate is:

> A robot uses short, force-bounded diagnostic motions to estimate the response of a
> selected leaf region, then chooses presentation, a new grasp location, or release
> according to whether the sensing goal is achievable with the current contact.

Suggested eventual title: **Response-Aware Leaf Presentation through Bounded Probing and
Regrasping**. The revised current manuscript is titled **Holding Is Not Presenting**:
it states the existing evidence honestly. `proposed_method.tex` is a separate mathematical
method specification, not a results manuscript. Promote it into the main paper only after
the comparisons below have been run.

The potential contribution is the *decision made using task-region response*, including
uncertainty and regrasp cost. A force servo, estimated Jacobian, RGB-D targeting, FEM plant,
or a second gripper is not independently a convincing new robotics method.

## Closest literature and the claim boundary

| Primary source | Established capability | Consequence for our claim |
|---|---|---|
| [Yao et al., ICRA 2025](https://www.hrl.uni-bonn.de/publications/2025/yao25icra) | Leaf manipulation planned with a deformation model to reveal fruit. | Do not claim first plant interaction for visibility. Focus on measured response of the grasped sensing region. |
| [RoMu4o, v3 September 2026](https://arxiv.org/abs/2501.10621v3) | Robotic leaf grasping and proximal hyperspectral measurement with integrated illumination. | An end-to-end leaf-sensing demonstration alone is insufficient. Cite as the verified preprint version. |
| [Foix et al., 2018](https://doi.org/10.1016/j.compag.2018.01.020) | Task-driven next-best-view selection for leaf probing. | Include a camera-only active-view baseline where the sensing objective permits it. |
| [Hu et al., 2017](https://arxiv.org/abs/1709.07218) | Online learning of tool-motion/deformation mappings for visual servoing. | Compare against an adaptive deformation servo; do not claim the mapping itself as novel. |
| [Zhou et al., 2022](https://doi.org/10.3390/s22155483) | Tactile slip detection and feedback in fruit grasps affected by leaves. | Force regulation or slip reaction alone is not novel; low leaf response is not proof of slip. |
| [Bhowmik et al., ICRA 2026 workshop](https://abhimanyubhowmik.github.io/rce/) | Relative plant compliance from wind-driven visual motion. | Distinguish effective grasp-to-region response from intrinsic material stiffness. Workshop, not main-conference publication. |
| [Nazari et al., 2025](https://www.nature.com/articles/s42256-025-01062-2) | Predictive trajectory modulation as an alternative to grip-force modulation for slip control. | Avoid claiming that changing trajectory instead of raising force is itself new. |

This was a targeted search, not an exhaustive systematic review. Before submission, expand
the forward/backward citation search around these papers, especially online contact-mode
inference, deformable regrasp planning and task-oriented grasp adaptation.

## What the present implementation already supports

- Two functioning tools, force control, centring, canopy-aware approach and separate roll.
- RGB-D targeting, a wrist view decoupled from tool roll, local leaf plane fitting.
- Current `sense_blade_normal`, `record_sensed_normal` and `sensor_turn` code provides a
  starting point for measurement, not a closed-loop response controller.
- Force-regulated lift/roll currently follows a scripted sweep. The leaf normal does not
  control its amplitude or select a replacement grasp.
- Existing logs and matrices are useful exploratory evidence, not randomized causal trials.

No files in either robot project or the plant were edited for this paper revision.

## Audit findings that matter to reviewers

1. **A completed sweep is not demonstrated presentation.** `blade_turn_deg` is computed
   when the leaf result is written. It can be measured after the roll returns to zero.
   Dividing it by maximum commanded roll is not a transfer gain. A good elastic response
   could also end near zero. Do not reinterpret the endpoint as peak deformation.
2. **The archived sensor evidence is absent.** All 89 attempted leaves in 32 `iaR*`/`iaS*`
   interaction runs lack saved `sensor_swing_deg`. Today's sensing implementation cannot
   retroactively validate earlier experiments.
3. **The baseline cell mixed force settings.** The historical Robotiq fraction 0.55,
   E=30000 cell pooled 2, 4 and 6 N runs. At 4 N alone it is 2/3 controller completions,
   not 8/9. Its terminal-angle mean is 10.5 degrees, not 7.4. The corrected force sequence
   3.0 / 10.5 / 8.5 degrees is not monotonic.
4. **Targets change across cells.** Nominal pinch fraction does not identify the same leaf
   or material region. Across-hand differences are confounded by force, reach, contact
   geometry and selected leaf. The plant need not change to fix the experiment design.
5. **Angle exclusions are outcome dependent.** The old analysis folds unsigned normals
   and drops angles above 60 degrees. Buckling or geometry may amplify local angle;
   diagnose fit quality/correspondence, retain invalid counts and show sensitivity.
6. **Colour is four-swatch classification, not five-class recognition.** Five nominal
   material shades are mapped onto four non-neutral chart swatches. The archived colour
   matrices contain 3,800 rows (3,555 valid leaf samples), with 19 condition names including
   the default. The old 6,700-count and 17/18-condition wording was inconsistent.
7. **Semantic grading is not target-identity accuracy.** The colour study can accept a
   known leaf under a sample pixel and grade that material. This cannot establish a 100%
   intended-leaf sampling rate. Also report whether sampled and intended leaf IDs agree.
8. **Available samples differ by calibration method.** Compare on matched intersections
   and report rejection/coverage as well as conditional error. Preserve the negative
   observation that presentation did not materially improve chromaticity in this renderer.
9. **No damage or tissue-property ground truth.** Pad load limits and FEM stability do not
   establish safe forces for living maize, anisotropic tissue realism, or a health diagnosis.

Reproduce the interaction audit with:

```bash
cd /home/yogesh/Grasp_direct/LCC_robotics_paper
/home/yogesh/anaconda3/bin/python scripts/audit_interaction.py
```

The output retains all raw endpoints, flags exclusions and hashes the source files.
Neither old experiment output nor its original analysis script is overwritten.

## Frozen-plant experiment contract

Keep the current plant mesh, material assignments, attachments, FEM resolution, damping,
masses, lighting for interaction tests and reset state fixed. Record a resolved-config
manifest and asset hashes, not only command-line defaults. The older modulus sweeps stay
as historical context; do not run new stiffness sweeps for this proposal.

Vary robot decisions: target leaf/region, grasp location among existing reachable patches,
small approach offsets, requested regional orientation, tool type and controller. Injected
observation noise/dropout may be added as a separately labelled sensor stress test without
changing physics. Do not claim this substitutes for unseen plant geometry.

The trial unit is a matched (leaf, starting patch, sensing region, desired pose, reset,
tool) episode. Controllers get the same force cap, time budget and maximum number of
grasps. Randomize method order; restore the same settled initial state where supported
and log reset variability. All target-selection failures remain in an end-to-end analysis.
Report a second conditional manipulation analysis so navigation does not hide contact effects.

### Stage 1: measurement validation before control claims

Track the same free-blade patch near the grasp and near the sensing region at sufficient
rate for the slow motion (start with 10 Hz). Evaluate correspondence, angular error,
coverage and latency against FEM ground truth used only by a separate evaluator. The
current prediction that a sample moves by the commanded lift must not become the only
search window: it would hide poor transfer. Use fit-quality gates, not an upper angle cut.

Run small forward/reverse probes with fixed force control. Estimate a local lift/roll
response and uncertainty. Test whether the first probe predicts a later held-out motion
on that same grasp. Estimate effective response, not Young's modulus. If response cannot
be predicted better than a constant/zero model, stop before claiming adaptive control.

### Stage 2: smallest decisive comparison

Use four methods first: current force-limited sweep; fixed-gain regional visual servo;
simple low-response-triggered regrasp; proposed response-aware controller. An adaptive
visual-servo baseline and the uncertainty/no-regrasp ablations follow if there is a gain.
All methods that can regrasp receive the same attempt budget. Do not compare a multi-attempt
method against a one-attempt baseline without separately reporting that advantage.

A practical pilot is three eligible leaves × three reachable grasp locations × two
approach offsets per hand, giving up to 36 matched blocks across both hands. Four methods
would require up to 144 episodes; this is a planning count, not a performed study or a
power calculation. Retain infeasible cells in eligibility reporting and separate the
common reachable subset from full-system performance. Determine replication needs from
paired pilot variance and a preregistered minimum useful effect, not from render-frame count.

### Primary endpoint and safeguards

Use actual leaf-region orientation error plus visible-region coverage and force-valid
dwell. Example development settings: 15-degree requested reorientation, 5-degree error
tolerance, 2-second dwell. Freeze thresholds on development episodes; evaluate held-out
leaf/patch combinations. A symmetric normal cannot prove front/back access; validate an
oriented representation before claiming both leaf faces were inspected.

Report paired success differences, time-to-goal including censored timeouts, pose tracking
error, valid-observation fraction, raw force peaks/exceedance duration, regrasp count,
force exposure (N s), and post-release residual displacement/recovery time. Force exposure
is not work, and recovery is not biological non-damage. Cluster statistical summaries by
run/leaf block; do not count illumination settings or video frames as independent plants.
One morphology allows within-model claims only. Do not advertise intervals over a plant
population that was never sampled.

### Tests that can disprove our story

- If ordinary visual feedback matches the proposal, the learned response is unnecessary.
- If a distal or random regrasp matches it under the same budget, the informed decision
  adds no demonstrated value.
- If the effect disappears at equal force/time/attempt budgets, it is not the claimed effect.
- If camera-only view selection matches measurement coverage without touching the plant,
  contact is not justified for that subset. Do not manufacture a colour benefit.
- If all gains require ground-truth tracking, the sensor-only claim fails.

## Submission path

Lead with the contact-to-region response decision, not navigation, simulator construction,
the 24-DoF hand, or an LCC health claim. Keep colour as a downstream measurement with
availability and ambiguity; move the extensive illumination sweep to supplementary material.
The current draft remains a working paper, not an ICRA-ready claim of a validated method.

Before submission: run the matched experiment, validate regional tracking, include a
real-leaf or carefully scoped physical contact validation if feasible, distinguish every
simulation-only claim, finalize affiliations, verify all bibliography metadata, and compile
the IEEE layout. Real tissue testing would require its own appropriate force/damage protocol;
the current simulation force cap should not be transferred uncritically. None of these
future experiments was fabricated or launched during this paper-editing task.
