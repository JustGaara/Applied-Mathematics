import math

x1 = input("What is the x for the first vector? ")

y1 = input("What is the y for the first vector? ")

x2 = input("What is the x for the second vector? ")

y2 = input("What is the y for the second vector? ")

angle = input ("What is the angle? ")

magnitude1 = math.sqrt(math.pow(int(x1), 2) + math.pow(int(y1), 2))
magnitude2 = math.sqrt(math.pow(int(x2), 2) + math.pow(int(y2), 2))

print("Magnitude of a (first vector) is", magnitude1)
print("Magnitude of b (second vector) is", magnitude2)

print()

magnitude_dot = float(magnitude1) * float(magnitude2) * math.cos(float(angle)/(180/math.pi))
magnitude_cross = float(magnitude1) * float(magnitude2) * math.sin(float(angle)/(180/math.pi))

print("The result dot product magnitude is", magnitude_dot)
print("The result cross product magnitude is", magnitude_cross)

