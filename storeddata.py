machine_data = [
    [1, 30.5, 110, 23.5, 1],
    [1, 30.8, 100, 24.5, 2],
    [1, 31.6, 121, 23.9, 3],
    [1, 39.5, 123, 26.3, 4],
    [1, 34.1, 120, 27.5, 5],
]
temperature = []
pressure = []
vibration = []
for row in machine_data:
    print(row)
    temperature.append(row[1])
    pressure.append(row[2])
    vibration.append(row[3])

print("temperature list is", temperature)
print("pressure list is", pressure)
print("vibration list is", vibration)
