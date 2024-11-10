# This is what a player would see on their go
from land_board_functions import upgrading_a_house, moving_around_the_board, Property, Card, Casino, Jail, Start, dice_roll
from casinofn import play_casino

def menu_options(Board, user, initial_position, player_funds, rounds):
    # If the user is in the jail positions, and their jail_counter is not initialised (hence within 1,2,3)
    if (user.position == 10 or user.position == 14) and user.jail_counter != 0:
        user.visit_jail()
        print('\n*************** Turn over! Next player\'s turn ***************')
    else:
        # If the user is not in jail
        while True:
            try:
                # Outputting round number and balance to user
                print(f'Round {user.round} of {rounds}!')
                print(f'Now your balance is ${user.balance:.2f}.')
                # Player is able to pick a property to upgrade before they roll
                option = input('Would you like to\n1 - Upgrade a property\n2 - Roll\n')
                if int(option) == 1:
                    # Upgrading a property option
                    upgrading_a_house(user, player_funds)
                    continue
                # Dice rolling option
                elif int(option) == 2:
                    dice_roll_val = dice_roll()
                    # Moves around board and outputs information, as well as front-end board grid
                    landed_on = Board[moving_around_the_board(user, initial_position, dice_roll_val)]
                    if type(landed_on) == Property:
                        if not landed_on.sold:
                            #  Request user if they'd like to purchase property
                            landed_on.property_purchase(user, player_funds)
                        # If property is sold and they do not own it
                        elif not landed_on.is_user_owner(user):
                            print(f'You must pay ${landed_on.rent:.2f} rent')
                            # Decreases user's balance and increases owners balance by rent amount
                            user.balance -= landed_on.rent
                            landed_on.owner.balance += landed_on.rent
                            # Confirmation message to user
                            print(f'${landed_on.rent:.2f} has been sent from {user.name} to {landed_on.owner.name}!')
                    # Calls card functions
                    elif type(landed_on) == Card:
                        landed_on.random_card(user)

                    # Calls casino functions
                    # Updates user balance
                    elif type(landed_on) == Casino:
                        outcome = play_casino(player_funds)
                        user.balance += outcome

                    # Calls jail function
                    elif type(landed_on) == Jail:
                        user.visit_jail()

                    # Call Start function
                    elif type(landed_on) == Start:
                        player_funds = landed_on.get_reward(user, player_funds)
                        user.balance = player_funds

                    print('\n*************** Turn over! Next player\'s turn ***************')

                    break
                else:
                    print('Invalid option - please try again!')
            except:
                print('Invalid option - please try again!')
                continue