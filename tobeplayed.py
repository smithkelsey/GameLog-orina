###################################
#        Database for Games       #
#           to be played          #
#           Kelsey Smith          #
###################################

import sqlite3
import csv
import json
from typing import Any, Dict, List, Union

tbp_log = "tbp_log.db"

#### setup the database
def db_setup():
    conn = sqlite3.connect(tbp_log)
    curs = conn.cursor()
    curs.execute("""
        CREATE TABLE IF NOT EXISTS game_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_name TEXT NOT NULL,
            platform TEXT,
            genre TEXT
        );
    """)

    conn.commit()
    conn.close()