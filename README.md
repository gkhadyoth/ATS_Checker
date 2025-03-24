# ATS_Checker

## This is the file structure to work this on Local PCs

graph TD
    A[main.py] --> B[Resume Parser]
    A --> C[Job Description Parser]
    B --> D[Resume Text]
    C --> E[JD Text]
    D --> F[ATS Matcher]
    E --> F
    F --> G[Match Score & Relevant Sections]
    G --> H[Enhancer: Suggestion Engine]
    H --> I[Suggested Resume Enhancements]

    subgraph parsers
        B[resume_parser.py]
        C[jd_parser.py]
    end

    subgraph matcher
        F[ats_matcher.py]
    end

    subgraph enhancer
        H[suggestion_engine.py]
    end

    subgraph utils
        J[text_cleaning.py]
    end

    style A fill:#f9f,stroke:#333,stroke-width:1px
    style I fill:#bbf,stroke:#333,stroke-width:1px

