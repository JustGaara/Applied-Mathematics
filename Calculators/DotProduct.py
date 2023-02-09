import math

def Calculate():
    dimension = input("""Is it 2D or 3D?
        1 - 2D
        2 - 3D
        Choice: """)

    if dimension == "1":
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

                dot_product = float(mag_a) * float(mag_b) * math.cos(float(angle))

                print("Magnitude of c = a.b =", dot_product)

                print()
                repeat = input("""Would you like to continue?
                1 for yes, 0 for no
                Choice = """)

            elif method == "2":
                ax = input("ax = ")
                ay = input("ay = ")
                bx = input("bx = ")
                by = input("by = ")

                mag_a = math.sqrt(math.pow(float(ax), 2) + math.pow(float(ay), 2))
                mag_b = math.sqrt(math.pow(float(bx), 2) + math.pow(float(by), 2))

                print("Magnitude of a =", mag_a)
                print("Magnitude of b =", mag_b)

                dot_product = (float(ax) * float(bx)) + (float(ay) * float(by))
                calc_angle = math.acos(float(dot_product) / (float(mag_a) * float(mag_b)))

                print("Magnitude of c = a.b =", dot_product)
                print("The angle is", calc_angle)

                print()
                repeat = input("""Would you like to continue?
                1 for yes, 0 for no
                Choice = """)

            else:
                print("Wrong input.")
                print()
                repeat = 1
    elif dimension == "2":
        repeat = "1"
        while repeat == "1":

            method = input("""Do you have the angle?
                        1 - Yes
                        2 - No
                        Choice: """)

            if method == "1":
                ax = input("ax = ")
                ay = input("ay = ")
                az = input("az = ")
                bx = input("bx = ")
                by = input("by = ")
                bz = input("bz = ")
                angle = input("angle = ")

                mag_a = math.sqrt(math.pow(float(ax), 2) + math.pow(float(ay), 2) + math.pow(float(az), 2))
                mag_b = math.sqrt(math.pow(float(bx), 2) + math.pow(float(by), 2) + math.pow(float(bz), 2))

                print("Magnitude of a =", mag_a)
                print("Magnitude of b =", mag_b)

                dot_product = float(mag_a) * float(mag_b) * math.cos(float(angle))

                print("Magnitude of c = a.b =", dot_product)

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

                mag_a = math.sqrt(math.pow(float(ax), 2) + math.pow(float(ay), 2) + math.pow(float(az), 2))
                mag_b = math.sqrt(math.pow(float(bx), 2) + math.pow(float(by), 2) + math.pow(float(bz), 2))

                print("Magnitude of a =", mag_a)
                print("Magnitude of b =", mag_b)

                dot_product = (float(ax) * float(bx)) + (float(ay) * float(by)) + (float(az) * float(bz))
                calc_angle = math.acos(float(dot_product) / (float(mag_a) * float(mag_b)))

                print("Magnitude of c = a.b =", dot_product)
                print("The angle is", calc_angle)

                print()
                repeat = input("""Would you like to continue?
                                           1 for yes, 0 for no
                                           Choice = """)
