import sys
import re

def tokenise(text):
    # List of abbreviations that should keep their periods
    abbreviations = {"Sr.", "Sra.", "Dr.", "Dra.", "etc.", "Ej."}

    # Replace periods in abbreviations temporarily
    for abbr in abbreviations:
        text = text.replace(abbr, abbr.replace(".", "_DOT_"))

    # Separate punctuation (excluding abbreviations)
    punctuations = [",", ":", ";", "(", ")"]
    for p in punctuations:
        text = text.replace(p, f" {p} ")

    # Separate periods that are not part of an abbreviation
    text = re.sub(r"(?<=\w)\.(?!\s|DOT_)", " .", text)  

    # Keep large numbers intact
    text = re.sub(r"(\d+)\s(\d{3})", r"\1\2", text)

    # Tokenise 
    tokens = text.split()

    # Restore abbreviations' periods
    tokens = [token.replace("_DOT_", ".") for token in tokens]

    # Print tokens in CoNLL-U format
    for i, token in enumerate(tokens, start=1):
        print(f"{i}\t{token}\t_\t_\t_\t_\t_\t_\t_")

if __name__ == "__main__":
    for line in sys.stdin:
        tokenise(line.strip())




