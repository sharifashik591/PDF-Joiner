# src/compare.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(jd_text, resume_texts):
    documents = [jd_text] + list(resume_texts.values())
    tfidf_vectorizer = TfidfVectorizer().fit_transform(documents)
    similarities = cosine_similarity(tfidf_vectorizer[0:1], tfidf_vectorizer[1:]).flatten()
    return similarities[1:]

if __name__ == "__main__":
    similarities = calculate_similarity(preprocessed_jd_text, preprocessed_resume_texts)
