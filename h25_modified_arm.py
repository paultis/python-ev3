#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D #, PowerSupply
from sys import stderr
# from time import sleep

# m = Motor(OUTPUT_D)
turntable = LargeMotor(OUTPUT_A)
elbow = LargeMotor(OUTPUT_B)
pump = LargeMotor(OUTPUT_C)
# powersupply = PowerSupply()

print("Starting",file=stderr)
# print('Voltage: ' + str(powersupply.measured_voltage))



def pick_up_card():
    # Move down to pick up card
    print('elbow down (positive)',file=stderr)
    elbow.on_for_rotations(5,0.2,True,True)  # elbow down
    # Apply suction
    print('pump suction (positive)',file=stderr)
    pump.on_for_rotations(5,0.4,True,True)  # pump pull out
    # Move up with card
    print('elbow up (negative)',file=stderr)
    elbow.on_for_rotations(-5,0.2,True,True)  # elbow up
    return 

def drop_card():
    # Move down to pick up card
    print('elbow down (positive)',file=stderr)
    elbow.on_for_rotations(5,0.18,True,True)  # elbow down
    # Drop card
    print('pump pressure (negative)',file=stderr)
    pump.on_for_rotations(-5,0.4,True,True)  # pump push in 
    # Move up with card
    print('elbow up (negative)',file=stderr)
    elbow.on_for_rotations(-5,0.18,True,True)  # elbow up
    return

def rotate_clockwise(num_rotations):
    # Rotate 
    print('turntable posittive',file=stderr)
    turntable.on_for_rotations(5,num_rotations,True,True)  # turntable clockwise
    return

def rotate_counterclockwise(num_rotations):
    # Rotate 
    print('turntable counterclockwise (negative)',file=stderr)
    turntable.on_for_rotations(-5,num_rotations,True,True)  # turntable counterclockwise
    return

def elbow_down(num_rotations):
    print('elbow down (positive)',file=stderr)
    elbow.on_for_rotations(5,num_rotations,True,True)  # elbow down
    return

def elbow_up(num_rotations):
    print('elbow up (negative)',file=stderr)
    elbow.on_for_rotations(-5,num_rotations,True,True)  # elbow up
    return


# print('turntable positive',file=stderr)
# turntable.on_for_rotations(5,0.2,True,True)  # turntable clockwise (0.4 rotations is about 90 degrees)
# print('turntable counterclockwise',file=stderr)
# turntable.on_for_rotations(-5,0.05,True,True)  # turntable counterclockwise

# print('elbow up (negative)',file=stderr)
# elbow.on_for_rotations(-5,0.20,True,True)  # elbow up

# print('pump negative',file=stderr)
# pump.on_for_rotations(-5,0.4,True,True)  # pump push in 
# print('pump positive',file=stderr)
# pump.on_for_rotations(5,0.4,True,True)  # pump pull out

# pick_up_card()
elbow_down(0.3)
rotate_counterclockwise(0.30)
# rotate_clockwise(0.30)
# elbow_up(0.3)
drop_card()


print("Done",file=stderr)