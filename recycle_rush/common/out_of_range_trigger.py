from wpilib.buttons import Trigger

class OutOfRangeTrigger(Trigger):
    
    def __init__(self, too_high, too_low, value):
        
        '''
            Creates a new trigger to know when to enable 
            break mode.
            
            :param grabber_lift : Subsystem GrabberLift
            
            :param too_high : upper bound after which the thing returns true
            :param too_low : lower bound that makes it and everything under trigger returns true
            
        '''
        self.too_high = too_high
        self.too_low = too_low
        self.value = value
        
    def get(self):
        value = self.value() if callable(self.value) else self.value
        
        return not self.too_low <= value <= self.too_high