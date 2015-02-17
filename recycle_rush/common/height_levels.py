#This creates variables for set heights
INCH_PER_BIT = .078125 
BIT_PER_INCH = 1 / INCH_PER_BIT

def inches_to_bits (height):
    #inch * (bit/inch)
    return round(height / INCH_PER_BIT)
    
    
TOTE_HEIGHT = 12.5 #height is in inches
TOTE_HEIGHT_BITS = inches_to_bits(TOTE_HEIGHT)


