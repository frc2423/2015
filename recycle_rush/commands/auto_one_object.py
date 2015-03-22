import wpilib
from wpilib.command.commandgroup import CommandGroup
from common import robot_speed as rs
from commands.turn_to_specified_angle import TurnToSpecifiedAngle
from commands.mecanum_drive import MecanumDrive 
from commands.claw_grab import ClawGrab
from commands.move_lift_to_position import MoveLiftToPosition
from commands.claw_release import ClawRelease
from commands.dont_move import DontMove
from common.robot_speed import time_to_move
from common import height_levels as hl

class Auto_One_Object (CommandGroup):
    
    def __init__ (self, drive, grabber_lift, gyro):
        super().__init__()
        self.drive = drive
        self.grabber_lift = grabber_lift
        
        self.addSequential(ClawGrab(grabber_lift))
        self.addSequential(MoveLiftToPosition(grabber_lift, hl.START_HEIGHT + hl.TOTE_HEIGHT))
        self.addParallel(TurnToSpecifiedAngle (drive, -90))
        self.addSequential(MecanumDrive(drive, 0, 1, 0, gyro), time_to_move(1, 10))
        self.addParallel(MoveLiftToPosition(grabber_lift, hl.START_HEIGHT)) 
        self.addSequential(ClawRelease(grabber_lift))
        self.addSequential(DontMove(drive))