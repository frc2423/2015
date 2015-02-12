import wpilib
from wpilib.command import Command

class CommandCall(Command):
    '''
        Command that executes a function and finishes immediately
    '''
    def __init__(self, call):
            
        '''
            Creates a new CommandCall
            
            :param call: The function that is executed
        '''
        super().__init__()
        self.call = call
   
        
    def isFinished(self):
        '''Command goes right to end'''
        
        return True
   
    def end(self):
        '''The function is immediately executed'''
            
        self.call()
