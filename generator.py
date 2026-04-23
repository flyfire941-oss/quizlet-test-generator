# generator.py

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os
import random

FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")

pdfmetrics.registerFont(TTFont("Roboto", os.path.join(FONT_DIR, "Roboto-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Roboto-Bold", os.path.join(FONT_DIR, "Roboto-Bold.ttf")))


def parse_words(input_text):
    word_pairs = []

    for line in input_text.strip().split("\n"):
        if not line.strip():
            continue

        # 1. TAB — лучший и самый безопасный вариант
        if "\t" in line:
            parts = line.split("\t", 1)

        # 2. дефис с пробелами
        elif " - " in line:
            parts = line.split(" - ", 1)

        # 3. обычный дефис
        elif "-" in line:
            parts = line.split("-", 1)

        # 4. пробел — только если ровно 2 элемента
        else:
            split_parts = line.split()

            if len(split_parts) == 2:
                parts = split_parts
            else:
                continue

        if len(parts) == 2:
            term = parts[0].strip()
            definition = parts[1].strip()

            if term and definition:
                word_pairs.append((term, definition))

    return word_pairs


def generate_tasks(word_pairs, language):
    selected_pairs = word_pairs[:10]

    terms = [pair[0] for pair in selected_pairs]
    definitions = [pair[1] for pair in selected_pairs]

    translate_text = "\n".join(definitions)

    sample_size = min(5, len(terms))
    random_terms = random.sample(terms, sample_size)
    random.shuffle(random_terms)

    discuss_terms = terms.copy()
    random.shuffle(discuss_terms)

    if language == "English":
        write_text = "Write 5 sentences using the words below:\n\n" + ", ".join(random_terms)
        discuss_text = "Discuss with a partner. Use the words below to make your own examples:\n\n" + ", ".join(discuss_terms)
    else:
        write_text = "Напишите 5 предложений, используя слова ниже:\n\n" + ", ".join(random_terms)
        discuss_text = "Обсудите с партнером. Используйте слова ниже:\n\n" + ", ".join(discuss_terms)

    answer_key_text = "\n".join([f"{t} - {d}" for t, d in word_pairs])

    return translate_text, write_text, discuss_text, answer_key_text


def generate_pdf(translate, write, discuss, answers, language, selected_sections, filename="worksheet.pdf"):

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm
    )

    title_style = ParagraphStyle(
        name="Title",
        fontName="Roboto-Bold",
        fontSize=22,
        leading=26,
        spaceAfter=16
    )

    section_style = ParagraphStyle(
        name="Section",
        fontName="Roboto-Bold",
        fontSize=14,
        leading=18,
        spaceBefore=14,
        spaceAfter=8
    )

    normal_style = ParagraphStyle(
        name="Normal",
        fontName="Roboto",
        fontSize=12,
        leading=16,
        spaceAfter=6
    )

    if language == "English":
        title = "Vocabulary Worksheet"
        t_title = "1. Translate"
        w_title = "2. Write"
        d_title = "3. Discuss"
        a_title = "Answer Key"
        name_line = "Name: ________________________    Date: ____________"
    else:
        title = "Лексическое задание"
        t_title = "1. Переведите"
        w_title = "2. Напишите"
        d_title = "3. Обсудите"
        a_title = "Ответы"
        name_line = "Имя: ________________________    Дата: ____________"

    content = []

    content.append(Paragraph(title, title_style))
    content.append(Paragraph(name_line, normal_style))
    content.append(Spacer(1, 12))

    if "Translation" in selected_sections:
        content.append(Paragraph(t_title, section_style))
        for i, item in enumerate(translate.split("\n")):
            content.append(Paragraph(f"{i+1}. {item}", normal_style))
        content.append(Spacer(1, 10))

    if "Writing" in selected_sections:
        content.append(Paragraph(w_title, section_style))
        content.append(Paragraph(write.replace("\n", "<br/>"), normal_style))

        for i in range(5):
            content.append(Paragraph(f"{i+1}. _______________________________", normal_style))

        content.append(Spacer(1, 10))

    if "Speaking" in selected_sections:
        content.append(Paragraph(d_title, section_style))
        content.append(Paragraph(discuss.replace("\n", "<br/>"), normal_style))

    content.append(PageBreak())

    content.append(Paragraph(a_title, section_style))
    content.append(Spacer(1, 8))

    answer_table_data = []

for a in answers.split("\n"):
    if " - " in a:
        left, right = a.split(" - ", 1)

        answer_table_data.append([
            Paragraph(left, normal_style),
            Paragraph(right, normal_style)
        ])
   table = Table(
    answer_table_data,
    colWidths=[60 * mm, 110 * mm]
)

    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, -1), "Roboto"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
    ]))

    content.append(table)

    doc.build(content)

    return filename
