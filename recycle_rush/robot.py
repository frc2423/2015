'''
    This is the main robot file 
'''
import wpilib
from subsystems.drive import Drive
from subsystems.grabber_lift import GrabberLift
from wpilib.command import Scheduler
class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        '''
            Initialize robot components here
        '''
        #
        # all ports relate to PWM ports
        #
        self.lf_motor = wpilib.TalonSRX(1)
        self.lb_motor = wpilib.TalonSRX(3)
        self.rf_motor = wpilib.TalonSRX(2)
        self.rb_motor = wpilib.TalonSRX(4)
        self.lift_motor = wpilib.TalonSRX(5)
        
        #
        # all ports relate to analog input
        #
        self.gyro = wpilib.Gyro(1)
        
        #
        # all ports/channels related to digital output
        #
        self.grabber = wpilib.DoubleSolenoid(0, 1)
        
        #
        # built-in sensors
        #
        self.accel = wpilib.BuiltInAccelerometer()
        
        #
        # initialize all subsystems
        #
        self.robot_drive = Drive(self.lf_motor, self.lb_motor, self.rf_motor, self.rb_motor)
        self.grabber_lift = GrabberLift(self.lift_motor, self.grabber, None)
        
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
        pass
    
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
        
        
        pass
    
    def teleopPeriodic(self):
           
        '''
            Periodically called to run our telop code run must be called at the 
            end of this function
        '''
        Scheduler.getInstance().run()
        self.log()
        
    def log(self):
        '''
            Calls the log function in the drive subsystem
        '''
        self.robot_drive.log()
        

if __name__ == '__main__':
    wpilib.run(MyRobot)
        
    
    
        