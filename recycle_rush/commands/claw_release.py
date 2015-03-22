from wpilib.command import Command
from subsystems.grabber_lift import GrabberLift

class ClawRelease(Command):
    
    def __init__(self, grabber_lift):
        '''
            Opens up the claw to release the totes/bins
            :param grabber_lift: the GrabberLift subsystem 
        '''
        super().__init__()
        self.setInterruptible(False)
        self.grabber_lift = grabber_lift
        self.requires(grabber_lift)
        self.setTimeout(1.0)
    
    def initialize(self):
        '''
            Called just before this Command runs the first time
        '''
        self.grabber_lift.release()
        
    
    def isFinished(self):
        '''
            Make this return true when this Command no longer needs
            to run execute()
        '''
        return self.isTimedOut()
    