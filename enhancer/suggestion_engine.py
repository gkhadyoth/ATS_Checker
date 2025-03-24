def generate_suggestions(resume, jd):
    suggestions = []
    resume_skills = set(resume["Skills"])
    jd_skills = set(jd["skills_required"])
    missing_skills = jd_skills - resume_skills

    if missing_skills:
        suggestions.append(f"Consider adding these skills: {', '.join(missing_skills)}")

    if jd["experience_required"] not in resume["experience"]:
        suggestions.append("Mention relevant experience with deploying ML models.")

    return suggestions
