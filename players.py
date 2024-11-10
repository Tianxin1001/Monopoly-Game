'''Player functions'''
# code to create player class with relevant attributes and methods for gameplay

import random
class Player:
    def __init__(self, name, position, balance, round, jail_counter) -> None:
        self.name = name #player name
        self.position = position #position on the board
        self.balance = balance #balance of money that player has
        self.round = round #how many rounds have been played by this player
        self.jail_counter = jail_counter #count the number of consecutive turns that the player has spent in jail

    #track how many rounds the player has played by adding one
    def round_record(self):
        self.round += 1

    #return the current balance of the player
    def get_balance(self):
        return self.balance

    def visit_jail(self):
        """Handles the actions when the player visits the jail."""
        if self.jail_counter >= 3:
            print("Congratulations! You are released from jail.")
            self.jail_counter = 0  # Reset the jail counter
        else:
            print("You are in jail.")
            while True:
                choice = input("Do you want to pay $50 to get out of jail? Y/N: ")
                if choice.lower() == 'y' or choice.lower() == 'n':
                    break
                else:
                    print('Please enter y or n only!')
                    continue
            if choice.lower() == 'y':
                self.balance -= 50
                self.jail_counter = 0  # Reset the jail counter
                print("You paid $50 and are released from jail.")
            else:
                dice_roll = (random.randint(1, 6), random.randint(1, 6))
                print(f'You\'ve rolled a {dice_roll[0]} and a {dice_roll[1]}!')
                if dice_roll[0] == dice_roll[1]:
                    self.jail_counter = 0  # Reset the jail counter
                    print("Congratulations! You rolled a double and are released from jail.")
                else:
                    self.jail_counter += 1  # Increment the jail counter
                    print("You didn't roll a double. You are still in jail.")

    #when the player passes go, $200 is added to their balance
    def passes_go(self):
        print('Pass go - collect $200!')
        self.balance += 200
