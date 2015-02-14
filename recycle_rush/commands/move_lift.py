'''
    Created on Jan 31, 2015
    @author: Taylor
'''

from wpilib.command import Command
from subsystems.grabber_lift import GrabberLift
import wpilib

class MoveLift(Command):
    
    def __init__(self, grabber_lift, param):
        '''
            Raises lift using manual control
            :param grabber_lift : subsystem of GrabberLift
            :param value : value should be either a function that returns between -1 to 1 or a number between -1 to 1
            
            
            
            Default command. We don't think we want it to be finished. EVER.
        '''
        super().__init__()
        self.grabber_lift = grabber_lift
        self.requires(grabber_lift)
        
            
        self.param = param
        
    def execute (self):
        '''
            Called repeatedly when this Command is scheduled to run
        '''
        #
        # Part 2. Continued from __init__()
        # if param is callable is, feeds move_lifter the appropriate thing (in execute)
        # so if the passed param is a value it gives move_lifter a value
        # otherwise it gives move_lifter the function. 
        #
        if callable(self.param):
            self.grabber_lift.move_lifter(self.param())
        else:
            self.grabber_lift.move_lifter(self.param)
        
    def isFinished(self):
        '''
            Make this return true when this Command no longer needs to run execute()
        '''
        return False
    
    def interrupted(self):
        '''
            Called when another command which requires one or more of the same
            subsystems is scheduled to run. Stops lift motor.
        '''
        
        self.grabber_lift.move_lifter(0)
        
