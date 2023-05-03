import os
import requests
from dotenv import load_dotenv

load_dotenv()

headers = {
    "authorization": os.getenv('API_KEY'),
    "content-type": "application/json"
}

def upload_transcribe(audio_file):

    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
    upload_endpoint = 'https://api.assemblyai.com/v2/upload'

    print('The file is being uploaded to AssemblyAI infrastructure...')
    upload_response = requests.post(
        upload_endpoint,
        headers=headers, data=audio_file
    )

    audio_url = upload_response.json()['upload_url']
    print('Fetching the audio data...')

    # Here we boost certain words to extract questions. This is similar to how Python spaCy's
    # PhraseMatcher but an order of magnitude more accurate. Also, can ensemble different
    # algorithms together via JSON parameters that are turned on.
    # By boosting words we increase the AI's sensitivity to these phrases, therefore increasing
    # the accuracy of these different question and answers extraction.
    #
    # We turn on dual channels to ensure that we are discerning the different people in the
    # audio call who are speaking.
    json = {
        "audio_url": audio_url,
        "word_boost": ["how's", "how is", "how are", "how", "what's", "what is", "what are", "what", "when", "where", "why", "who", "which", "whose", "whom", "do", "does", "did", "done", "doing", "have", "has", "had", "having", "be", "is", "are", "was", "were", "being", "been", "can", "could", "may", "might", "must", "shall", "should", "will", "would", "ought", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "sales intelligence"],
        "boost_param": "high",
        "dual_channel": True,
        "iab_categories": True,
        "auto_highlights": True
    }

    response = requests.post(transcript_endpoint, json=json, headers=headers)
    print('Parsing the transcript ID to run NLP on the transcript...')
    transcript_id = response.json()['id']
    polling_endpoint = transcript_endpoint + "/" + transcript_id
    
    return polling_endpoint
