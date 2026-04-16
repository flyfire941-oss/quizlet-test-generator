import streamlit as st
from generator import parse_words, generate_tasks, generate_pdf

st.set_page_config(page_title="Vocabulary Worksheet Generator", layout="centered")

st.title("Vocabulary Worksheet Generator")
st.caption("Create printable classroom activities quickly and easily")

st.divider()

st.markdown("### Enter your word list")
st.write(
    "Add **one word pair per line**.\n"
    "- The first item is always the **term or word**.\n"
    "- The second item is the **definition or translation**.\n"
    "- You can use a space, hyphen `-`, or tab to separate the two.\n\n"
    "**Examples:**\n"
    "cat - кот\n"
    "apple яблоко\n"
    "photosynthesis Photosynthesis is the process by which plants make food"
)

words_input = st.text_area("Your word list here:", height=200)

st.divider()

if st.button("Generate worksheet"):
    if not words_input.strip():
        st.warning("Please enter some words first.")
    else:
        word_pairs = parse_words(words_input)
        if not word_pairs:
            st.error("No valid words found. Please check your input format.")
        else:
            translate, write, discuss, answers = generate_tasks(word_pairs)

            st.markdown("### Worksheet Preview")
            st.markdown("**Translate**")
            st.text(translate)
            st.markdown("**Write**")
            st.text(write)
            st.markdown("**Discuss**")
            st.text(discuss)
            st.markdown("**🔑 Answer Key**")
            st.text(answers)

            pdf_file = generate_pdf(translate, write, discuss, answers)
            with open(pdf_file, "rb") as f:
                st.download_button(
                    label="Download Worksheet as PDF",
                    data=f,
                    file_name="worksheet.pdf",
                    mime="application/pdf"
                )
