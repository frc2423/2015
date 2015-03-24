from wpilib.command import Command
from subsystems.grabber_lift import GrabberLift

blah = 3

class ClawToggle(Command):
    
    def __init__(self, grabber_lift):
        """
            Opens claw if closed, and closes claw if open
            :param grabber_lift: the subsystem of GrabberLift
        """
        #Use self.requires() here to declare subsystem dependencies
        #eg. self.requires(chassis)
        super().__init__()
        self.setInterruptible(False)
        self.grabber_lift = grabber_lift
        self.requires(grabber_lift)
        self.setTimeout(1.0)

    def initialize(self):
        """Called repeatedly when this Command is scheduled to run"""
        if self.grabber_lift.is_clamped():
            self.grabber_lift.release()
        else:
            self.grabber_lift.clamp()

    def isFinished(self):
        """This should return true when this command no longer
        needs to run execute()"""
        return self.isTimedOut()