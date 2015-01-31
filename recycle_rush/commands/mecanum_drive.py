'''
    Created on Jan 31, 2015
    @author: Taylor
'''

import wpilib
from wpilib.command import Command
from subsystems.drive import Drive

class MecanumDrive(Command):
    '''
        Used to move the robot 
    '''
    def __init__(self):
        '''
            
        '''
        super().__init__()
        
    def initialize(self):
        '''
            Called just before this Command runs the first time
        '''
        
    def execute(self):
        '''
            Called repeatedly when this Command is scheduled
            to run
        '''
        
    def isFinished(self):
        '''
            Make this return true when this Command no longer
            needs to run execute()
        '''
        
    def end(self):
        '''
            Called once after isFinished returns true
        '''
        
    def interrupted(self):
        '''
            Called when another command which requires one or
            more of the same subsystems is scheduled to run
        '''
        