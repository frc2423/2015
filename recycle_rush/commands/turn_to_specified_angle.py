'''
Created on Feb 7, 2015

@author: Ghi
'''
from wpilib.command import Command

class TurnToSpecifiedAngle(Command):
    
    def __init__(self, drive, param):
        '''
            Turns to a given angle automatically
            :param drive; subsystem of Drive
            :param param: angle one wants to turn to
        '''
        super().__init__()
        self.drive = drive
        self.param = param
        self.requires(drive)
        
        if callable(param):
            self.param_is_callable = True
        
        else:
            self.param_is_callable = False
        
    def initialize (self):
        '''
            Called just before this Command runs the first time
            Moves robot if position passed is a value (not a function)
        '''
        if self.param_is_callable:
            pass
        else:
            self.drive.robot_rotate(self.param)
            
    def execute(self):
        '''
            Called repeatedly when this Command is scheduled to run
            Makes robot move if angle is a function
        '''
        if self.param_is_callable:
            self.drive.robot_rotate(self.param())
        else:
            pass
        
    def isFinished(self):
        '''
            Make this return true when this Command no longer needs to run execute()
        '''
        pass
    
    def end(self):
        '''
            We want the robot to stop when we want this command to end
        '''
        self.drive.robot_move(0,0,0, None)
        
    def interrupted(self):
        '''
            Called when another command which requires one or more of the same
            subsystems is scheduled to run.
        '''
        self.end()