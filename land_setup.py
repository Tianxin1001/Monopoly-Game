# Creating the game board
import random

class Land:
    def __init__(self, position, name):
        # Initialize a Land object with a position and name.
        self.position = position
        self.name = name

    def get_info(self, user):
        # Get information about the land.
        return f'You\'ve landed at position {self.position} - the {self.name}!'

    def get_pos(self):
        # Get the position of the land.
        return int(self.position)


class Card(Land):
    def random_card(self, user):
        # Randomly selects a card and performs the corresponding action.
        cards = ['card1', 'card2', 'card3', 'card4', 'card5', 'card6']
        random_card_name = random.choice(cards)
        method = getattr(self, random_card_name)
        method(user)

    def card1(self, user):
        # Real-world challenge.
        print('You meet a "real-world" challenge!')
        card = input(
            "You accidentally let out an embarrassing snort while laughing during a silent moment. Pay $50 to\n"
            "erase the sound and maintain your composure. Y/N ")
        # When player said yes, the balance will be deducted by 50.
        if card.lower() == "y":
            user.balance -= 50
            print(f'Accident avoided! Your new balance is ${user.balance:.2f}!')
        # When player said no, there will be a result.
        elif card.lower() == "n":
            print("Your crush notices that! ☹︎")
        else:
            # When player inputs is invalid, there will be a warning.
            print("Invalid input! Warning!")

    def card2(self, user):
        print('You meet a code challenge!')
        card = input("What is the output of the following code snippet in Python? Lose $100 if you are wrong.\n"
                     "my_string = 'Hello, World!'\n"
                     "print(my_string[::-1]\n")
        if card == "!dlroW ,olleH":
            user.balance += 100
            print(f'Correct - $100 has been added to your balance! Your new balance is ${user.balance:.2f}!')
        else:
            user.balance -= 100
            print(f'Incorrect - lose $100! Your new balance is ${user.balance:.2f}!')

    def card3(self, user):
        print('You meet a code challenge!')
        card = input("What is the output of the following code snippet in Python? Lose $100 if you are wrong.\n"
                     "print(5 % 2)\n")
        if card == "1":
            user.balance += 100
            print(f'Correct - $100 has been added to your balance! Your new balance is ${user.balance:.2f}!')
        else:
            user.balance -= 100
            print(f'Incorrect - lose $100! Your new balance is ${user.balance:.2f}!')

    def card4(self, user):
        print('You meet a "real-world" challenge!')
        card = input("You accidentally wear a Halloween costume to a formal office meeting. Pay $50 to transform your\n"
                     "attire into professional business wear. Y/N ")
        if card.lower() == "y":
            user.balance -= 50
            print(f'Accident avoided! Your new balance is ${user.balance:.2f}!')
            pass
        elif card.lower() == "n":
            print("Your may need to prepare the interviews! ☹︎")
        else:
            print("Invalid input! Warning!")


    def card5(self, user):
        print('You meet a "real-world" challenge!')
        card = input(
            "You accidentally tag your ex-partner in a photo on social media. Pay $50 to untag it and prevent\n"
            "any awkwardness. Y/N ")
        if card.lower() == "y":
            user.balance -= 50
            print(f'Accident avoided! Your new balance is ${user.balance:.2f}!')
        elif card.lower() == "n":
            print("Your ex-partner post it and keep asking why you cannot forget him! ☹︎")
        else:
            print("Invalid input! Warning!")

    def card6(self, user):
        print('You meet a code challenge!')
        card = input("What is the output of the following code snippet in Python? Lose $100 if you are wrong.\n"
                     "my_list = [1, 2, 3, 4, 5]\n"
                     "print(my_list[1:4])\n")
        if card == "[2, 3, 4]":
            user.balance += 100
            print(f'Correct - $100 has been added to your balance! Your new balance is ${user.balance:.2f}!')
        else:
            user.balance -= 100
            print(f'Incorrect - lose $100! Your new balance is ${user.balance:.2f}!')


class Casino(Land):
    pass


class Jail(Land):
    pass


class Start(Land):
    # Get the reward for landing on the start position.
    def get_reward(self, user, player_funds):
        player_funds += 400
        print(
            f'For landing on go, you get $400!\nCongratulations {user.name}, your updated balance is ${player_funds:.2f}')
        return player_funds
