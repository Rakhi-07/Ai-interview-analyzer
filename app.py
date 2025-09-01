import streamlit as st
from preprocess import clean_text
from model import InterviewAnalyzer, feedback_from_label

st.set_page_config(page_title="AI Interview Analyzer (Lite)", page_icon="🧠", layout="centered")

st.title("🧠 AI Interview Analyzer (Lite – Text Only)")
st.write("Select a question category, pick a question (or write your own), then answer it.")

categories = {
    "General HR Questions": [
        "Tell me about yourself.",
        "What are your strengths?",
        "What are your weaknesses?",
        "Why should we hire you?",
        "Where do you see yourself in 5 years?",
        "Describe a challenge you faced and how you handled it.",
        "Why do you want to work at our company?"
    ],
    "General Project Questions": [
        "What was your role in the project?",
        "What challenges did you face and how did you solve them?",
        "What technologies did you use and why?",
        "How did your project help the users or solve a problem?",
        "If you had more time, what improvements would you add?"
    ],
    "Custom Question (Write Your Own)": []
}

# Category selection
category = st.selectbox("Select Question Category", list(categories.keys()))

# Question selection / input
if category == "Custom Question (Write Your Own)":
    question = st.text_input("Enter your custom interview question")
else:
    question = st.selectbox("Select Question", categories[category])

if question:
    st.subheader("📌 Question:")
    st.write(question)

example_text = (
    "I am confident in my skills and have led multiple projects with measurable outcomes, "
    "collaborating with cross-functional teams to deliver on time."
)

if "text" not in st.session_state:
    st.session_state["text"] = ""

st.text_area(
    "Your answer",
    key="text",
    height=180,
    placeholder="Type your answer here...",
)

col1, col2 = st.columns([1,1])
with col1:
    analyze_clicked = st.button("Analyze")
with col2:
    if st.button("Use Sample"):
        st.session_state["text"] = example_text
        st.rerun()

if analyze_clicked:
    user_text = (st.session_state.get("text") or "").strip()
    if not user_text:
        st.warning("Please enter an answer to analyze.")
    else:
        with st.spinner("Analyzing..."):
            cleaned = clean_text(user_text)
            analyzer = InterviewAnalyzer()
            result = analyzer.analyze(cleaned)

        st.subheader("Result")
        st.metric("Sentiment", result["label"], delta=f"{result['score']:.2%}")
        st.info(feedback_from_label(result["label"]))
        with st.expander("Details"):
            st.write("**Question asked:**", question)
            st.write("**Cleaned text:**", cleaned)
            st.write("**Raw result:**", result)
        st.caption("Tip: Strengthen answers with specific metrics, actions, and outcomes (STAR method).")
else:
    st.caption("Paste your answer above or click **Use Sample** to try a prefilled response.")
