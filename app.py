import streamlit as st
from generator import parse_words, generate_tasks

st.set_page_config(page_title="Vocabulary Task Generator", layout="wide")

st.title("Vocabulary Task Generator")
st.caption("Create simple classroom activities from a list of words")

st.write("Enter your word list below. You can use English–Russian or Russian–English pairs, one per line.")

words_input = st.text_area(
    "Example:\ncat - кот\nяблоко apple",
    height=250
)

if st.button("Generate"):
    if not words_input.strip():
        st.warning("Please paste some words first!")
    else:
        word_pairs = parse_words(words_input)
        if not word_pairs:
            st.error("No valid words found. Please check your input.")
        else:
            translate_text, write_text, discuss_text, answer_key_text = generate_tasks(word_pairs)

            st.subheader("Translate")
            st.text(translate_text)

            st.subheader("Write")
            st.text(write_text)

            st.subheader("Discuss")
            st.text(discuss_text)

            st.subheader("🔑 Answer Key")
            st.text(answer_key_text)
