import os
import requests
import streamlit as st

def search_lyrics(band, music):
    endpoint = (f'https://api.lyrics.ovh/v1/{band}/{music}')
    response = requests.get(endpoint)

    if response.status_code == 200:
        return response.json()['lyrics']
    return 'Lyrics not found'

def widgets():
    image_path = os.path.join(r'C:\techWin11\pythonProjects\music-hunter\assets\logo.jpg')

    if os.path.exists(image_path):
        st.image(image_path, width=300)
    st.title('Music Hunter')

def inputs():
    band = st.text_input('Enter the band name', key='band')
    music = st.text_input('Enter the music name', key='music')
    
