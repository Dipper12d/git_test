idx = 1
sum = 0
print("finding the sum and mean of numbers starting from 1")
final = int(input("Please enter the final number as an integer:"))
while idx <= final:
    sum = sum + idx
    idx += 1
mean_val = sum / final
print(f"sum of  1 to {final} is {sum} and the mean is {mean_val:.2f}")
