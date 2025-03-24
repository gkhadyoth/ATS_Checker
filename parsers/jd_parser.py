from utils.text_cleaning import clean_text

def parse_job_description(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
    text = clean_text(text)

    return {
        "skills_required": ["Python", "Deep Learning", "SQL", "AWS"],
        "experience_required": "Experience with deploying ML models"
    }
