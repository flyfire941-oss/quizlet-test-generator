from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

# Путь к шрифтам
FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")

# Регистрация Roboto
pdfmetrics.registerFont(TTFont('Roboto', os.path.join(FONT_DIR, 'Roboto-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Roboto-Bold', os.path.join(FONT_DIR, 'Roboto-Bold.ttf')))

def parse_words(input_text):
    word_pairs = []
    for line in input_text.strip().split("\n"):
        if not line.strip():
            continue
        # Разделители: TAB, дефис, пробел
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

def generate_tasks(word_pairs):
    translate_words = [pair[1] for pair in word_pairs][:10]
    translate_text = "\n".join(translate_words)

    write_words = [pair[0] for pair in word_pairs][:10]
    write_text = "Write 5 sentences using the words below:\n\n" + ", ".join(write_words)

    discuss_text = "Discuss with a partner. Use the words below to make your own examples:\n\n" + ", ".join(write_words)

    answer_key_text = "\n".join([f"{term} - {definition}" for term, definition in word_pairs])

    return translate_text, write_text, discuss_text, answer_key_text

def generate_pdf(translate, write, discuss, answers, filename="worksheet.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            rightMargin=20*mm, leftMargin=20*mm,
                            topMargin=20*mm, bottomMargin=20*mm)

    title_style = ParagraphStyle(name='Title', fontName='Roboto-Bold', fontSize=22, leading=26, spaceAfter=10)
    section_style = ParagraphStyle(name='Section', fontName='Roboto-Bold', fontSize=14, leading=18, spaceAfter=6, spaceBefore=12)
    normal_style = ParagraphStyle(name='Normal', fontName='Roboto', fontSize=12, leading=16, spaceAfter=6)

    content = []

    # Заголовок
    content.append(Paragraph("Vocabulary Worksheet", title_style))
    content.append(Spacer(1, 6))
    content.append(Paragraph("Name: ________________________    Date: ____________", normal_style))
    content.append(Spacer(1, 12))

    # 1. Translate
    content.append(Paragraph("1. Translate", section_style))
    for i, w in enumerate(translate.split("\n")):
        content.append(Paragraph(f"{i+1}. {w}", normal_style))
        content.append(Spacer(1, 4))
    content.append(Spacer(1, 10))

    # 2. Write
    content.append(Paragraph("2. Write", section_style))
    content.append(Paragraph(write.replace("\n", "<br/>"), normal_style))
    for i in range(5):
        content.append(Paragraph(f"{i+1}. _______________________________", normal_style))
    content.append(Spacer(1, 10))

    # 3. Discuss (устное задание, без линий)
    content.append(Paragraph("3. Discuss", section_style))
    content.append(Paragraph(discuss.replace("\n", "<br/>"), normal_style))
    content.append(PageBreak())

    # Answer Key — таблица с переносом текста
    answer_table_data = [[a.split(" - ")[0], a.split(" - ")[1]] for a in answers.split("\n")]
    table = Table(answer_table_data, colWidths=[80*mm, None])
    table.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,-1), 'Roboto'),
        ('WORDWRAP', (0,0), (-1,-1), 'CJK')
    ]))
    content.append(Paragraph("Answer Key", section_style))
    content.append(table)

    doc.build(content)
    return filename
