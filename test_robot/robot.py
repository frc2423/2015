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
       
    def operatorControl (self):
        while self.isOperatorControl() and self.isEnabled(): 
            self.robot_drive.tankDrive (self.joy.getAxis (lc.L_AXIS_Y), self.joy.getAxis (lc.R_AXIS_Y)) 
            
            if self.joy.getRawButton(lc.L_TRIGGER):
                self.motor_master.set(-.6)
            elif self.joy.getRawButton(lc.L_BUMPER):
                self.motor_master.set(.6)
            else:
                self.motor_master.set(0)

            
            if self.joy.getRawButton(lc.R_TRIGGER):
                #grab
                self.grabber.set(wpilib.DoubleSolenoid.Value.kForward)
            elif self.joy.getRawButton(lc.R_BUMPER):
                #release
                self.grabber.set(wpilib.DoubleSolenoid.Value.kReverse)
            
            
            
        

if __name__ == "__main__":
    wpilib.run(MyRobot)
