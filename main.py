import os
from pypdf import PdfReader

# Change to where you keep the PDF's on your computer
PDF_FOLDER = "/Users/mollymidkiff/Desktop/GEG"
#this list can easily be modified for different words as well
SEARCH_WORDS = ["environment", "water","energy","cost","pollution","fight","economy"]
# this is where your results will write
OUTPUT_FILE = "results.txt"

results = []

for filename in sorted(os.listdir(PDF_FOLDER)):
    if not filename.endswith(".pdf"):
        continue

    filepath = os.path.join(PDF_FOLDER, filename)
    try:
        reader = PdfReader(filepath)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text() or ""

        lower_text = full_text.lower()
        counts = {word: lower_text.count(word.lower()) for word in SEARCH_WORDS}
        article_name = os.path.splitext(filename)[0]
        results.append((article_name, counts))
        print(f"✓ {article_name}: {counts}")

    except Exception as e:
        print(f"✗ Skipped {filename}: {e}")

with open(OUTPUT_FILE, "w") as f:
    for name, counts in results:
        f.write(f'"{name}"\n')
        for word, count in counts.items():
            f.write(f'  "{word}" - {count}\n')
        f.write("\n")
