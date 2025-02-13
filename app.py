import os
import requests
import streamlit as st

def search_lyrics(band, music):
    endpoint = (f'https://api.lyrics.ovh/v1/{band}/{music}')
    response = requests.get(endpoint)

    if response.status_code == 200:
        return response.json()['lyrics']
    return 'Lyrics not found'

