import streamlit as st
from generator import parse_words, generate_tasks, generate_pdf

st.set_page_config(page_title="Vocabulary Worksheet Generator", layout="centered")

st.title("Vocabulary Worksheet Generator")

# 🔹 выбор языка
language = st.radio("Select instruction language / Выберите язык:", ["English", "Русский"])

st.divider()

# 🔹 тексты интерфейса
if language == "English":
    st.caption("Create printable classroom activities quickly and easily")

    instructions = (
        "Add **one word pair per line**.\n"
        "- The first item is the **term or word**.\n"
        "- The second item is the **definition or translation**.\n"
        "- Use a space, hyphen `-`, or tab to separate them.\n\n"
        "**Examples:**\n"
        "cat - кот\n"
        "apple яблоко"
    )

    button_text = "Generate worksheet"
    warning_text = "Please enter some words first."
    error_text = "No valid words found. Please check your input format."

    section_translate = "Translate"
    section_write = "Write"
    section_discuss = "Discuss"
    section_answers = "🔑 Answer Key"

else:
    st.caption("Создавайте задания для уроков быстро и удобно")

    instructions = (
        "Введите **по одной паре слов на строку**.\n"
        "- Первое слово — это **термин или слово**.\n"
        "- Второе — это **перевод или определение**.\n"
        "- Используйте пробел, дефис `-` или TAB.\n\n"
        "**Пример:**\n"
        "cat - кот\n"
        "apple яблоко"
    )

    button_text = "Сгенерировать задание"
    warning_text = "Введите слова."
    error_text = "Не удалось распознать слова. Проверьте формат."

    section_translate = "Переведите"
    section_write = "Напишите"
    section_discuss = "Обсудите"
    section_answers = "🔑 Ответы"

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

            st.markdown(f"**{section_translate}**")
            st.text(translate)

            st.markdown(f"**{section_write}**")
            st.text(write)

            st.markdown(f"**{section_discuss}**")
            st.text(discuss)

            st.markdown(f"**{section_answers}**")
            st.text(answers)

            pdf_file = generate_pdf(translate, write, discuss, answers, language)

            with open(pdf_file, "rb") as f:
                st.download_button(
                    label="Download PDF",
                    data=f,
                    file_name="worksheet.pdf",
                    mime="application/pdf"
                )
