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

angle_cross = (math.asin((magnitude_c)/(magnitude_a * magnitude_b)))
angle_dot = (math.acos((magnitude_c)/(magnitude_a * magnitude_b)))

print("The magnitude of vector A is sqrt (",math.pow(ax,2) + math.pow(ay,2) + math.pow(az,2),") =", magnitude_a)
print("The magnitude of vector B is sqrt (",math.pow(bx,2) + math.pow(by,2) + math.pow(bz,2),") =", magnitude_b)
print("The magnitude of vector C is sqrt (",math.pow(cx,2) + math.pow(cy,2) + math.pow(cz,2),") =", magnitude_c)

print()
print("Theta is",((magnitude_c)/(magnitude_a * magnitude_b)))
print()

print("--- Cross Product ---")
print("The angle is",angle_cross,"radians and", (angle_cross * (180/math.pi)), "degrees")

print()

print("--- Dot Product ---")
print("The angle is",angle_dot,"radians and", (angle_dot * (180/math.pi)), "degrees")