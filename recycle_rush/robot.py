'''
    This is the main robot file 
'''
import wpilib

class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        '''
            Initialize robot components here
        '''
        
        #
        # This dictionary contains a reference of all components every component
        # all components must have a run function
        #
        self.component_dict = {
                               
                               }
        
    def autonomousInit(self):
        '''
            function initializes our autonomous modes, we may have more than one
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
        