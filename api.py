import os
import requests
from dotenv import load_dotenv

load_dotenv()

headers = {
    "authorization": '',
    "content-type": "application/json"
}

def upload_transcribe(audio_file):

    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
    upload_endpoint = 'https://api.assemblyai.com/v2/upload'

    print('uploading')
    upload_response = requests.post(
        upload_endpoint,
        headers=headers, data=audio_file
    )

    audio_url = upload_response.json()['upload_url']
    print('done')

    json = {
        "audio_url": audio_url,
        "word_boost": ["how's", "how is", "how are", "how", "what's", "what is", "what are", "what", "when", "where", "why", "who", "which", "whose", "whom", "do", "does", "did", "done", "doing", "have", "has", "had", "having", "be", "is", "are", "was", "were", "being", "been", "can", "could", "may", "might", "must", "shall", "should", "will", "would", "ought", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"],
        "boost_param": "high",
        "iab_categories": True,
        "speaker_labels": True,
        "auto_highlights": True
    }

    response = requests.post(transcript_endpoint, json=json, headers=headers)
    print(response.json())
    transcript_id = response.json()['id']
    polling_endpoint = transcript_endpoint + "/" + transcript_id

    return polling_endpoint
