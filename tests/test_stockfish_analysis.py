""" Tests for Stockfish interaction """

from stockfish import Stockfish

from src.chess.stockfish_analysis import StockfishAnalysis
from src.chess.pgn import Pgn


EXAMPLE_PGN = "[Event \"Live Chess\"]\n[Site \"Chess.com\"]\n[Date \"2020.07.19\"]\n[Round \"-\"]\n[White \"jfreels\"]\n[Black \"IVNJ5\"]\n[Result \"0-1\"]\n[CurrentPosition \"5b1r/pp1krppp/5n2/2Qp1PB1/1P6/P1N2qP1/2P1P2P/R3K3 w Q -\"]\n[Timezone \"UTC\"]\n[ECO \"A04\"]\n[ECOUrl \"https://www.chess.com/openings/Reti-Opening-Queens-Gambit-Invitation\"]\n[UTCDate \"2020.07.19\"]\n[UTCTime \"14:10:37\"]\n[WhiteElo \"165\"]\n[BlackElo \"305\"]\n[TimeControl \"180\"]\n[Termination \"IVNJ5 won on time\"]\n[StartTime \"14:10:37\"]\n[EndDate \"2020.07.19\"]\n[EndTime \"14:14:56\"]\n[Link \"https://www.chess.com/game/live/5172969478\"]\n\n1. Nf3 {[%clk 0:02:56.3]} 1... e6 {[%clk 0:02:59.4]} 2. d4 {[%clk 0:02:50.6]} 2... Nf6 {[%clk 0:02:56.4]} 3. Nc3 {[%clk 0:02:43]} 3... Nc6 {[%clk 0:02:55.8]} 4. g3 {[%clk 0:02:38.3]} 4... e5 {[%clk 0:02:54.9]} 5. Bh3 {[%clk 0:02:37.1]} 5... exd4 {[%clk 0:02:54]} 6. Nxd4 {[%clk 0:02:32.2]} 6... Nxd4 {[%clk 0:02:50.5]} 7. Qxd4 {[%clk 0:02:30.2]} 7... c5 {[%clk 0:02:47]} 8. Qe3+ {[%clk 0:02:17.6]} 8... Qe7 {[%clk 0:02:36.1]} 9. f4 {[%clk 0:02:13]} 9... d5 {[%clk 0:02:29.7]} 10. Bxc8 {[%clk 0:01:58.5]} 10... Rxc8 {[%clk 0:02:27]} 11. a3 {[%clk 0:01:44.1]} 11... Kd7 {[%clk 0:02:26.5]} 12. b4 {[%clk 0:01:34.7]} 12... Qd6 {[%clk 0:02:22.9]} 13. Rf1 {[%clk 0:01:19.8]} 13... Re8 {[%clk 0:02:21.5]} 14. Qxc5 {[%clk 0:01:13.7]} 14... Re6 {[%clk 0:02:07.9]} 15. f5 {[%clk 0:01:06.5]} 15... Re7 {[%clk 0:02:01.5]} 16. Bf4 {[%clk 0:00:56.2]} 16... Qe6 {[%clk 0:01:58]} 17. Bg5 {[%clk 0:00:15.9]} 17... Qe3 {[%clk 0:01:52.1]} 18. Rf3 {[%clk 0:00:09.1]} 18... Qxf3 {[%clk 0:01:50.5]} 0-1\n"
sf = Stockfish()
pgn = Pgn(pgn=EXAMPLE_PGN)
analysis = StockfishAnalysis(pgn=pgn)

def test_stockfish():
    sf.set_position(["e2e4", "e7e6"])
    assert sf.get_best_move() == "d2d4"

def test_get_current_evaluation():
    fen_position = analysis.fen_positions[0]
    assert analysis.get_current_evaluation(fen_position) == {"type": "cp", "value": 9}
    fen_position = analysis.fen_positions[-1]
    assert analysis.get_current_evaluation(fen_position) == {"type": "cp", "value": 158}

def test_get_best_move():
    fen_position = analysis.fen_positions[0]
    assert analysis.get_best_move(fen_position) == "d7d5"
    fen_position = analysis.fen_positions[-1]
    assert analysis.get_best_move(fen_position) == "c5e7"

def test_best_move_evaluation():
    fen_position = analysis.fen_positions[0]
    assert analysis.get_best_move_evaluation(fen_position) == {'type': 'cp', 'value': 60}
    fen_position = analysis.fen_positions[-1]
    assert analysis.get_best_move_evaluation(fen_position) == {'type': 'cp', 'value': 158}

def test_analyze():
    analysis.analyze()
    assert analysis.analysis[0] == {'move_number': 1, 'move': 'Nf3', 'stockfish_evaluation': {'type': 'cp', 'value': 9}, 'best_move': None, 'stockfish_evaluation_best_move': None}
    assert analysis.analysis[-1] == {'move_number': 36, 'move': 'Qxf3', 'stockfish_evaluation': {'type': 'cp', 'value': 158}, 'best_move': 'e3f3', 'stockfish_evaluation_best_move': {'type': 'cp', 'value': 158}}
