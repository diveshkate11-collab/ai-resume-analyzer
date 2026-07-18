# 🚀 AI Resume Copilot

<div align="center">

### AI-Powered Resume Analysis, ATS Optimization & Career Assistant

Build smarter resumes, analyze ATS compatibility, identify skill gaps, receive job recommendations, and prepare for technical interviews using an AI-powered backend.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?logo=fastapi)
![Tests](https://img.shields.io/badge/Tests-71_Passed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active_Development-orange)

</div>

---

# 📖 Table of Contents

- About
- Features
- Screenshots
- Demo
- Technology Stack
- System Architecture
- Project Structure
- Installation
- Configuration
- Running the Project
- API Documentation
- AI Engine
- Testing
- Roadmap
- Version History
- Future Enhancements
- Contributing
- License
- Author

---

# 📚 About

AI Resume Copilot is a modular AI-powered backend application that analyzes resumes and provides actionable career insights.

The application is designed to help users:

- Parse resumes
- Calculate ATS scores
- Detect resume weaknesses
- Recommend suitable job roles
- Identify missing technical skills
- Explain AI-generated recommendations
- Prepare for interviews

The project is being developed using modern software engineering practices including modular architecture, automated testing, and incremental feature development.

---

# 🎯 Objectives

The primary goals of this project are:

- Build an industry-ready AI Resume Analyzer
- Learn production-grade FastAPI development
- Design reusable AI modules
- Follow clean software architecture
- Implement automated testing using Pytest
- Build a deployment-ready backend
- Create a portfolio-quality software engineering project

---

# ✨ Current Features

## Resume Parsing

- PDF Resume Parsing
- DOCX Resume Parsing
- Resume Text Cleaning
- Contact Information Extraction
- Skills Extraction
- Education Extraction
- Experience Extraction

---

## ATS Analysis

- ATS Score Calculation
- Keyword Matching
- Resume Section Validation
- Formatting Analysis
- Grammar Analysis

---

## Job Recommendation

- Role Prediction
- Job Matching
- Skill Gap Analysis
- Career Recommendations

---

## Explainability

- ATS Score Explanation
- Job Recommendation Explanation
- Skill Gap Explanation

---

## Current Project Status

| Module | Status |
|---------|--------|
| Parser | ✅ Completed |
| ATS | ✅ Completed |
| Jobs | ✅ Completed |
| Explainability | ✅ Completed |
| Improvement | 🚧 In Progress |
| Analytics | ⏳ Planned |
| Interview | ⏳ Planned |
| Training | ⏳ Planned |
| AI Copilot | ⏳ Planned |

---

## 📊 Latest Milestone

Current Version

```
v0.4.0
```

Latest Achievement

```
71 Passing Unit Tests
```

Current Focus

```
Improvement Module
```

---

## ⭐ Why This Project?

Most resume analyzers only generate a score.

AI Resume Copilot is designed to become a complete career assistance platform capable of resume analysis, career guidance, interview preparation, analytics, and AI-powered recommendations within a single application.

---

# 🛠️ Technology Stack

AI Resume Copilot is built using modern backend technologies and follows a modular software architecture.

## Programming Language

- Python 3.14

---

## Backend Framework

- FastAPI
- Uvicorn

---

## Data Validation

- Pydantic

---

## Resume Parsing

- PyPDF2
- python-docx
- Regular Expressions (Regex)

---

## Testing

- Pytest
- HTTPX
- FastAPI TestClient

---

## Development Tools

- Visual Studio Code
- Git
- GitHub

---

## Planned Technologies

- PostgreSQL
- SQLAlchemy
- Docker
- Kubernetes
- AWS
- React
- LangChain
- LangGraph
- Vector Database
- OpenAI API
- Ollama
- RAG

---

# 🏛️ System Architecture

The project follows a layered architecture to keep the application modular, scalable, and easy to maintain.

```text
                        Client
                           │
                           ▼
                    FastAPI REST API
                           │
                           ▼
                    Request Validation
                           │
                           ▼
                      Service Layer
                           │
                           ▼
                      AI Engine Core
        ┌───────────┬───────────┬───────────┐
        ▼           ▼           ▼           ▼
     Parser        ATS        Jobs   Explainability
        │
        ▼
   Structured Resume
        │
        ▼
    JSON API Response
```

---

# 📂 Project Structure

```text
AI_RESUME_COPILOT/

├── app/
│
├── ai_engine/
│   ├── parser/
│   ├── ats/
│   ├── jobs/
│   ├── explainability/
│   ├── improvement/
│   ├── analytics/
│   ├── interview/
│   ├── training/
│   └── copilot/
│
├── api/
├── core/
├── database/
├── models/
├── prompts/
├── schemas/
├── services/
├── utils/
│
├── tests/
│   ├── ai_engine/
│   ├── api/
│   └── integration/
│
├── uploads/
├── storage/
├── docs/
├── deployment/
├── frontend/
│
├── requirements.txt
├── pyproject.toml
├── README.md
└── LICENSE
```

---

# ⚙️ Development Workflow

Every feature follows the same development lifecycle.

```text
Requirement
      │
      ▼
Planning
      │
      ▼
Design
      │
      ▼
Implementation
      │
      ▼
Unit Testing
      │
      ▼
Integration
      │
      ▼
Documentation
      │
      ▼
Git Commit
```

---

# 📸 Screenshots

The following screenshots will be added as development progresses.

| Screenshot | Status |
|------------|--------|
| Home Page | 🚧 |
| Resume Upload | 🚧 |
| Resume Analysis | 🚧 |
| ATS Report | 🚧 |
| Job Recommendation | 🚧 |
| Skill Gap Analysis | 🚧 |
| API Documentation | 🚧 |

---

# 🎥 Live Demo

The live demo will be available after deployment.

**Status:** 🚧 Coming Soon

---

# 🌐 API Documentation

Interactive API documentation will be available after running the FastAPI application.

## Swagger UI

```
http://127.0.0.1:8000/docs
```

## ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🚀 Installation

Follow the steps below to set up AI Resume Copilot on your local machine.

---

## Prerequisites

Before installing the project, make sure the following software is installed.

| Software | Version |
|----------|----------|
| Python | 3.12+ |
| Git | Latest |
| VS Code | Recommended |

---

## Clone Repository

```bash
git clone https://github.com/diveshkate11-collab/ai-resume-analyzer.git
```

Move into the project directory.

```bash
cd ai-resume-analyzer
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate the environment.

```bash
.venv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv .venv
```

Activate the environment.

```bash
source .venv/bin/activate
```

---

## Install Dependencies

Install all required Python packages.

```bash
pip install -r requirements.txt
```

---

## Verify Installation

Check the installed Python version.

```bash
python --version
```

Check installed packages.

```bash
pip list
```

---

# ▶️ Running the Project

Start the FastAPI development server.

```bash
uvicorn app.main:app --reload
```

If everything is configured correctly, the server will start successfully.

---

## Local Server

```
http://127.0.0.1:8000
```

---

## Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## ReDoc Documentation

```
http://127.0.0.1:8000/redoc
```

---

# 📁 Configuration

The project currently requires minimal configuration.

Future configuration options will include:

- Database Connection
- JWT Authentication
- API Keys
- Email Service
- Logging
- Cloud Storage

---

# 🔑 Environment Variables

A sample environment file will be added in future releases.

Example:

```env
DATABASE_URL=

SECRET_KEY=

OPENAI_API_KEY=

JWT_SECRET_KEY=

SMTP_USERNAME=

SMTP_PASSWORD=
```

---

# 🧪 Running Tests

Run all tests.

```bash
python -m pytest tests -v
```

---

## Run Parser Tests

```bash
python -m pytest tests/ai_engine/parser -v
```

---

## Run ATS Tests

```bash
python -m pytest tests/ai_engine/ats -v
```

---

## Run Jobs Tests

```bash
python -m pytest tests/ai_engine/jobs -v
```

---

## Run Explainability Tests

```bash
python -m pytest tests/ai_engine/explainability -v
```

---

## Current Test Status

| Module | Status |
|---------|--------|
| Parser | ✅ Passed |
| ATS | ✅ Passed |
| Jobs | ✅ Passed |
| Explainability | ✅ Passed |

---

## Latest Test Summary

```text
Total Unit Tests Passed : 71

Failed : 0

Build Status : PASSING
```

---

# 📦 Dependencies

Core dependencies currently used in the project.

| Package | Purpose |
|----------|----------|
| FastAPI | REST API Framework |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |
| PyPDF2 | PDF Parsing |
| python-docx | DOCX Parsing |
| Pytest | Unit Testing |
| HTTPX | API Testing |

---

# 🧠 AI Engine

The AI Engine is the core component of AI Resume Copilot. It processes resumes, performs ATS analysis, predicts job roles, explains AI decisions, and generates actionable recommendations.

The architecture is modular, allowing every component to be developed, tested, and maintained independently.

---

## AI Engine Modules

| Module | Purpose | Status |
|---------|---------|--------|
| Parser | Resume Parsing | ✅ Completed |
| ATS | ATS Score Calculation | ✅ Completed |
| Jobs | Job Recommendation | ✅ Completed |
| Explainability | AI Decision Explanation | ✅ Completed |
| Improvement | Resume Improvement | 🚧 In Progress |
| Analytics | Resume Analytics | ⏳ Planned |
| Interview | Interview Preparation | ⏳ Planned |
| Training | Learning Recommendation | ⏳ Planned |
| Copilot | AI Career Assistant | ⏳ Planned |

---

# 🏗️ AI Engine Architecture

```text
Resume
   │
   ▼
Parser
   │
   ▼
Structured Resume Data
   │
   ├──────────────┬──────────────┬──────────────┐
   ▼              ▼              ▼              ▼
 ATS           Jobs      Explainability   Improvement
   │              │              │              │
   └──────────────┴──────────────┴──────────────┘
                  │
                  ▼
            Final JSON Response
```

---

# 📄 Resume Parser Module

The Resume Parser extracts structured information from uploaded resumes.

### Supported Formats

- PDF
- DOCX

---

### Components

| Component | Description |
|-----------|-------------|
| PDF Parser | Extracts text from PDF resumes |
| DOCX Parser | Extracts text from DOCX resumes |
| Text Cleaner | Cleans extracted text |
| Contact Parser | Extracts contact details |
| Skills Parser | Extracts technical skills |
| Education Parser | Extracts education details |
| Experience Parser | Extracts work experience |
| Resume Parser | Integrates all parser modules |

---

### Extracted Information

```text
Resume

├── Contact Information

├── Skills

├── Education

├── Experience

└── Metadata
```

---

### Parser Workflow

```text
Resume Upload
      │
      ▼
PDF / DOCX Parser
      │
      ▼
Text Cleaner
      │
      ▼
Contact Parser
      │
      ▼
Education Parser
      │
      ▼
Experience Parser
      │
      ▼
Skills Parser
      │
      ▼
Structured Resume
```

---

### Current Status

```text
Status

Completed ✅

Supported Formats

✔ PDF

✔ DOCX

Unit Tests

✔ Passed
```

---

# 📊 Parser Output Example

```json
{
  "contact": {},
  "skills": [],
  "education": {},
  "experience": {},
  "metadata": {
    "characters": 1250
  }
}
```

---

# 🎯 ATS Engine

The ATS (Applicant Tracking System) Engine evaluates resumes based on commonly used ATS principles. It analyzes resume structure, technical keywords, formatting, grammar, and calculates an overall ATS score.

---

## ATS Components

| Component | Description | Status |
|-----------|-------------|--------|
| ATS Scorer | Calculates overall ATS score | ✅ Completed |
| Keyword Matcher | Matches technical keywords | ✅ Completed |
| Section Checker | Detects required resume sections | ✅ Completed |
| Formatting Checker | Validates formatting quality | ✅ Completed |
| Grammar Checker | Performs basic grammar validation | ✅ Completed |

---

# ATS Workflow

```text
Structured Resume
        │
        ▼
Section Checker
        │
        ▼
Keyword Matcher
        │
        ▼
Formatting Checker
        │
        ▼
Grammar Checker
        │
        ▼
ATS Score Calculation
        │
        ▼
ATS Report
```

---

# ATS Evaluation Criteria

| Criteria | Purpose |
|-----------|----------|
| Resume Sections | Verify required sections exist |
| Technical Keywords | Match important technical skills |
| Formatting | Detect formatting issues |
| Grammar | Identify basic grammar problems |
| Overall Score | Generate ATS score |

---

# ATS Output Example

```json
{
  "ats_score": 85,
  "section": {
    "education": true,
    "skills": true,
    "experience": true,
    "projects": true
  },
  "keywords": {
    "count": 4
  },
  "formatting": {
    "empty": false,
    "too_short": false
  },
  "grammar": {
    "grammar_score": 90
  }
}
```

---

# 💼 Job Recommendation Engine

The Job Recommendation Engine predicts suitable job roles based on the candidate's skills and recommends areas for improvement.

---

## Components

| Component | Description | Status |
|-----------|-------------|--------|
| Role Predictor | Predicts suitable job roles | ✅ Completed |
| Job Matcher | Matches candidate to predefined roles | ✅ Completed |
| Skill Gap Analyzer | Identifies missing skills | ✅ Completed |
| Recommendation Engine | Generates career recommendations | ✅ Completed |

---

# Job Recommendation Workflow

```text
Resume Skills
      │
      ▼
Role Predictor
      │
      ▼
Job Matcher
      │
      ▼
Skill Gap Analyzer
      │
      ▼
Recommendation Engine
      │
      ▼
Career Recommendations
```

---

# Supported Job Roles

- Backend Developer
- Python Developer
- AI/ML Engineer
- Data Analyst
- Software Developer

---

# Job Recommendation Example

```json
{
  "predicted_role": "Backend Developer",
  "matched_jobs": [
    "Backend Developer"
  ],
  "skill_gap": [
    "Docker",
    "Git"
  ],
  "recommendations": [
    "Build REST APIs using FastAPI.",
    "Learn Docker and containerization.",
    "Practice SQL optimization."
  ]
}
```

---

# Current Status

| Module | Status |
|---------|--------|
| ATS Engine | ✅ Completed |
| Job Recommendation Engine | ✅ Completed |
| Unit Tests | ✅ Passed |
| Integration | ✅ Completed |

---

# 💡 Explainability Engine

The Explainability Engine makes AI decisions transparent by providing clear, human-readable explanations for ATS scores, recommended job roles, and identified skill gaps.

Instead of only returning predictions, the system explains **why** a recommendation was generated.

---

## Components

| Component | Description | Status |
|-----------|-------------|--------|
| ATS Explanation | Explains ATS score | ✅ Completed |
| Job Reason | Explains recommended job roles | ✅ Completed |
| Skill Reason | Explains matched and missing skills | ✅ Completed |

---

# Explainability Workflow

```text
ATS Result
      │
      ▼
ATS Explanation
      │
      ▼
Job Recommendation
      │
      ▼
Job Reason
      │
      ▼
Skill Gap
      │
      ▼
Skill Reason
      │
      ▼
Final Explanation
```

---

# Explainability Output Example

```json
{
  "ats_score": 85,
  "explanation": [
    "Your resume has a strong ATS score.",
    "Education section is present.",
    "Skills section is present.",
    "Experience section is present.",
    "Projects section is present.",
    "Matched 4 technical skills."
  ]
}
```

---

# 🛠️ Resume Improvement Engine

The Resume Improvement Engine analyzes resume quality and provides practical suggestions to strengthen the resume.

This module is currently under active development.

---

## Planned Components

| Component | Description | Status |
|-----------|-------------|--------|
| Strength Analyzer | Identifies resume strengths | 🚧 In Progress |
| Weakness Analyzer | Detects missing areas | 🚧 In Progress |
| Suggestion Generator | Generates improvement suggestions | 🚧 In Progress |
| Improvement Engine | Combines all analyses | 🚧 In Progress |

---

# Planned Workflow

```text
Resume Analysis
       │
       ▼
Strength Analyzer
       │
       ▼
Weakness Analyzer
       │
       ▼
Suggestion Generator
       │
       ▼
Improvement Engine
       │
       ▼
Resume Improvement Report
```

---

# Planned Output

```json
{
  "strengths": [
    "Strong Python skills."
  ],
  "weaknesses": [
    "Docker skill is missing."
  ],
  "suggestions": [
    "Learn Docker for backend deployment.",
    "Add Git and GitHub experience."
  ]
}
```

---

# 📊 Analytics Module

The Analytics Module will enable users to monitor resume improvements across multiple analyses.

---

## Planned Features

- ATS Score History
- Resume Comparison
- Improvement Tracking
- Resume Progress Analytics
- Performance Dashboard

---

# 🎤 Interview Module

The Interview Module will assist users in preparing for technical and HR interviews.

---

## Planned Features

- Technical Interview Questions
- HR Interview Questions
- Coding Questions
- Answer Evaluation
- Feedback Generation
- Interview Performance Analysis

---

# 🎓 Training Module

The Training Module will recommend learning resources based on identified skill gaps.

---

## Planned Features

- Personalized Learning Roadmap
- Recommended Courses
- Skill Progress Tracking
- Learning Recommendations
- Career Growth Suggestions

---

# 🤖 AI Copilot

AI Copilot is the long-term vision of the project.

It will function as an AI career assistant capable of helping users throughout the placement journey.

---

## Planned Features

- Resume Chat Assistant
- Resume Review
- Resume Rewrite
- Job Description Analysis
- Resume vs Job Matching
- Career Guidance
- Interview Coaching
- AI Career Mentor
- LLM Integration
- RAG Pipeline

---

# 🧪 Testing

AI Resume Copilot follows a test-driven development approach. Every completed module includes unit tests to verify correctness and reduce regressions during development.

---

## Testing Framework

| Tool | Purpose |
|------|---------|
| Pytest | Unit Testing |
| HTTPX | API Testing |
| FastAPI TestClient | Endpoint Testing |

---

# Current Test Coverage

| Module | Status |
|---------|--------|
| Parser | ✅ Tested |
| ATS | ✅ Tested |
| Jobs | ✅ Tested |
| Explainability | ✅ Tested |
| Improvement | 🚧 In Progress |
| Analytics | ⏳ Planned |
| Interview | ⏳ Planned |

---

# Test Commands

## Run All Tests

```bash
python -m pytest tests -v
```

---

## Parser Tests

```bash
python -m pytest tests/ai_engine/parser -v
```

---

## ATS Tests

```bash
python -m pytest tests/ai_engine/ats -v
```

---

## Jobs Tests

```bash
python -m pytest tests/ai_engine/jobs -v
```

---

## Explainability Tests

```bash
python -m pytest tests/ai_engine/explainability -v
```

---

# Current Test Result

```text
=================================

Parser Tests          Passed

ATS Tests             Passed

Jobs Tests            Passed

Explainability Tests  Passed

---------------------------------

Total Passing Tests : 71

Failed Tests : 0

=================================
```

---

# 📌 API Overview

The backend exposes REST APIs using FastAPI.

| Endpoint | Description | Status |
|----------|-------------|--------|
| Resume Upload | Upload Resume | 🚧 |
| Resume Parser | Parse Resume | 🚧 |
| ATS Analysis | Analyze ATS Score | 🚧 |
| Job Recommendation | Recommend Jobs | 🚧 |
| Resume Improvement | Improve Resume | 🚧 |
| Interview | Interview Preparation | ⏳ |

---

# Sample Response

```json
{
  "contact": {},
  "skills": [],
  "education": {},
  "experience": {},
  "ats": {},
  "recommendation": {},
  "analytics": {},
  "explainability": {},
  "metadata": {}
}
```

---

# 📅 Version History

| Version | Description |
|----------|-------------|
| v0.1.0 | Initial Project Structure |
| v0.2.0 | Resume Parser Module |
| v0.3.0 | ATS Engine |
| v0.4.0 | Jobs & Explainability Modules |
| v0.5.0 | Resume Improvement *(Upcoming)* |

---

# 🛣️ Roadmap

## Phase 1 ✅

- Resume Parser
- ATS Engine
- Job Recommendation
- Explainability

---

## Phase 2 🚧

- Resume Improvement
- Resume Analytics
- Interview Module

---

## Phase 3 ⏳

- AI Copilot
- Authentication
- Database
- React Frontend
- Docker
- Cloud Deployment

---

# 📈 Repository Status

| Category | Status |
|----------|--------|
| Development | 🟢 Active |
| Current Version | v0.4.0 |
| Build Status | Passing |
| Latest Milestone | 71 Unit Tests Passed |
| License | MIT |

---

# 🚀 Future Enhancements

The following features are planned for future releases of AI Resume Copilot.

---

## AI Features

- AI Resume Chat Assistant
- Resume Rewrite Assistant
- Resume Optimization
- Resume Summary Generator
- Resume vs Job Description Matching
- AI Career Mentor
- Personalized Career Roadmap
- Skill Recommendation System
- Resume Quality Prediction
- AI Resume Builder

---

## Machine Learning

- Resume Classification
- Job Role Classification
- Resume Ranking
- Skill Recommendation Model
- ATS Score Prediction Model
- Learning Recommendation Model

---

## Backend

- JWT Authentication
- OAuth Login
- User Management
- Resume History
- Resume Versioning
- Background Tasks
- Email Notifications
- Logging
- Caching
- Database Optimization

---

## Frontend

- React Dashboard
- Resume Upload Portal
- User Profile
- Resume Analytics Dashboard
- Interview Dashboard
- Dark Mode
- Responsive Design

---

## Deployment

- Docker
- Docker Compose
- Kubernetes
- AWS
- Nginx
- GitHub Actions
- CI/CD Pipeline
- Monitoring
- Production Logging

---

# 🤝 Contributing

Contributions are welcome.

If you would like to contribute to this project:

1. Fork the repository.
2. Create a new branch.
3. Implement your changes.
4. Run all tests.
5. Commit your changes.
6. Push the branch.
7. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

See the LICENSE file for more details.

---

# 👨‍💻 Author

**Divesh Kate**

Artificial Intelligence & Machine Learning Undergraduate

Mumbai, India

### GitHub

https://github.com/diveshkate11-collab

### Repository

https://github.com/diveshkate11-collab/ai-resume-analyzer

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🐞 Report bugs
- 💡 Suggest improvements

---

# 📌 Current Development Status

```text
Project Name

AI Resume Copilot

Version

v0.4.0

Status

Active Development

Completed Modules

✔ Resume Parser

✔ ATS Engine

✔ Job Recommendation

✔ Explainability

Current Module

▶ Improvement Engine

Next Milestone

▶ Analytics Module

Backend

FastAPI

Programming Language

Python

Testing

71 Unit Tests Passing

License

MIT
```

---

# 📅 Changelog

## v0.4.0

### Added

- Resume Parser Integration
- ATS Engine
- Job Recommendation Engine
- Explainability Engine
- Recommendation Engine
- Role Predictor
- Skill Gap Analyzer

### Improved

- Resume Parsing Accuracy
- Project Architecture
- Unit Testing
- Documentation

### Fixed

- Resume Parser Integration
- DOCX Parser
- Import Errors
- Parser Method Naming
- Resume Parser Tests
- Job Recommendation Integration

---

# 🙌 Final Note

AI Resume Copilot is an actively developed software engineering project focused on building a production-ready AI-powered career assistance platform.

The project is continuously evolving with new AI modules, backend features, and deployment capabilities to provide an end-to-end resume analysis and career guidance solution.

---