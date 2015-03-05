import wpilib
from wpilib.joystick import Joystick
from common import logitec_controller as lc
from wpilib.buttons.joystickbutton import JoystickButton
from commands.move_lift import MoveLift
from commands.claw_release import ClawRelease
from commands.claw_grab import ClawGrab
from commands.mecanum_drive import MecanumDrive
from commands.command_call import CommandCall
from commands.move_lift_to_position import MoveLiftToPosition
from commands.auto_move_forward import AutoMoveForward
from commands.auto_one_object import Auto_One_Object
from subsystems.grabber_lift import GrabberLift
from common.smartdashboard_update_trigger import SmartDashboardUpdateTrigger
from common.out_of_range_trigger import OutOfRangeTrigger
from common import height_levels as hl
from wpilib.sendablechooser import SendableChooser
from wpilib.smartdashboard import SmartDashboard

class OI:
    
    def __init__ (self, grabber_lift, drive, gyro):
        self.joy = Joystick(0)
        self.drive = drive
        
        # Create buttons
        self.l_bumper = JoystickButton(self.joy, lc.L_BUMPER)
        self.l_trigger = JoystickButton(self.joy, lc.L_TRIGGER)
        self.r_bumper = JoystickButton(self.joy, lc.R_BUMPER)
        self.r_trigger = JoystickButton(self.joy, lc.R_TRIGGER)
        self.btn_one   = JoystickButton(self.joy, 1)
        self.btn_two   = JoystickButton(self.joy, 2)
        
        # Attach commands to buttons
        self.l_bumper.whileActive(MoveLift(grabber_lift, .5))
        self.l_trigger.whileActive(MoveLift(grabber_lift, -.5))
        self.r_bumper.whenPressed(ClawRelease(grabber_lift))
        self.r_trigger.whenPressed(ClawGrab(grabber_lift))
        self.btn_two.whenPressed(CommandCall(lambda : grabber_lift.move_to_position()))
        self.btn_one.whenPressed(CommandCall(lambda : grabber_lift.set_mode(GrabberLift.mPercentVbus)))

        
        # Default command
        self.drive.setDefaultCommand(MecanumDrive(self.drive, self._get_axis(self.joy, lc.R_AXIS_X),
                                                  self._get_axis(self.joy, lc.R_AXIS_Y),
                                                  self._get_axis(self.joy, lc.L_AXIS_X)))
        
        
        
        #create pid update triggers
        lift_p_trigger = SmartDashboardUpdateTrigger('lift_p', GrabberLift.kP_default)
        lift_p_trigger.whenActive(
              CommandCall(lambda : grabber_lift.update_pid( p = lift_p_trigger.get_key_value() ) ) )
        
        lift_i_trigger = SmartDashboardUpdateTrigger('lift_i', GrabberLift.kI_default)
        lift_i_trigger.whenActive(
              CommandCall(lambda : grabber_lift.update_pid( i = lift_i_trigger.get_key_value() ) ) )
        
        lift_d_trigger = SmartDashboardUpdateTrigger('lift_d', GrabberLift.kD_default)
        lift_d_trigger.whenActive(
              CommandCall(lambda : grabber_lift.update_pid( d = lift_d_trigger.get_key_value() ) ) )

        #create update trigger for position
        lift_pos_trigger = SmartDashboardUpdateTrigger('lift_goal_pos', .1)
        lift_pos_trigger.whenActive(
              CommandCall(lambda : grabber_lift.prepare_to_move_to_position(lift_pos_trigger.get_key_value())))
        
        lift_position = SmartDashboardUpdateTrigger('lift_position',0)
        lift_position.whenActive(
              MoveLiftToPosition(grabber_lift, hl.inches_to_bits(lift_position.get_key_value() + 
              wpilib.SmartDashboard.getNumber('lift_offset', 0))))
        
        out_of_range = OutOfRangeTrigger(hl.TOO_HIGH, hl.TOO_LOW, grabber_lift.pot_reading)
        out_of_range.whenActive(
              CommandCall(grabber_lift.change_break_mode(True)))
        
        in_range = OutOfRangeTrigger(hl.TOO_HIGH, hl.TOO_LOW, grabber_lift.pot_reading)
        in_range.whenInactive(
              CommandCall(grabber_lift.change_break_mode(False)))
        
        auto_chooser = SendableChooser()
        auto_chooser.addObject('Auto Move Forward', AutoMoveForward(drive, gyro))
        auto_chooser.addObject('Auto One Object', Auto_One_Object(drive, grabber_lift, 0, gyro))
        SmartDashboard.putData('Autonomous Modes', auto_chooser)
        
    def _get_axis(self, joystick, axis):
        return lambda : joystick.getAxis(axis)

