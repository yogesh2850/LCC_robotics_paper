# Colour study results

runs: outputs/stS_y0_e3e4_s0/, outputs/stS_y0_e3e4_s1/, outputs/stS_y0_e3e5_s0/, outputs/stS_y0_e3e5_s1/, outputs/stS_y120_e3e4_s0/, outputs/stS_y120_e3e4_s1/, outputs/stS_y120_e3e5_s0/, outputs/stS_y120_e3e5_s1/, outputs/stS_y240_e3e4_s0/, outputs/stS_y240_e3e4_s1/, outputs/stS_y240_e3e5_s0/, outputs/stS_y240_e3e5_s1/
rows: 2242 (valid 2055)

## Per method (chromaticity error to ground truth, class accuracy)
           method   n  leaves  raw_err_mean  raw_err_std  raw_acc  board_n  board_err_mean  board_err_std  board_acc  chip_n  chip_err_mean  chip_err_std  chip_acc  boardgain_err_mean  boardgain_acc
    passive_scene 378      20         0.110        0.069    0.553      292           0.125          0.074      0.455       0            NaN           NaN       NaN               0.132          0.389
    passive_wrist 433      23         0.102        0.057    0.568      339           0.115          0.072      0.490     313          0.105         0.063     0.620               0.122          0.418
     active_pinch 340      18         0.083        0.039    0.674      271           0.097          0.063      0.565     220          0.085         0.040     0.673               0.103          0.488
 active_roll_zero 339      18         0.085        0.039    0.676      271           0.098          0.059      0.542     222          0.088         0.042     0.703               0.106          0.496
 active_roll_plus 340      18         0.089        0.043    0.653      271           0.101          0.063      0.542       0            NaN           NaN       NaN               0.114          0.476
active_roll_minus 225      15         0.090        0.045    0.640      190           0.104          0.060      0.500     164          0.105         0.063     0.646               0.118          0.493

## Illumination sensitivity: std of the error over the 17 conditions per leaf (mean over leaves)
passive_scene      err_raw: 0.0243 (leaves 20)  err_board: 0.0332 (leaves 20)  err_chip: nan (leaves 0)
passive_wrist      err_raw: 0.0226 (leaves 23)  err_board: 0.0344 (leaves 23)  err_chip: 0.0158 (leaves 23)
active_pinch       err_raw: 0.0224 (leaves 18)  err_board: 0.0376 (leaves 18)  err_chip: 0.0170 (leaves 18)
active_roll_zero   err_raw: 0.0271 (leaves 18)  err_board: 0.0404 (leaves 18)  err_chip: 0.0216 (leaves 17)
active_roll_plus   err_raw: 0.0242 (leaves 18)  err_board: 0.0350 (leaves 18)  err_chip: nan (leaves 0)
active_roll_minus  err_raw: 0.0266 (leaves 15)  err_board: 0.0325 (leaves 15)  err_chip: 0.0197 (leaves 15)

## Per condition: passive_scene
                   n   raw  board  chip  board_acc  chip_acc
condition                                                   
bright_e60_a135   20 0.117  0.118   NaN      0.500     0.000
canopy_e40_a0     20 0.105  0.101   NaN      0.500     0.000
clear_e20_a0      20 0.103  0.101   NaN      0.300     0.000
clear_e20_a180    20 0.111  0.164   NaN      0.050     0.000
clear_e20_a270    20 0.109  0.121   NaN      0.600     0.000
clear_e20_a90     20 0.102  0.092   NaN      0.500     0.000
clear_e40_a0      20 0.113  0.123   NaN      0.500     0.000
clear_e40_a180    20 0.114  0.161   NaN      0.050     0.000
clear_e40_a270    20 0.112  0.128   NaN      0.450     0.000
clear_e40_a90     20 0.107  0.118   NaN      0.500     0.000
clear_e60_a0      20 0.114  0.141   NaN      0.400     0.000
clear_e60_a180    20 0.116  0.158   NaN      0.000     0.000
clear_e60_a270    20 0.114  0.137   NaN      0.400     0.000
clear_e60_a90     20 0.113  0.133   NaN      0.350     0.000
default           20 0.103  0.127   NaN      0.450     0.000
lowsun_e15_a225   20 0.119  0.108   NaN      0.100     0.000
lowsun_e15_a45    18 0.113  0.072   NaN      0.056     0.000
neutral_e40_a180  20 0.098  0.175   NaN      0.400     0.000
overcast          20 0.105  0.107   NaN      0.550     0.000

## Per condition: active_roll_zero
                   n   raw  board  chip  board_acc  chip_acc
condition                                                   
bright_e60_a135   18 0.104  0.104 0.134      0.556     0.167
canopy_e40_a0     18 0.105  0.072 0.064      0.667     0.611
clear_e20_a0      18 0.067  0.071 0.078      0.556     0.556
clear_e20_a180    18 0.082  0.146 0.088      0.056     0.500
clear_e20_a270    18 0.083  0.072 0.085      0.722     0.611
clear_e20_a90     18 0.074  0.074 0.077      0.611     0.389
clear_e40_a0      18 0.082  0.081 0.082      0.667     0.722
clear_e40_a180    18 0.088  0.156 0.092      0.056     0.333
clear_e40_a270    18 0.076  0.100 0.095      0.556     0.222
clear_e40_a90     18 0.079  0.079 0.082      0.667     0.389
clear_e60_a0      18 0.083  0.124 0.088      0.389     0.444
clear_e60_a180    18 0.086  0.158 0.103      0.000     0.167
clear_e60_a270    18 0.085  0.130 0.094      0.389     0.556
clear_e60_a90     18 0.092  0.115 0.106      0.389     0.444
default           18 0.070  0.070 0.075      0.556     0.611
lowsun_e15_a225   18 0.099  0.098 0.101      0.167     0.667
lowsun_e15_a45    15 0.102  0.065 0.080      0.133     0.467
neutral_e40_a180  18 0.085  0.159 0.112      0.444     0.278
overcast          18 0.078  0.076 0.078      0.611     0.611

## Sample identity (intended leaf) and verdict flips across the 18 conditions of one leaf
           method   n  intended_leaf  flip_raw  flip_board  flip_chip
    passive_scene 378          1.000     0.700       0.700        NaN
    passive_wrist 433          1.000     0.696       0.609      0.435
     active_pinch 340          1.000     0.667       0.444      0.444
 active_roll_zero 339          1.000     0.667       0.667      0.412
 active_roll_plus 340          1.000     0.667       0.500        NaN
active_roll_minus 225          1.000     0.600       0.467      0.333

## Paired comparison (rows with raw, board and chip all valid)
           method   n  leaves  raw_err  board_err  chip_err  raw_acc  board_acc  chip_acc  chip<raw  chip<board
    passive_wrist 249      23    0.100      0.110     0.107    0.614      0.546     0.602     0.329       0.357
     active_pinch 175      17    0.077      0.090     0.086    0.731      0.600     0.640     0.303       0.314
 active_roll_zero 177      17    0.080      0.092     0.088    0.718      0.554     0.678     0.311       0.299
active_roll_minus 140      15    0.091      0.101     0.110    0.636      0.507     0.593     0.193       0.207

## Presentation gain: error at each active stage minus passive_wrist, same estimator (negative = better)
            stage   n  raw_delta  board_delta  chip_delta  chip_pairs
     active_pinch 339     -0.001       -0.003      -0.002         199
 active_roll_zero 338      0.001       -0.002      -0.001         191
 active_roll_plus 339      0.004        0.002         NaN           0
active_roll_minus 225     -0.002        0.001       0.003         122

## Illumination-aware view selection (chip calibration): selected vs fixed vs oracle
groups: 232  err selected 0.0932 (acc 0.694)  mean over views 0.0880 (acc 0.692)  oracle 0.0792 (acc 0.728)

