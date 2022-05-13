""" Class and methods for Stockfish analytics """
from typing import List

from stockfish import Stockfish

# from pgntofen import PgnToFen


sf = Stockfish()

class StockfishAnalysis:
    def __init__(self, pgn):
        self.pgn = pgn
        self.fen_positions = pgn.fen_positions
        self.analysis = []

    def get_current_evaluation(self, fen_position:str) -> dict:
        # given a fen position, set stockfish to this position
        sf.set_fen_position(fen_position)
        # return the stockfish evaluation
        return sf.get_evaluation()

    def get_best_move(self, fen_position:str) -> str:
        # given a fen position, set stockfish to this position
        sf.set_fen_position(fen_position)
        # have stockfish determine the best move
        return sf.get_best_move()
    
    def get_best_move_evaluation(self, fen_position:str) -> dict:
        # given a fen position, set stockfish to this position
        sf.set_fen_position(fen_position)
        # have stockfish determine the best move
        best_move = sf.get_best_move()
        # set stockfish to the next position using the best move
        sf.make_moves_from_current_position([best_move])
        # return the "best move" evaluation
        return sf.get_evaluation()

    def analyze(self) -> List[dict]:
        """ Run the analysis on all the moves
        Given a set of fen positions, output a list of dicts with these metrics:
            1. move_number
            2. move
            3. stockfish evaluation of the current position
            4. best move possible this turn (instead of the actual move)
            5. stockfish evaluation of the best move possible
        """
        self.analysis = []
        for i, fen_position in enumerate(self.fen_positions):
            move_analysis = {}
            move_analysis["move_number"] = i+1
            move_analysis["move"] = self.pgn.moves[i]
            move_analysis["stockfish_evaluation"] = self.get_current_evaluation(fen_position)
            # best move logic
            if i == 0:
                move_analysis["best_move"] = None
                move_analysis["stockfish_evaluation_best_move"] = None
            else:
                move_analysis["best_move"] = self.get_best_move(self.fen_positions[i-1])
                move_analysis["stockfish_evaluation_best_move"] = self.get_best_move_evaluation(self.fen_positions[i-1])
            self.analysis.append(move_analysis)
        return self.analysis