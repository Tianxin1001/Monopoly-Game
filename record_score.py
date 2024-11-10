import mysql.connector
from config import USER, PASSWORD, HOST
from prettytable import PrettyTable
from colorama import Fore, Style
import datetime


class DBConnectionError(Exception):
    pass


# Establishes a connection to the MySQL database
def connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password",
        database=db_name
    )
    return cnx


# Retrieves all records from the database and displays them in a pretty table
def get_all_records(players):
    try:
        db_name = "players_history_result"
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: {}".format(db_name))

        query = """SELECT * FROM players_history_result ORDER BY score DESC"""
        cur.execute(query)
        result = cur.fetchall()
        column_names = [column[0] for column in cur.description]
        table = PrettyTable(column_names)

        current_run_data = None
        for i, record in enumerate(result):
            if record[0] in [player.name for player in players]:
                # Highlight the record of the player with green color
                record_color = Fore.GREEN
                current_run_data = i
            else:
                record_color = ""

            formatted_player = [f"{record_color}{value}{Style.RESET_ALL}" for value in record]
            table.add_row(formatted_player)
        num_rows = len(table._rows)
        rank_values = [
            f"{Fore.GREEN}{i + 1}{Style.RESET_ALL}" if result[i][0] in [player.name for player in players] else i + 1
            for i in range(num_rows)]
        table.add_column("Rank", rank_values)
        table.border = True
        table.header_style = "upper"
        table.align = "l"

        for i, row in enumerate(table._rows):
            if i == current_run_data:
                # Highlight the cells of the current run data with green color
                for j, value in enumerate(row):
                    if j == 0:
                        table._rows[i][j] = f"{Fore.GREEN}{value}{Style.RESET_ALL}"
                    else:
                        table._rows[i][j] = f"{Fore.GREEN}{value}{Style.RESET_ALL}"
            else:
                # Leave other cells as is
                for j, value in enumerate(row):
                    if j == 0:
                        table._rows[i][j] = f"{value}"
                    else:
                        table._rows[i][j] = f"{value}"

        print(table)
        cur.close()
    except Exception:
        raise DBConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB Connection is closed")


# Inserts a new record into the database
def insert_new_record(new_player):
    try:
        db_name = "players_history_result"
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        query = """INSERT INTO players_history_result (PLAYER_NAME, DATE, SCORE) VALUES ('{}','{}','{}')""".format(
            new_player["player_name"],
            formatted_datetime,
            new_player["score"]
        )
        cur.execute(query)
        db_connection.commit()
        cur.close()
    except Exception:
        raise DBConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()


def main():
    pass


if __name__ == '__main__':
    main()
