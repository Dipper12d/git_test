date = [1, 2, 3, 4, 5, 6, 7]
temperature = [32.5, 31.1, 29.1, 30.5, 30, 31.0, 28.9]
avg_temp = 29.5
for day, temp in zip(date, temperature):
    if temp < avg_temp:
        print(f"December {day} temperature is {temp:.2f} and lower than average.")
    else:
        print(f"December {day} temperature is {temp:.2f} and higher than average")
