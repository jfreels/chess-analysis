from urllib.error import HTTPError
import os

import streamlit as st

from get_chess_games import get_games


GAMES_DIRECTORY = "data/games/{username}"
ANALYZED_GAMES_DIRECTORY = "data/games_analyzed/{username}"


st.header('Chess Analyzer')
st.subheader('Enter your Chess.com username to analyze your games')

username = st.text_input('Chess.com Username')

if username:
    try:
        with st.spinner('Downloading Games...'):
            get_games(username)
    except Exception:
            st.error('Username not found...')   
        
    if os.path.exists(f"{ANALYZED_GAMES_DIRECTORY}"):
        for file in os.listdir(f"{ANALYZED_GAMES_DIRECTORY}"):
            st.write(file)
            with open(f'{ANALYZED_GAMES_DIRECTORY}{username}/{file}') as f:
                st.download_button('Download JSON', f) 
