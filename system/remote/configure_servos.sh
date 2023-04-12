#!/bin/sh
#
# Copyright 2022 Stéphane Caron
# Copyright 2023 Inria
#
# See https://github.com/tasts-robots/upkie_description#joint-limits

# Hip position limits
echo "conf set servopos.position_max 0.2" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 1 -c
echo "conf set servopos.position_max 0.2" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 4 -c
echo "conf set servopos.position_min -0.2" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 1 -c
echo "conf set servopos.position_min -0.2" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 4 -c

# Hip velocity limits
echo "conf set servo.max_velocity 2.0" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 1 -c
echo "conf set servo.max_velocity 2.0" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 4 -c

# Knee position limits
echo "conf set servopos.position_max 0.4" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 2 -c
echo "conf set servopos.position_max 0.4" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 5 -c
echo "conf set servopos.position_min -0.4" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 2 -c
echo "conf set servopos.position_min -0.4" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 5 -c

# Knee velocity limits
echo "conf set servo.max_velocity 2.0" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 2 -c
echo "conf set servo.max_velocity 2.0" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 5 -c

# Wheel position limits
echo "conf set servopos.position_max NaN" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 3 -c
echo "conf set servopos.position_max NaN" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 6 -c
echo "conf set servopos.position_min NaN" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 3 -c
echo "conf set servopos.position_min NaN" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 6 -c

# Wheel velocity limits
echo "conf set servo.max_velocity 10.0" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 3 -c
echo "conf set servo.max_velocity 10.0" | sudo moteus_tool --pi3hat-cfg "1=1,2,3;2=4,5,6" -t 6 -c
