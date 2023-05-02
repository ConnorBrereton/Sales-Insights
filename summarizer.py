import streamlit as st
import requests
import pandas as pd
from api import *

st.set_page_config(
    page_title="Sales Insights Summarizer",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.assemblyai.com/docs',
        'Report a bug': "https://www.github.com/assemblyai/assemblyai-summarizer/issues",
        'About': "Developed by Connor Brereton, May 2023"
    }
)

st.title('💼 Sales Insights Summarizer 📞')

if 'start_point' not in st.session_state:
    st.session_state['start_point'] = 0

def update_start(start_t):
    st.session_state['start_point'] = int(start_t/1000)

uploaded_file = st.file_uploader('Please upload a file...')

if uploaded_file is not None:
    st.audio(uploaded_file, start_time=st.session_state['start_point'])
    polling_endpoint = upload_transcribe(uploaded_file)
    
    status='submitted'
    while status != 'completed':
        polling_response = requests.get(polling_endpoint, headers=headers)
        print(polling_response.json())
        status = polling_response.json()['status']

        if status == 'completed':

            # Get/Show the transcript
            transcript = polling_response.json()['text']
            st.subheader('Call Transcript')
            with st.expander('Expand to see call transcript below...'):
                st.write(transcript)

            # Get/Show the paragraphs with questions in them
            st.subheader('Q&A - Breakdown')
            paragraph_response = requests.get(polling_endpoint + '/paragraphs', headers=headers)
            paragraphs = paragraph_response.json()['paragraphs']

            with st.expander('Expand to see Q&A w/ context below...'):
                for p in paragraphs:
                    if '?' in p['text']:
                        st.write(p['text'])
                    else:
                        continue
