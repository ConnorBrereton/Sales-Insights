
# 💼 Sales Insights 📞

This project allows anyone to upload a video file and be presented with a transcript and extracted questions & answers. The target user is a sales executive that wants to look back at questions asked during a call with a prospect/customer. [Here](https://connorbrereton-sales-insights-summarizer-4owrfp.streamlit.app/) is a link to a live demo if you don't want to deploy locally.




## Authors / License

- [@ConnorBrereton](https://github.com/ConnorBrereton)
* [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



## Pre-reqs

Must have ```git``` installed. If you don't [here](https://github.com/git-guides/install-git) is a great guide.

## Environment Variables (Pre-Deployment)

To run this project, you will need to add the following environment variables to your ```.env``` file in the *same folder path as the app, ```summarizer.py```.

```bash
$ touch .env
$ vi .env

copy and paste your key/value using API_KEY=<your_api_key_no_quotes> format

:wq -> ENTER
```


## Local Deployment

Note: if you see a ```KeyError: 'upload_url'``` if means you just need to paste in your API key appropriately.

To deploy this project run:

```bash
  git clone https://github.com/ConnorBrereton/Sales-Insights.git
```

Next, naviate to the app directory.
```bash
cd Sales-Insights/
```

Install all of the dependencies using *pip3*
```bash
pip3 install -r requirements.txt
```

To run the application using Streamlit do the following:
```bash
python3 -m streamlit run summarizer.py
```

You should see this image pop up on ```localhost:8501``` automatically.

![App Screenshot]([https://paste.pics/9eb14df4da0349be3523ef73e1a33e94](https://user-images.githubusercontent.com/13909335/235801065-0e7eb1b2-73fb-422d-baf2-d8944ae2d9bc.png))


## Demo

Below is a demo of how the application can be utilized for call analysis to extract questions and answers with full context.


## Documentation

* [AssemblyAI](https://www.assemblyai.com/docs/)
* [Streamlit](https://docs.streamlit.io/)
* [StackOverflow](https://stackoverflow.com)



## Roadmap

- Change color scheme to match AssemblyAI.
- Breakdown of speakers using Assembly's Speaker Diarization.
- Dockerize the application to avoid all dependency management.
- Remove filler words from Q&A - Breakdown.
- Use profanity filtering to see if prospect/rep used profanity during the call.
- Add webhooks to avoid using temporary variables to manage state within the application.
