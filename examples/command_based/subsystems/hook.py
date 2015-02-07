'''
Created on Jan 12, 2015

@author: amory_000
'''


import wpilib
from wpilib.command import Subsystem

class Hook(Subsystem):
    
    def __init(self):
        super().__init__('hook')
        
    def initComponents(self):
        self.solenoid = wpilib.DoubleSolenoid(0, 1)
     
    def initDefaultCommand(self):  
        #self.setDefaultCommand(command) 
        pass
        
    def extend(self):
        self.solenoid.set(wpilib.DoubleSolenoid.Value.kForward)
        
    
    def retract(self):
        self.solenoid.set(wpilib.DoubleSolenoid.Value.kReverse)
        
        
    def stop(self):
        self.solenoid.set(wpilib.DoubleSolenoid.Value.kOff)