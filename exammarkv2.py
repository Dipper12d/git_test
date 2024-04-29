mark = 0
total = 0
for quest in [1, 2, 3, 4, 5]:
    mark = int(input(f"Please enter mark for question {quest}:"))
    total = total + mark
print(f"Total marks is {total}")
if total < 50:
    print("Student has failed the subject")
else:
    print("Student has passed subject")
