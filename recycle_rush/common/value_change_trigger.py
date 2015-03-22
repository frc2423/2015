import wpilib

class ValueChangeTrigger (Trigger):
    '''
        This trigger is used to check for a change in value
    '''
    
    def __init__ (self, get_value):
        self.get_value ()
        
    def get(self):
        