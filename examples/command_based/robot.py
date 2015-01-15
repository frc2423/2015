'''
Created on Jan 12, 2015

@author: amory_000
'''


import wpilib
from wpilib import command
from subsystems.drivetrain import Drivetrain
from subsystems.hook import Hook
from wpilib.buttons import Button
from commands.getthing import GetThing


class MyRobot(wpilib.IterativeRobot):
    
    drivetrain = Drivetrain()
    hook = Hook()
    
    def robotInit(self):
        MyRobot.drivetrain.initComponents()
        MyRobot.hook.initComponents()     
        self.distanceSensor = Button(wpilib.DigitalInput(1))
        
    def autonomousInit(self):
        self.distanceSensor.whenPressed(GetThing())
    
    def autonomousPeriodic(self):
        command.Scheduler.getInstance().run()
        
    def teleopInit(self):
        pass
    
    def teleopPeriodic(self):
        command.Scheduler.getInstance().run()
        
        
if __name__ == '__main__':
    wpilib.run(MyRobot)
    