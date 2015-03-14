from wpilib.command import Command

class MoveLiftToPosition(Command):
    
    def __init__ (self, grabber_lift, position):
        '''
            Raises lift to a specified position.
            These will need to be based off the number of stacked totes and where the stack is.
            :param grabber_lift: subsystem of GrabberLift
            :param position: position that the lift needs to be raised to. Can be a function or a number
        '''
        super().__init__()
        self.grabber_lift = grabber_lift
        self.requires(grabber_lift)
        self.setInterruptible(True )
        self.position = position
        
        # When the lifter is in position, give the PID Controller a bit of time
        # to adjust
        self.pid_timer_started = False
        self.time_to_adjust = .2
        
    def initialize(self):
        '''
            Moves the lifter to a particular position. The PIDController
            takes over so it is only called once.
        '''
        if callable(self.position):
            self.grabber_lift.prepare_to_move_to_position(self.position())
            self.grabber_lift.move_to_position()
        else:
            self.grabber_lift.prepare_to_move_to_position(self.position)
            self.grabber_lift.move_to_position()
            
            
        self.grabber_lift.change_break_mode(False)
    
    
    def isFinished(self):
        '''
            Make this return true when this Command no longer needs to run execute()
        '''

        return False
    
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