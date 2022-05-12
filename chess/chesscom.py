""" Chess.com API class """
from typing import Generator, List, Dict
import json
import logging
import os

import requests


logging.basicConfig(level=logging.info)

BASE_URL = "https://api.chess.com/pub"


class ChessCom:
    """
    Connect to the Chess.com public web API
    https://www.chess.com/news/view/published-data-api
    """
    def __init__(self, username):
        self.base_url = BASE_URL
        self.username = username
        self.player_endpoint = f"/player/{self.username}"

    def _get(self, url:str):
        """
        Generic get requets method
        """
        response = requests.get(url=url)
        response.raise_for_status()
        data = response.json()
        return data

    def get_user_info(self) -> Dict:
        """
        Get data about a specific user
        """
        url = f"{self.base_url}{self.player_endpoint}"
        return self._get(url=url)

    def get_stats(self) -> Dict:
        """
        Get chess games stats
        """
        url = f"{self.base_url}{self.player_endpoint}/stats"
        return self._get(url=url)

    def get_games(self) -> List:
        """
        Get chess games data
        """
        url = f"{self.base_url}{self.player_endpoint}/games"
        return self._get(url=url)


    def get_games_archives(self) -> List:
        """
        Get chess games archives data
        """
        url = f"{self.base_url}{self.player_endpoint}/games/archives"
        data = self._get(url=url)
        logging.info(data["archives"])
        return data.get("archives")

    
    def get_games_by_month(self, year:int, month:int) -> Generator:
        """
        Get all chess games for a specific month
        """
        assert len(str(year)) == 4
        if len(str(month)) == 1:
            month = str(month).zfill(2)
        url = f"{self.base_url}{self.player_endpoint}/games/{year}/{month}"
        data = self._get(url=url)
        yield from data["games"]


    def get_games_all(self) -> Generator:
        """
        Get all chess games based on available archives.
        """
        archives = self.get_games_archives()
        for archive_url in archives:
            logging.info(f"Downloading games: {archive_url}")
            games_in_month = self._get(url=archive_url)["games"]
            yield from games_in_month


    def write_game_to_json(self, game, game_directory:str):
        """
        Write the chess game to a JSON file
        """
        game_id = game["url"].split("/")[-1]
        white_player = game["white"]["username"]
        black_player = game["black"]["username"]
        filename = f"{game_id}_{white_player}_vs_{black_player}.json"
        filepath = f"{game_directory}/{filename}"
        logging.info(f"Writing game to file: {filename}")
        with open(filepath, "w") as fp:
            json.dump(game, fp)
        return filename
