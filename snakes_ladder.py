import random


class snakesladder:
    """Snakes and ladder class"""

    def __init__(self, snakes, ladder):
        """Initilize the game with snakes and ladder mapping"""
        self.snakes = snakes
        self.ladder = ladder
        crooked = False
        self.player_name = input("***Enter your name***\n")
        self.crooked = input("Run with a crooked dice. Y/N\n") or False
        if self.crooked == "Y":
            crooked = True
        print("Welcome to Snakes And Ladders {0}".format(self.player_name))
        self.run(crooked)

    def dice_roll(self, crooked):
        """Returns the rolled dice. Crooked or normal

        :return int roll_dice : Face of currently rolled dice.
        """
        if crooked is True:
            roll_dice = random.choice([2, 4, 6])
        else:
            roll_dice = random.randint(1, 6)
        return roll_dice

    def check_snake(self, pos):
        """Checks if the current position have a snake and returns to tail

        :return int pos : if snake is detected, returns the tail position or remains the same
        """
        if pos in self.snakes.keys():
            pos = self.snakes.get(pos)
            print("Looks like we hit a snake uhhh...Moving to tail")
            print("Current Position:{0}".format(pos))
        return pos

    def check_ladder(self, pos):
        """Checks if the current position have a snake and returns to tail

        :return int pos : if ladder is detected, returns the top position or remains the same
        """
        if pos in self.ladder.keys():
            pos = self.ladder.get(pos)
            print("I hate stairs, but it's a shortcut. Taking a shortcut..")
            print("Current Position:{0}".format(pos))
        return pos

    def check_status(self, pos, turn):
        """Checks if the game has been won

        :param pos : Current position of the player
        :param turn: Current turn the player is at
        :return boolean : if player wins returns true
        """
        if pos >= 100:
            print(f"You win on {turn} turns. Congratulations")
            return True

    def run(self, crooked):
        """Contains the core game logic and the turns the players plays until loss or win

        :param crooked: if set, returns only even numbers on dice roll
        """
        pos = 1
        for i in range(1, 10):
            print(f"Current turn {i}")
            dice = self.dice_roll(crooked)
            print("Excellent roll, moving by {0} position".format(dice))
            pos = pos + dice
            print("Current Position:{0}".format(pos))
            final_pos = self.check_ladder(pos)
            final_pos = self.check_snake(pos)
            pos = final_pos
            print("\n")
            if self.check_status(pos, i):
                exit()
        return pos


if __name__ == "__main__":
    # Snakes dict, maps snakes head to tail
    snakes = {14: 7, 23: 17, 45: 5, 51: 33, 99: 24}
    # ladder dict, maps to bottom to top of a ladder
    ladder = {8: 29, 22: 61, 54: 68, 66: 97, 72: 93}
    # Creates the object and starts the game
    snakesladder = snakesladder(snakes, ladder)
