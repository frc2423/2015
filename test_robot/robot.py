import wpilib
import logitec_controller as lc
import port_values as pv

class MyRobot (wpilib.SampleRobot):
    
    def robotInit (self):
        '''
            This initializes the robot
        '''
        
        print('testing')
        
        #This is defines the joystick
        self.joy = wpilib.Joystick (0)
        
        #These are the motors for the tank drive
        self.lf_motor          = wpilib.CANTalon(pv.CAN_LIFT_TALON_FL)
        self.lb_motor          = wpilib.CANTalon(pv.CAN_LIFT_TALON_BL)
        self.rf_motor          = wpilib.CANTalon(pv.CAN_LIFT_TALON_FR)
        self.rb_motor          = wpilib.CANTalon(pv.CAN_LIFT_TALON_BR)

        # Lifter Motors
        self.motor_master = wpilib.CANTalon(pv.CAN_LIFT_TALON_MASTER)
        self.motor_slave  = wpilib.CANTalon(pv.CAN_LIFT_TALON_SLAVE)
        
        # Grabber 
        self.grabber = wpilib.DoubleSolenoid(pv.CAN_PCM, pv.SOLENOID_0, pv.SOLENOID_1)
    
        
        # set slave control mode - the salve is ALWAYS a slave to the master no
        # no matter the mode of the master
        self.motor_slave.changeControlMode(wpilib.CANTalon.ControlMode.Follower)
        
        #set slave to follow master commands(this sets the motor master id[which is 1]to the )
        self.motor_slave.set(self.motor_master.getDeviceID())
        
        
        #This handles basic drive operations
        self.robot_drive = wpilib.RobotDrive(self.lf_motor, self.lb_motor, self.rf_motor, self.rb_motor)

        #self.robot_drive.set
        self.robot_drive.setInvertedMotor(wpilib.RobotDrive.MotorType.kFrontLeft, True)
        self.robot_drive.setInvertedMotor(wpilib.RobotDrive.MotorType.kFrontRight, True)
        self.robot_drive.setInvertedMotor(wpilib.RobotDrive.MotorType.kRearLeft, True)
        self.robot_drive.setInvertedMotor(wpilib.RobotDrive.MotorType.kRearRight, True)
       
    def operatorControl (self):
        while self.isOperatorControl() and self.isEnabled(): 

            left_x = self.joy.getAxis(lc.L_AXIS_X)
            left_y = self.joy.getAxis(lc.L_AXIS_Y)
            right_x = self.joy.getAxis(lc.R_AXIS_X)
            right_y = self.joy.getAxis(lc.R_AXIS_Y)
            
            
            #self.robot_drive.mecanumDrive_Cartesian(left_x, left_y, right_x, 0)
       
            self.robot_drive.tankDrive(left_y, right_y)
            #self.lb_motor.set(right_y)
            
            if self.joy.getRawButton(lc.L_TRIGGER):
                self.motor_master.set(.6)
            elif self.joy.getRawButton(lc.L_BUMPER):
                self.motor_master.set(-.6)
            else:
                self.motor_master.set(0)

            
            if self.joy.getRawButton(lc.R_TRIGGER):
                self.grabber.set(wpilib.DoubleSolenoid.Value.kReverse)
            elif self.joy.getRawButton(lc.R_BUMPER):
                self.grabber.set(wpilib.DoubleSolenoid.Value.kForward)          
        

if __name__ == "__main__":
    wpilib.run(MyRobot)
