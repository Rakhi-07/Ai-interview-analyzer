import pytest
from model import InterviewAnalyzer

@pytest.mark.slow
def test_model_smoke():
    analyzer = InterviewAnalyzer()
    out = analyzer.analyze("I am confident about my skills and impact.")
    assert "label" in out and "score" in out
    assert isinstance(out["score"], float)