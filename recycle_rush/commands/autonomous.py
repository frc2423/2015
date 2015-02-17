import wpilib
from wpilib.command.commandgroup import CommandGroup

class Autonomous(CommandGroup):
    
    def __init__(self, drive, grabber_lift):
        super().__init__()
        self.drive = drive
        self.grabber_lift = grabber_lift
        
        self.addSequential(ClawGrab(grabber_lift))
        self.addSequential(MoveLift(grabber_lift, .5), 1.5)
        self.addParallel(TurnToSpecifiedAngle(drive, 180))
        
        self.addSequential(ArcadeDrive(drive, 0, 1))