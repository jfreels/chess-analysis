from urllib.error import HTTPError
import os

import streamlit as st

from chesscom import ChessCom


GAMES_ROOT = "data/games"
GAMES_DIRECTORY = "data/games/{username}"
ANALYZED_GAMES_DIRECTORY = "data/games_analyzed/{username}"


st.header("Chess Analyzer")
st.subheader("Games Collected")
file_metrics = []
for (root, dirs, files) in os.walk(GAMES_ROOT, topdown=False):
    if len(files) > 0:
        file_metrics.append({
            "directory": root,
            "games": len(files)
        })

st.table(file_metrics)

st.subheader('Enter your Chess.com username to download your games')
username = st.text_input('Chess.com Username')

if username:
    # try:
    chess = ChessCom(username=username)
    games_directory = f"data/games/{username}"
    if not os.path.exists(games_directory):
        # logging.info(f"Creating directory: {games_directory}")
        os.mkdir(games_directory)

    with st.spinner(f"Downloading Chess.com games for {username}..."):
        games = chess.get_games_all()
        game_files = []
        with st.expander(label=f"See game files"):
            for game in games:
                game_files.append(chess.write_game_to_json(game=game, game_directory=games_directory))
            st.table(game_files)
        st.metric(label="games downloaded", value=len(game_files))

    # except Exception as e:
    #         st.echo(e)
    #         st.error('Username not found...')   
        
    # if os.path.exists(f"{ANALYZED_GAMES_DIRECTORY}"):
    #     for file in os.listdir(f"{ANALYZED_GAMES_DIRECTORY}"):
    #         st.write(file)
    #         with open(f'{ANALYZED_GAMES_DIRECTORY}{username}/{file}') as f:
    #             st.download_button('Download JSON', f) 
