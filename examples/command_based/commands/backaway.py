'''
Created on Jan 12, 2015

@author: amory_000
'''

import wpilib
from wpilib.command import Command
from subsystems.drivetrain import Drivetrain
from robot import MyRobot

class BackAway(Command):
    
    def __init__(self):
        self.requires(Drivetrain)
        self.timer = wpilib.Timer()
        self.isInterruptible(False)
        
        
    def initialize(self):
        self.timer.reset()
        self.timer.start()
    
    def execute(self):
        MyRobot.drivetrain.moveBackward()
        
        
    def isFinished(self):
        return self.timer.hasPeriodPassed(1.0)
    
    def end(self):
        self.timer.stop()