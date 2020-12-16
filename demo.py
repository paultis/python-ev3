#!/usr/bin/env python3
from ev3dev2.motor import Motor, MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import UltrasonicSensor #TouchSensor
# from ev3dev.ev3 import UltrasonicSensor
from sys import stderr
import time

mL = Motor(OUTPUT_B)
mR = Motor(OUTPUT_C)
tank_pair = MoveTank(OUTPUT_B,OUTPUT_C)
# touch = TouchSensor()
ultra = UltrasonicSensor()

def MoveAndRecord(speed1, speed2, total_rotations, rotations_per_move):
    number_moves = int(total_rotations/rotations_per_move)
    # print('number of moves {0}'.format(number_moves), file=stderr)
    for i in range(0,number_moves):
        tank_pair.on_for_rotations(speed1,speed2,rotations_per_move)
        print('{0}, {1}, {2}'.format(speed1,speed2,rotations_per_move), end=", ", file=stderr)
        print('{0}, {1}, {2}'.format(mL.position,mR.position, ultra.distance_centimeters_continuous), file=stderr)
        # print("Speed1: {0} Speed2: {1}, Rotations: {2}".format(speed1,speed2,rotations_per_move), file=stderr)
        # print('Left: {0}, Right: {1}'.format(mL.position,mR.position), file=stderr)
        # print('Distance: {0}'.format(ultra.distance_centimeters_continuous), file=stderr)
        # print('---', file=stderr)
print('left_speed, right_speed, rotations, left_pos, right_pos, distance', file=stderr)
print('0, 0, 0, {0}, {1}, {2}'.format(mL.position,mR.position,ultra.distance_centimeters_continuous), file=stderr)
# print('Initial position', file=stderr)
# print('Left: {0}, Right: {1}'.format(mL.position,mR.position), file=stderr)
# print('Distance: {0}'.format(ultra.distance_centimeters_continuous), file=stderr)
# print('---', file=stderr)

MoveAndRecord(0,30,7,0.25)
# MoveAndRecord(30,10,3,0.5)

