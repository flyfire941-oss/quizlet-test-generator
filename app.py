import streamlit as st
from parser import parse_quizlet
from generator import split_variants, generate_doc

st.set_page_config(page_title="Quiz Generator")

st.title("📘 Quiz Generator")

url = st.text_input("Paste Quizlet link")
level = st.selectbox("Level", ["A1", "A2", "B1", "B2"])

if st.button("Generate"):
    words = parse_quizlet(url)

    if not words:
        st.error("No words found")
    else:
        st.success(f"{len(words)} words loaded")

        a, b = split_variants(words)

        docA = generate_doc(a, level, "A")
        docB = generate_doc(b, level, "B")

        docA.save("A.docx")
        docB.save("B.docx")

        with open("A.docx", "rb") as f:
            st.download_button("Download A", f)

        with open("B.docx", "rb") as f:
            st.download_button("Download B", f)
