'''
Created on Jan 19, 2015
@author: Taylor
'''
import wpilib
from wpilib.command import Subsystem

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
    
    kP = .5
    kI = .001
    kD = 0
    
    def __init__(self, motor_master, motor_slave, grabber, box_sensor):
        '''
            constructor for the GrabberLift object. Should take
            a talon and a solenoid.
        '''
        super().__init__()
        self.motor_master = motor_master
        self.motor_slave  = motor_slave 
        self.grabber = grabber
        self.box_sensor = box_sensor
        
        # set master control mode
        self.motor_master.setFeedbackDevice(GrabberLift.kAnalogPot)
        self.motor_master.setPID(GrabberLift.kP, GrabberLift.kI,GrabberLift.kD)
        
        # set slave control mode - the salve is ALWAYS a slave to the master no
        # no matter the mode of the master
        self.motor_slave.changeControlMode(GrabberLift.mFollower)
        #set slave to follow master commands
        self.motor_slave.set(self.motor_master.getDeviceID())
    def clamp(self):
        '''
            Grabber arm clamps so it can hold totes/bins.
        '''
        self.grabber.set(GrabberLift.kForward)
    
    def release (self):
        '''
            Grabber arm releases so it can let go of bins/totes.
        '''
        self.grabber.set(GrabberLift.kReverse)
        
    def move_lifter(self, speed):
        '''
            Moves lifter based off direct input to motor
        '''
        self.set_mode(GrabberLift.mPercentVbus)
        self.motor_master.set(speed)
        
    def move_to_position(self, position):
        ''' 
            Moves lifter to a specified position
        '''
        self.set_mode(GrabberLift.mPostion)
        self.motor_master.set(position)
        
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
    
    def get_mode (self):
        '''
            Gets the mode the lift motor is in
        '''
        return self.motor_master.getControlMode()
        
        
    def log(self):
        '''
            
        '''
        wpilib.SmartDashboard.putNumber('lift_position', 
                                        self.motor_master.getAnalogInPosition())
    