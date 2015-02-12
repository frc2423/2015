'''
    This is the main robot file 
'''
import wpilib
from subsystems.drive import Drive
from subsystems.grabber_lift import GrabberLift
from wpilib.command import Scheduler
from oi import OI
from common import port_values as pv

class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        '''
            Initialize robot components here
        '''
        #
        # all ports relate to PWM ports
        #
        self.lf_motor          = wpilib.CANTalon(pv.CAN_LIFT_TALON_FL)
        self.lb_motor          = wpilib.CANTalon(pv.CAN_LIFT_TALON_BL)
        self.rf_motor          = wpilib.CANTalon(pv.CAN_LIFT_TALON_FR)
        self.rb_motor          = wpilib.CANTalon(pv.CAN_LIFT_TALON_BR)
        self.lift_motor_master = wpilib.CANTalon(pv.CAN_LIFT_TALON_MASTER)
        self.lift_motor_slave  = wpilib.CANTalon(pv.CAN_LIFT_TALON_SLAVE)
        #
        # all ports relate to analog input
        #
        self.gyro = wpilib.Gyro(pv.AI_GIRO)
        
        #
        # all ports relate to digital input
        #
        self.box_sensor = wpilib.DigitalInput(pv.DIO_BOX_SENSOR)
        
        #
        # all ports/channels related to solenoid ports
        #
        self.grabber = wpilib.DoubleSolenoid(pv.SOLENOID_0, pv.SOLENOID_1)
        
        #
        # built-in sensors
        #
        self.accel = wpilib.BuiltInAccelerometer()
        
        #
        # initialize all subsystems
        #
        self.robot_drive = Drive(self.lf_motor, self.lb_motor, self.rf_motor, self.rb_motor, self.gyro, self.accel)
        self.grabber_lift = GrabberLift(self.lift_motor_master, self.lift_motor_slave, self.grabber, self.box_sensor)
        
        #
        # create OI
        #
        self.oi = OI(self.grabber_lift, self.robot_drive)
        
        #
        # timer 
        #
        self.timer = wpilib.Timer()
        self.timer_delay = 1
        self.log()
        
        #
        # This dictionary contains a reference of all 
        # components every component all components must have a run function
        #
        self.component_dict = {}
        
    def autonomousInit(self):
        '''
            function initializes our autonomous modes, we may
            have more than one
        '''
        self.timer.start()
    
    def autonomousPeriodic(self):
        '''
            This should call all autonomous based commands run must be called at
            the end of this function
        '''
        Scheduler.getInstance().run()
        self.log()
    
    def teleopInit(self):
        '''
            get the robot ready for teleop mode
        '''
        self.timer.reset()
    
    def teleopPeriodic(self):
           
        '''
            Periodically called to run our telop code run must be called at the 
            end of this function
        '''
        Scheduler.getInstance().run()
        self.log()
        
    def log(self):
        '''
            Calls the log function in the drive subsystem if timer is on then
            will only print when the timer has passed timer delay timer its
            the timer must be running so that we do not flood the rio and 
            network with messages
        '''
        #
        # check if the timer is running, if it is running and the period has 
        # not passed return
        #
        if self.timer.running:
            if not self.timer.hasPeriodPassed(self.timer_delay):
                return
            else:
                self.timer.reset()
            
        self.robot_drive.log()
        self.grabber_lift.log()
        

if __name__ == '__main__':
    wpilib.run(MyRobot)
        
    
    
        