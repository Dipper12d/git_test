temp_data = []
days = ["Sun", "Mon", "Tues", "Weds", "Thurs", "Fri", "Sat"]
for ik in range(0, 7):
    temp_day = float(input(f"Please enter the temperature for {days[ik]}"))
    temp_data.append(temp_day)
for ix, day in enumerate(days):
    print(f"Temperature on {day} is {temp_data[ix]}  ")
