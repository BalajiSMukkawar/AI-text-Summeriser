from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from transformers import pipeline
import os

app = Flask(__name__, static_folder='static')
CORS(app)

# Load summarization model (facebook/bart-large-cnn by default)
print("⏳ Loading summarization model... This may take a moment on first run.")
summarizer = pipeline("summarization")
print("✅ Model loaded successfully!")


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json

    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data['text'].strip()

    if len(text) < 50:
        return jsonify({"error": "Text is too short to summarize. Please provide at least 50 characters."}), 400

    try:
        # Adjust max_length based on input length
        input_length = len(text.split())
        max_len = min(150, max(30, input_length // 2))
        min_len = min(30, max_len - 1)

        summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)

        return jsonify({
            "summary": summary[0]['summary_text'],
            "original_length": len(text),
            "summary_length": len(summary[0]['summary_text']),
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
