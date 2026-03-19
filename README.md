# Quizlet Test Generator

A web app for teachers that generates vocabulary tests from Quizlet sets.

## Features
- Extracts words from Quizlet
- Generates Word tests
- Supports A1–B2 levels
- Creates 2 variants (A/B)
- Includes answer key

## Run locally

pip install -r requirements.txt
streamlit run app.py

## Usage
1. Paste Quizlet link
2. Select level
3. Click Generate
4. Download tests

## Tech
- Python
- Streamlit
- BeautifulSoup
- python-docx
