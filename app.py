import streamlit as st
from generator import generate_tests

st.title("📘 Quiz Generator")

text_input = st.text_area(
    "Paste words (term - translation):",
    height=200
)

level = st.selectbox("Select level", ["A1", "A2"])

if st.button("Generate"):
    lines = text_input.split("\n")

    words = []
    for line in lines:
        if "-" in line:
            term, translation = line.split("-", 1)
            term = term.strip()
            translation = translation.strip()

            # фильтр: убираем длинные предложения
            if len(term.split()) <= 3:
                words.append((term, translation))

    if not words:
        st.error("No suitable words found")
    else:
        result = generate_tests(words, level)

        st.subheader("📝 Test A")
        st.text(result["test_a"])

        st.subheader("📝 Test B")
        st.text(result["test_b"])

        st.subheader("✏️ Writing (use 3-5 words)")
        st.text(result["writing"])

        st.subheader("🔑 Answer Key")
        st.text(result["answers"])
