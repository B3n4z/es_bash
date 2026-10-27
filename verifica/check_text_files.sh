#!/bin/bash
# EXERCISE 1 – Bash: Analyse text files (30 points)
# Usage: bash check_text_files.sh DIRECTORY
# Example: bash check_text_files.sh bash_test
# Step 1 (6 points): Accept exactly one command-line argument (directory).
#     If the count is wrong, print Usage and exit 1; validate the directory.
# Step 2 (8 points): Search regular .txt files in the directory and its
#     immediate subdirectories using *.txt and */*.txt; support spaces.
# Step 3 (10 points): Count readable and unreadable .txt files separately;
#     sum the byte sizes of readable files only.
# Step 4 (6 points): Print exactly:
#     Readable TXT files: N
#     Unreadable TXT files: N
#     Total readable bytes: N
#     With no matches, all totals must be 0.
# Use normal Bash globbing, without shopt or find; no deeper recursion.

# Write your solution below.

#!/bin/bash

# esattamente un argomento
if [ $# -ne 1 ]; then
    echo "Uso: check_text_files.sh DIRECTORY"
    exit 
fi

dir="$1"

# la directory deve esistere
if [ ! -d "$dir" ]; then
    echo "Errore: '$dir' non e una dir"
    exit 
fi

readable=0
unreadable=0
bytes=0

# *.txt e */*.txt, virgolette per gestire gli spazi
for f in "$dir"/*.txt "$dir"/*/*.txt; do
    # contolla che siano dei veri file e non dei falsi 
    if [ ! -f "$f" ]; then
        continue
    fi

    # leggibili vs non leggibili, byte solo dei leggibili
    if [ -r "$f" ]; then
        readable=$((readable + 1))
        bytes=$((bytes + $(wc -c < "$f")))
    else
        unreadable=$((unreadable + 1))
    fi
done

#output
echo "Readable TXT files: $readable"
echo "Unreadable TXT files: $unreadable"
echo "Totale readable bytes: $bytes"