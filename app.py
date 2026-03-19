import streamlit as st
from generator import generate_tests

st.title("📘 Quiz Generator")

# Функция очистки слова/фразы
def clean_term(term):
    term = term.strip()

    # убираем скобки (всё после них)
    if "(" in term:
        term = term.split("(")[0].strip()

    # убираем варианты через слэш (берём первую часть)
    if "/" in term:
        term = term.split("/")[0].strip()

    # убираем лишние пробелы
    term = " ".join(term.split())

    # фильтр: слишком длинные выражения
    if len(term.split()) > 4:
        return None

    return term


# Ввод текста
text_input = st.text_area(
    "Paste vocabulary (term - translation):",
    height=250,
    placeholder="a T-shirt - футболка"
)

# Выбор уровня
level = st.selectbox("Select level", ["A1", "A2"])

if st.button("Generate"):
    lines = text_input.split("\n")

    words = []

    for line in lines:
        if "-" in line:
            term, translation = line.split("-", 1)

            term = clean_term(term)
            translation = translation.strip()

            if term and translation:
                words.append((term, translation))

    if not words:
        st.error("No valid words found. Check your input format.")
    else:
        result = generate_tests(words, level)

        st.subheader("📝 Test A")
        st.text(result["test_a"])

        st.subheader("📝 Test B")
        st.text(result["test_b"])

        st.subheader("✏️ Writing Task")
        st.text(result["writing"])

        st.subheader("🔑 Answer Key")
        st.text(result["answers"])
