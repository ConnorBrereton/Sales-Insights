import streamlit as st
import requests
import pandas as pd
from api import *

# Setting the CSS and HTML elements via Streamlit to avoid having
# to have so many files in the overall project. That's a lot of the
# value of using Streamlit for building the frontend.
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

# This is the title on the UI that gets automatically
# set by Streamlit.
st.title('💼 Sales Insights Summarizer 📞')

# Session State is a way to share variables between reruns,
# for each user session. In addition to the ability to store and persist state
# to be used in displaying data to the application.
if 'start_point' not in st.session_state:
    st.session_state['start_point'] = 0

# This is a flag used for the transcription processing algorithm.
response_ans = False

def update_start(start_t):
    st.session_state['start_point'] = int(start_t/1000)

    uploaded_file = st.file_uploader('Powered by AssemblyAI API')

    # Once file is uploaded go ahead and transcribe the audio that's hosted
    # on a CDN.
    if uploaded_file is not None:
        st.audio(uploaded_file, start_time=st.session_state['start_point'])
        polling_endpoint = upload_transcribe(uploaded_file)

        status='submitted'
        
        # Here is where the audio gets transcribed to JSON data and it
        # ultimately gets deserialized by the JSON parser.
        while status != 'completed':
            polling_response = requests.get(polling_endpoint, headers=headers)
            print(polling_response.json())
            status = polling_response.json()['status']

            if status == 'completed':

                # Get/show the transcript to the UI so that the entire conversation
                # can be viewed to get more clarify around the Q/A summary.
                transcript = polling_response.json()['text']
                st.subheader('Call Transcript')
                with st.expander('Expand to see call transcript below...'):
                    st.write(transcript)

                # Get/show the qusetions and answers using a parsing algorithm that is
                # roughly based on the sentence segmentation that's described in this
                # section of NLTK - https://www.nltk.org/book/ch06.html (look at section 2.1).
                st.subheader('Q&A - Breakdown')
                sentence_response = requests.get(polling_endpoint + '/sentences', headers=headers)
                sentences = sentence_response.json()['sentences']

                # Here we're going to build out Q/A bullet points that is based on another
                # "layer" of classifiction to the parsed trascript data.
                with st.expander('Expand to see Q&A w/ context below...'):
                    for s in sentences:
                        if '?' in s['text']:
                            st.write('* ' + 'Q: ' + s['text'])
                            response_ans = False
                        elif '?' not in s['text'] and response_ans == False:
                            st.write('* ' + 'A: ' + s['text'])
                            response_ans = True
                        else:
                            continue
