import random

def generate_tests(words, level):
    random.shuffle(words)

    split = len(words) // 2
    a_words = words[:split]
    b_words = words[split:]

    def format_words(word_list):
        return "\n".join([f"{t}" for t, _ in word_list])

    test_a = f"Translate into English (Level {level}):\n\n" + format_words(a_words)
    test_b = f"Translate into English (Level {level}):\n\n" + format_words(b_words)

    # Writing task
    writing_words = random.sample(words, min(5, len(words)))
    writing_task = "Use 3-5 words to write sentences:\n\n" + ", ".join([w[0] for w in writing_words])

    answers = "\n".join([f"{t} - {tr}" for t, tr in words])

    return {
        "test_a": test_a,
        "test_b": test_b,
        "writing": writing_task,
        "answers": answers
    }
