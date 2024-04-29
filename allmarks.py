marks = [40, 60, 70, 55, 62, 70, 50, 80, 88, 56]


def dispmarks(marks):
    for i, mk in enumerate(marks):
        print(f"Mark of student {i+1} is {mk}")


def dispmax(marks):
    maxmarks, maxindex = 0, 0
    maxmarks = max(marks)
    maxindex = marks.index(maxmarks) + 1
    print(f"Student {maxindex} scores maximum marks of {maxmarks}")


# dispmarks(marks)
# dispmax(marks)
def showMenu():
    # Display Menu with Border
    print("=" * 40)
    print("Please choose option")
    print("A - Display students' marks.")
    print("B - Display student who scores the maximum mark.")
    print("Q - Exit the program.")
    print("=" * 40)


loop = True
while loop:
    showMenu()
    sel = input("Please select A,B or Q:")
    if sel == "A" or sel == "a":
        dispmarks(marks)
    elif sel == "B" or sel == "b":
        dispmax()
    elif sel == "Q" or sel == "q":
        loop = False
    else:
        print("Invalid selection. Try again")
