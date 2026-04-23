import streamlit as st
from generator import parse_words, generate_tasks, generate_pdf

st.set_page_config(
    page_title="Vocabulary Worksheet Generator",
    layout="centered"
)

st.title("Vocabulary Worksheet Generator")

# === ЯЗЫК ===
language = st.radio(
    "Select worksheet language / Выберите язык задания:",
    ["English", "Русский"]
)

st.divider()

# === ВЫБОР ЗАДАНИЙ ===
st.subheader("Worksheet sections")

include_translate = st.checkbox("Translation", value=True)
include_write = st.checkbox("Writing", value=True)
include_discuss = st.checkbox("Speaking", value=True)

selected_sections = []

if include_translate:
    selected_sections.append("Translation")

if include_write:
    selected_sections.append("Writing")

if include_discuss:
    selected_sections.append("Speaking")

st.divider()

# === ТЕКСТЫ ===
if language == "English":
    st.caption("Create printable classroom activities quickly and easily")

    instructions = (
        "Enter one word pair per line.\n"
        "The first word is the term.\n"
        "The second is the translation or definition.\n"
        "Use a space, hyphen (-), or TAB.\n\n"
        "Example:\n"
        "cat - кот\n"
        "apple яблоко"
    )

    button_text = "Generate worksheet"
    warning_text = "Please enter some words first."
    format_error = "No valid words found."
    section_warning = "Please select at least one worksheet section."

    translate_label = "Translate"
    write_label = "Write"
    discuss_label = "Discuss"
    answer_label = "🔑 Answer Key"

else:
    st.caption("Создавайте задания для уроков быстро и удобно")

    instructions = (
        "Введите одну пару слов на строку.\n"
        "Первое — слово или термин.\n"
        "Второе — перевод или определение.\n"
        "Используйте пробел, дефис (-) или TAB.\n\n"
        "Пример:\n"
        "cat - кот\n"
        "apple яблоко"
    )

    button_text = "Сгенерировать"
    warning_text = "Введите слова."
    format_error = "Ошибка формата."
    section_warning = "Выберите хотя бы один раздел."

    translate_label = "Переведите"
    write_label = "Напишите"
    discuss_label = "Обсудите"
    answer_label = "🔑 Ответы"

# === INPUT ===
st.markdown("### Input")
st.write(instructions)

words_input = st.text_area("", height=280)

st.divider()

# === GENERATE ===
if st.button(button_text):

    if not words_input.strip():
        st.warning(warning_text)

    elif not selected_sections:
        st.warning(section_warning)

    else:
        word_pairs = parse_words(words_input)

        if not word_pairs:
            st.error(format_error)

        else:
            translate, write, discuss, answers = generate_tasks(
                word_pairs,
                language
            )

            st.markdown("### Preview")

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
                    label="Download PDF",
                    data=f,
                    file_name="worksheet.pdf",
                    mime="application/pdf"
                )
