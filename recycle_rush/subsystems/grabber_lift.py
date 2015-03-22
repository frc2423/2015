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
        self.motor_master.reverseOutput(True)
   #     self.motor_master.setForwardSoftLimit(900)
  #      self.motor_master.setReverseSoftLimit(100)
        #self.motor_master.setCloseLoopRampRate(.5)
        self.tolerance = 15
        #set master control mode to default %vbus
        self.set_mode(GrabberLift.mPercentVbus)
        
        
        # set slave control mode - the salve is ALWAYS a slave to the master no
        # no matter the mode of the master
        self.motor_slave.changeControlMode(GrabberLift.mFollower)
        
        #set slave to follow master commands(this sets the motor master id[which is 1]to the )
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
        self.change_break_mode(False)
        
    def prepare_to_move_to_position(self,position):
        '''
           set our position we shall go to when we change to position control mode
           :param position: position we should go to ranging from 0 to 1024  
        '''    
        self.goal_position = position
        
    def move_to_position(self):
        ''' 
            Moves lifter to a specified position 
        '''
        self.set_mode(GrabberLift.mPostion)
        self.motor_master.set(self.goal_position)
        self.change_break_mode(False)
        
    def is_at_position(self):
        '''
            compares the actual position of robot to current
            position of the robot
        '''
        #self.motor_master.getClosedLoopError() < self.tolerance
        return False
    
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
        print('updating PID P: ', p ,'i: ', i, 'd:', d)
        if p: 
            self.p = p
            self.motor_master.setP(p)
            
        if i: 
            self.i = i
            self.motor_master.setI(i)
            
        if d: 
            self.d = d
            self.motor_master.setD(d)
        
    def change_break_mode(self, yes_or_no_break):
        '''
        Enable's break mode. Yes_or_no_break is a boolean
        Unsure why this is necessary.
        '''
        self.motor_master.enableBrakeMode(yes_or_no_break)
        self.motor_slave.enableBrakeMode(yes_or_no_break)
        
    def pot_reading(self):
<<<<<<< HEAD
        
        return self.motor_master.getAnalogInRaw() #removing conflicts
=======

        #return 0
        return self.motor_master.getAnalogInRaw()
>>>>>>> remotes/upstream/master
        
    def log(self):
        '''
            
        '''
        
        wpilib.SmartDashboard.putBoolean('box_sensor', self.box_sensor.get())
        
        wpilib.SmartDashboard.putNumber('lift_error', self.motor_master.getClosedLoopError())
        
        wpilib.SmartDashboard.putNumber('lift_position', self.motor_master.getAnalogInPosition())
        
        wpilib.SmartDashboard.putString('lift_mode', GrabberLift.control_mode_map[self.mode])
    

        wpilib.SmartDashboard.putNumber('actual_goal_pos', self.goal_position)
        #wpilib.SmartDashboard.putNumber('actual_goal_pos', hl.bits_to_inches(self.goal_position))
    