# src/extract_text.py
import pdfplumber
import os

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text()
    return full_text

def extract_text_from_folder(folder_path):
    texts = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            texts[filename] = extract_text_from_pdf(pdf_path)
    return texts

if __name__ == "__main__":
    job_description_path = '../data/job_description.pdf'
    resumes_folder = '../data/resumes'

    jd_text = extract_text_from_pdf(job_description_path)
    resume_texts = extract_text_from_folder(resumes_folder)
