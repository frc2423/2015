from wpilib.command import Command

class MecanumDrive(Command):
    '''
        Used to move the robot
    '''
    def __init__(self, drive, get_x, get_y, get_z, gyro = None):
        '''
            initializes mecanum drive movement.
            :param drive : the drive subsystem
            :param get_x: Used to get the x angle, function that determines y direction
            :param get_y: Used to get the y angle, function that determines the y value and direction
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
        angle = self.gyro.getAngle() if self.gyro != None else 0
        x = self.get_x() if callable(self.get_x) else self.get_x
        y = self.get_y() if callable(self.get_y) else self.get_y
        z = self.get_z() if callable(self.get_z) else self.get_z
        self.drive.robot_move(x, y, z, angle)
        

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
        