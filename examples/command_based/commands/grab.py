'''
Created on Jan 12, 2015

@author: amory_000
'''

import wpilib
from wpilib.command import Command
from subsystems.drivetrain import Drivetrain
from subsystems.hook import Hook
from robot import MyRobot

class Grab(Command):
    def __init(self):
        self.requires(Drivetrain)
        self.requires(Hook)
        self.timer = wpilib.Timer()
        self.setInterruptible(False)
        
        
    def initialize(self):
        self.timer.reset()
        self.timer.start()
    
    def execute(self):
        MyRobot.drivetrain.stop()
        MyRobot.hook.extend()
        
    def isFinished(self):
        return self.timer.hasPeriodPassed(1.0)
    
    def end(self):
        self.timer.stop()