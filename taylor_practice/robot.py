'''
Created on January 13, 2015
@author: Taylor
'''

import wpilib


class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        '''
            initialize motors, sensors, etc.
        '''
        self.motor = wpilib.Jaguar(0)
        self.motor2 = wpilib.Talon(1)
    
    def autonomousInit(self):
        self.motor.set(0)
    
    def autonomousPeriodic(self):
        '''
            control robot in autonomous mode
        '''
        self.motor.set(.75)
        self.motor2.set(.3)
        
    
    def teleopInit(self):
        pass
    
    def teleopPeriodic(self):
        pass
    

if __name__ == "__main__":
    wpilib.run(MyRobot)
































