import re
import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

# Skill database (we'll expand this later)
SKILLS = [
    "Python",
    "SQL",
    "Postman",
    "API",
    "REST API",
    "OAuth",
    "SSO",
    "SAML",
    "Canvas",
    "Moodle",
    "Blackboard",
    "D2L",
    "Zendesk",
    "Salesforce",
    "HubSpot",
    "ServiceNow",
    "JIRA",
    "Confluence",
    "ChatGPT",
    "Claude",
    "Microsoft Copilot",
    "Slack",
    "Zoom",
    "AWS",
    "Azure",
    "Docker",
    "Kubernetes"
]

def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if (
            len(line) > 5
            and len(line) < 40
            and line.isupper()
            and "@" not in line
            and "LINKEDIN" not in line.upper()
            and "HTTP" not in line.upper()
        ):
            return line.title()

    return ""

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else ""


def extract_phone(text):
    match = re.search(r'(\+?\d[\d\s\-]{8,}\d)', text)
    return match.group(0).strip() if match else ""


def extract_skills(text):
    found = []

    for skill in SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", text, re.IGNORECASE):
            found.append(skill)

    return sorted(set(found))


def analyze_resume(text):

    doc = nlp(text)

    name = extract_name(text)

    organizations = []

    locations = []

    for ent in doc.ents:

        if ent.label_ == "PERSON" and not name:

            name = ent.text

        elif ent.label_ == "ORG":
            organizations.append(ent.text)

        elif ent.label_ == "GPE":
            locations.append(ent.text)

    return {
        "name": name,
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "organizations": sorted(set(organizations)),
        "locations": sorted(set(locations))
    }