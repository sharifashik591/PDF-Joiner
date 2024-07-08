import os
from PyPDF2 import PdfMerger, PdfReader

def merge_pdfs(folder_path, output_path):
    # Create a PdfMerger object
    merger = PdfMerger()

    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    # List all files in the folder for debugging
    all_files = os.listdir(folder_path)
    print(f"Files in the folder '{folder_path}': {all_files}")

    # Ensure there are PDF files in the folder
    pdf_files = sorted([f for f in all_files if f.lower().endswith('.pdf')])
    if not pdf_files:
        print(f"Error: No PDF files found in the folder '{folder_path}'.")
        return

    # Iterate through all the PDF files and merge them
    for filename in pdf_files:
        file_path = os.path.join(folder_path, filename)
        try:
            # Read the PDF file
            with open(file_path, 'rb') as f:
                reader = PdfReader(f)
                # Check if the file is a valid PDF
                if reader.pages:
                    print(f"Appending {file_path} to the merger.")
                    merger.append(file_path)
                else:
                    print(f"Warning: {file_path} is not a valid PDF or is empty.")
        except Exception as e:
            print(f"Error appending {file_path}: {e}")

    # Write the merged PDF to the output file
    try:
        with open(output_path, 'wb') as output_file:
            merger.write(output_file)
        print(f"Successfully merged PDFs into '{output_path}'.")
    except Exception as e:
        print(f"Error writing the merged PDF: {e}")

# Specify the folder containing the PDFs and the output file path
folder_path = 'C:/Users/FASHOL/Downloads/rooster_resume_1720344443670/MyPart'  # Update this to the correct path
output_path = 'merged_output.pdf'  # Update this to the desired output file path

# Merge the PDFs
merge_pdfs(folder_path, output_path)
