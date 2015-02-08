'''
Created on Feb 6, 2015

@author: Taylor
'''
from wpilib.joystick import Joystick
from common import logitec_controller as lc
from wpilib.buttons.joystickbutton import JoystickButton
from commands.move_lift import MoveLift
from commands.claw_release import ClawRelease
from commands.claw_grab import ClawGrab
from commands.mecanum_drive import MecanumDrive

class OI:
    def __init__ (self, grabber_lift, drive):
        self.joy = Joystick(0)
        self.drive = drive
        
        #Create buttons
        raise_lift = JoystickButton(self.joy, lc.L_BUMPER)
        lower_lift = JoystickButton(self.joy, lc.L_TRIGGER)
        claw_release = JoystickButton(self.joy, lc.R_BUMPER)
        claw_grab = JoystickButton(self.joy, lc.R_TRIGGER)
        
        #Attach commands to buttons
        raise_lift.whenPressed(MoveLift(grabber_lift, .5))
        lower_lift.whenPressed(MoveLift(grabber_lift, -.5))
        claw_release.whenPressed(ClawRelease(grabber_lift))
        claw_grab.whenPressed(ClawGrab(grabber_lift))
        
        #Default command
        self.drive.setDefaultCommand(MecanumDrive(self.drive, self._get_axis(self.joy, lc.L_AXIS_X),
                                                  self._get_axis(self.joy, lc.L_AXIS_Y),
                                                  self._get_axis(self.joy, lc.R_AXIS_X)))

    def _get_axis(self, joystick, axis):
        return lambda : joystick.getAxis(axis)

        
        
        