import wpilib

class Drive(object): 
    '''
        The drive object is used to move our robot with a mecanum drive. It
        uses a gyro to help achieve more precise 
    '''
    
    def __init__(self, lf_motor, lb_motor, rf_motor, rb_motor):
        '''
            constructor for the drive object. Should take in gyro and a mecanum
            drive.
        '''
        self.robot_drive = wpilib.RobotDrive(lf_motor, lb_motor, rf_motor, rb_motor)
        
        self.lf_motor = lf_motor
        self.lb_motor = lb_motor
        self.rf_motor = rf_motor
        self.rb_motor = rb_motor
        
    
    def robot_move(self, x, y, z, angle):
        '''
            this function is used to control the power/speed/torque
            of our robot/drive/motors
        '''
        self.robot_drive
        
    
    def run(self):
        '''
            This runs the changes that are made above
            could also be called "def update(self):"
        '''
        
        pass