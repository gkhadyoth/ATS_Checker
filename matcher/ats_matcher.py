def calculate_match_score(resume, jd):
    resume_skills = set(skill.lower().strip() for skill in resume["skills"])
    jd_skills = set(skill.lower().strip() for skill in jd["skills_required"])

    matched_skills = resume_skills & jd_skills

    if not jd_skills:
        return 0.0

    score = len(matched_skills) / len(jd_skills) * 100
    return round(score, 2)
