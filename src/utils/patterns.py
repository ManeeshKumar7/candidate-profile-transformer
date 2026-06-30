import re


EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)

PHONE_PATTERN = re.compile(
    r"(?:\+?\d{1,3}[- ]?)?\d{10}"
)

LINKEDIN_PATTERN = re.compile(
    r"https?://(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+"
)

GITHUB_PATTERN = re.compile(
    r"https?://(?:www\.)?github\.com/[A-Za-z0-9_-]+"
)