# app.py
from flask import Flask, render_template, request
from textblob import TextBlob
from summarizer import Summarizer, TransformerSummarizer

app = Flask(__name__)
language = 'en'  # Default language

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/language', methods=['POST'])
def set_language():
    global language
    language = request.form['language']
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']

        # Perform sentiment analysis
        blob = TextBlob(text)
        sentiment = "Positive" if blob.sentiment.polarity > 0 else "Negative" if blob.sentiment.polarity < 0 else "Neutral"

        # Generate summary in the selected language
        summarizer = Summarizer()
        if language == 'en':
            summary = summarizer(text, ratio=0.2)  # English summary
        else:
            # Use TransformerSummarizer for non-English languages
            summarizer = TransformerSummarizer()
            summary = summarizer(text, ratio=0.2)

        return render_template('index.html', text=text, sentiment=sentiment, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
