from wpilib.command import Command
from subsystems.grabber_lift import GrabberLift


class ClawGrab(Command):
    
    def __init__(self, grabber_lift):
        """
            Grabs bin/tote by closing claw
            :param grabber_lift: the subsystem of GrabberLift
        """
        #Use self.requires() here to declare subsystem dependencies
        #eg. self.requires(chassis)
        super().__init__()
        self.setInterruptible(False)
        self.grabber_lift = grabber_lift
        self.requires(grabber_lift)
        self.setTimeout(1.5)

    def initialize(self):
        """Called just before this Command runs the first time"""
        #self.grabber_lift.clamp()
        

    def execute(self):
        """Called repeatedly when this Command is scheduled to run"""
        self.grabber_lift.clamp()

    def isFinished(self):
        """This should return true when this command no longer
        needs to run execute()"""
        return self.isTimedOut()

    def end(self):
        """Called once after isFinished returns true"""
        pass