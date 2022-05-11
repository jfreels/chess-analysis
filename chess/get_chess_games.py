"""
Main chess program
"""

import json
import sys
import glob

from chesscom import ChessCom


GAMES_DIRECTORY = "data/games/{username}"


def get_games(username):
    """
    Download games from chess.com
    """
    chess = ChessCom(username=username)
    me = chess.get_user_info()
    print(json.dumps(me))
    stats = chess.get_stats()
    # print(json.dumps(stats))
    games = chess.get_games_all()
    # example_game = next(games)
    # print(json.dumps(example_game))

    # write games to files
    for game in games:
        chess.write_game_to_json(game=game, dir=f"{GAMES_DIRECTORY}")

    return True


if __name__ == "__main__":
    sys.exit(get_games())
