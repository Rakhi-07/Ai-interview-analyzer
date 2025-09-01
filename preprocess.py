import re
import nltk
from nltk.corpus import stopwords

_STOPWORDS = None

def _ensure_stopwords():
    global _STOPWORDS
    if _STOPWORDS is None:
        try:
            _STOPWORDS = set(stopwords.words("english"))
        except LookupError:
            nltk.download("stopwords")
            _STOPWORDS = set(stopwords.words("english"))

def clean_text(text: str) -> str:
    """
    Lowercase, remove non-letters, and strip English stopwords.
    Returns a space-joined string of meaningful tokens.
    """
    if not isinstance(text, str):
        text = str(text) if text is not None else ""
    _ensure_stopwords()
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)   # keep letters/space
    text = re.sub(r"\s+", " ", text).strip()   # collapse spaces
    words = [w for w in text.split() if w and w not in _STOPWORDS]
    return " ".join(words)