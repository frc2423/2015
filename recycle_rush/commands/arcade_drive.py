'''
    Created on Feb 5, 2015
    @author: Taylor
'''

import wpilib
from wpilib.command import Command
from subsystems.drive import Drive

class ArcadeDrive(Command):
    '''
        Used to move the robot
    '''
    def __init__(self, drive, joystick):
        
        
        '''
            initializes arcade drive movement
            :param joystick : the primary controls for controlling the robot
        '''
        super().__init__()
        
        self.drive = drive
        self.joystick = joystick
        
    def initialize(self):
        '''
            Called just before this Command runs the first time
        '''
        pass
    def execute(self):
        '''
            Called repeatedly when this Command is scheduled
            to run
        '''
        self.drive.robot_move(0, self.joystick.getY(), self.joystick.getX(), 0)
        
        
    def isFinished(self):
        '''
            Make this return true when this Command no longer
            needs to run execute()
        '''
        return False
    def end(self):
        '''
            Called once after isFinished returns true
        '''
        pass
    def interrupted(self):
        '''
            Called when another command which requires one or
            more of the same subsystems is scheduled to run
        '''
        self.drive.robot_move (0,0,0,0)