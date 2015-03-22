from wpilib.command import Command

class DontMove(Command):
    '''
        Used to move the robot
    '''
    def __init__(self, drive):
        '''
            Makes the robot not move
        '''
        super().__init__()
        self.drive = drive
        self.requires(drive)

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
        self.drive.robot_move(0, 0, 0, 0)
        

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
        