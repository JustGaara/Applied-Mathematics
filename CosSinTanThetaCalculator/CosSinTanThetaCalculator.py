import math

choice = input("""1 - Sin
2 - Cos
3 - Tan
Choice: """)

angle = input("What is the angle? ")

#match choice:
if choice == 1:
    answer = math.cos(angle * (180/math.pi))
if choice == 2:
    answer = math.sin(angle * (180/math.pi))
if choice == 3:
    answer = math.tan(angle * (180/math.pi))

print (answer)