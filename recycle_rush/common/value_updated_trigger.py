from wpilib.buttons import Trigger

class ValueUpdatedTrigger(Trigger):
    '''
        Trigger used to check when a value changes
    '''
    
    def __init__(self, get_value):
        '''
            Creates a new trigger that turns on when a value changes.
            
            @param get_value: The callable that gives the value
        '''
        
        self.get_value = get_value
        self.last_value = get_value()  

    def get(self):
        
        current_value = self.get_value()
        updated = self.last_value != current_value
        self.last_value = current_value
        return updated