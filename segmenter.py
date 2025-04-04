import sys

def segment_text(text):
    return text.replace('. ', '.\n')


text = sys.stdin.read()
segmented_text = segment_text(text)
sys.stdout.write(segmented_text)