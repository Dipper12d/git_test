height = float(input("Please enter in your height in m:"))
weight = int(input("Please enter in your weight in kg:"))
BMI = int(weight / (height * height))
if BMI >= 25:
    print(f"Your BMI is {BMI}.You are fat. Stop eating fatso")
else:
    print(f"your BMI is {BMI}.You are skinny. Eat more")
