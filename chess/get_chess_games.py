"""
Main chess program
"""

import json
import sys

from chesscom import ChessCom


USERNAME = sys.argv[1]
GAMES_DIRECTORY = f"data/games/{USERNAME}"

def main():
    """
    Download games from chess.com
    """
    chess = ChessCom(username=USERNAME)
    me = chess.get_user_info()
    print(json.dumps(me))
    stats = chess.get_stats()
    print(json.dumps(stats))
    games = chess.get_games_all()

    # write games to files
    for game in games:
        chess.write_game_to_json(game=game, game_directory=GAMES_DIRECTORY)


if __name__ == "__main__":
    sys.exit(main())
