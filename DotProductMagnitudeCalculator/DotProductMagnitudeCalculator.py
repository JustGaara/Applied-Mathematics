import math

x1 = input("What is the x for the first vector? ")

y1 = input("What is the y for the first vector? ")

x2 = input("What is the x for the second vector? ")

y2 = input("What is the y for the second vector? ")

angle = input ("What is the angle? ")

magnitude1 = math.sqrt(math.pow(int(x1),2) + math.pow(int(y1),2))
magnitude2 = math.sqrt(math.pow(int(x2),2) + math.pow(int(y2),2))

result_magnitude = magnitude1 * magnitude2 * math.cos(int(angle))

print("The result magnitude is", result_magnitude)
