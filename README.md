# Ai-interview-analyzer
AI-powered Interview Question Analyzer built with Streamlit and Hugging Face.
An AI-powered interview preparation tool that analyzes your answers to common interview questions.
Built with Python, Streamlit, and Hugging Face Transformers.

Features:

1- Pre-loaded interview question categories (HR, Technical, etc.)
2- User can type or paste answers in a text box
3- AI analyzes answers for sentiment and clarity
4- Displays feedback with confidence score
5- Real-time response with loading spinner
6- Simple and interactive web interface

Frontend (UI):

Streamlit → for building the interactive web app
Streamlit components used:

1- st.text_area() → for user input
2- st.button() → to trigger analysis
3- st.metric() → to display score
4- st.info() → to show tips/feedback
5- st.spinner() → to indicate processing

Backend:

Python Functions → handle user input, call ML model, process results
Hugging Face Transformers → pre-trained NLP models for sentiment/analysis
NLTK (Natural Language Toolkit) → basic text processing
