""" PGN related classes and methods """
import re
from typing import List

# https://github.com/SindreSvendby/pgnToFen
from .pgntofen import PgnToFen


def remove_clock_times_from_moves(moves_string:str) -> str:
    """ Remove all the clock times from the string 
    Example string: "1. Nf3 {[%clk 0:02:56.3]} 1... e6 {[%clk 0:02:59]} "
    Expected result: "1. Nf3  1... e6"
    """
    pattern = "{\[%clk \d+:\d+:\d+\.*\d*\]}"
    replacement = ""
    new_string = re.sub(pattern=pattern, repl=replacement, string=moves_string)
    return new_string.strip()

def remove_turns_from_moves(moves_string:str) -> str:
    """ Remove all the move numbers from the string 
    Example string: "1. Nf3  1... e6"
    Expected result: "Nf3  e6"
    """
    pattern = "\d+\.+\s"
    replacement = ""
    new_string = re.sub(pattern=pattern, repl=replacement, string=moves_string)
    return new_string.strip()

class Pgn:
    def __init__(self, pgn:str):
        self.pgn = pgn
        self.moves = self.create_moves_list()
        self.fen = PgnToFen()
        self.fen_positions = self.create_fen_positions()
        # self.evaluations = self.create_evaluations()

    def create_moves_list(self) -> List[str]:
        converted_pgn = self.pgn.splitlines()
        moves_string = converted_pgn[-1]
        moves_string = remove_clock_times_from_moves(moves_string)
        moves_string = remove_turns_from_moves(moves_string)
        moves = moves_string.split()
        moves = moves[:-1] # remove the final score?
        return moves

    def create_fen_positions(self) -> List[str]:
        for move in self.moves:
            self.fen.move(move)

