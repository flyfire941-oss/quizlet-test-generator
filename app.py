import streamlit as st
from generator import generate_tasks

st.set_page_config(page_title="Quizlet Test Generator", page_icon="📝")

st.title("Quizlet Test Generator")

# Ввод слов
st.write("Paste your words (English<TAB>Russian or Russian<TAB>English), one per line:")
text_input = st.text_area("Words", height=200)

# Уровень
level = st.selectbox("Select Level", ["A1", "A2", "B1", "B2"])

# Кнопка генерации
if st.button("Generate"):
    # Парсим слова
    words = []
    for line in text_input.strip().split("\n"):
        parts = [p.strip() for p in line.replace("-", "\t").split("\t") if p.strip()]
        if len(parts) >= 2:
            # Определяем, что первое — английский, что русское
            eng, rus = (parts[0], parts[1]) if any(c.isalpha() for c in parts[0]) else (parts[1], parts[0])
            words.append((eng, rus))

    if not words:
        st.error("No valid words found. Make sure to separate English and Russian with TAB or dash.")
    else:
        result = generate_tasks(words, level)

        st.subheader("📝 Test A")
        st.text(result["test"])

        st.subheader("✏️ Writing Task")
        st.text(result["writing"])

        st.subheader("🔑 Answer Key")
        st.text(result["answers"])
