import wpilib
import hal
from wpilib import RobotDrive

class KwarqsDriveMech(RobotDrive):
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.weight_multiplier = 1
        
    def set_multiplier(self, in_multi = None):
        if in_multi != None :
            self.weight_multiplier = in_multi
        else:
            self.weight_multiplier = 1
        
    def mecanumDrive_Cartesian(self, x, y, rotation, gyroAngle):
        """Drive method for Mecanum wheeled robots.

        A method for driving with Mecanum wheeled robots. There are 4 wheels
        on the robot, arranged so that the front and back wheels are toed in
        45 degrees.  When looking at the wheels from the top, the roller
        axles should form an X across the robot.

        This is designed to be directly driven by joystick axes.

        :param x: The speed that the robot should drive in the X direction.
            [-1.0..1.0]
        :param y: The speed that the robot should drive in the Y direction.
            This input is inverted to match the forward == -1.0 that
            joysticks produce. [-1.0..1.0]
        :param rotation: The rate of rotation for the robot that is
            completely independent of the translation. [-1.0..1.0]
        :param gyroAngle: The current angle reading from the gyro.  Use this
            to implement field-oriented controls.
        """
        if not wpilib.RobotDrive.kMecanumCartesian_Reported:
            hal.HALReport(hal.HALUsageReporting.kResourceType_RobotDrive,
                          self.getNumMotors(),
                          hal.HALUsageReporting.kRobotDrive_MecanumCartesian)
            RobotDrive.kMecanumCartesian_Reported = True
        xIn = x
        yIn = y
        # Negate y for the joystick.
        yIn = -yIn
        # Compenstate for gyro angle.
        xIn, yIn = RobotDrive.rotateVector(xIn, yIn, gyroAngle)

        wheelSpeeds = [0]*self.kMaxNumberOfMotors
        wheelSpeeds[self.MotorType.kFrontLeft] = xIn + yIn + rotation 
        wheelSpeeds[self.MotorType.kFrontRight] = -xIn + yIn - rotation
        wheelSpeeds[self.MotorType.kRearLeft] = -xIn + yIn + ( rotation * self.weight_multiplier )
        wheelSpeeds[self.MotorType.kRearRight] = xIn + yIn - ( rotation * self.weight_multiplier )

        RobotDrive.normalize(wheelSpeeds)


        self.frontLeftMotor.set(wheelSpeeds[self.MotorType.kFrontLeft] * self.invertedMotors[self.MotorType.kFrontLeft] * self.maxOutput, self.syncGroup)
        self.frontRightMotor.set(wheelSpeeds[self.MotorType.kFrontRight] * self.invertedMotors[self.MotorType.kFrontRight] * self.maxOutput, self.syncGroup)
        self.rearLeftMotor.set(wheelSpeeds[self.MotorType.kRearLeft] * self.invertedMotors[self.MotorType.kRearLeft] * self.maxOutput, self.syncGroup)
        self.rearRightMotor.set(wheelSpeeds[self.MotorType.kRearRight] * self.invertedMotors[self.MotorType.kRearRight] * self.maxOutput, self.syncGroup)

        if self.syncGroup != 0:
            wpilib.CANJaguar.updateSyncGroup(self.syncGroup)
        self.feed()
    