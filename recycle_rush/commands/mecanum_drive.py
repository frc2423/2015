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
    def __init__(self, drive, get_x, get_y, get_z, gyro = None):
        '''
            initializes mecanum drive movement.
            :param joystick : the primary controls for controlling the robot
            :param gyro: Used to compare robot's angle to the gyro's 0 angle,
            moves relative to the field if gyro is passed in. 
            :param get_z: Used to get the z angle, function that determines 
            rotation and direction of rotation. Z value must be given if it
            separate from the joystick. 
        '''
        super().__init__()
        
        self.drive = drive
        self.get_x = get_x
        self.get_y = get_y
        self.get_z = get_z
        self.gyro = gyro
        self.requires(Drive)
        
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
        angle = self.gyro.getAngle() if self.gyro != None else 0
        self.drive.robot_move(self.get_x, self.get_y, self.get_z, angle)
        
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
        