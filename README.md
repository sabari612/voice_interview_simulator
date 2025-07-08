# 🎤 Voice-Based Interview Quiz App

This is an interactive voice-enabled quiz application built with **Streamlit**, designed for conducting multiple-choice question (MCQ) interviews using a **PDF upload**. Users can answer questions either by speaking or selecting manually, with real-time feedback, scoring, and final result export.

---

## 🚀 Features

* 📄 **Upload PDF with MCQs**
* 🎙️ **Answer via Voice or Selection**
* ⏱️ **Timer per Question (60s)**
* ✅ **Score Calculation**
* 📊 **Final Summary & Feedback**
* 💾 **Results saved to CSV**
* 🗣️ **Text-to-Speech score at the end**
* 💫 **Sleek animated UI**

---

## 📂 Folder Structure

```
voice_interview_simulator/
├── app.py                 # Main Streamlit app
├── utils/
│   ├── stt.py            # Speech-to-text logic
│   ├── tts.py            # Text-to-speech logic
│   └── feedback.py       # (Optional) Custom feedback
├── results.csv           # Output results (auto-generated)
├── requirements.txt      # Dependencies
├── .gitignore            # Git ignored files (includes .env)
└── README.md             # Project documentation
```

---

## 📄 PDF Format

The PDF must contain:

```text
Question 1: What is AI?
A) Art & Illustration
B) Artificial Intelligence
C) Animal Instinct
D) Applied Innovation
Answer: B
```

* Supports any number of MCQs
* Options must be labeled with `A)`, `B)`, etc.
* Answer must follow `Answer: X` format

---

## 🧠 How It Works

1. User enters their name
2. Uploads a PDF with MCQ questions
3. App parses and displays one question at a time
4. User answers by voice or click
5. Each question has a 60-second timer
6. App evaluates answers and tracks score
7. At the end, user gives feedback and rating
8. Results saved and downloadable as CSV
9. App speaks the final score using TTS

---

## 🛠️ Installation (Step-by-step for Beginners)

1. **Install Python** (if not already):

   * Download Python from [python.org](https://www.python.org/downloads/) and install it.

2. **Open your terminal or command prompt**

3. **Clone the GitHub repository:**

```bash
git clone https://github.com/sabari612/voice_interview_simulator.git
cd voice_interview_simulator
```

4. **Create a virtual environment (recommended):**

```bash
python -m venv .venv
```

5. **Activate the virtual environment:**

* On Windows:

```bash
.venv\Scripts\activate
```

* On Mac/Linux:

```bash
source .venv/bin/activate
```

6. **Install required libraries:**

```bash
pip install -r requirements.txt
```

7. **Run the app:**

```bash
streamlit run app.py
```

---

## 📦 Dependencies

Add these to your `requirements.txt`:

```
streamlit
PyMuPDF
pandas
SpeechRecognition
pyttsx3
datetime
```

---

## 🔒 Important: Environment Variables & Secrets

* **Do not upload your `.env` file to GitHub.**
* Store API keys and secrets like `GROQ_API_KEY` inside `.env`
* Add `.env` to `.gitignore` to keep it safe:

```
# .gitignore
.env
```

If you accidentally commit secrets:

1. Remove `.env` using `git rm --cached .env`
2. Rewrite history:

```bash
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch .env" --prune-empty --tag-name-filter cat -- --all
```

3. Force push:

```bash
git push origin main --force
```

Learn more: [GitHub Secret Scanning Docs](https://docs.github.com/en/code-security/secret-scanning)

---

## ✨ Customization Ideas

* Add difficulty levels
* Store results in a database
* Email the report to the candidate
* Add webcam + face detection
* Theme toggle (dark/light)

---

## 📄 License

MIT License

---

## 🙋‍♂️ Author

Built with ❤️ by **Sabari Abishake K**
📧 Email: [sabariabishake17abd@gmail.com](mailto:sabariabishake17abd@gmail.com)
🌐 GitHub: [sabari612](https://github.com/sabari612)

Feel free to fork and improve this project!
