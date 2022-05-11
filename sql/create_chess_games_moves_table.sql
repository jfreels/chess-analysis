CREATE TABLE IF NOT EXISTS chess.games_moves (
    id serial,
    game_url varchar,
    fen_position varchar,
    move_number int,
    move varchar,
    stockfish_evaluation json,
    best_move varchar,
    stockfish_evaluation_best_move json
)
