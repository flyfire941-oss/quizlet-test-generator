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
            word1 = parts[0].strip()
            word2 = parts[1].strip()

            if any(c.isalpha() and c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in word1):
                eng, rus = word1, word2
            else:
                eng, rus = word2, word1

            word_pairs.append((eng, rus))

    return word_pairs


def generate_tasks(word_pairs):
    translate_words = [pair[1] for pair in word_pairs][:10]
    translate_text = "\n".join(translate_words)

    write_words = [pair[0] for pair in word_pairs][:10]
    write_text = (
        "Write 5 sentences using the words below:\n\n"
        + ", ".join(write_words)
    )

    discuss_text = (
        "Work with a partner. Use the words below to create your own examples and discuss them:\n\n"
        + ", ".join(write_words)
    )

    answer_key_text = "\n".join([f"{eng} - {rus}" for eng, rus in word_pairs])

    return translate_text, write_text, discuss_text, answer_key_text
