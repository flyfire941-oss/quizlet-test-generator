# app.py

import streamlit as st
import streamlit.components.v1 as components

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

# === ТЕКСТЫ ПО ЯЗЫКУ ===
if language == "English":
    st.caption("Create printable classroom activities quickly and easily")

    sections_title = "Worksheet sections"
    translate_checkbox = "Translation"
    write_checkbox = "Writing"
    discuss_checkbox = "Speaking"

    instructions = (
        "Enter one word pair per line.\n"
        "The first word is the term.\n"
        "The second is the translation or definition.\n"
        "Use a space, hyphen (-), or TAB.\n\n"
        "For phrases and definitions in the same language,\n"
        "please use TAB or hyphen (-).\n\n"
        "Example:\n"
        "cat - кот\n"
        "apple яблоко\n"
        "to go down a storm - to be successful with the audience"
    )

    tab_hint = "Press TAB to insert indentation inside the field"

    button_text = "Generate worksheet"
    warning_text = "Please enter some words first."
    format_error = "For phrases and definitions, please use TAB or hyphen (-)."
    section_warning = "Please select at least one worksheet section."

    translate_label = "Translate"
    write_label = "Write"
    discuss_label = "Discuss"
    answer_label = "🔑 Answer Key"

else:
    st.caption("Создавайте задания для уроков быстро и удобно")

    sections_title = "Разделы задания"
    translate_checkbox = "Перевод"
    write_checkbox = "Письменная часть"
    discuss_checkbox = "Устная часть"

    instructions = (
        "Введите одну пару слов на строку.\n"
        "Первое — слово или термин.\n"
        "Второе — перевод или определение.\n"
        "Используйте пробел, дефис (-) или TAB.\n\n"
        "Для фраз и определений на одном языке\n"
        "используйте TAB или дефис (-).\n\n"
        "Пример:\n"
        "cat - кот\n"
        "apple яблоко\n"
        "to go down a storm - to be successful with the audience"
    )

    tab_hint = "Нажмите TAB для вставки отступа внутри поля"

    button_text = "Сгенерировать"
    warning_text = "Введите слова."
    format_error = "Для фраз и определений используйте TAB или дефис (-)."
    section_warning = "Выберите хотя бы один раздел."

    translate_label = "Переведите"
    write_label = "Напишите"
    discuss_label = "Обсудите"
    answer_label = "🔑 Ответы"

# === ВЫБОР ЗАДАНИЙ ===
st.subheader(sections_title)

include_translate = st.checkbox(translate_checkbox, value=True)
include_write = st.checkbox(write_checkbox, value=True)
include_discuss = st.checkbox(discuss_checkbox, value=True)

selected_sections = []

if include_translate:
    selected_sections.append("Translation")

if include_write:
    selected_sections.append("Writing")

if include_discuss:
    selected_sections.append("Speaking")

st.divider()

# === INPUT ===
st.markdown("### Input")
st.write(instructions)

words_input = st.text_area(
    "",
    height=280,
    key="words_input"
)

st.caption(tab_hint)

# === TAB SUPPORT ===
components.html(
    """
    <script>
    const textarea = window.parent.document.querySelector('textarea');

    if (textarea && !textarea.dataset.tabEnabled) {
        textarea.dataset.tabEnabled = "true";

        textarea.addEventListener('keydown', function(e) {
            if (e.key === 'Tab') {
                e.preventDefault();

                const start = this.selectionStart;
                const end = this.selectionEnd;

                this.value =
                    this.value.substring(0, start) +
                    "\\t" +
                    this.value.substring(end);

                this.selectionStart = this.selectionEnd = start + 1;

                this.dispatchEvent(new Event('input', { bubbles: true }));
            }
        });
    }
    </script>
    """,
    height=0,
)

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
