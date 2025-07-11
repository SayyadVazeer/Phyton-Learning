import time

mytime = int(input("Enter the time in seconds : "))


#for x in reversed(range(0,mytime)):
for x in range(mytime,0, -1):
    hour = int(x/3600)
    minu = int(x/60) % 60
    sece = x % 60
    print(f"{hour:02}:{minu:02}:{sece:02}")
    time.sleep(1)

print("Times Up! ")