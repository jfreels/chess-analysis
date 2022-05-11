INSERT INTO chess.games (
    url,
    pgn,
    time_control,
    end_time,
    rated,
    tcn,
    uuid,
    initial_setup,
    fen,
    time_class,
    rules,
    white,
    black
) VALUES {{ sql_values }}
