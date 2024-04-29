import csv

datarows = []
datarows_f = []
temperature = []
pressure = []
vibration = []
# open and read csv file
openfile = open("mdata.csv")
csvreader = csv.reader(openfile)
next(csvreader)  # skip title row
# append row in the list
for row in csvreader:
    print("Current row : ", row)  # row is a list
    datarows.append(row)
    temperature.append(float(row[1]))  # Why not [0]?
    pressure.append(float(row[2]))
    vibration.append(float(row[3]))
    # another approach to create the 2D list where each element is a float
    row_f = [float(i) for i in row]
    datarows_f.append(row_f)
print("Temperature list is ", temperature)
print("Pressure list is ", pressure)
print("Vibration list is ", vibration)
