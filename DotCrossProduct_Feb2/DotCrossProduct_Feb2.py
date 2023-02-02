import math

ax = -2
ay = 4
az = 9

magnitude_a = math.sqrt( math.pow(ax,2) + math.pow(ay,2) + math.pow(az,2) )

bx = 1
by = 6
bz = -3

magnitude_b = math.sqrt( math.pow(bx,2) + math.pow(by,2) + math.pow(bz,2) )

cx = (ay*bz) - (az*by)
cy = (az*bx) - (ax*bz)
cz = (ay*bx) - (ax*by)

magnitude_c = math.sqrt( math.pow(cx,2) + math.pow(cy,2) + math.pow(cz,2) )

angle = (math.asin((magnitude_c)/(magnitude_a * magnitude_b))  * (180/math.pi))

print("The angle is",angle)