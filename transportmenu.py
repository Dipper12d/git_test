print("=" * 40)
print("Fare calculator-Changi Airport to City")
print("Please choose transport mode")
print("A-By Limousine-$55.00")
print("B-By Taxi-$30.00")
print("C-By Bus-$2.50")
print("D-By MRT-$2.00")
print("=" * 40)
selec = input("Please select A,B,C, or D:")
if selec == "A" or selec == "a":
    print("You have selected Limousine. Fare is $55.00 to city.Thank you and Goodbye")
elif selec == "B" or selec == "b":
    print("You have selected Taxi. Fare is $30.00 to city.Thank you and Goodbye")
elif selec == "C" or selec == "c":
    print("You have selected Bus. Fare is $2.50 to city.Thank you and Goodbye")
elif selec == "D" or selec == "d":
    print("You have selected MRT. Fare is $2.00 to city.Thank you and Goodbye")
else:
    print("Sorry invalid selection. No fare calculated.Thank you and Goodbye")
