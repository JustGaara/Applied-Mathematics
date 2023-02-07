import math

x1 = input("What is the x for the first vector? ")

y1 = input("What is the y for the first vector? ")

z1 = input("What is the z for the first vector? ")

x2 = input("What is the x for the second vector? ")

y2 = input("What is the y for the second vector? ")

z2 = input("What is the z for the second vector? ")

cx = (int(y1)*int(z2)) - (int(y2)*int(z1))
cy = (int(x1)*int(z2)) - (int(x2)*int(z1))
cz = (int(x1)*int(y2)) - (int(x2)*int(y1))

print()

print("cx =", cx)
print("cy =", cy)
print("cz =", cz)

print()

magnitude_c = math.sqrt(math.pow(cx, 2) + math.pow(cy, 2) + math.pow(cz, 2))

print("The magnitude of c is", magnitude_c)

