# EXERCISE 2 – Python: Recursive TXT report (40 points)
# Usage: python3 txt_report.py SOURCE_DIR OUTPUT_CSV
# Example: python3 txt_report.py python_test/project output/report.csv
# Step 1 (6 points): Read exactly two command-line arguments: source
#     directory and output CSV path. Otherwise print the Usage message
#     and exit 1. Validate the source directory.
# Step 2 (10 points): Recursively find regular .txt files inside the
#     source directory and all subdirectories; ignore other extensions.
# Step 3 (14 points): Write a UTF-8 CSV with header path,size_bytes.
#     Store source-relative paths and file sizes in bytes. Sort by
#     descending size and, for equal sizes, relative path ascending.
# Step 4 (10 points): Do not scan the output CSV file; create the output
#     parent directory when needed. Display exactly:
#     TXT files: N
#     Total bytes: N
#     Largest TXT: relative/path.txt (N bytes)
#     If none exists, print "Largest TXT: none".
# Use pathlib and csv (standard library). Do not use input().

# Write your solution below.

import sys
import csv
from pathlib import Path

def dimensione(r):
    return r[1]

# esattamente due argomenti
if len(sys.argv) != 3:
    print("Uso: python3 txt_report.py SOURCE_DIR OUTPUT_CSV")
    sys.exit()

source = Path(sys.argv[1])
output = Path(sys.argv[2])

# la sorgente deve essere una directory
if not source.is_dir():
    print(f"Errore: '{source}'non e una directory")
    sys.exit()

# .txt regolari in modo ricorsivo
# escluso il file di output
rows = []
for p in source.rglob("*.txt"):
    if p.is_file() and p.resolve() != output.resolve():
        percorso = p.relative_to(source).as_posix()   # nome del file
        grandezza = p.stat().st_size                  # dimensione del file in byte
        coppia = (percorso, grandezza)                # unisce nome e dimensione in una tupla
        rows.append(coppia)                           # aggiunge la tupla alla lista rows

# ordina le righe 
rows.sort() # a to Z
rows.sort(key=dimensione, reverse=True) # grande to piccolo

# crea la cartella di output se manca
output.parent.mkdir(parents=True, exist_ok=True)

# CSV UTF-8 con intestazione
with output.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["path", "size_bytes"])
    writer.writerows(rows)

# output
print(f"TXT files: {len(rows)}")
print(f"Total bytes: {sum(size for _, size in rows)}")
if rows:
    print(f"Largest TXT: {rows[0][0]} ({rows[0][1]} bytes)")
else:
    print("Largest TXT: none")
