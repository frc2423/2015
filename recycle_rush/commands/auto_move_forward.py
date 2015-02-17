import wpilib
from wpilib.command.commandgroup import CommandGroup
from common import robot_speed as rs

class AutoMoveForward(CommandGroup):
    
    def __init__(self, drive, gyro):
        super().__init__()
        self.drive = drive
        self.gyro = gyro
        time = rs.time_to_move(.5, 10)
        
        self.addSequential(MecanumDrive(drive, 0, rs.VOLTAGE_50, 0, self.gyro), rs.time)
        # The above one is 1 second.
        
        