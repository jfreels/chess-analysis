"""
Main chess program
"""
import json
import os
import sys
import glob

# from pgn import Pgn
from chess.pgntofen import PgnToFen
from chess.stockfish_analysis import StockfishAnalysis as sa


USERNAME = "jfreels"
GAMES_DIRECTORY = f"data/games/{USERNAME}"
ANALYZED_GAMES_DIRECTORY = f"data/games_analyzed/{USERNAME}"
if not os.path.exists(ANALYZED_GAMES_DIRECTORY):
    os.mkdir(ANALYZED_GAMES_DIRECTORY)

def main():
    """ Main function """
    # analyze games
    game_files = glob.glob(f"{GAMES_DIRECTORY}/*.json")
    for game in game_files:
        print(f"Analyzing: {game}")
        with open(game, "r") as fp:
            # load the game as JSON
            game_json = json.load(fp)
            # convert the raw pgn to a series of fens
            pgn = game_json["pgn"]
            fen = PgnToFen()
            fen.pgnToFen(pgn)
            game_json["fens"] = fen.fens

            # output to file
            game_id = game_json["url"].split("/")[-1]
            white_player = game_json["white"]["username"]
            black_player = game_json["black"]["username"]
            filename = f"analyzed_{game_id}_{white_player}_vs_{black_player}.json"

            with open(f"{ANALYZED_GAMES_DIRECTORY}/{filename}", "w") as fp2:
                json.dump(game_json, fp2)


if __name__ == "__main__":
    sys.exit(main())
