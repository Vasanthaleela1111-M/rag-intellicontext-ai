import re

def clean_text(text):

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)

    # Insert spaces before capital letters
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

    # Insert spaces between words stuck together
    text = re.sub(r'([A-Z]{2,})([A-Z][a-z])', r'\1 \2', text)

    return text.strip()
