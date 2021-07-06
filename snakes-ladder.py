import random

snakes = {
    14: 7,
    23: 17,
    45: 5,
    51: 33,
    99: 24
}

ladder = {
    8: 29,
    22: 61,
    54: 68,
    66: 97,
    72: 93
}


def setup_game():
    """Setting up various variables in game.

    :returns str player_name : Name of the player
    """
    player_name = input("***Enter your name***\n")
    crooked = input("Run with a crooked dice. Y/N\n")
    if crooked == 'Y':
        crooked = True
    print("Welcome to Snakes And Ladders {0}".format(player_name))
    run(crooked)
    return player_name


def dice_roll(crooked=True):
    """Returns the rolled dice. Crooked or normal

    :return int roll_dice : Face of currently rolled dice.
    """
    if crooked:
        roll_dice = random.choice([2, 4, 6])
    else:
        roll_dice = random.randint(1, 6)
    return roll_dice


def check_snake(pos):
    """Checks if the current position have a snake and returns to tail

    :return int pos : if snake is detected, returns the tail position or remains the same
    """
    if pos in snakes.keys():
        pos = snakes.get(pos)
        print("Looks like we hit a snake uhhh...Moving to tail")
        print("Current Position:{0}".format(pos))
    return pos


def check_ladder(pos):
    """Checks if the current position have a snake and returns to tail

    :return int pos : if ladder is detected, returns the top position or remains the same
    """
    if pos in ladder.keys():
        pos = ladder.get(pos)
        print("I hate stairs, but it's a shortcut. Taking a shortcut..")
        print("Current Position:{0}".format(pos))
    return pos


def run(crooked):
    """Contains the core game logic and the turns the players plays until loss or win

    :param crooked: if set, returns only even numbers on dice roll
    """
    pos = 1
    for i in range(1, 10):
        print(f"Current turn {i}")
        dice = dice_roll(crooked)
        print("Excellent roll, moving by {0} position".format(dice))
        pos = pos + dice
        print("Current Position:{0}".format(pos))
        final_pos = check_ladder(pos)
        final_pos = check_snake(pos)
        pos = final_pos
        print("\n")
        if pos >= 100:
            print(f"You win on {i} turns. Congratulations")
            exit(1)
    print("You Lose")


if __name__ == '__main__':
    setup_game()
