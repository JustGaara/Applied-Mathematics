import math

bool(repeat) = 1
while (repeat == 1)
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
    
        print("Magnitude of c = a.b =", dot_product)
        
        print()
        repeat = input("""Would you like to continue?
        1 for yes, 0 for no
        Choice = """)
        
    else
        print("Wrong input.")
        print()
        repeat = 1
    
    
    