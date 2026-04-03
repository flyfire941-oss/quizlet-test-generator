import random
from ai_generator import generate_ai_tasks

def generate_tasks(words, level):
    random.shuffle(words)
    selected_words = words[:10]  # до 10 слов

    # Test A — перевод с русского на английский
    test = "Translate into English:\n\n"
    for eng, rus in selected_words:
        test += f"{rus}\n"

    # AI задания (Writing + Speaking)
    ai_tasks = generate_ai_tasks(selected_words, level)

    # Answer Key
    answers = "Answer Key:\n\n"
    for eng, rus in selected_words:
        answers += f"{eng} - {rus}\n"

    return {
        "test": test,
        "writing": ai_tasks,
        "answers": answers
    }
