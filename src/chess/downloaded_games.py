import os

import chess

GAMES_ROOT = "data/games"

def get_downloaded_games_metrics():
    """
    Look through the downloaded games directory and generate metrics (number of games, etc)
    """
    file_metrics = []
    for (root, dirs, files) in os.walk(GAMES_ROOT, topdown=False):
        if len(files) > 0:
            file_metrics.append({
                "directory": root,
                "games": len(files)
            })
    return file_metrics


def get_username_latest_year_month(username) -> str:
    GAMES_DIRECTORY = f"{GAMES_ROOT}/{username}"
    """
    Look through the username's games directory and find the year and month of the most recent game.
    Return the date in "yyyy-mm" format.
    """
    
    # find max game


if __name__ == "__main__":
    print(get_downloaded_games_metrics())
