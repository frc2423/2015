import wpilib
import logitec_controller as lc
import port_values as pv

class MyRobot (wpilib.SampleRobot):
    
    def robotInit (self):
        '''
            This initializes the robot
        '''
        
        #This is defines the joystick
        self.joy = wpilib.Joystick (0)
        
        #These are the motors for the tank drive
        self.lf_motor          = wpilib.CANTalon(pv.CAN_LIFT_TALON_FL)
        self.lb_motor          = wpilib.CANTalon(pv.CAN_LIFT_TALON_BL)
        self.rf_motor          = wpilib.CANTalon(pv.CAN_LIFT_TALON_FR)
        self.rb_motor          = wpilib.CANTalon(pv.CAN_LIFT_TALON_BR)
        
        
        #This handles basic drive operations
        self.robot_drive = wpilib.RobotDrive(self.lf_motor, self.lb_motor, self.rf_motor, self.rb_motor)
       
    def operatorControl (self):
        while self.isOperatorControl() and self.isEnabled(): 
            self.robot_drive.tankDrive (self.joy.getAxis (lc.L_AXIS_Y), self.joy.getAxis (lc.R_AXIS_Y)) 
            
        

if __name__ == "__main__":
    wpilib.run(MyRobot)
