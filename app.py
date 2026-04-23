import streamlit as st
from generator import parse_words, generate_tasks, generate_pdf

st.set_page_config(page_title="Worksheet Generator", layout="wide")

# === СТИЛИ ===
st.markdown("""
<style>
.main {
    background-color: #fafafa;
}

.block {
    background-color: white;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    margin-bottom: 15px;
}

.title {
    font-size: 28px;
    font-weight: 600;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 14px;
    color: #666;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# === HEADER ===
st.markdown('<div class="title">Vocabulary Worksheet Generator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Create clean, printable classroom worksheets in seconds</div>',
    unsafe_allow_html=True
)

# === НАСТРОЙКИ ===
col_settings1, col_settings2 = st.columns(2)

with col_settings1:
    language = st.selectbox(
        "Worksheet language / Язык задания",
        ["English", "Русский"]
    )

with col_settings2:
    st.markdown("### Worksheet sections")

    include_translate = st.checkbox("Translation", value=True)
    include_write = st.checkbox("Writing", value=True)
    include_discuss = st.checkbox("Speaking", value=True)

st.divider()

# === ТЕКСТЫ ===
if language == "English":
    instructions = (
        "Enter one word pair per line.\n"
        "First = term, second = translation or definition.\n"
        "Use space, hyphen (-) or tab.\n\n"
        "Example:\n"
        "cat - кот\n"
        "apple яблоко"
    )

    button_text = "Generate worksheet"
    warning_text = "Please enter some words first."
    error_text = "No valid words found."

    translate_label = "Translate"
    write_label = "Write"
    discuss_label = "Discuss"
    answer_label = "🔑 Answer Key"

else:
    instructions = (
        "Введите одну пару слов на строку.\n"
        "Первое — термин.\n"
        "Второе — перевод или определение.\n\n"
        "Пример:\n"
        "cat - кот\n"
        "apple яблоко"
    )

    button_text = "Сгенерировать"
    warning_text = "Введите слова."
    error_text = "Ошибка формата."

    translate_label = "Переведите"
    write_label = "Напишите"
    discuss_label = "Обсудите"
    answer_label = "🔑 Ответы"

selected_sections = []

if include_translate:
    selected_sections.append("Translation")

if include_write:
    selected_sections.append("Writing")

if include_discuss:
    selected_sections.append("Speaking")

# === ДВЕ КОЛОНКИ ===
col1, col2 = st.columns([1, 1])

# === INPUT ===
with col1:
    st.markdown('<div class="block">', unsafe_allow_html=True)

    st.subheader("Input")
    st.write(instructions)

    words_input = st.text_area("", height=300)

    generate = st.button(button_text)

    st.markdown('</div>', unsafe_allow_html=True)

# === PREVIEW ===
with col2:
    st.markdown('<div class="block">', unsafe_allow_html=True)

    st.subheader("Preview")

    if generate:

        if not words_input.strip():
            st.warning(warning_text)

        elif not selected_sections:
            st.warning("Please select at least one worksheet section.")

        else:
            word_pairs = parse_words(words_input)

            if not word_pairs:
                st.error(error_text)

            else:
                translate, write, discuss, answers = generate_tasks(word_pairs, language)

                if "Translation" in selected_sections:
                    st.markdown(f"**{translate_label}**")
                    st.text(translate)

                if "Writing" in selected_sections:
                    st.markdown(f"**{write_label}**")
                    st.text(write)

                if "Speaking" in selected_sections:
                    st.markdown(f"**{discuss_label}**")
                    st.text(discuss)

                st.markdown(f"**{answer_label}**")
                st.text(answers)

                pdf_file = generate_pdf(
                    translate,
                    write,
                    discuss,
                    answers,
                    language,
                    selected_sections
                )

                with open(pdf_file, "rb") as f:
                    st.download_button(
                        "Download PDF",
                        f,
                        file_name="worksheet.pdf"
                    )

    st.markdown('</div>', unsafe_allow_html=True)
