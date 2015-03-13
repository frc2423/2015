import wpilib
from wpilib.command.commandgroup import CommandGroup
from commands.mecanum_drive import MecanumDrive
from commands.dont_move import DontMove

class AutoDoNothing(CommandGroup):
    
    def __init__(self, drive):
        super().__init__()
        self.addSequential(DontMove(drive))