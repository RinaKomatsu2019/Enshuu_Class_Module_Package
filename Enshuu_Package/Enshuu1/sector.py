import math

def calc_area(r,radius):
    # Check Radius
    if radius<=0 or radius>360:
        return None
    else:
        print("Calcurated The area of r={} radius={} Sector".format(r,radius))
        return r*r*math.pi*(radius/360.0)