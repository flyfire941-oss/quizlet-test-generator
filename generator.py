from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

# === ШРИФТЫ ===
FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")

pdfmetrics.registerFont(TTFont('Roboto', os.path.join(FONT_DIR, 'Roboto-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Roboto-Bold', os.path.join(FONT_DIR, 'Roboto-Bold.ttf')))


# === ПАРСИНГ ===
def parse_words(input_text):
    word_pairs = []

    for line in input_text.strip().split("\n"):
        if not line.strip():
            continue

        if "\t" in line:
            parts = line.split("\t")
        elif "-" in line:
            parts = line.split("-", 1)
        else:
            parts = line.split(maxsplit=1)

        if len(parts) == 2:
            term = parts[0].strip()
            definition = parts[1].strip()
            word_pairs.append((term, definition))

    return word_pairs


# === ГЕНЕРАЦИЯ ЗАДАНИЙ ===
def generate_tasks(word_pairs, language):
    terms = [pair[0] for pair in word_pairs][:10]
    definitions = [pair[1] for pair in word_pairs][:10]

    translate_text = "\n".join(definitions)

    if language == "English":
        write_text = "Write 5 sentences using the words below:\n\n" + ", ".join(terms)
        discuss_text = "Discuss with a partner. Use the words below to make your own examples:\n\n" + ", ".join(terms)
    else:
        write_text = "Напишите 5 предложений, используя слова ниже:\n\n" + ", ".join(terms)
        discuss_text = "Обсудите с партнером, используя слова ниже:\n\n" + ", ".join(terms)

    answer_key_text = "\n".join([f"{t} - {d}" for t, d in word_pairs])

    return translate_text, write_text, discuss_text, answer_key_text


# === PDF ===
def generate_pdf(translate, write, discuss, answers, language, worksheet_type, filename="worksheet.pdf"):

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm
    )

    # === СТИЛИ (исправленные) ===
    title_style = ParagraphStyle(
        name='Title',
        fontName='Roboto-Bold',
        fontSize=22,
        leading=26,
        spaceAfter=16
    )

    section_style = ParagraphStyle(
        name='Section',
        fontName='Roboto-Bold',
        fontSize=14,
        leading=18,
        spaceBefore=14,
        spaceAfter=8
    )

    normal_style = ParagraphStyle(
        name='Normal',
        fontName='Roboto',
        fontSize=12,
        leading=16,
        spaceAfter=6
    )

    # === ЯЗЫК ===
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

    # === HEADER ===
    content.append(Paragraph(title, title_style))
    content.append(Paragraph(name_line, normal_style))
    content.append(Spacer(1, 12))

    # === FULL WORKSHEET ===
    if worksheet_type == "Full worksheet":

        content.append(Paragraph(t_title, section_style))
        content.append(Spacer(1, 6))

        for i, w in enumerate(translate.split("\n")):
            content.append(Paragraph(f"{i+1}. {w}", normal_style))

        content.append(Spacer(1, 12))

        content.append(Paragraph(w_title, section_style))
        content.append(Paragraph(write.replace("\n", "<br/>"), normal_style))
        content.append(Spacer(1, 8))

        for i in range(5):
            content.append(Paragraph(f"{i+1}. _______________________________", normal_style))

        content.append(Spacer(1, 12))

        content.append(Paragraph(d_title, section_style))
        content.append(Paragraph(discuss.replace("\n", "<br/>"), normal_style))

    # === WRITING ONLY ===
    elif worksheet_type == "Writing only":

        content.append(Paragraph(t_title, section_style))
        content.append(Spacer(1, 6))

        for i, w in enumerate(translate.split("\n")):
            content.append(Paragraph(f"{i+1}. {w}", normal_style))

        content.append(Spacer(1, 12))

        content.append(Paragraph(w_title, section_style))
        content.append(Paragraph(write.replace("\n", "<br/>"), normal_style))
        content.append(Spacer(1, 8))

        for i in range(5):
            content.append(Paragraph(f"{i+1}. _______________________________", normal_style))

    # === SPEAKING ONLY ===
    elif worksheet_type == "Speaking only":

        content.append(Paragraph(d_title, section_style))
        content.append(Spacer(1, 6))
        content.append(Paragraph(discuss.replace("\n", "<br/>"), normal_style))

    # === ANSWER KEY ===
    content.append(PageBreak())
    content.append(Paragraph(a_title, section_style))
    content.append(Spacer(1, 8))

    answer_table_data = [
        [a.split(" - ")[0], a.split(" - ")[1]]
        for a in answers.split("\n")
    ]

    table = Table(answer_table_data, colWidths=[80 * mm, None])

    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, -1), 'Roboto'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))

    content.append(table)

    doc.build(content)

    return filename
