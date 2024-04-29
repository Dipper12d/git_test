for cx in range(10, -1, -1):
    if cx == 10:
        print(cx, "activate main engine hydrogen burnoff system")
    elif cx == 6:
        print(cx, "main engine start")
    elif cx == 0:
        print(cx, "solid rocket booster ignition and liftoff")

    else:
        print(f"{cx}")
else:
    print("\nHouston all systems go. Over to you.")
