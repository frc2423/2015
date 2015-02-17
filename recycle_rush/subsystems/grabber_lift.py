'''
Created on Jan 19, 2015
@author: Taylor
'''
import wpilib
from wpilib.command import Subsystem
from common import height_levels as hl
class GrabberLift(Subsystem):
    '''
        Used to mobilize grabby thing and lift up the item
        grabbied
    '''    
    kForward = wpilib.DoubleSolenoid.Value.kForward
    kOff = wpilib.DoubleSolenoid.Value.kOff
    kReverse = wpilib.DoubleSolenoid.Value.kReverse    
    kAnalogPot = wpilib.CANTalon.FeedbackDevice.AnalogPot
    
    mPercentVbus = wpilib.CANTalon.ControlMode.PercentVbus
    mPostion     = wpilib.CANTalon.ControlMode.Position
    mFollower    = wpilib.CANTalon.ControlMode.Follower
    
    kP_default = .5
    kI_default = 0
    kD_default = 0
    
    #
    # map used for printing the control mode
    #
    control_mode_map = { 
                            mPercentVbus:'mPerscentVbus',
                            mPostion:'mPosition',
                       }
    def __init__(self, 
                 motor_master, 
                 motor_slave, 
                 grabber, 
                 box_sensor, 
                 p = kP_default, 
                 i = kI_default, 
                 d = kD_default):
        
        '''
            constructor for the GrabberLift object. Should take
            a talon and a solenoid.
            
            :var motor_master: master CANTalon
            :var motor_slave:  slave CANTalon
            :var grabber    :  grabber double solenoid used to clamp and release the grabber
            :var box_sensor :  DIO sensor at front of claw that maybe used to detect boxes
            :var p          :  the p component of the PID controller
            :var i          :  the i component of the PID controller
            :var d          :  the d component of the PID controller
        '''
        super().__init__()
        self.motor_master = motor_master
        self.motor_slave  = motor_slave 
        self.grabber = grabber
        self.box_sensor = box_sensor
        self.p = p
        self.i = i
        self.d = d
        self.goal_position = 0
        self.mode = None
        # set master PID settings
        self.motor_master.setFeedbackDevice(GrabberLift.kAnalogPot)
        self.motor_master.setPID(p, i, d)
        
        #set master control mode to default %vbus
        self.set_mode(GrabberLift.mPercentVbus)
        
        
        # set slave control mode - the salve is ALWAYS a slave to the master no
        # no matter the mode of the master
        self.motor_slave.changeControlMode(GrabberLift.mFollower)
        
        #set slave to follow master commands(this sets the motor master id[which is 1]to the )
        self.motor_slave.set(self.motor_master.getDeviceID())
        print ("device ID:",self.motor_master.getDeviceID())
        
        
    def clamp(self):
        '''
            Grabber arm clamps so it can hold totes/bins.
        '''
        self.grabber.set(GrabberLift.kForward)
        print("Grabber:", self.grabber.get())
    
    def release (self):
        '''
            Grabber arm releases so it can let go of bins/totes.
        '''
        self.grabber.set(GrabberLift.kReverse)
        print("Grabber:", self.grabber.get())
        
    def move_lifter(self, speed):
        '''
            Moves lifter based off direct input to motor
        '''
        self.set_mode(GrabberLift.mPercentVbus)
        self.motor_master.set(speed)
        print("arg speed:", speed)
        print("actual speed:", self.motor_master.get())
        
    def move_to_position(self, position):
        ''' 
            Moves lifter to a specified position
        '''
        self.set_mode(GrabberLift.mPostion)
        position_in_bits = hl.inches_to_bits(position)
        self.motor_master.set(position_in_bits)
        self.goal_position = position_in_bits
        
    def is_at_position(self,position):
        '''
            compares the actual position of robot to current
            position of the robot
        '''
        pass
    
    def set_mode (self, mode):
        '''
            Changes lift motor to different modes
        '''
        self.motor_master.changeControlMode(mode)
        self.mode = mode
        
    def get_mode (self):
        '''
            Gets the mode the lift motor is in
        '''
        return self.mode
        
        
    def update_pid(self, p = None, i = None, d = None):
        '''
            Updates the PID coefficients
        '''
        
        if p: 
            self.p = p
            self.motor_master.setP(p)
            
        if i: 
            self.i = i
            self.motor_master.setI(i)
            
        if d: 
            self.d = d
            self.motor_master.setD(d)
        
        
        
        
    def log(self):
        '''
            
        '''
        wpilib.SmartDashboard.putNumber('lift_position', 
                                        self.motor_master.getAnalogInPosition())
        
        wpilib.SmartDashboard.putBoolean('box_sensor', self.box_sensor.get())
        
        wpilib.SmartDashboard.putNumber('lift_error', self.motor_master.getClosedLoopError() if self.mode == GrabberLift.mPostion  else 0)
        
        wpilib.SmartDashboard.putNumber('lift_position', self.motor_master.getAnalogInRaw())
        
        wpilib.SmartDashboard.putString('lift_mode', GrabberLift.control_mode_map[self.mode])
    
            
    