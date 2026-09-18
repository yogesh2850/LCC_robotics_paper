# Colour study results

runs: outputs/stS_y0_e3e4_s0/, outputs/stS_y0_e3e4_s1/, outputs/stS_y0_e3e5_s0/, outputs/stS_y0_e3e5_s1/, outputs/stS_y120_e3e4_s0/, outputs/stS_y120_e3e4_s1/, outputs/stS_y120_e3e5_s0/, outputs/stS_y120_e3e5_s1/, outputs/stS_y240_e3e4_s0/, outputs/stS_y240_e3e4_s1/, outputs/stS_y240_e3e5_s0/, outputs/stS_y240_e3e5_s1/, ../agronomist_robotiq/outputs/stR_y0_e3e4_s0/, ../agronomist_robotiq/outputs/stR_y0_e3e4_s1/, ../agronomist_robotiq/outputs/stR_y0_e3e5_s0/, ../agronomist_robotiq/outputs/stR_y0_e3e5_s1/, ../agronomist_robotiq/outputs/stR_y120_e3e4_s0/, ../agronomist_robotiq/outputs/stR_y120_e3e4_s1/, ../agronomist_robotiq/outputs/stR_y120_e3e5_s0/, ../agronomist_robotiq/outputs/stR_y120_e3e5_s1/, ../agronomist_robotiq/outputs/stR_y240_e3e4_s0/, ../agronomist_robotiq/outputs/stR_y240_e3e4_s1/, ../agronomist_robotiq/outputs/stR_y240_e3e5_s0/, ../agronomist_robotiq/outputs/stR_y240_e3e5_s1/
rows: 3800 (valid 3555)

## Per method (chromaticity error to ground truth, class accuracy)
           method   n  leaves  raw_err_mean  raw_err_std  raw_acc  board_n  board_err_mean  board_err_std  board_acc  chip_n  chip_err_mean  chip_err_std  chip_acc  boardgain_err_mean  boardgain_acc
    passive_scene 776      41         0.122        0.084    0.523      610           0.135          0.088      0.436       0            NaN           NaN       NaN               0.144          0.388
    passive_wrist 737      39         0.118        0.081    0.550      583           0.128          0.086      0.451     603          0.125         0.084     0.577               0.136          0.410
     active_pinch 530      28         0.084        0.036    0.655      426           0.095          0.057      0.552     326          0.089         0.043     0.632               0.103          0.487
 active_roll_zero 529      28         0.086        0.038    0.643      426           0.096          0.056      0.535     345          0.092         0.044     0.646               0.106          0.486
 active_roll_plus 549      29         0.088        0.039    0.643      445           0.096          0.055      0.542     150          0.088         0.033     0.667               0.109          0.481
active_roll_minus 434      26         0.089        0.039    0.638      364           0.097          0.054      0.566     212          0.101         0.058     0.670               0.111          0.525

## Illumination sensitivity: std of the error over the 17 conditions per leaf (mean over leaves)
passive_scene      err_raw: 0.0257 (leaves 41)  err_board: 0.0350 (leaves 41)  err_chip: nan (leaves 0)
passive_wrist      err_raw: 0.0218 (leaves 39)  err_board: 0.0315 (leaves 39)  err_chip: 0.0158 (leaves 39)
active_pinch       err_raw: 0.0223 (leaves 28)  err_board: 0.0348 (leaves 28)  err_chip: 0.0163 (leaves 27)
active_roll_zero   err_raw: 0.0269 (leaves 28)  err_board: 0.0388 (leaves 28)  err_chip: 0.0220 (leaves 26)
active_roll_plus   err_raw: 0.0238 (leaves 29)  err_board: 0.0330 (leaves 29)  err_chip: 0.0166 (leaves 11)
active_roll_minus  err_raw: 0.0243 (leaves 26)  err_board: 0.0319 (leaves 26)  err_chip: 0.0176 (leaves 23)

## Per condition: passive_scene
                   n   raw  board  chip  board_acc  chip_acc
condition                                                   
bright_e60_a135   41 0.131  0.131   NaN      0.463     0.000
canopy_e40_a0     41 0.112  0.111   NaN      0.488     0.000
clear_e20_a0      41 0.111  0.109   NaN      0.488     0.000
clear_e20_a180    41 0.121  0.164   NaN      0.073     0.000
clear_e20_a270    41 0.123  0.131   NaN      0.537     0.000
clear_e20_a90     41 0.113  0.106   NaN      0.561     0.000
clear_e40_a0      41 0.120  0.127   NaN      0.512     0.000
clear_e40_a180    41 0.125  0.168   NaN      0.073     0.000
clear_e40_a270    41 0.127  0.140   NaN      0.390     0.000
clear_e40_a90     41 0.122  0.129   NaN      0.463     0.000
clear_e60_a0      41 0.123  0.157   NaN      0.341     0.000
clear_e60_a180    41 0.130  0.167   NaN      0.024     0.000
clear_e60_a270    41 0.132  0.153   NaN      0.366     0.000
clear_e60_a90     41 0.127  0.149   NaN      0.293     0.000
default           41 0.125  0.136   NaN      0.415     0.000
lowsun_e15_a225   40 0.125  0.121   NaN      0.100     0.000
lowsun_e15_a45    39 0.123  0.111   NaN      0.077     0.000
neutral_e40_a180  41 0.112  0.177   NaN      0.366     0.000
overcast          41 0.115  0.119   NaN      0.463     0.000

## Per condition: active_roll_zero
                   n   raw  board  chip  board_acc  chip_acc
condition                                                   
bright_e60_a135   28 0.102  0.103 0.133      0.536     0.179
canopy_e40_a0     28 0.100  0.070 0.068      0.714     0.607
clear_e20_a0      28 0.069  0.068 0.081      0.643     0.536
clear_e20_a180    28 0.083  0.132 0.100      0.071     0.321
clear_e20_a270    28 0.083  0.073 0.089      0.679     0.536
clear_e20_a90     28 0.075  0.071 0.080      0.679     0.464
clear_e40_a0      28 0.084  0.082 0.086      0.643     0.643
clear_e40_a180    28 0.090  0.142 0.102      0.036     0.250
clear_e40_a270    28 0.079  0.097 0.096      0.536     0.286
clear_e40_a90     28 0.086  0.085 0.091      0.607     0.393
clear_e60_a0      28 0.082  0.117 0.090      0.357     0.464
clear_e60_a180    28 0.091  0.146 0.116      0.036     0.143
clear_e60_a270    28 0.090  0.125 0.103      0.429     0.429
clear_e60_a90     28 0.093  0.112 0.110      0.357     0.393
default           28 0.075  0.075 0.082      0.536     0.536
lowsun_e15_a225   28 0.085  0.090 0.096      0.143     0.607
lowsun_e15_a45    25 0.100  0.061 0.074      0.160     0.480
neutral_e40_a180  28 0.088  0.161 0.118      0.393     0.214
overcast          28 0.075  0.075 0.085      0.607     0.536

## Sample identity (intended leaf) and verdict flips across the 18 conditions of one leaf
           method   n  intended_leaf  flip_raw  flip_board  flip_chip
    passive_scene 776          0.952     0.732       0.707        NaN
    passive_wrist 737          1.000     0.744       0.667      0.538
     active_pinch 530          1.000     0.714       0.536      0.444
 active_roll_zero 529          1.000     0.750       0.679      0.500
 active_roll_plus 549          1.000     0.724       0.552      0.364
active_roll_minus 434          1.000     0.615       0.577      0.261

## Paired comparison (rows with raw, board and chip all valid)
           method   n  leaves  raw_err  board_err  chip_err  raw_acc  board_acc  chip_acc  chip<raw  chip<board
    passive_wrist 480      39    0.119      0.127     0.127    0.569      0.479     0.558     0.338       0.360
     active_pinch 268      26    0.082      0.092     0.091    0.660      0.552     0.597     0.299       0.287
 active_roll_zero 285      26    0.084      0.093     0.094    0.646      0.530     0.625     0.284       0.249
 active_roll_plus 130      11    0.083      0.087     0.090    0.677      0.546     0.638     0.277       0.262
active_roll_minus 183      22    0.089      0.095     0.105    0.656      0.552     0.623     0.213       0.213

## Presentation gain: error at each active stage minus passive_wrist, same estimator (negative = better)
            stage   n  raw_delta  board_delta  chip_delta  chip_pairs
     active_pinch 529     -0.003       -0.002      -0.003         304
 active_roll_zero 528     -0.001       -0.000      -0.002         311
 active_roll_plus 529      0.002        0.001      -0.006         127
active_roll_minus 415     -0.001        0.000      -0.001         169

## Illumination-aware view selection (chip calibration): selected vs fixed vs oracle
groups: 358  err selected 0.0952 (acc 0.656)  mean over views 0.0904 (acc 0.660)  oracle 0.0799 (acc 0.715)

