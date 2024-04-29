qn = 1
total = 0
for qn in range(1, 7):
    if qn < 6:
        mark = int(input(f"Please enter mark for question {qn}: "))
        total = total + mark
    else:
        print(f"Total marks for the subject is {total}")
