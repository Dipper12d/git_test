idx = 1
sum = 0
print("Finding sum and mean of integers from 1")
final = int(input("Please enter in the final integer"))
for idx in range(1, final + 1):
    sum = sum + idx

mean = sum / final
print(f"sum of 1 to {final} is {sum} and mean is {mean}")
