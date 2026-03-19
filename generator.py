import random

def detect_topic(words):
    keywords = {
        "clothes": ["shirt", "dress", "jacket", "wear", "clothes"],
        "food": ["eat", "food", "apple", "drink"],
    }

    for topic, keys in keywords.items():
        for eng, _ in words:
            for k in keys:
                if k in eng.lower():
                    return topic

    return "general"


def generate_questions(words, level):
    topic = detect_topic(words)

    if topic == "clothes":
        if level == "A1":
            return [
                "What do you wear at home?",
                "What do you wear at work?"
            ]
        else:
            return [
                "Describe your favorite outfit.",
                "What clothes are appropriate for different situations?"
            ]

    if topic == "food":
        return [
            "What do you usually eat?",
            "What is your favorite food?"
        ]

    if level == "A1":
        return [
            "Answer using the words.",
            "Make simple sentences."
        ]
    else:
        return [
            "Write a short paragraph using the words.",
            "Explain your answers."
        ]


def generate_tasks(words, level):

    random.shuffle(words)

    test_a_words = words[:5]
    test_b_words = words[5:10]

    test_a = "Translate into English:\n\n"
    for eng, rus in test_a_words:
        test_a += f"{rus}\n"

    test_b = "Translate into English:\n\n"
    for eng, rus in test_b_words:
        test_b += f"{rus}\n"

    writing_words = random.sample(words, min(5, len(words)))

    questions = generate_questions(words, level)

    writing = "Use these words:\n\n"
    writing += ", ".join([w[0] for w in writing_words]) + "\n\n"

    writing += "Answer these questions:\n\n"

    for q in questions:
        writing += q + "\n"

    answers = "Answer Key:\n\n"
    for eng, rus in words:
        answers += f"{eng} - {rus}\n"

    return {
        "test_a": test_a,
        "test_b": test_b,
        "writing": writing,
        "answers": answers
    }
