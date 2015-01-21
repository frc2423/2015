import wpilib
import math

class Drive(object): 
    '''
        The drive object is used to move our robot with a
        mecanum drive. It uses a gyro to help achieve a more
        precise angle measure
    '''
    
    def __init__(self, lf_motor, lb_motor, rf_motor, rb_motor, gyro):
        '''
            constructor for the drive object. Should take in
            gyro and a mecanum drive.
        '''
        self.robot_drive = wpilib.RobotDrive(lf_motor, lb_motor, rf_motor, rb_motor)
        
        self.lf_motor = lf_motor
        self.lb_motor = lb_motor
        self.rf_motor = rf_motor
        self.rb_motor = rb_motor
        self.gyro = gyro
    
    def robot_move(self, x, y, z, angle):
        '''
            this function is used to control the
            power/speed/torque of our robot/drive/motors
        '''
        self.robot_drive.mecanumDrive_Cartesian(x, y, z, angle)
        
    def robot_rotate(self, angle):
        '''
            rotate to a certain angle within a specified set
            of parameters
        '''
        
        angle_difference = self.get_angle_difference(angle, self.gyro.getAngle())
        z = 0
        if angle_difference < -5:
            z = -.5
        elif angle_difference > 5:
            z = .5
        
        self.robot_move(0, 0, z, angle)
        
    def get_angle_difference(self, target, source):
        # target> angle you want; source> the gyro angle
        return (target - source + math.pi) % (math.pi * 2) - math.pi
    
    def run(self):
        '''
            This runs the changes that are made above
            could also be called "def update(self):"
        '''
        
        pass
