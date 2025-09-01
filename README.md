# 🧠 AI Interview Analyzer (Lite – Text Only)

A minimal Streamlit app that cleans a user's interview answer, runs sentiment analysis using a BERT-family model from Hugging Face, and returns simple feedback (Positive/Negative/Neutral) with a confidence score.

## Project Structure
```
ai-interview-analyzer-lite/
├─ app.py
├─ model.py
├─ preprocess.py
├─ requirements.txt
├─ tests/
│  ├─ test_preprocess.py
│  └─ test_model_smoke.py
└─ README.md
```

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -c "import nltk; nltk.download('stopwords')"
streamlit run app.py
```