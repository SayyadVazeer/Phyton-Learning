principle = 0.0
rate = 0.0
time = 0

while principle <= 0:
    principle = float(input("Please enter the principle ammount :"))
    if principle <= 0:
        print ("Enter Valid amount: ")

while True:
    rate = float(input("Please enter the rate ammount :"))
    if rate <0:
        print ("Enter Valid amount: ")
    else:
        break

while time <= 0:
    time = int(input("please choose the time of inverstment :"))
    if time <=0:
        print("Time should be in years and more then 0")

total = principle* pow(1+(rate /100),time)

print(f"You will earn {total} after {time} years")