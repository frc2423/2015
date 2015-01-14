'''
Created on Jan 12, 2015

@author: amory_000
'''


import wpilib
from wpilib.command import Command
from subsystems.drivetrain import Drivetrain
from robot import MyRobot

class Search(Command):
    def __init__(self):
        self.requires(Drivetrain)
        
    
    def initialize(self):
        pass
    
    def execute(self):
        MyRobot.drivetrain.moveForward()
        
    def isFinished(self):
        return False
    
    def end(self):
        pass
    
    def interrupted(self):
        MyRobot.drivetrain.stop()