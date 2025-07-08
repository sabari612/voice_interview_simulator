🎤 Voice-Based Interview Quiz App

This is an interactive voice-enabled quiz application built with Streamlit, designed for conducting multiple-choice question (MCQ) interviews using a PDF upload. Users can answer questions either by speaking or selecting manually, with real-time feedback, scoring, and final result export.

🚀 Features

📄 Upload PDF with MCQs

🎙️ Answer via Voice or Selection

⏱️ Timer per Question (60s)

✅ Score Calculation

📊 Final Summary & Feedback

💾 Results saved to CSV

🗣️ Text-to-Speech score at the end

💫 Sleek animated UI

📂 Folder Structure

voice_interview_simulator/
├── app.py                 # Main Streamlit app
├── utils/
│   ├── stt.py            # Speech-to-text logic
│   ├── tts.py            # Text-to-speech logic
│   └── feedback.py       # (Optional) Custom feedback
├── results.csv           # Output results (auto-generated)
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

📄 PDF Format

The PDF must contain:

Question 1: What is AI?
A) Art & Illustration
B) Artificial Intelligence
C) Animal Instinct
D) Applied Innovation
Answer: B

Supports any number of MCQs

Options must be labeled with A), B), etc.

Answer must follow Answer: X format

🧠 How It Works

User enters their name

Uploads a PDF with MCQ questions

App parses and displays one question at a time

User answers by voice or click

Each question has a 60-second timer

App evaluates answers and tracks score

At the end, user gives feedback and rating

Results saved and downloadable as CSV

App speaks the final score using TTS

🛠️ Installation (Step-by-step for Beginners)

Install Python (if not already):

Download Python from python.org and install it.

Open your terminal or command prompt

Clone the GitHub repository:

git clone https://github.com/sabari612/voice_interview_simulator.git
cd voice_interview_simulator

Create a virtual environment (recommended):

python -m venv .venv

Activate the virtual environment:

On Windows:

.venv\Scripts\activate

On Mac/Linux:

source .venv/bin/activate

Install required libraries:

pip install -r requirements.txt

Run the app:

streamlit run app.py

📦 Dependencies

Add these to your requirements.txt:

streamlit
PyMuPDF
pandas
SpeechRecognition
pyttsx3
datetime

✨ Customization Ideas

Add difficulty levels

Store results in a database

Email the report to the candidate

Add webcam + face detection

Theme toggle (dark/light)

📄 License

MIT License

🙋‍♂️ Author

Built with ❤️ by Sabari Abishake K📧 Email: sabariabishake17abd@gmail.com🌐 GitHub: sabari612