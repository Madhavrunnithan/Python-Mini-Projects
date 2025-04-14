import random
dicelist = {
    1: [
        "-------------",
        "|           |",
        "|     0     |",
        "|           |",
        "-------------"
    ],
    2: [
        "-------------",
        "|         0 |",
        "|           |",
        "| 0         |",
        "-------------"
    ],
    3: [
        "-------------",
        "|         0 |",
        "|     0     |",
        "| 0         |",
        "-------------"
    ],
    4: [
        "-------------",
        "| 0       0 |",
        "|           |",
        "| 0       0 |",
        "-------------"
    ],
    5: [
        "-------------",
        "| 0       0 |",
        "|     0     |",
        "| 0       0 |",
        "-------------"
    ],
    6: [
        "-------------",
        "| 0       0 |",
        "| 0       0 |",
        "| 0       0 |",
        "-------------"
    ]}
def dice_roll():
    roll = random.randint(1,6)
    return roll

while(1):
    n = int(input("Enter the no.of rolls (press 0 to exit) : "))
    if n == 0:
        break
    else:
        rolllist = []
        for i in range(n):
            roll = dice_roll()
            rolllist.append(roll)
        print("You've Rolled : ")
        lines = [dicelist.get(r) for r in rolllist]
        for i in range(5):
            print("   ".join(face[i] for face in lines))
        rolllist.clear()
