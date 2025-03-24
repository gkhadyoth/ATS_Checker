# ATS_Checker

## This is the file structure to work this on Local PCs

ats_resume_filter/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── sample_resume.pdf                                                                    # Or .docx (actual resume file)
│   └── sample_jd.txt (Will work on URL if text format starts executing properly)            # Job description in plain text
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
