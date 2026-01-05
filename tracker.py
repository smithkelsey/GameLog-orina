import sqlite3
from datetime import datetime

game_log = "game_log.db"

#### setup the database
def db_setup():
    conn = sqlite3.connect(game_log)
    curs = conn.cursor()
    curs.execute("""
        CREATE TABLE IF NOT EXISTS game_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_name TEXT NOT NULL,
            platform TEXT,
            genre TEXT,
            hours_played REAL DEFAULT 0,
            year_started TEXT,
            year_completed TEXT,
            status TEXT
        );
    """)

    conn.commit()
    conn.close()

#### CRUD (add game, view game, update game, delete game)

# to add a game (one at a time)
def add_game(game_name, platform, genre, hours_played, year_started=None, year_completed=None, status=None):
    conn = sqlite3.connect(game_log)
    curs = conn.cursor()
    curs.execute("""
                INSERT INTO game_log (game_name, platform, genre, hours_played, year_started, year_completed, status)
                VALUES (?, ?, ?, ?, ?, ?, ?);
                """, (game_name, platform, genre, hours_played, year_started, year_completed, status))
    
    conn.commit()
    conn.close()
    print("Game has been added.")

# to view all games
# ** ideally i want to try to get it where a specific game is selected, filters, or the whole table**
def view_all_games():
    conn = sqlite3.connect(game_log)
    curs = conn.cursor()

    curs.execute("SELECT * from game_log;")
    rows = curs.fetchall()

    conn.close()
    if not rows:
        print("No games have been played.")
    else:
        print("")
        print("---- Games Log ----")
        print("")
        print(rows)

def update_name(game_id, game_name):
    conn = sqlite3.connect(game_log)
    curs = conn.cursor()

    curs.execute("""
                UPDATE game_log
                SET game_name = ?
                WHERE id = ?
                 """, (game_name, game_id))
    
    conn.commit()
    conn.close()
    print("Game name has been updated.")

def update_platform(game_id, platform):
    conn = sqlite3.connect(game_log)
    curs = conn.cursor()

    curs.execute("""
                UPDATE game_log
                SET platform = ?
                WHERE id = ?
                 """, (platform, game_id))
    
    conn.commit()
    conn.close()
    print("Platform for this game has been updated.")

# update hours by adding what the user enters to what is already there
def add_hours(game_id, hours_played):
    conn = sqlite3.connect(game_log)
    curs = conn.cursor()

    curs.execute("""
                UPDATE game_log
                SET hours_played = hours_played + ?
                WHERE id = ?
                 """, (hours_played, game_id))
    
    conn.commit()
    conn.close()
    print("Hours have been added.")

# update hours completely
def update_hours(game_id, hours_played):
    conn = sqlite3.connect(game_log)
    curs = conn.cursor()

    curs.execute("""
                UPDATE game_log
                SET hours_played = ?
                WHERE id = ?
                 """, (hours_played, game_id))
    
    conn.commit()
    conn.close()
    print("Overall hours played has been updated.")

def update_start_year(game_id, year_started):
    conn = sqlite3.connect(game_log)
    curs = conn.cursor()

    curs.execute("""
                UPDATE game_log
                SET year_started = ?
                WHERE id = ?
                 """, (year_started, game_id))
    
    conn.commit()
    conn.close()
    print("Year game was started has been updated.")

def update_end_year(game_id, year_completed):
    conn = sqlite3.connect(game_log)
    curs = conn.cursor()

    curs.execute("""
                UPDATE game_log
                SET year_completed = ?
                WHERE id = ?
                 """, (year_completed, game_id))
    
    conn.commit()
    conn.close()
    print("Year game was completed has been updated.")

def update_status(game_id, status):
    conn = sqlite3.connect(game_log)
    curs = conn.cursor()

    curs.execute("""
                UPDATE game_log
                SET status = ?
                WHERE id = ?
                 """, (status, game_id))
    
    conn.commit()
    conn.close()
    print("Game status has been updated.")

# -----------------------------

#### Menu System
def main_menu():
    print("")
    print("Personal Game Log")
    print("-----------------------")
    print("1. Add a new game")
    print("2. View all logged games")
    print("3. Add additional hours to hours played")
    print("4. Update game status")
    print("5. Update additional game details")
    print("6. Exit")    

def sub_menu():
    print("")
    print("Update Game Details")
    print("-----------------------")
    print("1. Update game name")
    print("2. Update platform")
    print("3. Update total hours played")
    print("4. Update year started")
    print("5. Update year completed")
    print("6. Back to main menu")

def main():
    db_setup()

    while True:
        main_menu()
        choice = input("Choose an option (number of choice): ")

        if choice == "1":
            game_name = input("Game name: ")
            platform = input("Platform: ")
            genre = input("Genre: ")
            hours_played = float(input("Hours played or leave blank: "))
            if hours_played == "":
                hours_played = 0
            year_started = input("Year started (YYYY) or leave blank: ")
            if year_started.strip() == "":
                year_started = None
            year_completed = input("Year completed, finished, or abandoned (YYYY) or leave blank: ")
            if year_completed.strip() == "":
                year_completed = None
            status = input("Status of game (Playing, Finished, Completed, Abandoned, Endless): ")
            status_options = ["playing", "finished", "completed", "abandoned", "endless"]
            if status.strip().lower() not in status_options:
                status  = input("The entered response is not an option. Please choose between playing, finished, completed, abandoned, or endless: ")
            add_game(game_name, platform, genre, year_started, year_completed, status)

        elif choice == "2":
            view_all_games()

        elif choice == "3":
            game_id = int(input("Game ID: "))
            hours = float(input("Additional hours: "))
            add_hours(game_id, hours)

        elif choice == "4":
            game_id = int(input("Game ID: "))
            status = input("Updated game status (Playing, Finished, Completed, Abandoned, or Endless): ")
            if status.strip().lower() not in status_options:
                status  = input("The entered response is not an option. Please choose between playing, finished, completed, abandoned, or endless: ")

        elif choice == "5":
            while True:
                sub_menu()
                sub_choice = input("Choose an option (number of choice): ")
                if sub_choice == "1":
                    #game name
                    game_id = int(input("Game ID: "))
                    game_name = input("Updated game name: ")
                    update_name(game_id, game_name)

                elif sub_choice == "2":
                    #platform
                    game_id = int(input("Game ID: "))
                    platform = input("Updated platform: ")
                    update_platform(game_id, platform)

                elif sub_choice == "3":
                    #total hours
                    game_id = int(input("Game ID: "))
                    hours_played = input("Updated TOTAL number of hours played: ")
                    update_hours(game_id, hours_played)

                elif sub_choice == "4":
                    #year started
                    game_id = int(input("Game ID: "))
                    year_started = input("Updated start year: ")
                    update_start_year(game_id, year_started)

                elif sub_choice == "5":
                    #year completed
                    game_id = int(input("Game ID: "))
                    year_completed = input("Updated end year: ")
                    update_end_year(game_id, year_completed)
                
                elif sub_choice == "6":
                    #exit to main menu
                    main_menu()
                    break

                else:
                    print("Not an option, try again.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Hey so that's not an option. Try again.")


if __name__ == "__main__":
    main()
