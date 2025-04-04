import sys

def segment_text(text):
    pattern = r'(?<!\.\s)(?<!;\s)\. '
    return re.sub(pattern, '.\n', text)


text = sys.stdin.read()
segmented_text = segment_text(text)
sys.stdout.write(segmented_text)