""" Tests for converting PGN format to Python class """
from chess.pgn import Pgn, remove_clock_times_from_moves, remove_turns_from_moves

EXAMPLE_PGN = "[Event \"Live Chess\"]\n[Site \"Chess.com\"]\n[Date \"2020.07.19\"]\n[Round \"-\"]\n[White \"jfreels\"]\n[Black \"IVNJ5\"]\n[Result \"0-1\"]\n[CurrentPosition \"5b1r/pp1krppp/5n2/2Qp1PB1/1P6/P1N2qP1/2P1P2P/R3K3 w Q -\"]\n[Timezone \"UTC\"]\n[ECO \"A04\"]\n[ECOUrl \"https://www.chess.com/openings/Reti-Opening-Queens-Gambit-Invitation\"]\n[UTCDate \"2020.07.19\"]\n[UTCTime \"14:10:37\"]\n[WhiteElo \"165\"]\n[BlackElo \"305\"]\n[TimeControl \"180\"]\n[Termination \"IVNJ5 won on time\"]\n[StartTime \"14:10:37\"]\n[EndDate \"2020.07.19\"]\n[EndTime \"14:14:56\"]\n[Link \"https://www.chess.com/game/live/5172969478\"]\n\n1. Nf3 {[%clk 0:02:56.3]} 1... e6 {[%clk 0:02:59.4]} 2. d4 {[%clk 0:02:50.6]} 2... Nf6 {[%clk 0:02:56.4]} 3. Nc3 {[%clk 0:02:43]} 3... Nc6 {[%clk 0:02:55.8]} 4. g3 {[%clk 0:02:38.3]} 4... e5 {[%clk 0:02:54.9]} 5. Bh3 {[%clk 0:02:37.1]} 5... exd4 {[%clk 0:02:54]} 6. Nxd4 {[%clk 0:02:32.2]} 6... Nxd4 {[%clk 0:02:50.5]} 7. Qxd4 {[%clk 0:02:30.2]} 7... c5 {[%clk 0:02:47]} 8. Qe3+ {[%clk 0:02:17.6]} 8... Qe7 {[%clk 0:02:36.1]} 9. f4 {[%clk 0:02:13]} 9... d5 {[%clk 0:02:29.7]} 10. Bxc8 {[%clk 0:01:58.5]} 10... Rxc8 {[%clk 0:02:27]} 11. a3 {[%clk 0:01:44.1]} 11... Kd7 {[%clk 0:02:26.5]} 12. b4 {[%clk 0:01:34.7]} 12... Qd6 {[%clk 0:02:22.9]} 13. Rf1 {[%clk 0:01:19.8]} 13... Re8 {[%clk 0:02:21.5]} 14. Qxc5 {[%clk 0:01:13.7]} 14... Re6 {[%clk 0:02:07.9]} 15. f5 {[%clk 0:01:06.5]} 15... Re7 {[%clk 0:02:01.5]} 16. Bf4 {[%clk 0:00:56.2]} 16... Qe6 {[%clk 0:01:58]} 17. Bg5 {[%clk 0:00:15.9]} 17... Qe3 {[%clk 0:01:52.1]} 18. Rf3 {[%clk 0:00:09.1]} 18... Qxf3 {[%clk 0:01:50.5]} 0-1\n"
EXAMPLE_PGN2 = "[Event \"Live Chess\"]\n[Site \"Chess.com\"]\n[Date \"2020.07.19\"]\n[Round \"-\"]\n[White \"jfreels\"]\n[Black \"Priyanshu268\"]\n[Result \"0-1\"]\n[CurrentPosition \"3r1k2/pp1P4/3R2p1/2p1NpPp/4bP2/4n2K/PP2P2P/2B5 w - h6\"]\n[Timezone \"UTC\"]\n[ECO \"A15\"]\n[ECOUrl \"https://www.chess.com/openings/English-Opening-Anglo-Indian-Kings-Knight-Variation\"]\n[UTCDate \"2020.07.19\"]\n[UTCTime \"14:49:49\"]\n[WhiteElo \"355\"]\n[BlackElo \"467\"]\n[TimeControl \"180\"]\n[Termination \"Priyanshu268 won on time\"]\n[StartTime \"14:49:49\"]\n[EndDate \"2020.07.19\"]\n[EndTime \"14:55:45\"]\n[Link \"https://www.chess.com/game/live/5173125405\"]\n\n1. Nf3 {[%clk 0:02:59.9]} 1... Nf6 {[%clk 0:02:59.9]} 2. c4 {[%clk 0:02:56.4]} 2... e5 {[%clk 0:02:59.8]} 3. Qc2 {[%clk 0:02:51.4]} 3... c5 {[%clk 0:02:59.1]} 4. Qf5 {[%clk 0:02:46.3]} 4... d5 {[%clk 0:02:56]} 5. Qxe5+ {[%clk 0:02:44.3]} 5... Be7 {[%clk 0:02:53.6]} 6. Qxd5 {[%clk 0:02:41.8]} 6... Ne4 {[%clk 0:02:41.2]} 7. Qxe4 {[%clk 0:02:38.8]} 7... Nc6 {[%clk 0:02:35.1]} 8. Ne5 {[%clk 0:02:33.9]} 8... O-O {[%clk 0:02:27.2]} 9. d4 {[%clk 0:02:21.8]} 9... Nxd4 {[%clk 0:02:23.4]} 10. Qd5 {[%clk 0:02:12]} 10... Bd6 {[%clk 0:02:09.2]} 11. Qxd6 {[%clk 0:02:07.5]} 11... Qxd6 {[%clk 0:02:07.4]} 12. Nd3 {[%clk 0:01:56.7]} 12... Nc2+ {[%clk 0:02:05.3]} 13. Kd2 {[%clk 0:01:47.9]} 13... Nxa1 {[%clk 0:02:00.6]} 14. g3 {[%clk 0:01:42.1]} 14... Bf5 {[%clk 0:01:56]} 15. f4 {[%clk 0:01:24.5]} 15... Rae8 {[%clk 0:01:54.3]} 16. Bg2 {[%clk 0:01:18.4]} 16... Re3 {[%clk 0:01:49.1]} 17. Kxe3 {[%clk 0:01:15.7]} 17... Re8+ {[%clk 0:01:45.8]} 18. Ne5 {[%clk 0:01:09.7]} 18... Qd4+ {[%clk 0:01:39.2]} 19. Kf3 {[%clk 0:01:01.7]} 19... Be4+ {[%clk 0:01:32.5]} 20. Kg4 {[%clk 0:00:56.2]} 20... f5+ {[%clk 0:01:22.4]} 21. Kh3 {[%clk 0:00:47.3]} 21... Bxb1 {[%clk 0:01:15]} 22. Bd5+ {[%clk 0:00:41.3]} 22... Kf8 {[%clk 0:01:10.6]} 23. g4 {[%clk 0:00:26.7]} 23... Qxd5 {[%clk 0:01:01.2]} 24. cxd5 {[%clk 0:00:23.8]} 24... Be4 {[%clk 0:00:54.8]} 25. Rd1 {[%clk 0:00:17.5]} 25... Nc2 {[%clk 0:00:38.1]} 26. d6 {[%clk 0:00:13.5]} 26... Ne3 {[%clk 0:00:34.5]} 27. d7 {[%clk 0:00:11.9]} 27... Rd8 {[%clk 0:00:32.3]} 28. g5 {[%clk 0:00:07.5]} 28... g6 {[%clk 0:00:28.7]} 29. Rd6 {[%clk 0:00:00.2]} 29... h5 {[%clk 0:00:18.6]} 0-1\n"
EXAMPLE_MOVES = "1. Nf3 {[%clk 0:02:56.3]} 1... e6 {[%clk 0:02:59.4]} 2. d4 {[%clk 0:02:50.6]} 2... Nf6 {[%clk 0:02:56.4]} 3. Nc3 {[%clk 0:02:43]} 3... Nc6 {[%clk 0:02:55.8]} 4. g3 {[%clk 0:02:38.3]} 4... e5 {[%clk 0:02:54.9]} 5. Bh3 {[%clk 0:02:37.1]} 5... exd4 {[%clk 0:02:54]} 6. Nxd4 {[%clk 0:02:32.2]} 6... Nxd4 {[%clk 0:02:50.5]} 7. Qxd4 {[%clk 0:02:30.2]} 7... c5 {[%clk 0:02:47]} 8. Qe3+ {[%clk 0:02:17.6]} 8... Qe7 {[%clk 0:02:36.1]} 9. f4 {[%clk 0:02:13]} 9... d5 {[%clk 0:02:29.7]} 10. Bxc8 {[%clk 0:01:58.5]} 10... Rxc8 {[%clk 0:02:27]} 11. a3 {[%clk 0:01:44.1]} 11... Kd7 {[%clk 0:02:26.5]} 12. b4 {[%clk 0:01:34.7]} 12... Qd6 {[%clk 0:02:22.9]} 13. Rf1 {[%clk 0:01:19.8]} 13... Re8 {[%clk 0:02:21.5]} 14. Qxc5 {[%clk 0:01:13.7]} 14... Re6 {[%clk 0:02:07.9]} 15. f5 {[%clk 0:01:06.5]} 15... Re7 {[%clk 0:02:01.5]} 16. Bf4 {[%clk 0:00:56.2]} 16... Qe6 {[%clk 0:01:58]} 17. Bg5 {[%clk 0:00:15.9]} 17... Qe3 {[%clk 0:01:52.1]} 18. Rf3 {[%clk 0:00:09.1]} 18... Qxf3 {[%clk 0:01:50.5]} 0-1"

def test_converted_pgn():
    pgn = Pgn(pgn=EXAMPLE_PGN)
    assert isinstance(pgn.converted_pgn, list)
    assert pgn.converted_pgn[0] == '[Event "Live Chess"]'

def test_converted_pgn_2():
    pgn = Pgn(pgn=EXAMPLE_PGN2)
    assert isinstance(pgn.converted_pgn, list)
    assert pgn.converted_pgn[0] == '[Event "Live Chess"]'

def test_create_moves_list():
    pgn = Pgn(pgn=EXAMPLE_PGN)
    assert isinstance(pgn.moves, list)
    assert len(pgn.moves) == 36
    assert pgn.moves[0] == "Nf3"
    assert pgn.moves[1] == "e6"
    assert pgn.moves[-1] == "Qxf3"
    assert pgn.moves[-2] == "Rf3"

def test_remove_clock_times_from_moves():
    initial = "1. Nf3 {[%clk 0:02:56.3]} 1... e6 {[%clk 0:02:59]} "
    expected = "1. Nf3  1... e6"
    assert remove_clock_times_from_moves(initial) == expected

def test_remove_turns_from_moves():
    initial = "1. Nf3  1... e6"
    expected = "Nf3  e6"
    assert remove_turns_from_moves(initial) == expected

def test_create_fen_positions():
    initial = EXAMPLE_MOVES
    pgn = Pgn(pgn=EXAMPLE_PGN)
    assert pgn.fen_positions[0] == "rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b - KQkq"
    assert pgn.fen_positions[-1] == "5b1r/pp1krppp/5n2/2Qp1PB1/1P6/P1N2qP1/2P1P2P/R3K3 w - Q"
