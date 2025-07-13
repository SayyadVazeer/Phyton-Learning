import threading
import time


def walk_dog(first , second):
    time.sleep(8)
    print(f"Walk Donee with {first} and {second}")
def clean():
    time.sleep(4)
    print("Cleaan done")


chore1 = threading.Thread(target=walk_dog,args=("Pinky","Bannu"))
chore2 = threading.Thread(target=clean)
chore1.start()
chore2.start()

chore1.join()
chore2.join()
print("ALL DOne !")
