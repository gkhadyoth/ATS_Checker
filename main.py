from parsers.resume_parser import parse_resume
from parsers.jd_parser import parse_job_description
from matcher.ats_matcher import calculate_match_score
from enhancer.suggestion_engine import generate_suggestions

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--resume', required=True, help='Path to resume text file')
    parser.add_argument('--job', required=True, help='Path to job description text file')
    args = parser.parse_args()

    resume_data = parse_resume(args.resume)
    jd_data = parse_job_description(args.job)

    score = calculate_match_score(resume_data, jd_data)
    suggestions = generate_suggestions(resume_data, jd_data)

    print("Match Score:", score)
    print("\nSuggestions:")
    for s in suggestions:
        print("\n-", s)  
    
   # print("Resume skills:", resume_data["skills"])
   # print("JD skills:", jd_data["skills_required"])


