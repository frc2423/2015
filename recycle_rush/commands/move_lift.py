from wpilib.command import Command
from subsystems.grabber_lift import GrabberLift
from common.height_levels import BIT_PER_INCH
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
        self.last_set = 0
            
        self.param = param
        
    def initialize(self):
        '''
        '''
        
        self.grabber_lift.change_break_mode(True)
        
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
            self.last_set = self.param()
        else:
            self.last_set = self.param
            
        
        self.grabber_lift.move_lifter(self.last_set)
        
    def isFinished(self):
        '''
            Make this return true when this Command no longer needs to run execute()
        '''
        
        return False
    
    def end(self):  
        '''
            Called when another command which requires one or more of the same
            subsystems is scheduled to run. Stops lift motor.
        '''
        
        self.grabber_lift.change_break_mode(True)
        self.grabber_lift.move_lifter(0)
        position = self.grabber_lift.pot_reading()
        
        if self.last_set > 0:
            position += int(BIT_PER_INCH * .5)
        elif self.last_set < 0:
            position += int(-BIT_PER_INCH * .5)
            
        self.grabber_lift.prepare_to_move_to_position(position)
        self.grabber_lift.move_to_position()
        print("moving to position: ", position)
        
        
    def interrupted(self):
        '''
            Called when another command which requires one or more of the same
            subsystems is scheduled to run.
            We want the command to end if this happens.
        '''
        self.end()
