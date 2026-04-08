import streamlit as st
from generator import parse_words, generate_tasks

st.set_page_config(page_title="Quiz Generator", layout="wide")
st.title("Quiz Generator")

words_input = st.text_area(
    "Paste your words (English or Russian TAB/SPACE/RUS-ENG), one per line:",
    height=250
)

level = st.selectbox("Select Level", ["A1", "A2", "B1", "B2"])

if st.button("Generate"):
    if not words_input.strip():
        st.warning("Please paste some words first!")
    else:
        word_pairs = parse_words(words_input)
        if not word_pairs:
            st.error("No valid words found. Please check your input.")
        else:
            translate_text, write_text, discuss_text, answer_key_text = generate_tasks(word_pairs)

            st.subheader("Translate:")
            st.text(translate_text)

            st.subheader("Write:")
            st.text(write_text)

            st.subheader("Discuss:")
            st.text(discuss_text)

            st.subheader("🔑 Answer Key:")
            st.text(answer_key_text)
