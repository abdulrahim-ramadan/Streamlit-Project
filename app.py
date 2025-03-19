import streamlit as st
import re
from collections import Counter

# --- App Configuration ---
st.set_page_config(page_title="Text Analyzer", page_icon="🔍", layout="centered")
st.markdown("<h1 style='text-align: center; font-size: 40px;'>🔍 Simple Text Analyzer</h1>", unsafe_allow_html=True)

# --- Dark Mode Toggle ---
dark_mode = st.toggle("🌙 Enable Dark Mode")

# --- Apply Dark Mode Styling ---
if dark_mode:
    st.markdown(
        """
        <style>
        body { background-color: #121212; color: white; }
        .stTextArea textarea { background-color: #333; color: white; font-size: 18px; }
        .stDataFrame { background-color: #333; color: white; }
        .stMetric { background-color: #222; color: white; border-radius: 10px; padding: 15px; font-size: 22px; }
        .stButton>button { background-color: #444; color: white; border-radius: 8px; padding: 10px 20px; font-size: 18px; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# --- User Input Section ---
st.markdown("<h3 style='font-size: 24px;'>📝 Enter your text below:</h3>", unsafe_allow_html=True)
user_input = st.text_area("", height=200)

# --- Analyze Button ---
if st.button("🚀 Analyze Text", help="Click to analyze the text!"):
    if user_input:
        # --- Text Processing ---
        words = [word.strip(".,!?;:()[]{}") for word in user_input.split()]
        num_words = len(words)
        num_chars = len(user_input.replace(" ", ""))
        sentences = re.split(r'[.!?]+', user_input)
        num_sentences = len([s for s in sentences if s.strip()])
        word_counts = Counter(words)
        most_common_words = word_counts.most_common(5)

        # --- Progress Bar Effect ---
        progress = st.progress(0)
        for percent in range(100):
            progress.progress(percent + 1)

        # --- Display Results in Large Text ---
        st.markdown("<h2 style='text-align: center;'>📊 Analysis Results</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        col1.metric("📌 Words", num_words)
        col2.metric("📝 Characters", num_chars)
        col3.metric("📖 Sentences", num_sentences)

        # --- Display Most Frequent Words ---
        st.markdown("<h2>🔝 Most Frequent Words</h2>", unsafe_allow_html=True)
        st.markdown(
            """
            <style>
            table {
                width: 100%;
                border-collapse: collapse;
                font-size: 18px;
            }
            th, td {
                padding: 10px;
                text-align: center;
                border: 1px solid #ddd;
            }
            th {
                background-color: #444;
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        st.write("**Word | Count**")
        st.write("--- | ---")
        for word, count in most_common_words:
            st.write(f"🔹 {word} | {count}")

        # --- Fun Balloon Effect ---
        st.balloons()

    else:
        st.warning("⚠️ Please enter some text for analysis!")

# --- General Styling for a Clean Look ---
st.markdown(
    """
    <style>
    .stTextArea textarea { font-size: 20px; direction: ltr; text-align: left; }
    </style>
    """,
    unsafe_allow_html=True,
)