# This creates variables for set heights
INCH_PER_BIT = .078125 
BIT_PER_INCH = 1 / INCH_PER_BIT

def inches_to_bits (height):
    # inch * (bit/inch)
    return round(height / INCH_PER_BIT)
    
    
TOTE_HEIGHT = 12.5 #height is in inches
TOTE_HEIGHT_BITS = inches_to_bits(TOTE_HEIGHT)
# In inches
STEP_HEIGHT = 6.25
STEP_OFFSET_BITS = inches_to_bits(STEP_HEIGHT)
# In inches
SCORING_PLATFORM_HEIGHT = 2
SCORING_PLATFORM_HEIGHT_BITS = inches_to_bits(SCORING_PLATFORM_HEIGHT)

# Not sure if it's necessary but...
FLOOR_HEIGHT = 0
FLOOR_HEIGHT_BITS = inches_to_bits(FLOOR_HEIGHT)

# PID values in bits to enable break mode so the motor actually stops
# when it is supposed to
TOO_HIGH = 500
TOO_LOW = 200