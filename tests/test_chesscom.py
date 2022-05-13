""" Tests for chess/chesscom.py """
from src.chess import ChessCom

USERNAME = "jessieyikes"
GAMES_URI = f"/player/{USERNAME}/games"

def test_get_url():
    """ Test generic get request against Chess.com """
    chess = ChessCom(username=USERNAME)
    url = f"{chess.base_url}{GAMES_URI}"
    data = chess._get(url=url)
    assert data

def test_get_user_info():
    """ Get Chess.com user information """
    chess = ChessCom(username=USERNAME)
    user_info = chess.get_user_info()
    assert user_info

def test_get_stats():
    """ Get Chess.com user stats """
    chess = ChessCom(username=USERNAME)
    stats = chess.get_stats()
    assert stats

def test_get_games():
    """ Get Chess.com user's games """
    chess = ChessCom(username=USERNAME)
    games = chess.get_stats()
    assert games

def test_get_games_by_month():
    """ Test getting all chess.com games based on a specific user and month. """
    chess = ChessCom(username=USERNAME)
    year = 2022
    month = 5
    games = chess.get_games_by_month(year=year, month=month)
    assert games

def test_get_games_archives():
    """ Test Get Chess.com user's games archives """
    chess = ChessCom(username=USERNAME)
    games_archives = chess.get_games_archives()
    assert games_archives

def test_get_games_all():
    """ Test getting all chess.com games based on available archives. """
    chess = ChessCom(username=USERNAME)
    for game in chess.get_games_all():
        assert isinstance(game, dict)
 