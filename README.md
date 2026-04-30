# Vocabulary Worksheet Generator

A simple web app for teachers to create clean, printable vocabulary worksheets in seconds.

Built with Streamlit. No AI. No APIs. Fully local logic.

---

## What it does

Paste a list of word pairs (term + translation or definition), and the app automatically generates:

- Translation exercise  
- Writing task (randomized words)  
- Speaking activity  
- Answer Key  
- Printable PDF worksheet  

---

## Features

- Clean, teacher-friendly interface  
- Select worksheet sections with checkboxes  
- English / Russian interface  
- Supports words, phrases, and definitions  
- Randomized writing task (no easy matching)  
- Speaking task (no unnecessary writing lines)  
- Answer Key included  
- Export to PDF (A4 worksheet format)  
- Roboto font embedded (works on all devices)  

---

## No AI

This project uses:

- No OpenAI  
- No external APIs  
- No internet data sources  

Everything is generated locally using simple Python logic.

---

## Input format

Enter one pair per line:

cat - кот  
apple яблоко  
environment окружающая среда  
photosynthesis process by which plants make food  

---

## Formatting rules

Single words → use space  
Example:  
cat кот  

Phrases → use hyphen (-)  
Example:  
environmental protection - защита окружающей среды  

---

## Supported use cases

- EN → RU  
- RU → EN  
- EN → EN (term + definition)  
- vocabulary lists  
- academic terms  
- business English  
- exam preparation  

---

## Quizlet support

You can paste lists exported from Quizlet directly into the app.

The parser will automatically process them.

---

## Worksheet sections

Select what to include:

- Translation  
- Writing  
- Speaking  

You can combine them in any way.

---

## PDF Output

The app generates a printable worksheet with:

- Title  
- Name / Date line  
- Clear sections  
- Writing lines  
- Proper spacing  
- Answer Key (on separate page)  

---

## Fonts

Uses Roboto (embedded) for consistent rendering across:

- Windows  
- macOS  
- Android  
- iOS  

---

## Tech Stack

- Python  
- Streamlit  
- ReportLab  
- GitHub  
- Render  

---

## Deployment (Render)

Build command:

pip install -r requirements.txt

Start command:

streamlit run app.py

---

## Project structure

quizlet-test-generator/
│
├── app.py
├── generator.py
├── requirements.txt
│
├── fonts/
│   ├── Roboto-Regular.ttf
│   └── Roboto-Bold.ttf
│
└── .streamlit/
    └── config.toml

---

## Installation (local)

pip install -r requirements.txt  
streamlit run app.py  

---

## Status

- Fully working  
- Deployed on Render  
- Ready for portfolio  
- Used in real teaching  

---

## Future improvements

- gap-fill exercises  
- matching tasks  
- worksheet templates  
- branding / logos  
- student mode  
- saving worksheets  

---

## Use case

Designed for teachers who want to:

- save lesson prep time  
- generate materials quickly  
- avoid repetitive manual work  

---

## License

Free to use for educational purposes.
