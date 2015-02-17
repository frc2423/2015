import wpilib
from wpilib.command.commandgroup import CommandGroup
from common import robot_speed as rs

class Auto_One_Object (CommandGroup):
    
    def __init__ (self, drive, grabber_lift):
        super().__init__()
        self.drive = drive
        self.grabber_lift = grabber_lift
        self.addSequential(ClawGrab(grabber_lift))
        self.addSequential(MoveLiftToPosition(grabber_lift, )