weight = float(input("Enter your weight "))
unit = input("kilograms or pounds ? (k or l)")

if unit == "k":
    weight *= 2.205
    unit = "lbs."
    print(f"Your weight is : {round( weight,1)}{unit}")
elif unit == "l":
    weight /= 2.205
    unit = "kgs."
    print(f"Your weight is : {round( weight,1)}{unit}")
else:
    print (f"{unit} is not valid")
