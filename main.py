import os
import json
from datetime import datetime
from flask import Flask, render_template, request
from google.cloud import bigquery

app = Flask(__name__)

NUM_QUIZ = 6

# Load correct answer map from environment variable (JSON string)
CORRECT_MAP = json.loads(os.environ.get('CORRECT_MAP', '{}'))
CORRECT_MAP = {int(k): int(v) for k, v in CORRECT_MAP.items()}

bq_client = bigquery.Client()

BQ_DATASET = os.environ.get('BQ_DATASET', 'quail_quiz')
BQ_TABLE = os.environ.get('BQ_TABLE', 'results')
BQ_TABLE_REF = f"{bq_client.project}.{BQ_DATASET}.{BQ_TABLE}"


@app.route('/')
def index():
    babies = [f'babies/baby{i}.jpg' for i in range(1, NUM_QUIZ + 1)]
    adults = [f'adults/adult{i}.jpg' for i in range(1, NUM_QUIZ + 1)]
    user_email = request.headers.get('X-Goog-Authenticated-User-Email')
    if user_email is None:
        user_email = "test@test.com"
    return render_template(
        'index.html',
        babies=babies,
        adults=adults,
        num=NUM_QUIZ,
        enumerate=enumerate,
        chr=chr,
        user_email=user_email
    )


@app.route('/submit', methods=['POST'])
def submit():
    user_email = request.headers.get('X-Goog-Authenticated-User-Email')
    if user_email is None:
        user_email = "test@test.com"

    answers = {}
    correct_count = 0
    for i in range(1, NUM_QUIZ + 1):
        val = request.form.get(f'answer_{i}')
        try:
            sel = int(val)
        except (TypeError, ValueError):
            sel = None
        answers[i] = sel
        if sel is not None and CORRECT_MAP.get(i) == sel:
            correct_count += 1

    try:
        time_seconds = float(request.form.get('time_seconds', 0))
    except (TypeError, ValueError):
        time_seconds = 0.0

    row = {
        "email": user_email,
        "correct": correct_count,
        "time_seconds": time_seconds,
        "answers_json": json.dumps(answers),
        "created_at": datetime.utcnow().isoformat()
    }

    errors = bq_client.insert_rows_json(BQ_TABLE_REF, [row])
    if errors:
        app.logger.error(f"BigQuery insert errors: {errors}")

    return render_template(
        'result.html',
        email=user_email,
        correct=correct_count,
        total=NUM_QUIZ,
        time_seconds=time_seconds
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)
