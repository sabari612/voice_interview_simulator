import streamlit as st
import fitz  # PyMuPDF
import re
import time
import pandas as pd
from datetime import datetime
from utils.stt import listen_and_transcribe
from utils.feedback import get_feedback
from utils.tts import speak_text  # ✅ Make sure this exists and works

# 🎨 Animation Styling
st.markdown("""
    <style>
    .stApp { animation: fadeIn 0.8s ease-in-out; }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .stButton>button {
        transition: 0.2s ease-in-out;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background-color: #0e76a8;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="🎙️ PDF Interview Quiz", layout="centered")

# ---- SESSION STATE ----
if "name" not in st.session_state:
    st.session_state.name = ""
if "questions" not in st.session_state:
    st.session_state.questions = []
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answers" not in st.session_state:
    st.session_state.answers = []
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "spoken_answer" not in st.session_state:
    st.session_state.spoken_answer = ""

# ---- STEP 1: NAME INPUT ----
if not st.session_state.name:
    st.title("🎓 Welcome to Your Voice Interview Test")
    name = st.text_input("Enter your name to begin:")
    if st.button("Start Test") and name.strip():
        st.session_state.name = name.strip()
        st.rerun()
    st.stop()

# ---- STEP 2: PDF UPLOAD & PARSE ----
if not st.session_state.questions:
    st.title(f"👋 Hi {st.session_state.name}, upload your MCQ PDF")

    uploaded_file = st.file_uploader("📄 Upload your PDF with MCQ Questions", type=["pdf"])
    if uploaded_file:
        with st.spinner("🔍 Reading your questions..."):
            doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            text = "\n".join([page.get_text() for page in doc])

            st.markdown("### 🔍 Extracted Text from PDF")
            st.code(text)

            lines = text.split("\n")
            questions = []
            current = {}

            for line in lines:
                line = line.strip()

                if re.match(r"^(question\s*\d*|q\s*\d*|q)[\.:)]?", line.lower()):
                    if current:
                        questions.append(current)
                    current = {"question": line, "options": [], "answer": None}
                elif re.match(r"^[A-Da-d][\)\.] ?.+", line):
                    if "options" in current:
                        current["options"].append(line.strip())
                elif re.search(r"answer\s*[:\-]\s*[A-Da-d]", line.lower()):
                    ans = re.findall(r"answer\s*[:\-]\s*([A-Da-d])", line, flags=re.IGNORECASE)
                    if ans:
                        current["answer"] = ans[0].upper()

            if current:
                questions.append(current)

            valid_questions = [
                q for q in questions
                if q.get("question") and isinstance(q.get("options"), list) and len(q["options"]) >= 2
            ]

            st.markdown("### 🧪 Parsed Questions (Debug)")
            st.code(valid_questions)

            st.session_state.questions = valid_questions

        st.success(f"✅ Loaded {len(st.session_state.questions)} valid questions!")
        st.rerun()
    else:
        st.info("Please upload a PDF file to begin.")
    st.stop()

# ---- STEP 3: QUIZ TIME ----
if st.session_state.q_index >= len(st.session_state.questions):
    st.title(f"🎉 Test Complete, {st.session_state.name}!")
    st.write(f"✅ Final Score: **{st.session_state.score} / {len(st.session_state.questions)}**")

    st.text_area("📝 Share your experience", key="feedback_text")
    rating = st.slider("⭐ Rate the test", 1, 5, 3)

    if st.button("Finish"):
        df = pd.DataFrame(st.session_state.answers)
        df["username"] = st.session_state.name
        df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df["feedback"] = st.session_state.get("feedback_text", "")
        df["rating"] = rating

        df.to_csv("results.csv", mode="a", index=False, header=not pd.io.common.file_exists("results.csv"))

        final_message = f"{st.session_state.name}, you completed the test and scored {st.session_state.score} out of {len(st.session_state.questions)}. Great job!"
        st.markdown(f"🗣️ `{final_message}`")
        speak_text(final_message)

        st.download_button("⬇️ Download Your Answers", df.to_csv(index=False), file_name="your_results.csv", mime="text/csv")
        st.success("✅ Your answers and feedback are saved.")
        st.stop()

else:
    q = st.session_state.questions[st.session_state.q_index]
    st.markdown(f"### Q{st.session_state.q_index + 1}: {q['question']}")
    selected_option = st.radio("Choose or Speak:", q["options"], key=f"opt_{st.session_state.q_index}")

    elapsed = int(time.time() - st.session_state.start_time)
    left = 60 - elapsed
    st.info(f"⏰ Time left: {left} seconds")

    if left <= 0:
        st.warning("⏳ Time's up! Moving to next question...")
        st.session_state.q_index += 1
        st.session_state.start_time = time.time()
        st.rerun()

    if st.button("🎤 Speak Now"):
        transcript = listen_and_transcribe()
        st.session_state.spoken_answer = transcript
        st.markdown(f"🎙️ You said: `{transcript}`")

    if st.button("✅ Submit Answer"):
        final = st.session_state.spoken_answer or selected_option
        user_letter = final[0].upper() if final else None
        correct = q.get("answer")

        is_correct = user_letter == correct
        if is_correct:
            st.session_state.score += 1

        st.session_state.answers.append({
            "question": q["question"],
            "selected": final,
            "correct": correct,
            "is_correct": is_correct
        })

        st.session_state.q_index += 1
        st.session_state.spoken_answer = ""
        st.session_state.start_time = time.time()
        st.rerun()