def generate_suggestions(resume, jd):
    suggestions = []

    resume_skills = set(skill.lower().strip() for skill in resume["skills"])
    jd_skills = set(skill.lower().strip() for skill in jd["skills_required"])
    missing_skills = jd_skills - resume_skills

    if missing_skills:
        suggestions.append(f"Consider adding these skills to your resume: {', '.join(sorted(missing_skills))}")

    # Better experience matching
    resume_experience_text = resume["experience"].lower()
    jd_experience_keywords = [word.strip() for word in jd["experience_required"].lower().split() if len(word) > 4]

    matches = [word for word in jd_experience_keywords if word in resume_experience_text]

    if len(matches) < 2:  # threshold for fuzzy match
        suggestions.append("Your resume may be missing relevant experience like: " + jd["experience_required"])

    if not suggestions:
        suggestions.append("Your resume seems well-matched for this role!")

    return suggestions
