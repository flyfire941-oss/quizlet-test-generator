import streamlit as st
from generator import parse_words, generate_tasks, generate_pdf

st.set_page_config(page_title="Vocabulary Worksheet Generator", layout="centered")

st.title("Vocabulary Worksheet Generator")

# язык
language = st.radio(
    "Select worksheet language / Выберите язык задания:",
    ["English", "Русский"]
)

# тип задания
worksheet_type = st.selectbox(
    "Select worksheet type / Тип задания:",
    ["Full worksheet", "Writing only", "Speaking only"]
)

st.divider()

# тексты
if language == "English":
    st.caption("Create printable classroom activities quickly and easily")

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

else:
    st.caption("Создавайте задания для уроков быстро и удобно")

    instructions = (
        "Введите одну пару слов на строку.\n"
        "Первое — слово/термин, второе — перевод или определение.\n"
        "Используйте пробел, дефис или TAB.\n\n"
        "Пример:\n"
        "cat - кот\n"
        "apple яблоко"
    )

    button_text = "Сгенерировать"
    warning_text = "Введите слова."
    error_text = "Ошибка формата."

st.markdown("### Input")
st.write(instructions)

words_input = st.text_area("")

st.divider()

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

            if worksheet_type == "Full worksheet":
                st.text(translate)
                st.text(write)
                st.text(discuss)

            elif worksheet_type == "Writing only":
                st.text(write)

            elif worksheet_type == "Speaking only":
                st.text(discuss)

            st.markdown("🔑")
            st.text(answers)

            pdf_file = generate_pdf(
                translate, write, discuss, answers,
                language, worksheet_type
            )

            with open(pdf_file, "rb") as f:
                st.download_button(
                    label="Download PDF",
                    data=f,
                    file_name="worksheet.pdf",
                    mime="application/pdf"
                )
