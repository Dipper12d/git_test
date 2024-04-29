price=float(input("Please enter in the price:$"))
weight=float(input("Please enter in the weight in kg:"))
if weight<=20:
    ship_cost=(weight*2.5)
elif weight>20 and weight<50:
    ship_cost=(20.0*2.50)+(weight-20)*1.75
else:
    ship_cost=weight*2.15
Total=ship_cost+price
price2="{:.2f}".format(price)
ship_cost2="{:.2f}".format(ship_cost)
Total2="{:.2f}".format(Total)
weight2="{:.2f}".format(weight)
print(f"Product cost:${price2}")
print(f"Product weight:{weight2}kg")
print(f"Shipping cost:${ship_cost2}")
print(f"Total cost:${Total2}")