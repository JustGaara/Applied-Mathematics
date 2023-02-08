import math

repeat = "1"
while repeat == "1":
    method = input("""Do you have the angle?
    1 - Yes
    2 - No
    Choice: """)

    if method == "1":
        ax = input("ax = ")
        ay = input("ay = ")
        bx = input("bx = ")
        by = input("by = ")
        angle = input("angle = ")

        mag_a = math.sqrt(math.pow(float(ax), 2) + math.pow(float(ay), 2))
        mag_b = math.sqrt(math.pow(float(bx), 2) + math.pow(float(by), 2))

        print("Magnitude of a =", mag_a)
        print("Magnitude of b =", mag_b)

        cross_product = float(mag_a) * float(mag_b) * math.sin(float(angle))

        print("Magnitude of c = a x b =", cross_product)

        print()
        repeat = input("""Would you like to continue?
        1 for yes, 0 for no
        Choice = """)

    elif method == "2":
        ax = input("ax = ")
        ay = input("ay = ")
        az = input("az = ")
        bx = input("bx = ")
        by = input("by = ")
        bz = input("bz = ")

        cx = (int(ay)*int(bz)) - (int(az)*int(by))
        cy = (int(az)*int(bx)) - (int(ax)*int(bz))
        cz = (int(ax)*int(by)) - (int(ay)*int(bx))

        print()

        magnitude_c = math.sqrt(math.pow(cx, 2) + math.pow(cy, 2) + math.pow(cz, 2))

        print("The magnitude of c is", magnitude_c)

        print()
        repeat = input("""Would you like to continue?
        1 for yes, 0 for no
        Choice = """)
    else:
        print("Wrong input.")
        print()
        repeat = 1
