'''
Created on Jan 19, 2015
@author: Taylor
'''
import wpilib
from wpilib.command import Subsystem


class GrabberLift(Subsystem):
    '''
        Used to mobilize grabby thing and lift up the item
        grabbied
    '''    
    kForward = wpilib.DoubleSolenoid.Value.kForward
    kOff = wpilib.DoubleSolenoid.Value.kOff
    kReverse = wpilib.DoubleSolenoid.Value.kReverse
    
    
    def __init__(self, lift_motor, grabber, box_sensor):
        '''
            constructor for the GrabberLift object. Should take
            a talon and a solenoid.
        '''
        self.lift_motor = lift_motor
        self.grabber = grabber
        self.box_sensor = box_sensor
        self.pid_controller = wpilib.PIDController
        
    def clamp(self):
        '''
            Grabber arm clamps so it can hold totes/bins.
        '''
        self.grabber.set(GrabberLift.kForward)
    
    def release (self):
        '''
            Grabber arm releases so it can let go of bins/totes.
        '''
        self.grabber.set(GrabberLift.kReverse)
        
    def move_lifter(self, speed):
        '''
            Moves lifter based off direct input to motor
        '''
        self.lift_motor.set(speed)
        
    def move_to_position(self, position):
        ''' 
            Moves lifter to a specified position
        '''
        pass
    
    def set_mode (self, mode):
        '''
            Changes lift motor to different modes
        '''
        pass
    
    def get_mode (self):
        '''
            Gets the mode the lift motor is in
        '''
        pass
        
    