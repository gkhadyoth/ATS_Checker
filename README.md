# ATS_Checker

> This is the file structure to run on Local PCs (Open to understand)

ats_resume_filter/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── sample_resume.pdf         # Or .docx (actual resume file)
│   └── sample_jd.txt             # Job description in plain text (Will work on URL format once text format starts executing properly)
│
├── parsers/
│   ├── __init__.py
│   ├── resume_parser.py
│   └── jd_parser.py
│
├── matcher/
│   ├── __init__.py
│   └── ats_matcher.py
│
├── enhancer/
│   ├── __init__.py
│   └── suggestion_engine.py
│
├── utils/
│   ├── __init__.py
│   └── text_cleaning.py
│   └── skills_list.py

