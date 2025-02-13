import os
import requests
import streamlit as st

def search_lyrics(band, music):
    endpoint = f'https://api.lyrics.ovh/v1/{band}/{music}'
    response = requests.get(endpoint)

    if response.status_code == 200:
        return response.json().get('lyrics', 'Lyrics not found')
    return 'Lyrics not found'

def widgets():
    image_path = os.path.join(r'C:\techWin11\pythonProjects\music-hunter\assets\logo.jpg')

    if os.path.exists(image_path):
        st.image(image_path)
    
    st.markdown(
        """
        <h1 style="font-family: 'Times New Roman', serif; color: rgb(10, 44, 28); text-align: center;">
            Music Hunter
        </h1>
        
        <p style="font-family: 'Times New Roman', serif; color: #555; text-align: center;">
            Discover and explore your favorite song lyrics in seconds, like a hunter finding its prey!
        </p>
        """, unsafe_allow_html=True)
                
def inputs():
    band = st.text_input('Enter the band name: ', key='band')
    music = st.text_input('Enter the music name: ', key='music')
    return band, music

def search_button(band, music):
    search = st.button('Search', key='search')
    
    if search:
        lyrics = search_lyrics(band, music)
        if lyrics != 'Lyrics not found':
            st.success('Success!')
            st.write(lyrics)
        else:
            st.error('Lyrics not found')

def footer():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 10px;">
        <p style="font-size: 16px; color: #555;">Developed by Lucas Felipe</p>
    </div>
                
    <div style="display: flex; justify-content: center; gap: 20px;">
        <a href="https://github.com/lucasfelipecastro" target="_blank">
            <img src="https://img.icons8.com/?size=100&id=12599&format=png&color=000000" width="40" alt="GitHub">
        </a>
        <a href="https://www.linkedin.com/in/lucasfelipecastro" target="_blank">
            <img src="https://img.icons8.com/?size=100&id=8808&format=png&color=000000" width="40" alt="LinkedIn">
        </a>
    </div>
                """, unsafe_allow_html=True)

if __name__ == '__main__':
    widgets()
    band, music = inputs()
    search_button(band, music)
    footer()