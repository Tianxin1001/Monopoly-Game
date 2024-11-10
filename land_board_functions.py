"""
Creating a land function
Parameters
+ Position: int
+ Name: string
+ Sold/unsold: boolean
+ Owner: string
+ Price: int
+ Price per hotel: int
+ Rent: int

Methods:
+ Build house
+ Rent house

Types of land
-Casino
-Jail
-Property
-Card
"""

import random
from collections import Counter
from tabulate import tabulate
from monopoly.land_setup import Land, Card, Casino, Jail, Start


class Property(Land):
    # By default, the properties are unsold, therefore with no owner, rent or houses
    sold = False
    owner = None
    rent = 0
    number_of_houses = 0

    def __init__(self, position, name, type, group, price, price_per_house):
        super().__init__(position, name)
        self.position = position
        self.name = name
        self.type = type
        self.group = group
        self.price = price
        self.price_per_house = price_per_house

    # Booldean function that determines if the user owns a property
    def is_user_owner(self, user):
        if self.owner == user:
            return True
        else:
            return False

    # Outputs information about the property, depending on if it is sold and who the owner is
    def get_info(self, user):
        # Outputting if property is free to buy or not
        if not self.sold:
            status = f'is free to buy and costs {self.price}. \nIt\'s in the {self.group}, of which you currently own {self.get_number_of_houses_user_owns_in_group(user)} of {self.get_number_of_houses_per_group()}'
        else:
            # If the user owns the property, they do not owe rent
            if self.is_user_owner(user):
                status = f'is owned by you!'
            else:
                # If the property is owned by someone else they owe rent
                status = f'is owned by {self.owner.name}. This means you owe ${self.rent:.2f} to {self.owner.name}'
        return f'The property, {self.name}, {status}.'

    # This function checks the property is unsold, asks a user if they would like to buy the property
    # ... checks they can afford it, sets the property as sold and changes the user's balance
    def property_purchase(self, user, player_funds):
        # Function returns False if property is already sold
        # Extra layer of error handling
        if not self.sold:
            while True:
                # Ensures user only inputs y or n
                request = input(f'Would you like to buy {self.name}? Y/N ').upper()
                if request == 'Y':
                    # Checks player funds compared to price of property
                    if self.check_can_they_afford(user, player_funds):
                        # Sets property as sold and returns updated player fund total
                        player_funds = self.set_as_sold(user, player_funds)
                        # Updates user's balance
                        user.balance = player_funds
                        return True
                    else:
                        return False
                elif request == 'N':
                    print('No purchase...')
                    return False
                else:
                    print('Input not recognised - please try again')
                    continue
        else:
            return False

    # This function checks if the user has enough funds to buy the property
    def check_can_they_afford(self, user, player_funds):
        if player_funds >= self.price:
            return True
        else:
            print('Insufficient funds!')
            return False

    # This function checks if the user has enough funds to buy the house upgrade
    def check_can_they_afford_house(self, user, player_funds):
        if player_funds >= self.price_per_house:
            return True
        else:
            return False

    # This function sets the property as sold by changing the boolean value, creating a rent price,
    # ..., changing the owner and taking the property price away from the user's balance
    # It returns the updated player fund variable (float)
    def set_as_sold(self, owner, player_funds):
        self.sold = True
        self.rent = 0.10 * self.price
        self.owner = owner
        player_funds -= self.price
        print(
            f'Purchase successful! You have purchased {self.name} for {self.price}\nYou\'re remaining balance is ${player_funds:.2f}.\n')
        return player_funds


    # This sets an additional house upgrade to a property, checking they can afford it, upping the rent
    # Adding a house to the property number_of_houses variable and taking the house price away from the user's balance
    # It returns the updated player fund variable (float)
    def set_additional_house(self, user, player_funds):
        if self.check_can_they_afford_house(user, player_funds):
            self.rent += 0.10 * self.price_per_house
            self.number_of_houses += 1
            player_funds -= self.price_per_house
        return player_funds


    def get_number_of_houses_per_group(self):
        # Count how many houses in each group (dictionary)
        groups = dict(Counter([item.group for item in Board if type(item) == Property]))
        if self.group in groups:
            return groups[self.group]
        else:
            return 0


    def get_number_of_houses_user_owns_in_group(self, user):
        # Examine the owners for the group
        owners_for_group = [item.owner for item in Board if type(item) == Property and item.group == self.group]
        # Count how many times user appears
        return owners_for_group.count(user)

    def check_upgrade_eligibility(self, user):
        group_counter = self.get_number_of_houses_per_group()
        owners_for_group = self.get_number_of_houses_user_owns_in_group(user)
        # If the owner's count is the same as the number of houses then they own all the houses in the group
        if owners_for_group != group_counter:
            print(
                f'To upgrade {self.name}, you need to own all the properties in {self.group}\nYou currently own {owners_for_group} of the necessary {group_counter} properties in {self.group}!')
            return False
        else:
            print('You are eligible to buy houses for your property')
            return True


def get_users_houses(user):
    # Examine the properties for the owner
    properties_for_owner = [item.name for item in Board if type(item) == Property and item.owner == user]
    return properties_for_owner

# This function encompasses the get_users_houses, check_upgrade_eligibility, and check_they_can_afford_house functions
# As well as setting the extra hosue
def upgrading_a_house(user, player_funds):
    # Gathering a list of the user's currently owned properties
    users_houses = get_users_houses(user)
    # Exits if user owns nothing
    if len(users_houses) == 0:
        print('You don\'t own any properties yet...')
        return False
    else:
        # Outputs props
        print('You own these properties: ')
        for index, item in enumerate(users_houses):
            print(f'{index} - {item}')
        while True:
            try:
                # Requests user which property they'd like to upgrade
                property_to_update = int(input(
                    'Which property would you like to upgrade? Enter the number or enter -1 if you don\'t want to upgrade any:\n'))
                # Allowing exit option
                if property_to_update == -1:
                    print('No upgraded property... ')
                    return False
                # If they choose a valid property
                elif property_to_update in range(len(users_houses)):
                    # Check upgrade eligibility
                    chosen_property = users_houses[property_to_update]
                    # Need to find the chosen property in the board list
                    print(f'The property you want to upgrade is {chosen_property}')
                    #  Searches through Board for the property
                    for item in Board:
                        if item.name == chosen_property:
                            chosen_property = item
                    # Checks user owns all the properties in the group
                    if chosen_property.check_upgrade_eligibility(user):
                        # Sets the additional house and returns updated player funds
                        player_funds = chosen_property.set_additional_house(user, player_funds)
                        user.balance = player_funds
                        # Outputs confirmation message to user
                        print('House purchased!')
                        return True
                    else:
                        return False
                # Re-requests input
                else:
                    print('Input not in numbered list - please try again')
                    continue
            except:
                print('Invalid input - please enter a number from the list, or -1 for none')
                continue


# Resetting the board to its original front-end grid
def reset_board():
    game = []
    for j in range(5):
        col = []
        # First and last row of the board
        if j == 0:
            col = ['JAIL', 'CASINO', 'MOVIE STREAMING', 'MUSIC STREAMING', 'CHANCE CARD', 'AUDIOBOOKS', 'CHANCE CARD']
        elif j == 4:
            col = ['JAIL', 'POLITICAL NEWS', 'CHANCE CARD', 'ENTERTAINMENT NEWS', 'CASINO', 'FINANCIAL NEWS', 'START']
        # Central rows of the board
        else:
            for i in range(7):
                # Left and right columns of the board
                if i == 0 and j == 1:
                    col.append('DATING APP')
                elif i == 0 and j == 2:
                    col.append('CHANCE CARD')
                elif i == 0 and j == 3:
                    col.append('SOCIAL MEDIA APP')
                elif i == 6 and j == 1:
                    col.append('CHANCE CARD')
                elif i == 6 and j == 2:
                    col.append('RECIPE SITE')
                elif i == 6 and j == 3:
                    col.append('FITNESS SITE')
                # Central columns of the board
                else:
                    col.append(' ')
        game.append(col)
    return game

# Printing the game board with their position on it using the tabulate module
def show_player_position(position):
    game = reset_board()
    print(f'You are here:')
    # Even though the moving_around_the_board function does this check
    # We add an extra layer of error handling
    if position >= 20:
        position = position % 20
    # Showing the user's position dependent on which line of the square they are in
    # First 'road' of the board
    if position <= 4:
        game[4 - position][6] = '\033[93m★\033[0m'
        print(tabulate(game, tablefmt="pretty"))
    # Second 'road' of the board
    elif 4 < position <= 10:
        game[0][10 - position] = '\033[93m★\033[0m'
        print(tabulate(game, tablefmt="pretty"))
    # Third 'road' of the board
    elif 10 < position <= 14:
        game[position - 10][0] ='\033[93m★\033[0m'
        print(tabulate(game, tablefmt="pretty"))
        reset_board()
    # Fourth 'road' of the board
    elif 14 < position <= 19:
        game[4][position - 14] = '\033[93m★\033[0m'
        print(tabulate(game, tablefmt="pretty"))
        reset_board()


# Rolling the dice and outputting the user's new position
def dice_roll():
    dice_roll_val = (random.randint(1, 6), random.randint(1, 6))
    print(f'You\'ve rolled a {dice_roll_val[0]} and a {dice_roll_val[1]} - move {sum(dice_roll_val)} squares!')
    return dice_roll_val

# This function returns the user's final position, checking that if their new total is over 20
# then they are restarting the board and gaining $200 for passing go
def moving_around_the_board(user, initial_position, dice_roll_val):
    if (initial_position + sum(dice_roll_val)) > 20:
        user.passes_go()
    final_position = (initial_position + sum(dice_roll_val)) % 20
    show_player_position(final_position)
    print(Board[final_position].get_info(user))
    user.position = final_position
    return final_position


# Initialising the board
Start0 = Start(position=0, name='Start square')
Prop1 = Property(position=1, name='FITNESS SITE', type='Property', group='Websites', price=100, price_per_house=50)
Prop2 = Property(position=2, name='RECIPE SITE', type='Property', group='Websites', price=100, price_per_house=50)
Card1 = Card(position=3, name='CHANCE CARD')
Card2 = Card(position=4, name='CHANCE CARD')
Prop3 = Property(position=5, name='MUSIC STREAMING', type='Property', group='Streaming Services', price=200, price_per_house=100)
Card3 = Card(position=6, name='CHANCE CARD')
Prop4 = Property(position=7, name='MOVIE STREAMING', type='Property', group='Streaming Services', price=200, price_per_house=100)
Prop5 = Property(position=8, name='AUDIOBOOKS', type='Property', group='Streaming Services', price=200, price_per_house=100)
Casino1 = Casino(position=9, name='Casino')
Jail1 = Jail(position=10, name='Jail')
Prop6 = Property(position=11, name='DATING APP', type='Property', group='Apps/Platforms', price=300, price_per_house=150)
Card4 = Card(position=12, name='CHANCE CARD')
Prop7 = Property(position=13, name='SOCIAL MEDIA APP', type='Property', group='Apps/Platforms', price=300, price_per_house=150)
Jail2 = Jail(position=14, name='Jail')
Prop8 = Property(position=15, name='POLITICAL NEWS', type='Property', group='Media Outlets', price=400, price_per_house=200)
Card5 = Card(position=16, name='CHANCE CARD')
Prop9 = Property(position=17, name='ENTERTAINMENT NEWS', type='Property', group='Media Outlets', price=400, price_per_house=200)
Casino2 = Casino(position=18, name='Casino')
Prop10 = Property(position=19, name='FINANCIAL NEWS', type='Property', group='Media Outlets', price=400, price_per_house=200)

Board = [Start0, Prop1, Prop2, Card1, Card2, Prop3, Card3, Prop4, Prop5, Casino1, Jail1, Prop6, Card4, Prop7, Jail2,
         Prop8,
         Card5, Prop9, Casino2, Prop10]
