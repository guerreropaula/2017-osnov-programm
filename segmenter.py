import sys
import re

def segment_text(text):
    # Evitar dividir en:
    # 1. Puntos suspensivos (...)
    # 2. Punto y coma (;)
    # 3. Exclamación después de la primera palabra
    text = text.replace("... ", "...$")  # Protege puntos suspensivos
    text = text.replace("; ", ";$")  # Protege punto y coma
    
    # Expresión regular para segmentar correctamente
    pattern = r'(?<!\.\s)(?<!;\s)\. '
    text = re.sub(pattern, '.\n', text)
    
    # Restaurar valores protegidos
    text = text.replace("...$", "... ")
    text = text.replace(";$", "; ")

    return text

if __name__ == "__main__":
    text = sys.stdin.read()
    segmented_text = segment_text(text)
    sys.stdout.write(segmented_text)
