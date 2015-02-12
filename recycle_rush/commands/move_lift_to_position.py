'''
Created on Feb 7, 2015

@author: Ghi
'''
from wpilib.command import Command

class MoveLiftToPosition(Command):
    
    def __init__ (self, grabber_lift, param):
        '''
            Raises lift to a specified position.
            These will need to be based off the number of stacked totes and where the stack is.
            :param grabber_lift: subsystem of GrabberLift
            :param position: position that the lift needs to be raised to. Can be a function or a number
        '''
        super().__init__()
        self.grabber_lift = grabber_lift
        self.requires(grabber_lift)
        
        if callable(param):
            self.param_is_callable = True
        
        else:
            self.param_is_callable = False
        
        self.param = param
        
    def initialize(self):
        '''
            Called just before this Command runs the first time
            Moves lifter is param passed is a position (number as opposed to a function)
        '''
        if self.param_is_callable:
            pass
        
        else:
            self.grabber_lift.move_to_position(self.position)
            
    def execute(self):
        '''
            Called repeatedly when this Command is scheduled to run
            Moves lifter when param passed is a function
        '''
        if self.param_is_callable:
            self.grabber_lift.move_to_position(self.position())
        else:
            pass
    
    def isFinished(self):
        '''
            Make this return true when this Command no longer needs to run execute()
        '''
        pass
    # Not sure what we do here because we use the PID stuff to know when it is finished
    # And any other command can take over any point
    
    def end(self):
        '''
            Called once after isFinished returns true.
            Want lifter to stop before other stuff happens
        ''' 
        self.grabber_lift.move_lifter(0)
    
    def interrupted(self):
        '''
            Called when another command which requires one or more of the same
            subsystems is scheduled to run.
            We want the command to end if this happens.
        '''
        self.end()