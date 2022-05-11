"""
Main chess program
"""
import json
import sys
import glob

from pgn import Pgn


USERNAME = "jfreels"
GAMES_DIRECTORY = f"data/games/{USERNAME}"


def main():
    """ Main function """
    # analyze games
    game_files = glob.glob(f"{GAMES_DIRECTORY}/*.json")[3:4]
    print(game_files)
    for game in game_files:
        with open(game, "r") as fp:
            # load the game as JSON
            game_json = json.load(fp)
            # convert the raw pgn
            pgn = Pgn(pgn=game_json["pgn"])
            print(pgn.fen_positions)


if __name__ == "__main__":
    sys.exit(main())
