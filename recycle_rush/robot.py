'''
    This is the main robot file 
'''
import wpilib
from components.drive import Drive

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
        # initialize all components
        #
        self.robot_drive = Drive(self.lf_motor, self.lb_motor, self.rf_motor, self.rb_motor)
        #
        # all ports/channels related to digital output
        #
        self.grabber = wpilib.DoubleSolenoid(0, 1)
        
        #
        # This dictionary contains a reference of all 
        # components every component all components must have a run function
        #
        self.component_dict = {
                               
                               }
        
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
        pass
    
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
        pass
    
    
    def run(self):
        
        for v in self.component_dict.values():
            v.run()
        