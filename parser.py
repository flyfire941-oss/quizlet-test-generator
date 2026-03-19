import re

def is_russian(text):
    return bool(re.search("[а-яА-Я]", text))

def split_line(line):
    # разделитель: таб или 2+ пробела
    parts = re.split(r"\t|\s{2,}", line)
    if len(parts) >= 2:
        return parts[0].strip(), parts[1].strip()
    return None, None

def parse_input(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    pairs = []

    for line in lines:

        # сначала пробуем разделители
        eng, rus = split_line(line)

        if eng and rus:
            pairs.append((eng, rus))
            continue

        # пробуем дефис
        if "-" in line:
            parts = line.split("-", 1)
            if len(parts) == 2:
                pairs.append((parts[0].strip(), parts[1].strip()))
                continue

    return pairs
