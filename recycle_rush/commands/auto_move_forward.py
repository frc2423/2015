import wpilib
from wpilib.command.commandgroup import CommandGroup
from commands.mecanum_drive import MecanumDrive
from commands.dont_move import DontMove
from common import robot_speed as rs

class AutoMoveForward(CommandGroup):
    
    def __init__(self, drive, gyro, time):
        super().__init__()
        self.drive = drive
        self.gyro = gyro
        #time = rs.time_to_move(.5, 10)
        #time = 2.5
        
        self.addSequential(MecanumDrive(drive, 0, -1, 0, None), time)
        self.addSequential(DontMove(drive))
        
        # The above one is 1 second.
        
        