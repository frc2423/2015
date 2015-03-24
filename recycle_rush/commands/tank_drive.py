import wpilib
from wpilib.command import Command
from subsystems.drive import Drive

class TankDrive(Command):
    '''
        Used to move the robot
    '''
    def __init__(self, drive, left, right):
        '''
            initializes arcade drive movement
            :param drive : instance of the class Drive
            :param get_x : can be a function or #
            :param get_y : 
        '''
        super().__init__()
        
        self.drive = drive
        self.left = left
        self.right = right
        self.requires(drive)
        
   
    def execute(self):
        '''
            Called repeatedly when this Command is scheduled
            to run
        '''
        self.drive.tank(self.left(), self.right())
        
        
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
        self.drive.robot_move (0,0,0,0)
        
    def interrupted(self):
        '''
            Called when another command which requires one or
            more of the same subsystems is scheduled to run
        '''
        self.end()