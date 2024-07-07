# main.py
from extract_text import extract_text_from_pdf, extract_text_from_folder
from preprocess import preprocess_text, preprocess_texts
from compare import calculate_similarity
from evaluate import generate_scores
from utils import save_scores_to_csv

def main():
    job_description_path = 'data/job_description.pdf'
    resumes_folder = 'data/resumes'

    # Extract text
    jd_text = extract_text_from_pdf(job_description_path)
    resume_texts = extract_text_from_folder(resumes_folder)

    # Preprocess text
    preprocessed_jd_text = preprocess_text(jd_text)
    preprocessed_resume_texts = preprocess_texts(resume_texts)

    # Calculate similarity
    similarities = calculate_similarity(preprocessed_jd_text, preprocessed_resume_texts)

    # Generate scores
    resume_scores = generate_scores(similarities, resume_texts)

    # Save scores to CSV
    save_scores_to_csv(resume_scores, 'resume_scores.csv')

    # Optionally, print or visualize the scores
    for filename, score in resume_scores.items():
        print(f"{filename}: Score - {score}")

if __name__ == "__main__":
    main()
