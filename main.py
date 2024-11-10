from record_score import insert_new_record, get_all_records
from players import Player
from menu_options import menu_options
from land_board_functions import Board

# Print all the names of the highest score
def get_winner(players):
    players.sort(key=lambda x: x.balance)
    highest_score = players[-1].balance
    winners = [player.name for player in players if player.balance == highest_score]
    print("The winners are:")
    for winner in winners:
        print(winner + "!!!")


# welcome page which include asking the number of the players and the rounds
def main_function():
    print("Welcome to the game!")

    while True:
        try:
            num_player = int(input("How many people are playing? "))
            if num_player <= 0:
                print('Must be an integer above 0!')
                continue
            break
        except ValueError:
            print('Must be an integer!')
            continue

    players = []

    for n in range(num_player):
        player_name = input(f"What is the name of Player {n + 1}? ")
        players.append(Player(name=player_name, position=0, balance=1000, round=1, jail_counter=0))

    while True:
        try:
            rounds = int(input('How many rounds would you like to play? '))
            if rounds < 0:
                print('You must play more than 0 rounds!')
                continue
            break
        except:
            print('The number of rounds must be an integer!')
            continue

    round_counter = 1
    while round_counter <= rounds:
        for user in players:
            print(f'\nPlayer name: {user.name}')
            menu_options(Board, user, user.position, user.balance, rounds)
            user.round_record()  # This adds one to the user's records
            # print(f'User balance: {user.balance:.2f}')
        round_counter += 1
    # The end of the game will show the winner, save the records and get all the history records from database
    print('The game is over! ')
    get_winner(players)
    print("Connected to DB: players_history_result")
    # save player's name and balance and insert them into the database
    for player in players:
        new_player = {
            "player_name": player.name,
            "score": player.balance
        }
        insert_new_record(new_player)
    print("Record added to DB")
    print("DB Connection is closed")
    get_all_records(players)


if __name__ == '__main__':
    main_function()