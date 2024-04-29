import csv
import matplotlib.pyplot as plt
import numpy as np

# initialize the columns
year = []
dividends = []
interest = []
others = []
rent = []
royalties = []
trade_income = []

dividends2 = []
interest2 = []
others2 = []
rent2 = []
royalties2 = []
tradinc2 = []

dividends3 = []
interest3 = []
others3 = []
rent3 = []
royalties3 = []
tradinc3 = []


# open the file
openfile = open("incometypesg_datatype.csv")
csvreader = csv.reader(openfile)
next(csvreader)  # skip title row
# append row in the list
for row in csvreader:
    # row is a list
    year.append(row[0])
    dividends.append(row[1])
    interest.append(row[2])
    others.append(row[3])
    rent.append(row[4])
    royalties.append(row[5])
    trade_income.append(row[6])

# create new lists of range 2011 to 2016
for ix in range(4, 10, 1):
    dividends2.append(dividends[ix])
    interest2.append(interest[ix])
    others2.append(others[ix])
    rent2.append(rent[ix])
    royalties2.append(royalties[ix])
    tradinc2.append(trade_income[ix])

# create new integer lists of range 2011 to 2016
for ix in range(4, 10, 1):
    dividends3.append(int(dividends[ix]))
    interest3.append(int(interest[ix]))
    others3.append(int(others[ix]))
    rent3.append(int(rent[ix]))
    royalties3.append(int(royalties[ix]))
    tradinc3.append(int(trade_income[ix]))


def dispmenu():  # The displayed menu [working]
    print("=" * 40)
    print("Income Calculator-Choose what to calculate")
    print("A-Information for year 2010")
    print("B-Maximum, minimum and mean values from 2011 to 2016")
    print("C-Find 30 percent change between years ")
    print("D-Make plots")
    print("Q-Quit")
    print("=" * 40)


def dispinfo():  # The first function [working]
    print(f"For year {year[3]},")
    print(f"Dividends is {dividends[3]}")
    print(f"Interest is {interest[3]}")
    print(f"Other types is {others[3]}")
    print(f"Rent is {rent[3]}")
    print(f"Royalties is {royalties[3]}")
    print(f"Trade income is {trade_income[3]}")


def meanminmax():  # select between mean and minimum maximum
    print("=" * 40)
    print("Choose either:")
    print("A-Mean")
    print("B-Maximum and minimum")
    print("=" * 40)
    option = input("Please choose:")
    if option == "A" or option == "a":
        meancalc()
    elif option == "B" or option == "b":
        minmaxcalc()
    else:
        print("Invalid Input")


def meancalc():  # The second function pt1 [working]
    print("=" * 40)
    print("Please choose an income type")
    print("1-Dividends")
    print("2-Interest")
    print("3-Other types")
    print("4-Rent")
    print("5-Royalties")
    print("6-Trade income")
    print("=" * 40)
    chooserow = input("Please select 1,2,3,4,5 or 6:")
    if chooserow == "1":
        sum1 = sum(dividends3)
    elif chooserow == "2":
        sum1 = sum(interest3)
    elif chooserow == "3":
        sum1 = sum(others3)
    elif chooserow == "4":
        sum1 = sum(rent3)
    elif chooserow == "5":
        sum1 = sum(royalties3)
    elif chooserow == "6":
        sum1 = sum(tradinc3)
    else:
        print("Invalid Input")
    output1 = sum1 / 6
    print(f"The mean value is {output1:.2f}")


def minmaxcalc():  # The second function pt2 [working]
    print("Please choose an income type")
    print("1-Dividends")
    print("2-Interest")
    print("3-Other types")
    print("4-Rent")
    print("5-Royalties")
    print("6-Trade income")
    chooserow = input("Please select 1,2,3,4,5 or 6:")
    if chooserow == "1":
        print(
            f"The maximum is {max(dividends2, key=int)} in {year[dividends.index(max(dividends2, key=int))]} and minimum is {min(dividends2, key=int)} in {year[dividends.index(min(dividends2, key=int))]}."
        )
    elif chooserow == "2":
        print(
            f"The maximum is {max(interest2, key=int)} in {year[interest.index(max(interest2, key=int))]} and minimum is {min(interest2, key=int)} in {year[interest.index(min(interest2, key=int))]}."
        )
    elif chooserow == "3":
        print(
            f"The maximum is {max(others2, key=int)} in {year[others.index(max(others2, key=int))]} and minimum is {min(others2, key=int)} in {year[others.index(min(others2, key=int))]}."
        )
    elif chooserow == "4":
        print(
            f"The maximum is {max(rent2, key=int)} in {year[rent.index(max(rent2, key=int))]} and minimum is {min(rent2, key=int)} in {year[rent.index(min(rent2, key=int))]}."
        )
    elif chooserow == "5":
        print(
            f"The maximum is {max(royalties2, key=int)} in {year[royalties.index(max(royalties2, key=int))]} and minimum is {min(royalties2, key=int)} in {year[royalties.index(min(royalties2, key=int))]}."
        )
    elif chooserow == "6":
        print(
            f"The maximum is {max(tradinc2, key=int)} in {year[trade_income.index(max(tradinc2, key=int))]} and minimum is {min(tradinc2, key=int)} in {year[trade_income.index(min(tradinc2,key=int))]}."
        )
    else:
        print("Invalid Input.")


def percent30():  # The third function [working]
    print("=" * 40)
    print("Please choose an income type")
    print("1-Dividends")
    print("2-Interest")
    print("3-Other types")
    print("4-Rent")
    print("5-Royalties")
    print("6-Trade income")
    print("=" * 40)

    chooserow2 = input("Please select 1,2,3,4,5 or 6:")
    print(
        "In this category, values that changes by at least 30 percent compared to the previous year are:"
    )
    if chooserow2 == "1":
        for ik in range(1, 11):
            if ((int(dividends[ik])) / (int(dividends[ik - 1]))) * 100 >= 130 or (
                (int(dividends[ik])) / (int(dividends[ik - 1]))
            ) * 100 <= 70:
                print(
                    f"{dividends[ik]} in {year[ik]} from {dividends[ik - 1]} in {year[ik-1]}"
                )
            else:
                continue
    elif chooserow2 == "2":
        for ik in range(1, 11):
            if ((int(interest[ik])) / (int(interest[ik - 1]))) * 100 >= 130 or (
                (int(interest[ik])) / (int(interest[ik - 1]))
            ) * 100 <= 70:
                print(
                    f"{interest[ik]} in {year[ik]} from {interest[ik - 1]} in {year[ik-1]}"
                )
            else:
                continue
    elif chooserow2 == "3":
        for ik in range(1, 11):
            if ((int(others[ik])) / (int(others[ik - 1]))) * 100 >= 130 or (
                (int(others[ik])) / (int(others[ik - 1]))
            ) * 100 <= 70:
                print(
                    f"{others[ik]} in {year[ik]} from {others[ik - 1]} in {year[ik-1]}"
                )
            else:
                continue
    elif chooserow2 == "4":
        for ik in range(1, 11):
            if ((int(rent[ik])) / (int(rent[ik - 1]))) * 100 >= 130 or (
                (int(rent[ik])) / (int(rent[ik - 1]))
            ) * 100 <= 70:
                print(f"{rent[ik]} in {year[ik]} from {rent[ik - 1]} in {year[ik-1]}")
            else:
                continue
    elif chooserow2 == "5":
        for ik in range(1, 11):
            if ((int(royalties[ik])) / (int(royalties[ik - 1]))) * 100 >= 130 or (
                (int(royalties[ik])) / (int(royalties[ik - 1]))
            ) * 100 <= 70:
                print(
                    f"{royalties[ik]} in {year[ik]} from {royalties[ik - 1]} in {year[ik-1]}"
                )
            else:
                continue
    elif chooserow2 == "6":
        for ik in range(1, 11):
            if ((int(trade_income[ik])) / (int(trade_income[ik - 1]))) * 100 >= 130 or (
                (int(trade_income[ik])) / (int(trade_income[ik - 1]))
            ) * 100 <= 70:
                print(
                    f"{trade_income[ik]} in {year[ik]} from {trade_income[ik - 1]} in {year[ik-1]}"
                )
            else:
                continue
    print("There are no more values with such a change.")


def plots():  # The fourth function pt1
    plt.plot(year, dividends, label="Dividends")
    plt.plot(year, trade_income, label="Trade income")
    plt.xlabel("x - axis")
    # naming the y axis
    plt.ylabel("y - axis")
    # giving a title to my graph
    plt.title("Dividends and trade income from 2007 to 2018")

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()


def plots2():  # The fourth function pt2
    barWidth = 0.25
    fig = plt.subplots(figsize=(11, 8))
    br1 = np.arange(len(interest))
    br2 = [x + barWidth for x in br1]
    plt.bar(
        br1, interest, color="r", width=barWidth, edgecolor="grey", label="Interest"
    )
    plt.bar(br2, rent, color="g", width=barWidth, edgecolor="grey", label="Rent")
    plt.xlabel("Years", fontweight="bold", fontsize=15)
    plt.ylabel("X-axis", fontweight="bold", fontsize=15)
    plt.xticks(
        [r + barWidth for r in range(len(interest))],
        [
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
            "2018",
        ],
    )

    plt.legend()
    plt.show()


def graphs():
    print("=" * 40)
    print("Please choose between:")
    print("1-Line Graph of Dividends and Trade income against Time")
    print("2-Bar Graph of Interest and Rent against Time")
    print("=" * 40)

    choice = input("Input:")
    if choice == "1":
        plots()
    elif choice == "2":
        plots2()
    else:
        print("Invalid Input")
