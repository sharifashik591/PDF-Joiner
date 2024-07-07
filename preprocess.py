# src/preprocess.py
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def preprocess_texts(texts):
    preprocessed_texts = {}
    for filename, text in texts.items():
        preprocessed_texts[filename] = preprocess_text(text)
    return preprocessed_texts

if __name__ == "__main__":
    preprocessed_jd_text = preprocess_text(jd_text)
    preprocessed_resume_texts = preprocess_texts(resume_texts)
