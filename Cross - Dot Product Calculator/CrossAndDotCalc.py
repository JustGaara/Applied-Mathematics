import CrossProduct
import DotProduct

rep = "1"

while rep == "1":
    ch = input("""What would you like to do?
    1 - Cross Product Calculation
    2 - Dot Product Calculation
    
    Choice: """)

    if ch == "1":
        CrossProduct.Calculate()

        print()
        rep = input("""Would you like to continue?
                   1 for yes, 0 for no
                   Choice = """)

    elif ch == "2":
        DotProduct.Calculate()

        print()
        rep = input("""Would you like to continue?
                   1 for yes, 0 for no
                   Choice = """)
    else:
        print("Wrong input.")
        print()
        rep = "1"
