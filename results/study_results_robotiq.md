# Colour study results

runs: outputs/stR_y0_e3e4_s0/, outputs/stR_y0_e3e4_s1/, outputs/stR_y0_e3e5_s0/, outputs/stR_y0_e3e5_s1/, outputs/stR_y120_e3e4_s0/, outputs/stR_y120_e3e4_s1/, outputs/stR_y120_e3e5_s0/, outputs/stR_y120_e3e5_s1/, outputs/stR_y240_e3e4_s0/, outputs/stR_y240_e3e4_s1/, outputs/stR_y240_e3e5_s0/, outputs/stR_y240_e3e5_s1/
rows: 1558 (valid 1500)

## Per method (chromaticity error to ground truth, class accuracy)
           method   n  leaves  raw_err_mean  raw_err_std  raw_acc  board_n  board_err_mean  board_err_std  board_acc  chip_n  chip_err_mean  chip_err_std  chip_acc  boardgain_err_mean  boardgain_acc
    passive_scene 398      21         0.134        0.095    0.495      318           0.145          0.098      0.418       0            NaN           NaN       NaN               0.156          0.387
    passive_wrist 304      16         0.141        0.102    0.523      244           0.146          0.101      0.398     290          0.146         0.098     0.531               0.155          0.398
     active_pinch 190      10         0.085        0.032    0.621      155           0.091          0.043      0.529     106          0.097         0.047     0.547               0.104          0.484
 active_roll_zero 190      10         0.087        0.036    0.584      155           0.093          0.050      0.523     123          0.100         0.046     0.545               0.106          0.468
 active_roll_plus 209      11         0.086        0.032    0.627      174           0.089          0.041      0.540     150          0.088         0.033     0.667               0.101          0.488
active_roll_minus 209      11         0.088        0.033    0.636      174           0.088          0.046      0.638      48          0.087         0.036     0.750               0.104          0.560

## Illumination sensitivity: std of the error over the 17 conditions per leaf (mean over leaves)
passive_scene      err_raw: 0.0271 (leaves 21)  err_board: 0.0368 (leaves 21)  err_chip: nan (leaves 0)
passive_wrist      err_raw: 0.0207 (leaves 16)  err_board: 0.0273 (leaves 16)  err_chip: 0.0158 (leaves 16)
active_pinch       err_raw: 0.0223 (leaves 10)  err_board: 0.0299 (leaves 10)  err_chip: 0.0150 (leaves 9)
active_roll_zero   err_raw: 0.0265 (leaves 10)  err_board: 0.0358 (leaves 10)  err_chip: 0.0228 (leaves 9)
active_roll_plus   err_raw: 0.0232 (leaves 11)  err_board: 0.0296 (leaves 11)  err_chip: 0.0166 (leaves 11)
active_roll_minus  err_raw: 0.0218 (leaves 11)  err_board: 0.0312 (leaves 11)  err_chip: 0.0141 (leaves 8)

## Per condition: passive_scene
                   n   raw  board  chip  board_acc  chip_acc
condition                                                   
bright_e60_a135   21 0.145  0.144   NaN      0.429     0.000
canopy_e40_a0     21 0.120  0.120   NaN      0.476     0.000
clear_e20_a0      21 0.119  0.114   NaN      0.667     0.000
clear_e20_a180    21 0.130  0.163   NaN      0.095     0.000
clear_e20_a270    21 0.136  0.140   NaN      0.476     0.000
clear_e20_a90     21 0.125  0.118   NaN      0.619     0.000
clear_e40_a0      21 0.128  0.130   NaN      0.524     0.000
clear_e40_a180    21 0.136  0.174   NaN      0.095     0.000
clear_e40_a270    21 0.141  0.151   NaN      0.333     0.000
clear_e40_a90     21 0.137  0.139   NaN      0.429     0.000
clear_e60_a0      21 0.131  0.172   NaN      0.286     0.000
clear_e60_a180    21 0.143  0.175   NaN      0.048     0.000
clear_e60_a270    21 0.150  0.168   NaN      0.333     0.000
clear_e60_a90     21 0.141  0.163   NaN      0.238     0.000
default           21 0.145  0.145   NaN      0.381     0.000
lowsun_e15_a225   20 0.131  0.133   NaN      0.100     0.000
lowsun_e15_a45    21 0.132  0.127   NaN      0.095     0.000
neutral_e40_a180  21 0.125  0.179   NaN      0.333     0.000
overcast          21 0.124  0.130   NaN      0.381     0.000

## Per condition: active_roll_zero
                   n   raw  board  chip  board_acc  chip_acc
condition                                                   
bright_e60_a135   10 0.100  0.100 0.133      0.500     0.200
canopy_e40_a0     10 0.092  0.065 0.076      0.800     0.600
clear_e20_a0      10 0.075  0.064 0.087      0.800     0.500
clear_e20_a180    10 0.086  0.110 0.146      0.100     0.000
clear_e20_a270    10 0.084  0.076 0.096      0.600     0.400
clear_e20_a90     10 0.078  0.066 0.083      0.800     0.600
clear_e40_a0      10 0.088  0.083 0.094      0.600     0.500
clear_e40_a180    10 0.093  0.119 0.124      0.000     0.100
clear_e40_a270    10 0.085  0.091 0.097      0.500     0.400
clear_e40_a90     10 0.097  0.095 0.103      0.500     0.400
clear_e60_a0      10 0.080  0.106 0.094      0.300     0.500
clear_e60_a180    10 0.099  0.127 0.139      0.100     0.100
clear_e60_a270    10 0.099  0.117 0.128      0.500     0.200
clear_e60_a90     10 0.095  0.108 0.115      0.300     0.300
default           10 0.083  0.084 0.096      0.500     0.400
lowsun_e15_a225   10 0.060  0.079 0.085      0.100     0.500
lowsun_e15_a45    10 0.097  0.056 0.066      0.200     0.500
neutral_e40_a180  10 0.093  0.164 0.135      0.300     0.100
overcast          10 0.071  0.073 0.098      0.600     0.400

## Sample identity (intended leaf) and verdict flips across the 18 conditions of one leaf
           method   n  intended_leaf  flip_raw  flip_board  flip_chip
    passive_scene 398          0.907     0.762       0.714        NaN
    passive_wrist 304          1.000     0.812       0.750      0.688
     active_pinch 190          1.000     0.800       0.700      0.444
 active_roll_zero 190          1.000     0.900       0.700      0.667
 active_roll_plus 209          1.000     0.818       0.636      0.364
active_roll_minus 209          1.000     0.636       0.727      0.125

## Paired comparison (rows with raw, board and chip all valid)
           method   n  leaves  raw_err  board_err  chip_err  raw_acc  board_acc  chip_acc  chip<raw  chip<board
    passive_wrist 231      16    0.140      0.144     0.147    0.519      0.407     0.511     0.346       0.364
     active_pinch  93       9    0.090      0.095     0.101    0.527      0.462     0.516     0.290       0.237
 active_roll_zero 108       9    0.091      0.094     0.102    0.528      0.491     0.537     0.241       0.167
 active_roll_plus 130      11    0.083      0.087     0.090    0.677      0.546     0.638     0.277       0.262
active_roll_minus  43       7    0.082      0.075     0.089    0.721      0.698     0.721     0.279       0.233

## Presentation gain: error at each active stage minus passive_wrist, same estimator (negative = better)
            stage   n  raw_delta  board_delta  chip_delta  chip_pairs
     active_pinch 190     -0.005        0.000      -0.005         105
 active_roll_zero 190     -0.003        0.002      -0.003         120
 active_roll_plus 190     -0.001        0.001      -0.006         127
active_roll_minus 190      0.000        0.000      -0.010          47

## Illumination-aware view selection (chip calibration): selected vs fixed vs oracle
groups: 126  err selected 0.0990 (acc 0.587)  mean over views 0.0948 (acc 0.601)  oracle 0.0812 (acc 0.690)

