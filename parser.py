import requests
from bs4 import BeautifulSoup

def clean_text(text):
    return text.split(".")[0].split("(")[0].strip()

def parse_quizlet(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    terms = soup.find_all("span", class_="TermText")
    words = []

    for i in range(0, len(terms), 2):
        try:
            eng = clean_text(terms[i].get_text())
            rus = clean_text(terms[i+1].get_text())
            words.append((eng, rus))
        except:
            continue

    return words
