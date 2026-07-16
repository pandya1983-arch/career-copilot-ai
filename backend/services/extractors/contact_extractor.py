import re


EMAIL_REGEX = r"[\w\.-]+@[\w\.-]+\.\w+"

PHONE_REGEX = r"(\+?\d[\d\s\-]{8,}\d)"


def extract_email(text: str):
    match = re.search(EMAIL_REGEX, text)
    return match.group(0) if match else ""


def extract_phone(text: str):
    match = re.search(PHONE_REGEX, text)
    return match.group(0).strip() if match else ""