from typing import Dict
from transformers import pipeline

DEFAULT_MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"

class InterviewAnalyzer:
    """
    Wrapper around Hugging Face sentiment pipeline.
    Produces NEGATIVE/NEUTRAL/POSITIVE with default model.
    """
    def __init__(self, model_name: str = DEFAULT_MODEL, device: int = -1):
        self.sentiment_analyzer = pipeline("sentiment-analysis", model=model_name, device=device)

    def analyze(self, text: str) -> Dict[str, float]:
        result = self.sentiment_analyzer(text)[0]
        label = str(result.get("label", "")).upper()
        score = float(result.get("score", 0.0))
        return {"label": label, "score": score}

def feedback_from_label(label: str) -> str:
    label = (label or "").upper()
    if label == "POSITIVE":
        return "✅ Great job! Shows confidence."
    if label == "NEGATIVE":
        return "⚠️ Try to be more specific and add concrete examples."
    return "ℹ️ Decent start — add more details and clarity."