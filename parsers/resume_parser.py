import os
import docx
from pdfminer.high_level import extract_text
import spacy
from utils.text_cleaning import clean_text
import re

nlp = spacy.load("en_core_web_sm")

def extract_text_from_file(filepath):
    if filepath.lower().endswith(".pdf"):
        return extract_text(filepath)
    elif filepath.lower().endswith(".docx"):
        doc = docx.Document(filepath)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format: must be .pdf or .docx")
    
def extract_skills_from_structured_text(text):
    skill_pattern = re.compile(r'[\u2022•]?\s*[\w\s&]+:\s*(.+)', re.IGNORECASE)
    matches = skill_pattern.findall(text)

    skills = []
    for line in matches:
        parts = re.split(r',\s*', line)
        for skill in parts:
            skills.append(skill.strip().lower())

    return list(set(skills))

def extract_skills(text):
    return extract_skills_from_structured_text(text)

def extract_experience(text):
    sentences = text.split(".")
    relevant = [s for s in sentences if "experience" in s.lower() or "worked" in s.lower()]
    return ". ".join(relevant).strip()

def parse_resume(filepath):
    raw_text = extract_text_from_file(filepath)
    cleaned = clean_text(raw_text)
    
    skills = extract_skills(cleaned)
    experience = extract_experience(cleaned)
    
    return {
        "name": "Candidate",
        "Skills": skills,
        "experience": experience,
        "education": "Auto-extraction not yet implemented"
    }
