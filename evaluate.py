# src/evaluate.py
from compare import calculate_similarity

def generate_scores(similarities, resume_texts):
    scores = {}
    for idx, filename in enumerate(resume_texts.keys()):
        scores[filename] = similarities[idx]
    return scores

if __name__ == "__main__":
    resume_scores = generate_scores(similarities, resume_texts)
    for filename, score in resume_scores.items():
        print(f"{filename}: Score - {score}")
