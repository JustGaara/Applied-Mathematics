import math

print("""1 - Sin
2 - Cos
3 - Tan""")

choice = input("Choice: ")

angle = input("What is the angle? ")
radian = int(angle)/(180/math.pi)

if choice == "1":
    answer = math.cos(radian)
    print(answer)
elif choice == "2":
    answer = math.sin(radian)
    print(answer)
elif choice == "3":
    answer = math.tan(radian)
    print(answer)
