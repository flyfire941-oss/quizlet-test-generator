import streamlit as st
from parser import parse_input
from generator import generate_tasks

st.title("Quiz Generator for Teachers")

# Ввод
text_input = st.text_area("Paste Quizlet words here")

# Уровень
level = st.selectbox("Select level", ["A1", "A2"])

if st.button("Generate"):

    words = parse_input(text_input)

    if not words:
        st.error("No valid word pairs found")
    else:
        result = generate_tasks(words, level)

        st.subheader("📝 Test A")
        st.text(result["test_a"])

        st.subheader("📝 Test B")
        st.text(result["test_b"])

        st.subheader("✏️ Writing Task")
        st.text(result["writing"])

        st.subheader("🔑 Answer Key")
        st.text(result["answers"])
