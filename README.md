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
2. Set required environment variables:  
   - `CORRECT_MAP` (JSON string mapping baby indexes to adult indexes)  
   - `BQ_DATASET` (BigQuery dataset name)  
   - `BQ_TABLE` (BigQuery table name)  
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
