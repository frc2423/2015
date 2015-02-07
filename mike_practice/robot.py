import wpilib

class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        '''
            Initializes robot components
        '''
        
        #initialize motor
        self.motor = wpilib.Jaguar(0)
    
    def autonomousInit(self):   
        pass
    
    def autonomousPeriodic(self):
        pass
    
    def teleopInit(self):
        pass
    
    def teleopPeriodic(self):
        pass
    
    