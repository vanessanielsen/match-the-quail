# match-the-quail

Flask app for a quail image matching quiz. Displays baby and adult quail images on one page. Users match each chick to its adult by selecting the corresponding letter (A–F). The app records user email via Google authentication, times the quiz, scores answers server-side, and stores results in BigQuery. Designed for deployment on Google App Engine.

## Features

- Displays all quiz items in a clean grid layout  
- Tracks quiz time with a visible timer that changes color as time passes  
- Uses Google authentication to capture user email  
- Scores user answers against environment-configured correct mappings  
- Stores quiz results with timestamps in BigQuery  
- Responsive and modern UI with accessible controls  

## Setup

1. Clone the repo  
2. Ensure the Google Cloud SDK is installed and initialized:  
   ```bash
   gcloud init
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
3. Make sure app.yaml exists in the project root with the correct runtime and entrypoint.
4. Set environment variables in app.yaml or in Cloud Console:
   - `CORRECT_MAP` (JSON string mapping baby indexes to adult indexes)
   - `GOOGLE_CLOUD_PROJECT` (Google Cloud project name)
   - `BQ_DATASET` (BigQuery dataset name)  
   - `BQ_TABLE` (BigQuery table name)  
5. Deploy the app:
   ```bash
   gcloud app deploy
6. Open the app in your browser:
   ```bash
   gcloud app browse
