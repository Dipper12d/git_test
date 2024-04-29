avg_temp = 0
total = 0
day = 0
temp_data = [32.5, 31.2, 29.6, 30.7, 30.5, 31.2, 29.9]
for day in range(1, 8):
    print(f"Temperature of day {day} is {temp_data[day-1]} degC")
    total = total + temp_data[day - 1]
avg_temp = total / len(temp_data)
print(f"average weekly temperature is {avg_temp:.2f} degC")
