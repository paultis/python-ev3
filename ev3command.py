#!/usr/bin/env python3
from sys import stderr
import argparse
from ev3dev2.motor import LargeMotor, Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D 

# Script to be invoked from the command line to control EV3 motors

class ev3command:
    command = None
    output = None
    motor = None
    speed = None
    rotations = None
    
    def __init__(self):
        self.parse_args()
        self.run_command()
        
    # def get_number(self, s):
    #     # TODO check type to see if string or number
    #     if isinstance(s, float) or isinstance(s, int):
    #         return s
    #     else: 
    #         s = float(s)
    #         return s

    def on_for_rotations(self):
        print('speed ' + str(self.speed), file=stderr)
        print('rotations ' + str(self.rotations), file=stderr)
        print('output ' + str(self.output), file=stderr)
        print('motor ' + str(self.motor), file=stderr)

        if self.motor and self.speed and self.rotations:
            print('run on_for_rotations',file=stderr)
            self.motor.on_for_rotations(self.speed,self.rotations,True,True) 
        else:
            print('Error - requires motor(output), speed, rotation inputs.',file=stderr)
    
    def parse_args(self):
        self.parser = argparse.ArgumentParser('How to run ev3command')
        # c - command
        # d - direction of motor (pos, neg)
        # m - motor type (large, normal)
        # o - output (ABCD1234)
        # r - rotations (float)
        # s - speed (float)
        self.parser.add_argument('-c', type=str, required=True, help='ev3 command to run (e.g. on_for_rotations) - case-sensitive')
        self.parser.add_argument('-o', type=str, choices=['A','B','C','D','1','2','3','4'], help='output to use: ABCD1234')
        self.parser.add_argument('-m', type=str, choices=['large','normal'], default='large', help='motor type: large|normal')
        self.parser.add_argument('-d', type=str, choices=['neg','pos'], default='large', help='direction: neg|pos')
        self.parser.add_argument('-s', type=float, help='speed: float')
        self.parser.add_argument('-r', type=float, help='rotations: float')

        self.args = self.parser.parse_args()
        
        self.command = self.args.c
        self.set_output(self.args.o)
        self.set_motor(self.args.m, self.output)
        if self.args.d == 'pos':
            self.speed = self.args.s
        else: 
            self.speed = -1 * self.args.s
        self.rotations = self.args.r
        
    def run_command(self):
        if self.command == 'on_for_rotations':
            self.on_for_rotations()
        else:
            print('Error - command not recognized: ' + self.command,file=stderr)

    def set_output(self,s):
        if s in 'ABCD':
            if s == 'A':
                self.output = OUTPUT_A  
            if s == 'B':
                self.output = OUTPUT_B
            if s == 'C':
                self.output = OUTPUT_C  
            if s == 'D':
                self.output = OUTPUT_D  
        else:
            print('Error: Output not set', file=stderr)    

    def set_motor(self, s, output):
        if s == 'large': 
            self.motor = LargeMotor(output)
        elif s == 'normal':
            self.motor = Motor(output)
        else:
            print('Motor type not recognized.',file=stderr)


if __name__ == '__main__':
    ev3command() 