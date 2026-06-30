# Candidate Profile Transformer

## Overview

Candidate Profile Transformer is a modular Python application that consolidates candidate information from both structured and unstructured sources into a unified candidate profile.

For this implementation:

- Structured source: Recruiter CSV
- Unstructured source: Resume PDF

The application extracts candidate information, normalizes inconsistent values, merges information from multiple sources while preserving provenance metadata internally, validates the final profile, and generates a configurable JSON output.

---

## Features

- Read structured recruiter data from CSV
- Extract information from Resume PDF
- Normalize phone numbers
- Normalize common skill aliases
- Merge information from multiple sources
- Maintain confidence and provenance metadata internally
- Config-driven output projection
- Validate required fields before generating output
- Generate clean JSON output

---

## Project Architecture

```mermaid
flowchart TD

    subgraph Structured Source
        A[Recruiter CSV]
        B[CSV Reader]
        C[CSV Extractor]
        D[Candidate (CSV)]

        A --> B
        B --> C
        C --> D
    end

    subgraph Unstructured Source
        E[Resume PDF]
        F[Resume Reader]
        G[Resume Extractor]
        H[Candidate (Resume)]

        E --> F
        F --> G
        G --> H
    end

    D --> I[Candidate Normalizer]
    H --> I

    I --> J[Profile Merger]
    J --> K[Projector]
    K --> L[Validator]
    L --> M[Candidate Profile JSON]
```
## Folder Structure

```
candidate-profile-transformer/
│
├── data/
│   ├── config/
│   ├── input/
│   └── output/
│
├── src/
│   ├── models/
│   ├── readers/
│   ├── extractors/
│   ├── normalizers/
│   ├── mergers/
│   ├── projection/
│   ├── validators/
│   ├── utils/
│   └── main.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

1. Clone the repository.

2. Create a virtual environment.

```bash
python -m venv venv
```

3. Activate the environment.

Windows

```bash
venv\Scripts\activate
```

4. Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Project

Place the following files inside:

```
data/input/
```

- recruiter.csv
- resume.pdf

Then execute:

```bash
python -m src.main
```

The generated output will be stored in:

```
data/output/
```

---

## Configuration

The output is controlled through:

```
data/config/config.json
```

This allows selecting which fields should appear in the final JSON and supports field renaming without modifying application code.

---

## Design Decisions

During implementation, the following design principles were followed:

- Separation of responsibilities across modules
- Object-oriented data model using Pydantic
- Configurable output projection
- Internal provenance tracking
- Modular normalization pipeline
- Simple and explainable merge strategy

The focus was on readability, maintainability, and extensibility rather than over-engineering.

---

## Assumptions

- One recruiter CSV represents one candidate.
- Resume text contains recognizable section headings such as Skills, Experience and Education.
- Skill normalization is dictionary-based.
- Phone normalization assumes Indian phone numbers for this implementation.
- Confidence scores are heuristic values assigned during extraction.

---

## Sample Output

```json
{
  "candidate_id": "...",
  "full_name": "John Doe",
  "headline": "AI Engineer",
  "primary_emails": [
    "john.doe@gmail.com"
  ],
  "primary_phones": [
    "+919876543210"
  ],
  "skills": [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "SQL"
  ],
  "years_experience": 3.0,
  "overall_confidence": 0.9
}
```

---

## Future Improvements

Potential enhancements include:

- Advanced resume parsing using NLP
- Support for additional structured data sources
- Better confidence scoring
- Automatic skill ontology mapping
- Enhanced experience and education extraction
- Unit and integration tests
- REST API deployment

---
