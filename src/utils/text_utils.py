import re


def clean_text(text: str) -> str:
    """
    Removes unwanted spaces and blank lines.
    """

    text = re.sub(r"\r", "", text)

    text = re.sub(r"\t", " ", text)

    text = re.sub(r"\n+", "\n", text)

    text = re.sub(r" +", " ", text)

    return text.strip()