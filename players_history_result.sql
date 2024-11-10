CREATE DATABASE players_history_result;

USE players_history_result;

CREATE TABLE players_history_result(
	player_name VARCHAR(200) NOT NULL,
    date TIMESTAMP NOT NULL,
    score INT NOT NULL);




INSERT INTO players_history_result(player_name, date, score)
VALUE
("Benjamin Smith", "2023-04-15 12:30:45", 1400),
("Olivia Johnson", "2022-11-02 08:15:20", 1110),
("Ethan Davis", "2023-07-29 17:45:10", 1030),
("Ava Martinez", "2023-01-20 16:55:40", 100),
("Mia Clark", "2023-05-01 15:00:55", 340),
("Alexander Lewis", "2022-08-25 10:50:05", 560),
("Charlotte Turner", "2023-02-05 13:35:00", 40),
("Daniel Rodriguez", "2022-11-17 06:05:15 ", 20),
("Amelia Walker", "2023-07-05 19:30:20", 170),
("Matthew Scott", "2022-12-28 08:55:30", 1400),
("Michael Hall", "2023-01-08 14:45:10", 350),
("Jacob Turner", "2022-09-23 07:10:25", 900),
("Emily Martinez", "2023-04-03 18:35:45", -100)
;

SELECT * FROM players_history_result;