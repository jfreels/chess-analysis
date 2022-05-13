"""
Write chess game data to PostgreSQL
"""
import sys
import psycopg2
import glob
import json

from jinja2 import Template
from dotenv import dotenv_values

from chess.pgn import Pgn
from chess.stockfish_analysis import StockfishAnalysis


CONFIG = dotenv_values(".env")

DATABASE_URL = CONFIG["DATABASE_URL"]
DATABASE_PORT = CONFIG["DATABASE_PORT"]
DATABASE_USER = CONFIG["DATABASE_USER"]
DATABASE_PASSWORD = CONFIG["DATABASE_PASSWORD"]
DATABASE_DB = CONFIG["DATABASE_NAME"]

SQL_DML_CHESS_GAMES_MOVES = "sql/insert_chess_game_moves_data.sql"

CHESS_GAME_FILES = glob.glob("data/games/*/*.json")

def main():
    """ Main function """

    # connect to the db
    database_url = f"postgresql://{DATABASE_URL}:{DATABASE_PORT}/{DATABASE_DB}"
    conn = psycopg2.connect(database_url)
    cur = conn.cursor()

    # open dml sql script
    with open(SQL_DML_CHESS_GAMES_MOVES, "r") as fp:
        query = fp.read()

    # To insert game data, for each game
    # 1. open the game file
    # 2. convert the pgn
    # 3. analyze the game
    # 4. for each move, send sql dml query to insert the data
    for game_file in CHESS_GAME_FILES:
        with open(game_file, "r") as gfp:
            game = json.load(gfp)
            pgn = Pgn(game["pgn"])
            analysis = StockfishAnalysis(pgn=pgn)
            analysis.analyze()
            for index in range(len(analysis.analysis)):
                move = analysis.analysis[index]
                fen_position = pgn.fen_positions[index]
                template = Template(query)
                sql_values = (
                    game["url"],
                    fen_position,
                    move["move_number"],
                    move["move"],
                    json.dumps(move["stockfish_evaluation"]),
                    json.dumps(move["best_move"]),
                    json.dumps(move["stockfish_evaluation_best_move"])
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
