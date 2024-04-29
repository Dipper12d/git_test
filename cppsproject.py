from projectmain import *


doagain = True  # Loop for accessing the functions
while doagain := True:
    dispmenu()
    selec = input("Please choose A,B,C,D or Q:")
    if selec == "A" or selec == "a":
        dispinfo()
    elif selec == "B" or selec == "b":
        meanminmax()
    elif selec == "C" or selec == "c":
        percent30()
    elif selec == "D" or selec == "d":
        graphs()
    elif selec == "Q" or selec == "q":
        print("Thank you for using the system")
        do_again = False
        break
    else:
        print("Invalid selection, Try again.")
