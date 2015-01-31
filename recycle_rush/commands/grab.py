'''
Created on Jan 29, 2015

@author: Ghi
'''
from wpilib.command import Command



class Grab(Command):

    def __init__(self, robot, name=None, timeout=None):
        """Grabs bin/tote by closing claw"""
        #Use self.requires() here to declare subsystem dependencies
        #eg. self.requires(chassis)
        super().__init__(name, timeout)
        self.robot = robot

    def initialize(self):
        """Called just before this Command runs the first time"""
        self.robot.grab()

    def execute(self):
        """Called repeatedly when this Command is scheduled to run"""
        self.robot.grab() #I think? The example doesn't have anything
        #which seems like it would break

    def isFinished(self):
        """This should return true when this command no longer needs to run execute()"""
        return False
        # this would have to be based on a sensor right?

    def end(self):
        """Called once after isFinished returns true"""
        pass
        #would this stop grabbing? Do nothing? We don't want it to just drop
        #the totes/bins right? The example had something that looked like 
        #a part of a state machine was set, but that doesn't exist in our
        #code as far as I can tell.

    def interrupted(self):
        """Called when another command which requires one or more of the same subsystems is scheduled to run"""
        self.end()
        #because when it is interrupted we want it to end