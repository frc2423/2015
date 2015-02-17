
# measurements in feet/second

MAX_SPEED = 1

#1/4 speed voltage = 
#1/2 speed voltage = 
#3/4 speed voltage = 

VOLTAGE_25 = .25
VOLTAGE_50 = .5
VOLTAGE_75 = .75

def time_to_move (speed_percent, distance):
    time = distance / (MAX_SPEED * speed_percent)
    return time

