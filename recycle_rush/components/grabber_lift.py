'''
Created on Jan 19, 2015
@author: Taylor
'''
import wpilib


class GrabberLift():
    '''
        Used to mobilize grabby thing and lift up the item
        grabbied
    '''
    def __init__(self, lift_motor, grabby_thing):
        '''
            constructor for the GrabberLift object. Should take
            a talon and a solenoid.
        '''
        self.lift_motor = lift_motor
        self.grabber = grabby_thing
        