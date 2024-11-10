# CODEnopoly: an interactive Python and SQL-based project
## Description
Monopoly, a beloved board game, has been entertaining players for decades with its strategic gameplay and economic simulation. The game revolves around players buying and trading properties, aiming to accumulate wealth and bankrupt their opponents. Understanding the rules and logic of the game is crucial in developing an interactive and engaging digital adaptation.

In our project, we have incorporated the core rules of Monopoly into our game's design. Each player takes turns rolling the dice, moving their token around the board, and landing on various squares. One of the key aspects is the property squares, where players have the option to purchase the property they land on. By acquiring properties, players can collect rent from opponents who land on their owned properties, gradually building their wealth.

Furthermore, our game adheres to the rule associated with the Start square. Whenever a player passes or lands on the Start square, they receive a specific amount of money, which is added to their account balance. This additional income provides players with a financial boost as they progress through the game.

By implementing these fundamental rules, our game aims to recreate the strategic decision-making, negotiation, and economic aspects of the original Monopoly. We have taken care to ensure that players can experience the thrill and excitement of the traditional game while introducing customization options to enhance their gameplay experience.


## Visuals
When the main.py file is run, the opening message on the Console should be:
"Welcome to the game!
How many people are playing?"

Users are then instructed to enter any further inputs into the Console.

## Installation
User needs to install tabulate and prettytable modules before they can run code. In addition, MySQL Workbench needs to be open for the final high score database to connect to the system. Users are instructed to enter their MySQl password into the config.py file

Depending on your IDE, we have used Pycharm CE as an example, the steps are as follows:
1 - Navigate to 'Python Packages' in the bottom toolbar of Pycharm
2 - Search the necessary packages (Tabulate and prettytable in this instance)
3 - Click 'Install Package' on right hand side of lower toolbar
Note you may need to restart Pycharm for these modules to run

## Usage
1 - The config.py include the database information, please change the password into your own password.

2 - The players_history_result.sql is the history record database and table, please run this in SQL first to build database.

3 - Users are instructed to run the main.py file to run the CODEnopoly program!


## File Breakdown
MONOPOLY FOLDER
+ casinofn.py - defines casino functions
+ config.py - includes the database information, please change the password into your own password.
+ land_board_functions.py - includes methods for the sub-class Property & functions for the board layouts
+ land_setup.py - defines the classes for all squares on the board. Defines Land, Card and Start functions
+ main.py - where the main program should be ran - includes functions for returning the winner, as well as code for the start and end of the game
+ menu_options.py - defines the menu option function that compiles all objects methods - this is called every time a user has their turn
+ players.py - all methods for the class Player
+ players_history_result.sql - history record database and table, please run this in SQL first to build database
+ record_score.py - establishes a connection to the MySQL database and defines associated functions, include inserting new records and getting all records.

TEST FILES FOLDER
+ test_card.py
+ test_casinofn.py
+ test_jail.py
+ test_land_board_functions.py
+ test_land_setup.py
+ test_players.py

## Support
For support please contact Sarah Carlotti, Kadidiatou Wague, Tianxin Dong or Sophie Ross.

## Roadmap
Ideas for future releases include:
+ HTML/CSS front-end interface
+ Computerised/automated opponents
+ More colourful board
+ Line by line console output

## Authors and acknowledgment
Thanks to CFG instructors for supporting us throughout this project!
