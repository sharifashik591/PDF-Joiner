# 📄 Resume Evaluation Project

Welcome to the Resume Evaluation Project! This project evaluates resumes against a job description (JD) PDF to generate scores based on their relevance.

## 📁 Project Structure

resume_evaluation_project/
├── 📂 data/
│ ├── job_description.pdf # Job description PDF file
│ └── 📂 resumes/ # Folder containing resume PDFs
│ ├── resume1.pdf
│ ├── resume2.pdf
│ ├── ...
│ └── resumeN.pdf
├── 📂 src/
│ ├── init.py
│ ├── extract_text.py # Script to extract text from PDFs
│ ├── preprocess.py # Script to preprocess text data
│ ├── compare.py # Script to compare text similarity
│ ├── evaluate.py # Script to evaluate resumes against JD
│ └── utils.py # Utility functions
├── 📄 requirements.txt # Dependencies
└── 📄 README.md # Project documentation



## 🔄 Flow

1. **Extract Text from PDFs (`extract_text.py`)**:
   - Uses `pdfplumber` to extract text from both the job description and resume PDFs.
   - Cleans and preprocesses the extracted text data.

2. **Preprocess Text Data (`preprocess.py`)**:
   - Cleans and preprocesses the extracted text data (e.g., remove special characters, lowercase, tokenize).

3. **Compare Text Similarity (`compare.py`)**:
   - Uses text similarity metrics (e.g., TF-IDF, cosine similarity) to compare preprocessed resume texts with the preprocessed JD text.

4. **Evaluate Resumes Against JD (`evaluate.py`)**:
   - Generates scores or rankings based on the similarity metrics.

5. **Utilities (`utils.py`)**:
   - Includes utility functions used across scripts.

## 🛠️ Setup

### Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/your_username/resume_evaluation_project.git
   cd resume_evaluation_project
    pip install -r requirements.txt


▶️ Usage
Prepare your files:

Ensure data/job_description.pdf contains your job description.
Place resume PDFs in data/resumes/ folder.
Run the main script to evaluate resumes: python src/main.py



👨‍💻 Author
Sharif Ashik