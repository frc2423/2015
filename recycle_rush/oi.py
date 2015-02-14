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
from commands.command_call import CommandCall
from subsystems.drive import Drive
from subsystems.grabber_lift import GrabberLift
from wpilib.buttons import Trigger
from networktables import NetworkTable

class OI:
    
    class SmartDashboardUpdateTrigger(Trigger):
        '''
            Trigger used to check when entries are updated
            in the SmartDashboard
        '''
        
        def __init__(self, table_key, default_value):
            '''
                Creates a new trigger for entries when updated.
                
                :param table_key: The name of the entry in the
                SmartDashboard NetworkTable
                :param default_value: The value the entry will
                take if it doesn't already exist in the
                SmartDashboard
            '''
                
            self.table_key = table_key
            self.sd = NetworkTable.getTable('SmartDashboard')
            self.auto_update_value = self.sd.getAutoUpdateValue(table_key, default_value)
            self.last_value = self.auto_update_value.get()
    
        def get(self):
            updated = self.auto_update_value.get() != self.last_value
            self.last_value = self.auto_update_value.get()
            return updated
        
        
        def get_table_key(self):
            return self.table_key
        
        def get_key_value(self):
            return self.auto_update_value.get()
    
    def __init__ (self, grabber_lift, drive):
        self.joy = Joystick(0)
        self.drive = drive
        
        # Create buttons
        self.l_bumper = JoystickButton(self.joy, lc.L_BUMPER)
        self.l_trigger = JoystickButton(self.joy, lc.L_TRIGGER)
        self.r_bumper = JoystickButton(self.joy, lc.R_BUMPER)
        self.r_trigger = JoystickButton(self.joy, lc.R_TRIGGER)
        
        # Attach commands to buttons
        self.l_bumper.whileActive(MoveLift(grabber_lift, .5))
        self.l_trigger.whileActive(MoveLift(grabber_lift, -.5))
        self.r_bumper.whenPressed(ClawRelease(grabber_lift))
        self.r_trigger.whenPressed(ClawGrab(grabber_lift))
        
        # Default command
        self.drive.setDefaultCommand(MecanumDrive(self.drive, self._get_axis(self.joy, lc.L_AXIS_X),
                                                  self._get_axis(self.joy, lc.L_AXIS_Y),
                                                  self._get_axis(self.joy, lc.R_AXIS_X)))
        
        
        
        #create pid update triggers
        lift_p_trigger = OI.SmartDashboardUpdateTrigger('lift_p', GrabberLift.kP_default)
        lift_p_trigger.whenActive(
              CommandCall(lambda : grabber_lift.update_pid( p = lift_p_trigger.get_key_value() ) ) )
        
        lift_i_trigger = OI.SmartDashboardUpdateTrigger('lift_i', GrabberLift.kI_default)
        lift_i_trigger.whenActive(
              CommandCall(lambda : grabber_lift.update_pid( i = lift_i_trigger.get_key_value() ) ) )
        
        lift_d_trigger = OI.SmartDashboardUpdateTrigger('lift_d', GrabberLift.kD_default)
        lift_d_trigger.whenActive(
              CommandCall(lambda : grabber_lift.update_pid( d = lift_d_trigger.get_key_value() ) ) )


    def _get_axis(self, joystick, axis):
        return lambda : joystick.getAxis(axis)

        