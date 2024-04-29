import math

do_again = True
while do_again := True:
    print("=" * 40)
    print("Calculator-Choose what area to calculate")
    print("A-Area of a Rectangle")
    print("B-Area of a Right angled Triangle")
    print("C-Area of a Circle")
    print("Q-Quit")
    print("=" * 40)

    selec = input("Please select an option:")

    if selec == "A" or selec == "a":
        rectlength = int(input("Please enter the length:"))
        rectwidth = int(input("Please enter the width:"))
        rectarea = rectlength * rectwidth
        print(f"Area of rectangle is {rectarea:.2f}unit square")
    elif selec == "B" or selec == "b":
        trilength = int(input("Please enter the length:"))
        triwidth = int(input("Please enter the width:"))
        triarea = 0.5 * trilength * triwidth
        print(f"Area of triangle is {triarea:.2f}unit square")
    elif selec == "C" or selec == "c":
        circradius = int(input("Please enter the radius:"))
        circarea = 3.1415 * circradius * circradius
        print(f"Area of rectangle is {rectarea:.2f}unit square")
    elif selec == "Q" or selec == "q":
        print("Thank you for using the system")
        do_again = False
        break
    else:
        print("Invalid choice.Please select A,B,C or Q")
print("Goodbye")
