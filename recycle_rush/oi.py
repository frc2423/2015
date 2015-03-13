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
from commands.auto_do_nothing import AutoDoNothing
from commands.auto_move_forward import AutoMoveForward
from commands.auto_one_object import Auto_One_Object
from subsystems.grabber_lift import GrabberLift
from common.smartdashboard_update_trigger import SmartDashboardUpdateTrigger
from common.out_of_range_trigger import OutOfRangeTrigger
from common.value_updated_trigger import ValueUpdatedTrigger
from common import height_levels as hl
from wpilib.sendablechooser import SendableChooser
from wpilib.smartdashboard import SmartDashboard

class OI:
    
    def __init__ (self, grabber_lift, drive, gyro):
        self.joy = Joystick(0)
        self.drive = drive
        self.grabber_lift = grabber_lift
        
        #Sendable Choosers used to create radio button groups on SmartDashboard
        self.auto_choose = SendableChooser()
        self.auto_choose.addObject('Auto Do Nothing', AutoDoNothing(drive))
        self.auto_choose.addObject('Auto Move Forward', AutoMoveForward(drive, gyro))
        self.auto_choose.addObject('Auto One Object', Auto_One_Object(drive, grabber_lift, gyro))
        SmartDashboard.putData('Autonomous Mode', self.auto_choose)
           
        self.height_level = SendableChooser()
        self.height_level.addObject('Level 5',  hl.START_HEIGHT + hl.TOTE_HEIGHT * 4)
        self.height_level.addObject('Level 4',   hl.START_HEIGHT + hl.TOTE_HEIGHT * 3)
        self.height_level.addObject('Level 3',  hl.START_HEIGHT + hl.TOTE_HEIGHT * 2)
        self.height_level.addObject('Level 2', hl.START_HEIGHT + hl.TOTE_HEIGHT)
        self.height_level.addObject('Level 1', hl.START_HEIGHT)     
        SmartDashboard.putData('Height Level', self.height_level)
        
        self.offset = SendableChooser()
        self.offset.addObject('Step', hl.STEP_HEIGHT)
        self.offset.addObject('Scoring Platform', hl.SCORING_PLATFORM_HEIGHT)
        self.offset.addObject('Floor', 0)
        SmartDashboard.putData('Offset Height', self.offset)
        
        
        # Create buttons
        self.l_bumper = JoystickButton(self.joy, lc.L_BUMPER)
        self.l_trigger = JoystickButton(self.joy, lc.L_TRIGGER)
        self.r_bumper = JoystickButton(self.joy, lc.R_BUMPER)
        self.r_trigger = JoystickButton(self.joy, lc.R_TRIGGER)
        self.btn_one   = JoystickButton(self.joy, 1)
        self.btn_two   = JoystickButton(self.joy, 2)
        self.height_level_trigger = ValueUpdatedTrigger(self.height_level.getSelected)
        
        # Attach commands to buttons
        self.l_bumper.whileActive(MoveLift(grabber_lift, -.5))
        self.l_trigger.whileActive(MoveLift(grabber_lift, .5))
        self.r_bumper.whenPressed(ClawRelease(grabber_lift))
        self.r_trigger.whenPressed(ClawGrab(grabber_lift))
        self.btn_two.whenPressed(CommandCall(lambda : grabber_lift.move_to_position()))
        self.btn_one.whenPressed(CommandCall(lambda : grabber_lift.set_mode(GrabberLift.mPercentVbus)))
        self.height_level_trigger.whenActive(
             MoveLiftToPosition(grabber_lift, 
                                hl.inches_to_bits(self.height_level.getSelected() +
                                                            self.offset.getSelected())))
        
        # Default command
        self.drive.setDefaultCommand(MecanumDrive(self.drive, self._get_axis(self.joy, lc.L_AXIS_X),
                                                  self._get_axis(self.joy, lc.L_AXIS_Y),
                                                  self._get_axis(self.joy, lc.R_AXIS_X)))
        self.grabber_lift.setDefaultCommand(MoveLift(grabber_lift, 0))
        
        
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
        
        
        out_of_range = OutOfRangeTrigger(hl.TOO_HIGH, hl.TOO_LOW, grabber_lift.pot_reading)
        out_of_range.whenActive(
              CommandCall(grabber_lift.change_break_mode(True)))
        
        in_range = OutOfRangeTrigger(hl.TOO_HIGH, hl.TOO_LOW, grabber_lift.pot_reading)
        in_range.whenInactive(
              CommandCall(grabber_lift.change_break_mode(False)))
        
    
        
    def _get_axis(self, joystick, axis):
        return lambda : joystick.getAxis(axis)