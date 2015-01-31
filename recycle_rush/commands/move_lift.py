'''
    Created on Jan 31, 2015
    @author: Taylor
'''

from wpilib.command import Command
from subsystems.grabber_lift import GrabberLift

class RaiseLift(Command):
    
    def __init__(self, grabber_lift):
        '''
            Raises lift using manual control
            :param grabber_lift: subsystem of GrabberLift
        '''
        super().__init__()
        self.setInterruptible(True)
        self.grabber_lift = grabber_lift
        self.requires(GrabberLift)
        
    def initialize(self):
        '''
            Called just before this Command runs the first time
        '''
        pass
        
    def execute (self):
        '''
            Called repeatedly when this Command is scheduled to run
        '''
        self.grabber_lift.move_lifter()
        