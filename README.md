# 🧠 AI Text Summarizer — Deep Learning Mini Project

An AI-powered web application that automatically summarizes long text into concise, readable summaries using state-of-the-art Natural Language Processing (NLP) models.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white)
![HuggingFace](https://img.shields.io/badge/🤗_Transformers-4.36+-FFD21E)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 What Is This Project?

This is a **Deep Learning Mini Project** that demonstrates the practical application of **transformer-based NLP models** for automatic text summarization.

### How It Works

1. **You paste** a long piece of text (article, essay, report, etc.) into the input box.
2. **The AI model** (Facebook's BART — Bidirectional and Auto-Regressive Transformers) processes the text.
3. **You get** a concise, meaningful summary in seconds.

### The Technology Behind It

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Flask (Python) | REST API server |
| **AI Model** | Hugging Face `transformers` | Text summarization pipeline |
| **Model Used** | `facebook/bart-large-cnn` | Pre-trained summarization model |
| **Frontend** | HTML, CSS, JavaScript | User interface |
| **Deep Learning Framework** | PyTorch | Model inference engine |

### What is BART?

**BART (Bidirectional and Auto-Regressive Transformers)** is a sequence-to-sequence model developed by Facebook AI. It's pre-trained by:
1. Corrupting text with a noising function (masking, deletion, shuffling).
2. Learning to reconstruct the original text.

The `bart-large-cnn` variant is fine-tuned specifically on the **CNN/DailyMail** news dataset for abstractive text summarization.

---

## 🚀 How to Run This Project

### Prerequisites

- **Python 3.9 or higher** installed on your system
- **pip** (Python package manager)
- **Internet connection** (for first-time model download ~ 1.6 GB)

### Step-by-Step Setup

```bash
# 1. Navigate to the project directory
cd DLMINI

# 2. (Optional but recommended) Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python app.py
```

### After Running

1. Open your browser and go to: **http://127.0.0.1:5000**
2. Paste any long text into the input box (minimum 50 characters)
3. Click **"Summarize"** and wait for the AI to process
4. See your summary along with reduction statistics!

> ⚠️ **First Run Note**: The model (~1.6 GB) will be downloaded automatically on the first run. This may take a few minutes depending on your internet speed. Subsequent runs will use the cached model.

---

## 📁 Project Structure

```
DLMINI/
├── app.py                  # Flask backend server & API
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── Doc.txt                 # Original combined code file
└── static/
    ├── index.html          # Frontend HTML page
    ├── style.css           # Styling with animations
    └── script.js           # Client-side JavaScript logic
```

### File Descriptions

| File | Description |
|------|-------------|
| `app.py` | The Flask server that loads the AI model and exposes a `/summarize` API endpoint. It receives text via POST request and returns the AI-generated summary. |
| `static/index.html` | The main web page with the input textarea, summarize button, and output display area. |
| `static/style.css` | Premium dark-themed UI with glassmorphism effects, animated gradient orbs, floating particles, and micro-animations. |
| `static/script.js` | Handles user interactions — sending text to the API, displaying results, toast notifications, clipboard functions, and background animations. |
| `requirements.txt` | Lists all Python packages needed: Flask, flask-cors, transformers, and torch. |

---

## 🔌 API Reference

### `POST /summarize`

Summarizes the provided text.

**Request Body:**
```json
{
    "text": "Your long text to summarize goes here..."
}
```

**Success Response (200):**
```json
{
    "summary": "The AI-generated summary text.",
    "original_length": 1500,
    "summary_length": 280
}
```

**Error Response (400):**
```json
{
    "error": "Text is too short to summarize. Please provide at least 50 characters."
}
```

---

## ✨ Features

- 🤖 **AI-Powered Summarization** — Uses Facebook's BART model for high-quality abstractive summaries
- 📊 **Stats Dashboard** — Shows original vs. summary length and reduction percentage
- 📋 **Copy & Paste** — One-click clipboard integration
- ⌨️ **Keyboard Shortcut** — Press `Ctrl + Enter` to summarize instantly
- 🎨 **Premium Dark UI** — Glassmorphism, animated particles, gradient effects
- 📱 **Responsive Design** — Works on desktop, tablet, and mobile
- 🔔 **Toast Notifications** — Visual feedback for all actions
- ⚡ **Smart Length Adjustment** — Summary length adapts based on input size

---

## 🛠️ Technologies Used

- **Python 3** — Programming language
- **Flask** — Lightweight web framework
- **Hugging Face Transformers** — NLP model library
- **PyTorch** — Deep learning framework
- **BART (facebook/bart-large-cnn)** — Pre-trained summarization model
- **HTML5 / CSS3 / JavaScript** — Frontend technologies

---

## 📝 Notes

- The model requires approximately **1.6 GB** of disk space and **~2 GB RAM** during inference.
- GPU is optional but recommended for faster inference. The model will automatically use GPU if CUDA is available.
- For very long texts (>1024 tokens), the model will process the first 1024 tokens.

---

## 👥 Team

Deep Learning Mini Project — Text Summarization using Transformers

---

*Built with ♥ using Flask & Hugging Face Transformers*
