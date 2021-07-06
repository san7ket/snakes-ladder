

DICE_SIZE = 6
Board_Size = 100

snakes = {
    14:7,
    23 :17,
    45: 5,
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
    return player_name, crookedness

if __name__ == '__main__':
    setup_game()