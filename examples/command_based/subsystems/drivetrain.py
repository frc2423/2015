'''
Created on Jan 12, 2015

@author: amory_000
'''

import wpilib
from wpilib.command import Subsystem
from commands.search import Search

class Drivetrain(Subsystem):
    
    def __init__(self):
        super().__init__('drivetrain')
        
    def initComponents(self):
        self.leftMotor = wpilib.Talon(2)
        self.rightMotor = wpilib.Talon(1)
        
    def initDefaultCommand(self):
        self.setDefaultCommand(Search(self.robot))
        
    def moveForward(self):
        self.leftMotor.set(.5)
        self.rightMotor.set(.5)
        
    def moveBackward(self):
        self.leftMotor.set(-.5)
        self.rightMotor.set(-.5)
        
    def stop(self):
        self.leftMotor.set(0)
        self.rightMotor.set(0)
    
