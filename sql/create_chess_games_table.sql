CREATE TABLE IF NOT EXISTS chess.games (
    id serial,
    url varchar,
    pgn varchar,
    time_control varchar,
    end_time int,
    rated boolean,
    tcn varchar,
    uuid varchar,
    initial_setup varchar,
    fen varchar,
    time_class varchar,
    rules varchar,
    white json,
    black json
)
