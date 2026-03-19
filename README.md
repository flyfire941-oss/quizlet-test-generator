# 📘 Quiz Generator for Teachers

A simple web application for teachers to generate quizzes from vocabulary lists.

The app helps create:
- Translation exercises
- Writing tasks
- Two test variants (A & B)
- Answer keys for teachers

---

## 🚀 Features

- ✏️ Paste vocabulary directly (no CSV needed)
- 🎯 Level-based tasks (A1–A2)
- 🔄 Two test variants with equal difficulty
- 📝 Writing task (use 3–5 words)
- 🔑 Automatic answer key generation
- 🚫 Ignores full sentences (only short words/phrases)

---

## 🧠 How It Works

1. Paste vocabulary in the format:
apple - яблоко
to run - бегать
beautiful - красивый

2. Choose the level (A1–A2)

3. Click **Generate**

4. Get:
   - Test A
   - Test B
   - Writing task
   - Answer key

---

## 🌐 Live Demo

If deployed via Render, your app will be available at:
https://your-app-name.onrender.com

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas

---

## ⚙️ Installation (for local run)

1. Clone the repository:
git clone https://github.com/your-username/quiz-generator.git

2. Install dependencies:
pip install -r requirements.txt

3. Run the app:
streamlit run app.py

---

## 📁 Project Structure
quiz-generator/
│
├── app.py # Main application
├── generator.py # Test generation logic
├── requirements.txt # Dependencies
└── .streamlit/
└── config.toml # Streamlit configuration

---

## 🎯 Future Improvements

- 📄 Export to Word (.docx)
- 🗣️ Speaking tasks generation
- 🧩 More advanced level filtering
- 🎨 Improved UI
- 📊 Progress tracking for students

---

## ⚠️ Notes

- The app does NOT rely on Quizlet parsing to ensure stability.
- Designed for educational use and flexibility.

---

## 👩‍🏫 Author

Created as a learning project for educational use and teaching support.
