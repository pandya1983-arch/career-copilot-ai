import re


def clean_resume_text(text: str) -> str:
    """Normalize resume text before extraction."""

    # Normalize line endings
    text = text.replace("\r", "\n")

    # Collapse repeated whitespace
    text = re.sub(r"[ \t]+", " ", text)

    # Collapse multiple blank lines
    text = re.sub(r"\n{2,}", "\n", text)

    # Remove bullet symbols but keep text
    text = text.replace("•", "")

    return text.strip()