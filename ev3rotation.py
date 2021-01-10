#!/usr/bin/env python3
from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from sys import stderr

# m = Motor(OUTPUT_D)
big_motor = Motor(OUTPUT_C)

print("Starting",file=stderr)
big_motor.on_for_rotations(5,0.2,True,True)  # pull syringe open
# big_motor.on_for_rotations(-5,0.15,True,True)  # push syringe closed

# m.on_for_rotations(-10,7,True,True)  # Clockwise  (close claw)
# m.on_for_rotations(10,5,True,True) # Counterclockwise (open claw)
print("Done",file=stderr)