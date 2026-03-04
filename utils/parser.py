import PyPDF2

def extract_questions_from_pdf(pdf_path):

    questions = []

    with open(pdf_path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        text = ""

        for page in reader.pages:
            text += page.extract_text()

    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if line:
            questions.append(line)

    return questions