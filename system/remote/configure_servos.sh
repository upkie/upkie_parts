#!/bin/sh
#
# Copyright 2022 Stéphane Caron
# Copyright 2023 Inria

# Hips
echo "conf set servopos.position_max 0.75" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 1 -c
echo "conf set servopos.position_max 0.75" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 4 -c
echo "conf set servopos.position_min -0.75" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 1 -c
echo "conf set servopos.position_min -0.75" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 4 -c

# Knees
echo "conf set servopos.position_max 0.375" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 2 -c
echo "conf set servopos.position_max 0.375" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 5 -c
echo "conf set servopos.position_min -0.375" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 2 -c
echo "conf set servopos.position_min -0.375" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 5 -c

# Wheels
echo "conf set servopos.position_max NaN" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 3 -c
echo "conf set servopos.position_max NaN" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 6 -c
echo "conf set servopos.position_min NaN" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 3 -c
echo "conf set servopos.position_min NaN" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 6 -c
