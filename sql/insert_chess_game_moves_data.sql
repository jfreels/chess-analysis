INSERT INTO chess.games_moves (
    game_url,
    fen_position,
    move_number,
    move,
    stockfish_evaluation,
    best_move,
    stockfish_evaluation_best_move
) VALUES {{ sql_values }}
