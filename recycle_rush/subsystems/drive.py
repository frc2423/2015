import wpilib
from wpilib.command import Subsystem
import math
import sys
from custom.kwarqs_drive_mech import KwarqsDriveMech

class Drive(Subsystem): 
    '''
        The drive object is used to move our robot with a
        mecanum drive. It uses a gyro to help achieve a more
        precise angle measure
    '''
    
    kP_default = 5
    kI_default = 0
    kD_default = 0
    
    def __init__(self, 
                 lf_motor, 
                 lb_motor, 
                 rf_motor, 
                 rb_motor, 
                 gyro, 
                 accel,
                 p = kP_default,
                 i = kP_default,
                 d = kP_default):
        '''
            constructor for the drive object. Should take in
            gyro and a mecanum drive.
        '''
        super().__init__()
        self.robot_drive = KwarqsDriveMech(lf_motor, lb_motor, rf_motor, rb_motor)
        self.robot_drive.setInvertedMotor(wpilib.RobotDrive.MotorType.kFrontRight, True)
        self.robot_drive.setInvertedMotor(wpilib.RobotDrive.MotorType.kRearRight, True)
        self.lf_motor = lf_motor
        self.lb_motor = lb_motor
        self.rf_motor = rf_motor
        self.rb_motor = rb_motor
        self.gyro = gyro
        self.accel = accel 
        self.p = p
        self.i = i
        self.d = d
        
        self.curr_x = 0
        self.curr_y = 0
        self.curr_z = 0
        
        self.max_change = .1
        
#         self.gyro_pid = wpilib.PIDController(p, i, d, self.gyro, self.rb_motor)
#         
#         # we are using a continuous sensor here 
#         self.gyro_pid.setContinuous()
#         
#         # sets input range from zero to 360, dont know if that is right just yet
#         # todo testing for correctness
#         self.gyro_pid.setInputRange(0, 360)
#         
#         # output normilized to motor settings
#         self.gyro_pid.setOutputRange(-1, 1)
#         
#         # percent tolerance for now is 5% should probably be a lot less
#         self.gyro_pid.setPercentTolerance(5)
#         
    
        
    def pid_output(self, output):
        self.robot_drive.mecanumDrive_Cartesian(0, 0, output, 0)
    
    
    def tank(self, left, right):
        self.robot_drive.tankDrive(-1 * left * .75, right * .75)

    
    
    def robot_move(self, x, y, z, angle, weight_modifier = None):
        '''
            this function is used to control the
            power/speed/torque of our robot/drive/motors
        '''
        #self.gyro_pid.disable()
        
        speed_limit = .75
        
        self.curr_x = self.slow_change(self.curr_x, x * speed_limit)
        self.curr_y = self.slow_change(self.curr_y, y * speed_limit)
        self.curr_z = self.slow_change(self.curr_z, z * speed_limit)

        self.robot_drive.set_multiplier(weight_modifier)
        
        self.robot_drive.mecanumDrive_Cartesian(self.curr_x, self.curr_y, self.curr_z, angle)
        wpilib.SmartDashboard.putNumber("x axis", self.curr_x)
        wpilib.SmartDashboard.putNumber("y axis", self.curr_y)
        wpilib.SmartDashboard.putNumber("z axis", self.curr_z)
        
    def slow_change(self, val, goal):
        '''
            make speed ups or slow downs less intense to prevent power drain 
        '''
        diff = val - goal
        if diff < (-1 * self.max_change) :
            #goal is greater then self.max_change more than current val
            return val + self.max_change
        
        elif diff > self.max_change:
            #goal is less then max_change less the current_val
            return val - self.max_change
        
        else:
            return goal
               
    def robot_rotate(self, angle):
        '''
            rotate to a certain angle within a specified set
            of parameters
        '''
        #self.gyro_pid.enable()
        #self.gyro_pid.setSetpoint(angle)
        
    def get_angle_difference(self, target, source):
        # target> angle you want; source> the gyro angle
        return (target - source + math.pi) % (math.pi * 2) - math.pi
    
    def log(self):
        '''
            log records various things about the robot
        '''
        wpilib.SmartDashboard.putNumber("angle", self.gyro.getAngle())
        wpilib.SmartDashboard.putNumber("acceleration_x", self.accel.getX())
        wpilib.SmartDashboard.putNumber("acceleration_y", self.accel.getY())
        wpilib.SmartDashboard.putNumber("acceleration_z", self.accel.getZ())
    