'''3: Casino: User can play three times of Sic Bo if they step into the casino.
There are two types of ways. User can bid for either large (4-6) or small (1-3) before the dice is rolled.
If they win, they can receive a reward which is three times the money they bid for. User can also bid for
the exact number of dice rolled. If user win, they can receive a reward which is ten times the money they bid for.
User can leave whenever they want.'''

import random

# The requesting function is the main error handling function
def request_valid_bid(player_funds):
    while True:
        try:
            amount_to_bet = float(input('How much would you like to bet, or enter -1 to exit:\n'))
            # If a user tries to bet a negative amount they are requested a new input
            if amount_to_bet == -1:
                return None
            if amount_to_bet < 0:
                print('Must be a valid $ amount above 0, or -1 to exit')
                continue
            # If the user tries to bet more than they own they are requested a new input
            if amount_to_bet > player_funds:
                print('You cannot bet more than you have!')
                continue
            return amount_to_bet
        # If a user inputs a value that is not a float they are requested again
        except ValueError:
            print('Must be a valid $ amount')
            continue


def get_bid_amount(amount_to_bet):
    # Even though the request_valid_bid handles most of the errors
    # This if statement adds an extra layer of error handling incase it fails
    if type(amount_to_bet) != int and type(amount_to_bet) != float:
        return None
    if amount_to_bet == -1 or amount_to_bet < 0: #This function has an extra layer of error handling
        return None
    else:
        return amount_to_bet


def high_or_low():
    while True:
        # Initialises list of dice options incase user inputs the exact number
        dice_options = [int(i) for i in range(1, 7)]
        try:
            high_or_low_opt = input('Would you like to bet on small, large, or an exact number? Enter 1-3, 4-6 or the '
                                'exact number:')
            # Creates a list of 1-3 or 4-6 depending on what user inputs
            # Returns list of integers
            if high_or_low_opt == '1-3':
                choice = [int(i) for i in range(1, 4)]
                return choice
            elif high_or_low_opt == '4-6':
                choice = [int(i) for i in range(4, 7)]
                return choice
            elif int(high_or_low_opt) in dice_options:
                choice = int(high_or_low_opt)
                return choice
        # If user inputs something other than 1-3, 4-6 or a number on the dice
        # They are asked for a new input
        except:
            print('Invalid option - please try again')
            continue


# This function determines what the numerical outcome is
def casino_outcome(dice_roll, choice, amount_to_bet):
    # If the user has chosen an exact number
    if type(choice) == int:
        # And they are correct, they win 10 * their bet
        if choice == dice_roll:
            outcome = 10 * amount_to_bet
        # If they are wrong they lose their bet
        else:
            outcome = -1 * amount_to_bet
    # If the user has inputted a range
    elif dice_roll in choice:
        # They win 3 * their bet
        outcome = 3 * float(amount_to_bet)
    else:
        # If they are wrong they lose their bet
        outcome = -1 * amount_to_bet
    # The amount is returned
    return outcome

# This function encompasses the prior functions, including the rules and print statements
# It outputs the affect on the player's funds
def play_casino(player_funds):
    # Printing rules
    print(
        '\t\t\tRules\nYou can bid for either large (4-6) or small (1-3) before the dice is rolled.\nIf you win, you receive a reward which is three times the money you bid for.\nYou can also bid for the exact number on the rolled dice. If you win, you receive a reward ten times the amount you bid for.')
    amount_to_bet = get_bid_amount(request_valid_bid(player_funds))
    # If they have chosen not to bet anything, 0 is returned
    # Otherwise, they are asked to choose a number/range
    if amount_to_bet is not None:
        choice = high_or_low()
        # Dice roll (note this only uses 1 dice so we couldn't reuse the dice_roll() function)
        print('...dice rolling...')
        dice_roll = int(random.randint(1, 6))
        print(f'You\'ve rolled a {dice_roll}!')
        # Calculating outcome
        outcome = casino_outcome(dice_roll,choice,amount_to_bet)
        # If outcome is +ve, a congratulations message is outputted
        if outcome > 0:
            print(f'Congratulations - you\'ve won ${abs(outcome):.2f}!')
        # Otherwise a sorry message is outputted
        if outcome < 0:
            print(f'Sorry - you lose ${abs(outcome):.2f}!')
        return outcome
    else:
        return 0



