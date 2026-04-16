import streamlit as st
from generator import parse_words, generate_tasks, generate_pdf

st.set_page_config(page_title="Vocabulary Worksheet Generator", layout="centered")

st.title("Vocabulary Worksheet Generator")

# === ВЫБОР ЯЗЫКА ===
language = st.radio(
    "Select worksheet language / Выберите язык задания:",
    ["English", "Русский"]
)

# === ВЫБОР ТИПА ЗАДАНИЯ ===
worksheet_type = st.selectbox(
    "Select worksheet type / Тип задания:",
    ["Full worksheet", "Writing only", "Speaking only"]
)

st.divider()

# === ТЕКСТЫ ===
if language == "English":
    st.caption("Create printable classroom activities quickly and easily")

    instructions = (
        "Enter one word pair per line.\n"
        "The first word is the term.\n"
        "The second is the translation or definition.\n"
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
    st.caption("Создавайте задания для уроков быстро и удобно")

    instructions = (
        "Введите одну пару слов на строку.\n"
        "Первое — слово или термин.\n"
        "Второе — перевод или определение.\n"
        "Используйте пробел, дефис или TAB.\n\n"
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

# === INPUT ===
st.markdown("### Input")
st.write(instructions)

words_input = st.text_area("")

st.divider()

# === ГЕНЕРАЦИЯ ===
if st.button(button_text):

    if not words_input.strip():
        st.warning(warning_text)

    else:
        word_pairs = parse_words(words_input)

        if not word_pairs:
            st.error(error_text)

        else:
            translate, write, discuss, answers = generate_tasks(word_pairs, language)

            st.markdown("### Preview")

            # === FULL ===
            if worksheet_type == "Full worksheet":

                st.markdown(f"**{translate_label}**")
                st.text(translate)

                st.markdown(f"**{write_label}**")
                st.text(write)

                st.markdown(f"**{discuss_label}**")
                st.text(discuss)

            # === WRITING ONLY ===
            elif worksheet_type == "Writing only":

                st.markdown(f"**{translate_label}**")
                st.text(translate)

                st.markdown(f"**{write_label}**")
                st.text(write)

            # === SPEAKING ONLY ===
            elif worksheet_type == "Speaking only":

                st.markdown(f"**{discuss_label}**")
                st.text(discuss)

            # === ANSWERS ===
            st.markdown(f"**{answer_label}**")
            st.text(answers)

            # === PDF ===
            pdf_file = generate_pdf(
                translate,
                write,
                discuss,
                answers,
                language,
                worksheet_type
            )

            with open(pdf_file, "rb") as f:
                st.download_button(
                    label="Download PDF",
                    data=f,
                    file_name="worksheet.pdf",
                    mime="application/pdf"
                )
