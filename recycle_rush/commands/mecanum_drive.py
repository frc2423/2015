from wpilib.command import Command
import wpilib

class MecanumDrive(Command):
    '''
        Used to move the robot
    '''
    def __init__(self, drive, get_x, get_y, get_z, gyro = None, weight_modifier = None):
        '''
            initializes mecanum drive movement.
            :param drive : the drive subsystem
            :param get_x: Used to get the x angle, function that determines y direction
            :param get_y: Used to get the y angle, function that determines the y value and direction
            :param get_z: Used to get the z angle, function that determines 
            rotation and direction of rotation. Z value must be given if it
            separate from the joystick. 
        '''
        super().__init__()
        self.drive = drive
        self.get_x = get_x
        self.get_y = get_y
        self.get_z = get_z
        self.get_multi = weight_modifier
        self.gyro = gyro
        self.requires(drive)
        
        
        self.input_ramp_timer = wpilib.Timer()
        self.current_x = 0
        self.current_y = 0
        self.current_z = 0

    def initialize(self):
        '''
            Called just before this Command runs the first time
        '''
        self.input_ramp_timer.start()
    
    def execute(self):
        '''
            Called repeatedly when this Command is scheduled
            to run
        '''
        angle = self.gyro.getAngle() if self.gyro != None else 0
        x = self.get_x() if callable(self.get_x) else self.get_x
        y = self.get_y() if callable(self.get_y) else self.get_y
        z = self.get_z() if callable(self.get_z) else self.get_z
        mutli = self.get_multi() if callable(self.get_multi) else self.get_multi
        
        if self.input_ramp_timer.hasPeriodPassed(.08):
            
            if (x > 0 and self.current_x < 0) or (x < 0 and self.current_x > 0):
                self.current_x = 0
                
            if (y > 0 and self.current_y < 0) or (y < 0 and self.current_y > 0):
                self.current_y = 0
                
            if (z > 0 and self.current_z < 0) or (z < 0 and self.current_z > 0):
                self.current_z = 0
            
            x_ramp_rate = 1
            y_ramp_rate = 1
            z_ramp_rate = .08
            #ramp_rate = 1
            
            dx = x - self.current_x
            dy = y - self.current_y
            dz = z - self.current_z
            
            if dx < 0:
                self.current_x = self.current_x + max(-x_ramp_rate, dx)
            else:
               self.current_x = self.current_x + min(x_ramp_rate, dx) 
               
            if dy < 0:
                self.current_y = self.current_y + max(-y_ramp_rate, dy)
            else:
               self.current_y = self.current_y + min(y_ramp_rate, dy) 
               
            if dz < 0:
                self.current_z = self.current_z + max(-z_ramp_rate, dz)
            else:
               self.current_z = self.current_z + min(z_ramp_rate, dz) 
               
            self.input_ramp_timer.reset()
            print('period passed')
            
        
        self.drive.robot_move(self.current_x, self.current_y, self.current_z, angle, mutli)
        

    def isFinished(self):
        '''
            Make this return true when this Command no longer
            needs to run execute()
        '''
        return False
    
    def end(self):
        '''
            Called once after isFinished returns true
        '''
        self.drive.robot_move (0,0,0,0)
        
    def interrupted(self):
        '''
            Called when another command which requires one or
            more of the same subsystems is scheduled to run
        '''
        self.end()
        