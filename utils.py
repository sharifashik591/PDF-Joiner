# src/utils.py
def save_scores_to_csv(scores, output_file):
    import csv
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Resume', 'Score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for filename, score in scores.items():
            writer.writerow({'Resume': filename, 'Score': score})
