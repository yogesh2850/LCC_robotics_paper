# ICRA study plan (2026-09-18)

## Verdict on the current work
Both pipelines (Robotiq rq36, Shadow sh14) are working systems demonstrations: one plant
instance, one run per configuration, no hypothesis, no baseline, no statistics, simulation
only. That is not an ICRA paper. What simulation CAN establish rigorously is a controlled
study with many paired measurements, which is what the LCC application needs anyway.

## Scientific question
Leaf colour charts are read by eye under whatever light the field offers. A robot that can
grasp the leaf can *present* it: lift it out of the canopy shade, turn it toward the camera,
and hold a colour reference next to it. Does that make colour assessment illumination-robust,
and where should the reference be?

Hypotheses
- H1 Passive imaging of a leaf in situ (scene camera or close-up wrist camera, no contact),
  calibrated with a board on the platform, has a colour error that varies strongly with
  illumination (sun angle / intensity / overcast, canopy shadow): leaf and board see
  different light.
- H2 Active presentation (pinch, lift, roll toward the camera) reduces the error and its
  spread; lifting (out of the shade) and turning (facing the camera) contribute separately.
- H3 A reference co-located with the gripper (white + gray chips on the finger, 2 cm from the
  pinched blade) removes most of the residual error, because reference and leaf share the
  same illumination and viewing geometry.
- H4 The result holds for two end-effectors (2F-85, Shadow Hand) and across plant instances
  (yaw, leaf stiffness, shade assignment), with a characterised failure taxonomy.

## Evaluation
Unit of measurement: one (leaf, illumination condition, method) triple.
- Illumination set L (16): clear sky, sun elevation {20, 40, 60} deg x azimuth {0, 90, 180,
  270} deg; low sun 15 deg (2 azimuths, half intensity, dimmer sky); overcast (sky only);
  bright (sun 1.6x). Applied at run time (RTX lights), physics untouched.
- Methods M: passive-scene (platform RGB-D camera, board calibration), passive-wrist (wrist
  camera at the pre-pinch pose, no contact, board calibration), active-hold at roll 0, +35,
  -35 deg with board calibration, and the same with chip calibration; raw (no calibration)
  as a floor.
- Metrics: chromaticity distance between the calibrated leaf colour and the ground-truth
  shade; correct-class rate (5 shades); decision margin; spread (std over L) as the
  illumination sensitivity; manipulation: pinch success, hold seconds, max force, blade
  turn, lift.
- Plant instances P: yaw {0, 120, 240} x leaf Young's modulus {3e4, 3e5} x shade seed {0, 1}
  (12), 3 leaves each. Grippers G: Shadow, 2F-85. => ~12 x 3 x 16 x 7 ~ 4000 measurements
  per gripper.
- Ground truth: leaf material sRGB (Plant handles), also reported as the ideal reference.

## Build list
1. illumination.py: condition table, apply(stage, cond) on /World/Sun and /World/Sky.
2. Co-located reference chips (white + gray) on the upper jaw, visible to the wrist camera.
3. ColorStudy hooks in the controller: passive-scene after targeting, passive-wrist at the
   pre-pinch pose, active at each roll dwell; writes color_study.csv.
4. run flags: --plant-yaw, --shade-seed (with --leaf-youngs); a matrix driver; analysis.
5. Port to agronomist_robotiq; run both matrices; write up.

## Log
- 2026-09-18 19:00 sh15 (Shadow, neutral illuminants): machinery works; board mis-calibrates in 4/17
  conditions when the board is sunlit and the leaf shaded; chips (buried in the thumb mesh at
  8.5 mm) read the thumb surface -> moved proud (14.5 mm), verified with test_posture images.
- 19:35 first matrix run with mild chromatic illuminants: raw chromaticity barely moves with
  illumination (std 0.01-0.02 over 17 conditions) while both calibrations ADD error; the affine
  two-point chip model is ill-conditioned for a dark leaf with dim chips -> chip calibration is
  now a pure illuminant gain (white chip when unclipped, else grey), recomputed offline from
  the stored chip readings; board swatches are stored too for a gain-only board variant.
- 20:00 illuminant set widened to realistic daylight/canopy chromaticities (sun 5000 K vs sky
  10000 K, golden low sun, cool overcast, green canopy ambient); matrices restarted:
  Shadow stS_* (12 runs) then Robotiq stR_* (12 runs), ~11 min each.
- 20:20 light colour was not reaching the render: RTX's default neutral ambient fill
  (/rtx/sceneDb/ambientLightIntensity 1.0) dominated the chromaticity (a red sun+sky gave a
  near-white card). Disabled in run.py for both projects (physically based sun + sky only);
  matrices restarted.
- 21:30 interim (5 Shadow runs): manipulation degrades off the tuned instance (yaw 120 / stiff
  leaves): failure classes seen: (a) "unreachable" at selection (no heading with a feasible
  transit+pinch IK), (b) approach timeout, (c) no pinch (thumb closed without loading), (d) hold
  established but no valid colour frame: with 3e5 Pa leaves the blade does not follow the
  30 mm lift, the sample points (modelled as carried by the lift) miss the blade (depth check
  fails) -> "probe timeout, frames 0". Kept as-is for the matrix (no mid-matrix changes).
  Colour: over 9 leaves raw acc 0.64 (adjacent shades), chip 0.86-0.88 when exposed (~40 %),
  board 0.45-0.54; passive_scene raw 0.46.
- 21:45 (clock corrected; the previous timestamps were ~1 h ahead) the first Shadow/Robotiq
  matrices are INVALID and were deleted: disabling the RTX ambient fill took effect
  non-deterministically (run 1 kept it, later runs lost it), the canopy interior then rendered
  4x darker than the perception was tuned for (leaf pixels 180k -> 40k), fewer usable patches,
  and "no pinch" failures turned out to be ghost targets: patches on visual-only neighbour
  leaves (gt gap 70-400 mm). New lighting model: fill kept at its tuned level but scaled with
  the sky intensity and TINTED with the sky colour per condition (illumination.apply); ghost
  targets are now a separate outcome class in analyze_manip (gt gap > 30 mm). Both matrices
  restarted 21:45; ~9 min per run, 24 runs.
- 23:35 Shadow matrix done (12 runs, docs/study_results_shadow.md, docs/manip_results_shadow.txt):
  manipulation 16/27 leaves complete; targeting failures: 5 ghost targets (visual-only neighbour
  leaf), 3 runs with no usable patch; 2 holds without a visible sample, 1 unreachable. Excluding
  targeting failures 16/19. Colour (n = 340-433 rows/stage, 15-23 leaves): chips give the most
  illumination-stable verdicts (flip rate 0.33-0.44 of leaves vs raw 0.67-0.70, board 0.44-0.70;
  error std over conditions chips 0.016-0.022 < raw 0.022-0.027 < board 0.033-0.040); the board
  is the worst estimator in accuracy (0.46-0.57 vs raw 0.55-0.68, chips 0.62-0.70). Paired stage
  gain: pinch/lift/roll change the same leaf's chromaticity error by < 0.005 -> the higher
  accuracy of active stages (0.67 vs 0.57) is selection (leaves that could be pinched), not
  presentation. View-selection proxy (best-exposed chip) does not beat the mean view.
- 01:05 Robotiq matrix done (docs/study_results_robotiq.md, manip_results_robotiq.txt): 10/23
  leaves complete (yaw 0: 8/10, yaw 120: 0 (4 runs no usable patch), yaw 240: 2/9 (6 ghosts));
  pinch 4.0 N. Colour: chip flip rate 0.13-0.69 vs raw 0.64-0.90, board 0.64-0.75; chip spread
  0.014-0.023 < raw 0.021-0.027 < board 0.027-0.037; presentation gain -0.005..0. Combined
  analysis docs/study_results_both.md; figures in the paper repo; paper committed + pushed.
Conclusions for the paper: (1) board-on-platform calibration hurts; (2) jaw reference = most
stable verdict when exposed; (3) presentation does not change chromaticity, it buys identity
and both faces; (4) generalisation limit = targeting (ghost / no usable), not the hand.
- 02:00 iteration 2 on the turned instances (stT_*, blade-direction filter dropped, root radius
  0.12): 3/16 leaves; 6 ghosts remain, 6 pinched leaves had no visible sample (thumb hides the
  sheath-side sample points). Iteration 3 (stU_*): planting-grid prior (root closer to the target
  than to any neighbour by 5 cm) + sample points alternating sides of the pinch.
- 03:00 iteration 3 (stU_*, planting-grid prior + two-sided sample points): 0 ghosts (was 6),
  3/10 complete; the remaining 6 are ONE-SIDED HOLDS: thumb presses the blade on the finger
  body, index load cell < 0.08 N, yet summed load 1.2-1.8 N, lift 30 mm, 55-59 valid colour
  frames -> the validity rule (both pads loaded) rejects a presented, measured leaf. Reported as
  a design choice in the paper (commit pushed). Stopping the loop here.

## Interaction study (2026-09-19, after the user's "is this ICRA-worthy?" -> focus on the physics)
Verdict on the colour study: not ICRA-worthy alone (renderer-dependent colour, negative headline,
~55 % manipulation success). New focus: what determines whether a pinched blade can be held and
re-oriented: E1 pinch fraction {0.35, 0.55, 0.75} x leaf E {3e4, 3e5, 3e6} x hand; E3 placement
error along the normal (+-1.5, +-3 cm) and across (+-2 cm); E2 pinch force {2, 4, 6 N} (2F-85).
Controls: `--pinch-frac` (camera candidates sorted by |along_frac - frac|; ground-truth targeting
turned out stale vs the planner), `--offset-normal/--offset-across` (injected into the pinch
target), `--force-target` (scales the force window); `run_meta.json` per run;
`run_interaction.sh <dir> <prefix>` (iaR_*, iaS_*), `analyze_interaction.py`. Launched 11:35.
- 15:50 interaction study done (docs/interaction_results_{robotiq,shadow}.txt). Blade turn per
  35 deg roll is set by stiffness and pinch location, not the hand: soft blade 7-11 deg (2F-85,
  4 N) / 15-17 deg (Shadow, 2 N) at mid/outer pinch; ~0 at 3e5+ Pa (2F-85 still 10 deg at 3e5).
  Force 2/4/6 N -> 3/7.4/8.5 deg (pads slip; torque budget limits). Placement error: 2F-85
  tolerates +-3 cm along the normal (2-3/3), Shadow loses a third (2/3; across: 1-2/3). Sheath
  pinches (0.35) fail at the approach (crowded corridor). GT turn metric folded (<=90, >60 = NaN).
  Paper updated + pushed.
- 16:40 pre-submission list: (1) cell sizes -> expanded matrix run_interaction2.sh (seeds 1,2,0 x
  4 leaves, ibR_*/ibS_*, ~96 runs, launched 16:40); (2) sensor-based turn: wrist-camera blade
  normal 5 cm toward the tip at pinch / +35 / -35 / 0 dwells (`sense_blade_normal`,
  `sensor_swing_deg`, `sensor_turn_deg` in leaf records); Robotiq smoke: GT patch turn 2.5 deg vs
  sensed free-blade turn 27 deg at -35 -> the two measure different things (clamped nodes vs the
  free blade the camera sees), both reported; (3) paper reframed: title "What Makes a Leaf Follow
  the Gripper", interaction study first, colour study supporting (committed); (4) real-plant check
  impossible here (sim only) - left as the TODO in the paper.
