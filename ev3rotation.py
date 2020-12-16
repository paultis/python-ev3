#!/usr/bin/env python3
from ev3dev2.motor import Motor, OUTPUT_D
from sys import stderr

m = Motor(OUTPUT_D)

print("Starting",file=stderr)
m.on_for_rotations(-10,7,True,True)  # Clockwise  (close claw)
# m.on_for_rotations(10,5,True,True) # Counterclockwise (open claw)
print("Starting",file=stderr)