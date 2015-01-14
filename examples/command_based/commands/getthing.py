'''
Created on Jan 12, 2015

@author: amory_000
'''

from wpilib.command import CommandGroup
from commands.grab import Grab
from commands.pull import Pull
from commands.backaway import BackAway

class GetThing(CommandGroup):
    
    def __init__(self):
        self.addSequential(Grab())
        self.addSequential(Pull())
        self.addSequential(BackAway())
        