def calculate_match_score(resume, jd):
    resume_skills = set(resume["Skills"])
    jd_skills = set(jd["skills_required"])
    matched_skills = resume_skills & jd_skills
    score = len(matched_skills) / len(jd_skills) * 100
    return round(score, 2)
