from textblob import TextBlob

def autocorrect_text(input_text: str) -> str:
    """
    Uses TextBlob to autocorrect spelling in the given text.
    Returns the corrected text.
    """
    blob = TextBlob(input_text)
    corrected = blob.correct()  # Spell-check
    return str(corrected)