import random

sv = {
     1:("1:1","1:2", "1:3", "1:4", "1:5"), 2:("2:1","2:2", "2:3", "2:4", "2:5"),3:("3:1","3:2", "3:3", "3:4", "3:5"),4:("4:1","4:2", "4:3", "4:4", "4:5"),5:("5:1","5:2", "5:3", "5:4", "5:5"),6:("6:1","6:2", "6:3", "6:4", "6:5")
}
dice_art ={
1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘"
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘"
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘"
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘"
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘"
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘"
    )
}

dice =[]
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))


# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#             print(line)
# print(dice)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print("")
 
for die in dice:
    total += die

print(f"Total: {total}")