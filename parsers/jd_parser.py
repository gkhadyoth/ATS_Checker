from utils.text_cleaning import clean_text
from utils.skills_list import common_skills

def parse_job_description(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    cleaned = clean_text(text)
    text_words = cleaned.lower()

    # Match known skills present in text
    skills_required = [skill for skill in common_skills if skill.lower() in text_words]

    # Get one experience line, optional
    experience_required = ""
    for line in cleaned.split("."):
        if "experience" in line.lower():
            experience_required = line.strip()
            break

    return {
        "skills_required": skills_required,
        "experience_required": experience_required
    }
