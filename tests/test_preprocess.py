from preprocess import clean_text

def test_clean_text_basic():
    assert clean_text("Hello!!! This is a TEST.") == "hello test"

def test_clean_text_numbers_punct():
    assert clean_text("Year 2025: Growth +45%!") == "year growth"