import re
import fitz  # PyMuPDF

def parse_pdf_with_answers(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    raw_text = ""
    for page in doc:
        raw_text += page.get_text()

    lines = raw_text.split("\n")
    questions = []
    current = {}

    for line in lines:
        line = line.strip()
        if re.match(r"^(question|q\d*|q)[\.:)]", line.lower()):
            if current:
                questions.append(current)
            current = {"question": line, "options": [], "answer": None}
        elif line[:1].lower() in ["a", "b", "c", "d"] and ")" in line:
            if "options" in current:
                current["options"].append(line)
        elif line.lower().startswith("answer:"):
            current["answer"] = line.split("answer:")[-1].strip().upper()
        else:
            pass

    if current:
        questions.append(current)
    return questions
