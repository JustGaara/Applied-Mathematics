import math

choice = input("""1 - Sin
2 - Cos
3 - Tan
Choice: """)

angle = input("What is the angle? ")
radian = int(angle) / (180 / math.pi)

if choice == 1:
    answer = math.cos(int(radian))
    print(answer)
elif choice == 2:
    answer = math.sin(int(radian))
    print(answer)
elif choice == 3:
    answer = math.tan(int(radian))
    print(answer)
