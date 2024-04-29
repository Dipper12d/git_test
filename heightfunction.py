def getheight(V, G, T):
    height = abs(V * T - 0.5 * G * T**2)
    print(f"The height of the building is {height:.2f} meters")


Bheight = getheight(4, 9.81, 3)

# print(f"The height of the building is {Bheight:.2f} meters")
