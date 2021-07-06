import random

snakes = {
    14:7,
    23:17,
    45:5,
    51:33,
    99:24
}

ladder = {
    8:29,
    22:61,
    54:68,
    66:97,
    72:93
}

def setup_game():
    player_name = input("***Enter your name***\n")
    crookedness = input("Enter crookedness percentage\n")

    print("Welcome to Snakes And Ladders {0}".format(player_name))
    return player_name, crookedness


def check(pos):
    if pos in snakes.keys():
        pos = snakes.get(pos)
    if pos in ladder.keys():
        pos = ladder.get(pos)
    return pos

def run():
    pos = 1
    for i in range(1000):
        roll_dice = random.randint(1, 6)
        roll_crooked = random.choice([2,4,6])
        print("Excellent roll, moving by {0} position".format(roll_dice))
        pos = pos + roll_dice
        final_pos = check(pos)
        if final_pos < pos:
            print("Looks like we hit a snake uhhh...Moving to tail")
        elif final_pos > pos:
            print("I hate stairs, but it's a shortcut. Taking a shortcut..")
        pos = final_pos
        print("Current Position:{0}".format(pos))
        if pos >= 100:
            print("You win. Congratulations")
            exit(1)
    print("You Lose")

if __name__ == '__main__':
    run()