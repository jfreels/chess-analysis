from pgntofen import PgnToFen


class ChessMoves:
    def __init__(self, pgn) -> None:
        self.chess_moves = PgnToFen()
        self.chess_moves.pgnToFen(pgn)
