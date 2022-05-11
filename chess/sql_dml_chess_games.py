"""
Write chess game data to PostgreSQL
"""
import sys
import psycopg2
import glob
import json

from jinja2 import Template
from dotenv import dotenv_values

CONFIG = dotenv_values(".env")

DATABASE_URL=config["DATABASE_URL"]
DATABASE_PORT=config["DATABASE_PORT"]
DATABASE_USER=config["DATABASE_USER"]
DATABASE_PASSWORD=config["DATABASE_PASSWORD"]
DATABASE_DB=config["DATABASE_NAME"]

SQL_DML_CHESS_GAME = "sql/insert_chess_game_data.sql"

CHESS_GAME_FILES = glob.glob("data/games/*/*.json")

def main():
    """ Main function """

    # connect to the db
    database_url = f"postgresql://{DATABASE_URL}:{DATABASE_PORT}/{DATABASE_DB}"
    conn = psycopg2.connect(database_url)
    cur = conn.cursor()

    # open dml sql script
    with open(SQL_DML_CHESS_GAME, "r") as fp:
        query = fp.read()

        # To insert game data, for each game
        # 1. open the game file
        # 2. convert the pgn
        # 3. analyze the game
        # 4. send sql dml queries to insert the data
    for game_file in CHESS_GAME_FILES:
        with open(game_file, "r") as gfp:
            game = json.load(gfp)
            template = Template(query)
            sql_values = (
                game["url"],
                game["pgn"],
                game["time_control"],
                game["end_time"],
                game["rated"],
                game["tcn"],
                game["uuid"],
                game["initial_setup"],
                game["fen"],
                game["time_class"],
                game["rules"],
                json.dumps(game["white"]),
                json.dumps(game["black"])
            )
            sql_query = template.render(sql_values=sql_values)
            print(f"Executing SQL:\n{sql_query}")
            cur_response = cur.execute(sql_query)
            conn.commit()
            if cur_response:
                results = cur.fetchall()
                for result in results:
                    print(result)
       

    # close the db connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    sys.exit(main())
