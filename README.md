# 🚀 AI Resume Copilot

<div align="center">

### AI-Powered Resume Analysis, ATS Optimization & Career Preparation Platform

Analyze resumes, evaluate ATS compatibility, recommend career paths, identify skill gaps, generate interview preparation resources, and monitor resume improvement through a modular AI-powered backend built with FastAPI.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?logo=fastapi)
![Tests](https://img.shields.io/badge/Tests-110_Passed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active_Development-orange)

</div>

---

# 📖 Table of Contents

- About
- Objectives
- Features
- Technology Stack
- System Architecture
- Project Structure
- Installation
- Configuration
- Running the Project
- AI Engine
  - Resume Parser
  - ATS Engine
  - Job Recommendation Engine
  - Explainability Engine
  - Resume Improvement Engine
  - Analytics Engine
  - Interview Engine
  - Training Engine
  - AI Copilot
- Testing
- API Overview
- Development Roadmap
- Version History
- Future Enhancements
- Contributing
- License
- Author
- Changelog

---

# 📚 About

AI Resume Copilot is a modular backend platform that helps candidates improve their resumes and prepare for technical hiring processes.

The application accepts resumes in **PDF** and **DOCX** formats, extracts structured information, evaluates ATS compatibility, recommends suitable job roles, identifies skill gaps, explains analysis results, suggests resume improvements, tracks progress across multiple analyses, and assists with interview preparation.

The project is designed around a modular architecture where each AI component has a clear responsibility, making the system easier to maintain, test, and extend.

Current development emphasizes:

- Modular Software Architecture
- FastAPI REST APIs
- Reusable AI Components
- Test-Driven Development
- Scalable Project Structure
- Production-Oriented Design

---

# 🎯 Project Objectives

AI Resume Copilot is being developed to achieve the following goals:

- Build a complete AI-powered resume analysis platform.
- Design independent and reusable AI modules.
- Practice production-style FastAPI backend development.
- Apply clean architecture and software engineering principles.
- Develop comprehensive automated test coverage.
- Build deployment-ready REST APIs.
- Create a portfolio-quality backend project.
- Expand the platform into a complete AI career assistant.

---

# ✨ Current Features

## 📄 Resume Analysis

- PDF Resume Parsing
- DOCX Resume Parsing
- Resume Text Cleaning
- Contact Information Extraction
- Skills Extraction
- Education Extraction
- Experience Extraction
- Structured Resume Generation

---

## 📊 ATS Evaluation

- ATS Score Calculation
- Resume Section Validation
- Technical Keyword Analysis
- Resume Formatting Checks
- Grammar Evaluation

---

## 💼 Career Recommendations

- Role Prediction
- Job Matching
- Skill Gap Identification
- Career Recommendations

---

## 💡 Resume Intelligence

- AI Explainability
- Strength Analysis
- Weakness Analysis
- Resume Improvement Suggestions

---

## 📈 Resume Analytics

- ATS Score History
- Resume Comparison
- Improvement Tracking
- Analytics Reports

---

## 🎤 Interview Preparation

- Technical Interview Questions
- HR Interview Questions
- Answer Evaluation
- Interview Feedback
- Personalized Learning Roadmap

---

# 📊 Current Project Status

| Module | Status |
|---------|--------|
| Resume Parser | ✅ Completed |
| ATS Engine | ✅ Completed |
| Job Recommendation Engine | ✅ Completed |
| Explainability Engine | ✅ Completed |
| Resume Improvement Engine | ✅ Completed |
| Analytics Engine | ✅ Completed |
| Interview Engine | ✅ Completed |
| Training Engine | 🚧 In Development |
| AI Copilot | ⏳ Planned |

---

# 🏆 Latest Milestone

### Current Version

```text
v0.7.0
```

### Test Status

```text
110 Passing Tests
```

### Current Development Focus

```text
Training Engine
```

---

# ⭐ Project Highlights

- Modular AI Engine
- FastAPI Backend
- RESTful API Design
- Automated Testing
- Resume Parsing Pipeline
- ATS Evaluation
- Career Recommendation Engine
- Resume Improvement System
- Resume Analytics
- Interview Preparation
- Service-Oriented Architecture
- GitHub Portfolio Ready

---

# 🛠️ Technology Stack

AI Resume Copilot is built with a modern Python backend that emphasizes modularity, maintainability, automated testing, and scalable software architecture.

---

## 💻 Core Technologies

| Technology | Purpose |
|------------|---------|
| Python 3.14 | Core programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI application server |
| Pydantic | Request and response validation |

---

## 📄 Resume Processing

| Technology | Purpose |
|------------|---------|
| PyPDF2 | PDF text extraction |
| python-docx | DOCX text extraction |
| Regular Expressions (Regex) | Information extraction |

---

## 🧪 Testing

| Technology | Purpose |
|------------|---------|
| Pytest | Unit testing |
| FastAPI TestClient | API testing |
| HTTPX | HTTP endpoint testing |

---

## 🛠️ Development Tools

| Tool | Purpose |
|------|---------|
| Visual Studio Code | Code editor |
| Git | Version control |
| GitHub | Repository hosting |

---

## 🚀 Planned Technologies

| Technology | Purpose |
|------------|---------|
| PostgreSQL | Persistent storage |
| SQLAlchemy | ORM |
| Docker | Containerization |
| AWS | Cloud deployment |
| React | Frontend dashboard |
| LangChain | LLM workflow |
| LangGraph | AI agent workflow |
| Vector Database | Semantic search |
| Ollama | Local LLM support |
| OpenAI API | AI-powered features |
| RAG | Context-aware responses |

---

# 🏛️ System Architecture

AI Resume Copilot follows a layered architecture that separates request handling, business logic, AI processing, and future infrastructure components.

```text
                Client
                   │
                   ▼
            FastAPI REST API
                   │
                   ▼
        Request / Response Validation
               (Pydantic Models)
                   │
                   ▼
             Service Layer
                   │
                   ▼
              AI Engine Core
                   │
 ┌──────────┬──────────┬──────────┬──────────┐
 ▼          ▼          ▼          ▼
Parser      ATS       Jobs    Improvement
 │           │          │           │
 ▼           ▼          ▼           ▼
Analytics Explainability Interview Training
                   │
                   ▼
          Structured JSON Response
```

---

## 🧩 AI Engine Workflow

```text
Resume Upload
      │
      ▼
Resume Parser
      │
      ▼
Structured Resume Data
      │
      ├────────► ATS Engine
      │
      ├────────► Job Recommendation
      │
      ├────────► Resume Improvement
      │
      ├────────► Analytics Engine
      │
      ├────────► Explainability Engine
      │
      ├────────► Interview Engine
      │
      ├────────► Training Engine
      │
      └────────► AI Copilot (Future)
```

---

## 🧱 Architectural Principles

The project is designed around the following software engineering principles:

- Modular architecture
- Separation of concerns
- Reusable AI components
- Service-oriented design
- Test-driven development
- Scalable project organization
- Maintainable codebase

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
│   ├── integration/
│   └── services/
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

## 📁 Directory Overview

| Directory | Responsibility |
|-----------|----------------|
| app | Main application |
| ai_engine | Independent AI modules |
| api | REST API endpoints |
| services | Business logic layer |
| schemas | Pydantic models |
| tests | Automated tests |
| uploads | Uploaded resumes |
| storage | Future persistent storage |
| deployment | Deployment resources |
| frontend | Planned React application |

---

## 📌 Current Development Stage

```text
Completed Modules
─────────────────
✔ Resume Parser
✔ ATS Engine
✔ Job Recommendation
✔ Explainability
✔ Resume Improvement
✔ Analytics
✔ Interview

Currently Developing
────────────────────
▶ Training Engine

Planned
───────
• AI Copilot
• Database Integration
• Authentication
• Frontend
• Cloud Deployment
```

---

# 🚀 Installation

Follow the steps below to set up **AI Resume Copilot** on your local machine.

---

## 📋 Prerequisites

Ensure the following software is installed.

| Software | Version |
|----------|----------|
| Python | 3.12 or later |
| Git | Latest |
| Visual Studio Code | Recommended |

Verify the installation:

```bash
python --version
git --version
```

---

## 📥 Clone the Repository

Clone the repository.

```bash
git clone https://github.com/diveshkate11-collab/ai-resume-analyzer.git
```

Move into the project directory.

```bash
cd ai-resume-analyzer
```

---

## 🐍 Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

---

## 📦 Install Dependencies

Install all required packages.

```bash
python -m pip install -r requirements.txt
```

---

## ✅ Verify Installation

Confirm that Python and the project dependencies are available.

```bash
python --version
```

```bash
python -m pip list
```

---

# ⚙️ Configuration

The current version works without additional configuration.

Future releases will introduce configurable services through environment variables.

Planned configuration options include:

- Database Connection
- Authentication
- Logging
- AI Model Settings
- Email Notifications
- Cloud Storage

---

## 🔑 Environment Variables

Future releases will include a `.env.example` file.

Example configuration:

```env
DATABASE_URL=

SECRET_KEY=

JWT_SECRET_KEY=

OPENAI_API_KEY=

SMTP_USERNAME=

SMTP_PASSWORD=
```

---

# ▶️ Running the Project

Start the FastAPI development server.

```bash
uvicorn app.main:app --reload
```

A successful startup should display output similar to:

```text
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## 🌐 Local Access

| Service | URL |
|---------|-----|
| Application | http://127.0.0.1:8000 |
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

---

# 📂 Project Configuration Files

| File | Purpose |
|------|---------|
| `requirements.txt` | Project dependencies |
| `pyproject.toml` | Build and project configuration |
| `.gitignore` | Ignored files and folders |
| `README.md` | Project documentation |
| `LICENSE` | License information |

---

# 🔄 Development Workflow

Every completed feature follows the same development lifecycle.

```text
Planning
    │
    ▼
Implementation
    │
    ▼
Unit Testing
    │
    ▼
Service Integration
    │
    ▼
API Integration
    │
    ▼
Documentation
    │
    ▼
Git Commit
    │
    ▼
GitHub Push
```

---

# 📸 Screenshots

User interface screenshots will be added after frontend development begins.

| Screen | Status |
|---------|--------|
| Dashboard | ⏳ Planned |
| Resume Upload | ⏳ Planned |
| Resume Analysis | ⏳ Planned |
| ATS Report | ⏳ Planned |
| Analytics Dashboard | ⏳ Planned |
| Interview Dashboard | ⏳ Planned |

---

# 🎥 Live Demo

A live demonstration will be published after the first deployment.

**Status:** ⏳ Planned

---

# 🌐 API Documentation

FastAPI automatically generates interactive API documentation.

| Documentation | URL |
|---------------|-----|
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |

---

# 📄 Resume Parser

The **Resume Parser** is the first stage of the AI Resume Copilot pipeline. It processes uploaded resumes, extracts structured information, and prepares standardized data for the remaining AI modules.

Currently, the parser supports both **PDF** and **DOCX** documents.

---

## 🎯 Responsibilities

The Resume Parser performs the following tasks:

- Validate uploaded resume files
- Extract text from PDF documents
- Extract text from DOCX documents
- Clean extracted text
- Parse contact details
- Extract technical skills
- Identify educational qualifications
- Extract work experience
- Generate structured resume data

---

## 📂 Supported Formats

| Format | Status |
|---------|--------|
| PDF | ✅ Supported |
| DOCX | ✅ Supported |

---

## 🧩 Components

| Component | Responsibility | Status |
|-----------|----------------|--------|
| PDF Parser | Extract text from PDF resumes | ✅ |
| DOCX Parser | Extract text from DOCX resumes | ✅ |
| Text Cleaner | Normalize extracted text | ✅ |
| Contact Parser | Parse contact information | ✅ |
| Skills Parser | Identify technical skills | ✅ |
| Education Parser | Extract education details | ✅ |
| Experience Parser | Extract work experience | ✅ |
| Resume Parser | Coordinate the complete parsing process | ✅ |

---

# 🔄 Processing Pipeline

```text
Resume Upload
      │
      ▼
File Validation
      │
      ▼
PDF Parser / DOCX Parser
      │
      ▼
Raw Resume Text
      │
      ▼
Text Cleaner
      │
      ▼
Contact Parser
      │
      ▼
Skills Parser
      │
      ▼
Education Parser
      │
      ▼
Experience Parser
      │
      ▼
Structured Resume Data
```

---

# 📋 Extracted Information

The parser produces a standardized structure used by every downstream module.

```text
Resume
│
├── Contact
│
├── Skills
│
├── Education
│
├── Experience
│
├── ATS
│
├── Recommendation
│
├── Improvement
│
├── Analytics
│
├── Explainability
│
├── Text
│
└── Metadata
```

---

# 📤 Sample Response

```json
{
  "contact": {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+91 9876543210"
  },
  "skills": [
    "Python",
    "FastAPI",
    "SQL"
  ],
  "education": {
    "degree": "Bachelor of Technology"
  },
  "experience": {
    "experience": "Fresher"
  },
  "ats": {},
  "recommendation": {},
  "improvement": {},
  "analytics": {},
  "explainability": {},
  "text": "...",
  "metadata": {
    "characters": 1824
  }
}
```

---

# 🧪 Testing

The Resume Parser is validated through automated unit tests covering:

- PDF parsing
- DOCX parsing
- Text cleaning
- Contact extraction
- Skill extraction
- Education extraction
- Experience extraction
- End-to-end parser execution

Run parser tests:

```bash
python -m pytest tests/ai_engine/parser -v
```

---

## 📊 Module Summary

| Metric | Value |
|---------|-------|
| Supported Formats | 2 |
| Parser Components | 8 |
| Unit Tested | ✅ |
| API Integrated | ✅ |
| Status | Completed |

---

# 🔗 Position in the AI Pipeline

```text
Resume Upload
      │
      ▼
Resume Parser
      │
      ▼
Structured Resume Data
      │
      ├────────► ATS Engine
      ├────────► Job Recommendation
      ├────────► Resume Improvement
      ├────────► Analytics Engine
      ├────────► Explainability Engine
      ├────────► Interview Engine
      └────────► Training Engine
```

---

# 📊 ATS Engine

The **Applicant Tracking System (ATS) Engine** evaluates resume quality by analyzing structure, technical keywords, formatting, and basic grammar. It generates an ATS report that highlights strengths and identifies areas requiring improvement before job applications.

The engine operates on structured resume data generated by the Resume Parser.

---

## 🎯 Responsibilities

The ATS Engine performs the following tasks:

- Calculate the ATS score
- Validate essential resume sections
- Match technical keywords
- Analyze resume formatting
- Perform basic grammar evaluation
- Generate a structured ATS report

---

## 🧩 Components

| Component | Responsibility | Status |
|-----------|----------------|--------|
| ATS Scorer | Calculates the final ATS score | ✅ |
| Section Checker | Verifies required resume sections | ✅ |
| Keyword Matcher | Detects technical keywords | ✅ |
| Formatting Checker | Evaluates resume formatting | ✅ |
| Grammar Checker | Performs grammar validation | ✅ |

---

# ⚙️ Evaluation Pipeline

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
ATS Scorer
        │
        ▼
ATS Report
```

---

# 📊 Scoring Criteria

| Category | Maximum Score |
|----------|--------------:|
| Resume Sections | 40 |
| Technical Keywords | 30 |
| Formatting | 20 |
| Grammar | 10 |
| **Total** | **100** |

---

## 📑 Resume Sections

The engine checks for the presence of key resume sections.

- Contact Information
- Education
- Skills
- Experience
- Projects

Missing sections reduce the overall ATS score.

---

## 💻 Technical Keyword Analysis

The Keyword Matcher searches for commonly expected technical skills.

Example keywords include:

- Python
- FastAPI
- SQL
- Git
- Docker
- Machine Learning
- Deep Learning
- TensorFlow
- PyTorch
- NumPy
- Pandas

The keyword list can be expanded as new technologies are added.

---

## 📄 Formatting Evaluation

The Formatting Checker performs lightweight structural validation.

Current checks include:

- Empty resume detection
- Very short resume detection
- Basic formatting quality

---

## ✍️ Grammar Evaluation

The Grammar Checker performs simple grammar analysis that contributes to the overall ATS score.

Future versions may integrate NLP-based grammar checking for more detailed evaluation.

---

# 📤 Sample Response

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
    "count": 5
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

# 🧪 Testing

The ATS Engine is validated through automated tests covering:

- ATS score calculation
- Section validation
- Keyword matching
- Formatting checks
- Grammar evaluation

Run ATS tests:

```bash
python -m pytest tests/ai_engine/ats -v
```

---

## 📈 Module Summary

| Metric | Value |
|---------|-------|
| Components | 5 |
| Maximum Score | 100 |
| Resume Sections Checked | 5 |
| Unit Tested | ✅ |
| API Integrated | ✅ |
| Status | Completed |

---

# 🔗 Position in the AI Pipeline

```text
Resume Upload
      │
      ▼
Resume Parser
      │
      ▼
Structured Resume
      │
      ▼
ATS Engine
      │
      ▼
ATS Analysis
      │
      ├────────► Job Recommendation
      ├────────► Resume Improvement
      ├────────► Analytics Engine
      ├────────► Explainability Engine
      ├────────► Interview Engine
      └────────► Training Engine
```

---

# 💼 Job Recommendation Engine

The **Job Recommendation Engine** predicts suitable career roles by analyzing the candidate's skills and experience. It also identifies missing competencies and generates practical recommendations to improve job readiness.

The engine uses structured resume data produced by the Resume Parser and complements the ATS analysis.

---

## 🎯 Responsibilities

The Job Recommendation Engine performs the following tasks:

- Predict suitable job roles
- Match resume skills with predefined roles
- Identify missing technical skills
- Generate career recommendations

---

## 🧩 Components

| Component | Responsibility | Status |
|-----------|----------------|--------|
| Role Predictor | Predicts the most suitable job role | ✅ |
| Job Matcher | Matches candidates with predefined roles | ✅ |
| Skill Gap Analyzer | Identifies missing technical skills | ✅ |
| Recommendation Engine | Generates career recommendations | ✅ |

---

# ⚙️ Recommendation Workflow

```text
Structured Resume
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
Career Recommendation
```

---

# 💼 Supported Roles

The current version provides recommendations for:

- Python Developer
- Backend Developer
- AI Engineer
- Data Scientist
- Java Developer

Additional roles will be introduced in future releases.

---

# 📤 Sample Response

```json
{
  "recommended_role": "Backend Developer",
  "recommendations": [
    "Learn Docker.",
    "Improve SQL skills.",
    "Build REST API projects."
  ]
}
```

---

# 🧪 Testing

The Job Recommendation Engine is verified through automated tests covering:

- Role prediction
- Job matching
- Skill gap analysis
- Recommendation generation

Run tests:

```bash
python -m pytest tests/ai_engine/jobs -v
```

---

## 📈 Module Summary

| Metric | Value |
|---------|-------|
| Components | 4 |
| Supported Roles | 5 |
| Unit Tested | ✅ |
| API Integrated | ✅ |
| Status | Completed |

---

# 🔗 Position in the AI Pipeline

```text
Resume Parser
      │
      ▼
ATS Engine
      │
      ▼
Job Recommendation Engine
      │
      ▼
Career Recommendation
```

---

# 💡 Explainability Engine

The **Explainability Engine** improves transparency by providing human-readable explanations for AI-generated outputs. Instead of returning only scores or predictions, it explains why those results were produced.

---

## 🎯 Responsibilities

The Explainability Engine provides explanations for:

- ATS evaluation
- Recommended job role
- Skill gap analysis

---

## 🧩 Components

| Component | Responsibility | Status |
|-----------|----------------|--------|
| ATS Explanation | Explains ATS score | ✅ |
| Job Explanation | Explains role prediction | ✅ |
| Skill Explanation | Explains detected skill gaps | ✅ |

---

# ⚙️ Explainability Workflow

```text
ATS Analysis
      │
      ▼
Job Recommendation
      │
      ▼
Skill Gap Analysis
      │
      ▼
Explainability Engine
      │
      ▼
Explanation Report
```

---

# 📤 Sample Response

```json
{
  "ats_explanation": "Education, skills, and experience sections were detected.",
  "job_explanation": "Backend Developer recommended because of Python and FastAPI skills.",
  "skill_gap_explanation": "Docker and SQL were identified as missing skills."
}
```

---

# 🧪 Testing

The Explainability Engine is covered by automated unit tests validating:

- ATS explanation
- Job explanation
- Skill explanation

Run tests:

```bash
python -m pytest tests/ai_engine/explainability -v
```

---

## 📈 Module Summary

| Metric | Value |
|---------|-------|
| Components | 3 |
| Explanation Types | 3 |
| Unit Tested | ✅ |
| API Integrated | ✅ |
| Status | Completed |

---

# 🔗 Position in the AI Pipeline

```text
Resume Parser
      │
      ▼
ATS Engine
      │
      ▼
Job Recommendation Engine
      │
      ▼
Explainability Engine
      │
      ▼
Structured Resume Analysis
```

---

# 🛠️ Resume Improvement Engine

The **Resume Improvement Engine** analyzes resume quality and generates practical suggestions to help candidates strengthen their resumes before applying for jobs.

Unlike the ATS Engine, which measures compatibility, this module focuses on identifying weaknesses and recommending improvements.

---

## 🎯 Responsibilities

The Resume Improvement Engine performs the following tasks:

- Identify resume strengths
- Detect missing information
- Highlight improvement areas
- Generate personalized suggestions

---

## 🧩 Components

| Component | Responsibility | Status |
|-----------|----------------|--------|
| Strength Analyzer | Identifies positive aspects of the resume | ✅ |
| Weakness Analyzer | Detects missing sections and skills | ✅ |
| Suggestion Generator | Creates improvement suggestions | ✅ |
| Improvement Engine | Combines all improvement components | ✅ |

---

# ⚙️ Improvement Workflow

```text
Structured Resume
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
Improvement Report
```

---

# 📤 Sample Response

```json
{
  "strengths": [
    "Strong Python skills",
    "Education section detected"
  ],
  "weaknesses": [
    "Docker skill missing",
    "Projects section missing"
  ],
  "suggestions": [
    "Learn Docker",
    "Add personal projects",
    "Include GitHub profile"
  ]
}
```

---

# 🧪 Testing

The Resume Improvement Engine is verified through automated tests covering:

- Strength analysis
- Weakness analysis
- Suggestion generation
- Engine integration

Run tests:

```bash
python -m pytest tests/ai_engine/improvement -v
```

---

## 📈 Module Summary

| Metric | Value |
|---------|-------|
| Components | 4 |
| Unit Tested | ✅ |
| API Integrated | ✅ |
| Status | Completed |

---

# 🔗 Position in the AI Pipeline

```text
Resume Parser
      │
      ▼
ATS Engine
      │
      ▼
Resume Improvement Engine
      │
      ▼
Improvement Report
```

---

# 📊 Analytics Engine

The **Analytics Engine** tracks resume progress across multiple analyses. Instead of evaluating only the latest resume, it helps users monitor improvements, compare versions, and review historical ATS performance.

---

## 🎯 Responsibilities

The Analytics Engine performs the following tasks:

- Store ATS score history
- Compare resume versions
- Track resume improvements
- Generate analytics summaries

---

## 🧩 Components

| Component | Responsibility | Status |
|-----------|----------------|--------|
| ATS History | Stores ATS score history | ✅ |
| Resume Compare | Compares resume versions | ✅ |
| Improvement Tracker | Tracks score progression | ✅ |
| Analytics Engine | Generates analytics reports | ✅ |

---

# ⚙️ Analytics Workflow

```text
Resume Analysis
        │
        ▼
ATS History
        │
        ▼
Resume Comparison
        │
        ▼
Improvement Tracker
        │
        ▼
Analytics Engine
        │
        ▼
Analytics Report
```

---

# 📤 Sample Response

```json
{
  "history": [
    72,
    81,
    88
  ],
  "comparison": {
    "previous_score": 81,
    "current_score": 88,
    "difference": 7
  },
  "progress": "Improving"
}
```

---

## 📊 Report Contents

The Analytics Engine provides:

- ATS score history
- Resume comparison
- Improvement trend
- Score difference between analyses

---

# 🧪 Testing

The Analytics Engine is covered by automated tests validating:

- ATS history
- Resume comparison
- Improvement tracking
- Analytics report generation
- Analytics service integration

Run tests:

```bash
python -m pytest tests/ai_engine/analytics -v
```

Service tests:

```bash
python -m pytest tests/services/test_analytics_service.py -v
```

---

## 📈 Module Summary

| Metric | Value |
|---------|-------|
| Components | 4 |
| Service Layer | ✅ |
| Unit Tested | ✅ |
| API Integrated | ✅ |
| Status | Completed |

---

# 🔗 Position in the AI Pipeline

```text
Resume Parser
      │
      ▼
ATS Engine
      │
      ▼
Resume Improvement Engine
      │
      ▼
Analytics Engine
      │
      ▼
Analytics Report
```

---

# 🎤 Interview Engine

The **Interview Engine** helps candidates prepare for technical interviews by generating role-specific interview questions, evaluating responses using rule-based analysis, providing feedback, and recommending learning activities based on interview performance.

It extends resume analysis by supporting interview preparation after a suitable role has been identified.

---

## 🎯 Responsibilities

The Interview Engine performs the following tasks:

- Generate technical interview questions
- Provide common HR interview questions
- Evaluate candidate answers
- Generate interview feedback
- Recommend a personalized learning roadmap

---

## 🧩 Components

| Component | Responsibility | Status |
|-----------|----------------|--------|
| Technical Questions | Role-specific technical questions | ✅ |
| HR Questions | Common HR interview questions | ✅ |
| Question Generator | Combines interview questions | ✅ |
| Answer Evaluator | Evaluates candidate responses | ✅ |
| Feedback | Generates interview feedback | ✅ |
| Interview Analyzer | Coordinates interview analysis | ✅ |
| Interview Roadmap | Generates learning roadmap | ✅ |

---

# ⚙️ Interview Workflow

```text
Predicted Job Role
        │
        ▼
Question Generator
        │
        ▼
Technical + HR Questions
        │
        ▼
Candidate Answer
        │
        ▼
Answer Evaluator
        │
        ▼
Feedback Generator
        │
        ▼
Interview Roadmap
```

---

# 📤 Sample Response

```json
{
  "role": "Python Developer",
  "technical_questions": [
    "What is Python?",
    "Explain decorators."
  ],
  "hr_questions": [
    "Tell me about yourself."
  ],
  "evaluation": {
    "score": 100,
    "result": "Good Answer"
  },
  "feedback": "Excellent answer. Keep up the good work.",
  "roadmap": [
    "Practice advanced interview questions.",
    "Solve coding challenges regularly.",
    "Participate in mock interviews."
  ]
}
```

---

# 🧪 Testing

The Interview Engine is validated through automated tests covering:

- Question generation
- Answer evaluation
- Feedback generation
- Interview analysis
- Learning roadmap
- Interview service

Run AI Engine tests:

```bash
python -m pytest tests/ai_engine/interview -v
```

Run service tests:

```bash
python -m pytest tests/services/test_interview_service.py -v
```

---

## 📈 Module Summary

| Metric | Value |
|---------|-------|
| Components | 7 |
| Service Layer | ✅ |
| Unit Tested | ✅ |
| API Ready | ✅ |
| Status | Completed |

---

# 🔗 Position in the AI Pipeline

```text
Resume Parser
      │
      ▼
ATS Engine
      │
      ▼
Job Recommendation
      │
      ▼
Interview Engine
      │
      ▼
Interview Report
```

---

# 🎓 Training Engine

The **Training Engine** will recommend learning resources based on missing skills, interview performance, and career objectives. Its purpose is to help candidates close identified skill gaps through structured learning plans.

---

## 🎯 Planned Responsibilities

- Recommend personalized learning paths
- Suggest courses and study resources
- Prioritize missing technical skills
- Generate skill development plans
- Track learning progress

---

## 🧩 Planned Components

| Component | Responsibility | Status |
|-----------|----------------|--------|
| Skill Analyzer | Analyze missing skills | ⏳ |
| Course Recommender | Recommend learning resources | ⏳ |
| Learning Planner | Generate learning roadmap | ⏳ |
| Progress Tracker | Track completed learning | ⏳ |
| Training Engine | Coordinate training recommendations | ⏳ |

---

# ⚙️ Planned Workflow

```text
Resume Analysis
        │
        ▼
Skill Gap Analysis
        │
        ▼
Training Engine
        │
        ▼
Learning Roadmap
        │
        ▼
Course Recommendations
```

---

# 🤖 AI Copilot

AI Copilot is the long-term vision of the project. It will combine every AI module into a single intelligent assistant capable of supporting candidates throughout their placement journey.

Rather than focusing on a single task, AI Copilot will coordinate resume analysis, interview preparation, training recommendations, and career guidance.

---

## 🎯 Planned Features

- Resume Chat Assistant
- Resume Review
- Resume Rewrite
- Resume Summary Generation
- Resume vs Job Description Matching
- AI Career Guidance
- Interview Coaching
- LLM Integration
- Retrieval-Augmented Generation (RAG)
- Context-Aware Career Assistance

---

## 🔄 Future AI Workflow

```text
Resume
    │
    ▼
AI Copilot
    │
    ├────────► Resume Analysis
    ├────────► ATS Evaluation
    ├────────► Career Recommendation
    ├────────► Resume Improvement
    ├────────► Analytics
    ├────────► Interview Preparation
    ├────────► Training Guidance
    └────────► Career Assistant
```

---

## 📍 Current Development Progress

| Module | Status |
|---------|--------|
| Resume Parser | ✅ Completed |
| ATS Engine | ✅ Completed |
| Job Recommendation | ✅ Completed |
| Explainability | ✅ Completed |
| Resume Improvement | ✅ Completed |
| Analytics Engine | ✅ Completed |
| Interview Engine | ✅ Completed |
| Training Engine | 🚧 In Development |
| AI Copilot | ⏳ Planned |

---

# 🧪 Testing

AI Resume Copilot follows a **Test-Driven Development (TDD)** approach. Every completed module is validated through automated unit and service tests before integration.

---

## 📊 Current Test Status

| Category | Status |
|----------|--------|
| Total Tests | ✅ 110 Passed |
| Failed Tests | ✅ 0 |
| Warnings | ⚠️ 1 |
| AI Engine Tests | ✅ Passed |
| Service Tests | ✅ Passed |
| API Tests | ✅ Passed |

---

## 📂 Test Structure

```text
tests/

├── ai_engine/
│   ├── parser/
│   ├── ats/
│   ├── jobs/
│   ├── explainability/
│   ├── improvement/
│   ├── analytics/
│   ├── interview/
│   └── training/
│
├── services/
│   ├── test_analytics_service.py
│   └── test_interview_service.py
│
├── api/
│
└── integration/
```

---

## ▶️ Run All Tests

```bash
python -m pytest
```

---

## ▶️ Run Module Tests

| Module | Command |
|---------|---------|
| Resume Parser | `python -m pytest tests/ai_engine/parser -v` |
| ATS Engine | `python -m pytest tests/ai_engine/ats -v` |
| Job Recommendation | `python -m pytest tests/ai_engine/jobs -v` |
| Explainability | `python -m pytest tests/ai_engine/explainability -v` |
| Resume Improvement | `python -m pytest tests/ai_engine/improvement -v` |
| Analytics | `python -m pytest tests/ai_engine/analytics -v` |
| Interview | `python -m pytest tests/ai_engine/interview -v` |

---

## ▶️ Run Service Tests

```bash
python -m pytest tests/services -v
```

---

## ▶️ Run API Tests

```bash
python -m pytest tests/api -v
```

---

## ✔️ Test Coverage

The current test suite validates:

- Resume parsing
- ATS evaluation
- Job recommendation
- Skill gap analysis
- Resume improvement
- Analytics processing
- Interview preparation
- Service layer integration
- API responses
- Error handling

---

# 🌐 API Overview

AI Resume Copilot exposes REST APIs built with **FastAPI**. The API layer provides a consistent interface for frontend applications and external integrations.

---

## 📦 Available APIs

| API | Status |
|------|--------|
| Resume API | ✅ Available |
| Job Recommendation API | ✅ Available |
| Analytics API | 🚧 Planned |
| Interview API | 🚧 Planned |
| Training API | ⏳ Planned |
| Authentication API | ⏳ Planned |

---

## 📡 Current Endpoints

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/` | GET | Health check |
| `/resume/analyze` | POST | Upload and analyze a resume |
| `/jobs/recommend` | POST | Generate job recommendations |

---

## 📤 Sample Response

```json
{
  "success": true,
  "filename": "resume.pdf",
  "message": "Resume analyzed successfully.",
  "analysis": {
    "contact": {},
    "education": {},
    "experience": {},
    "skills": [],
    "ats": {},
    "recommendation": {},
    "improvement": {},
    "analytics": {},
    "explainability": {},
    "text": "",
    "metadata": {}
  }
}
```

---

## 📘 API Documentation

FastAPI automatically generates interactive API documentation.

| Documentation | URL |
|---------------|-----|
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |

---

# ⚠️ Error Handling

The API currently handles:

- Unsupported file formats
- Missing upload files
- Invalid request data
- Processing failures

All endpoints return a consistent JSON response structure to simplify frontend integration.

---

## 📈 Current Project Metrics

| Metric | Value |
|---------|-------|
| Completed AI Modules | 7 |
| Module In Development | 1 |
| Planned Modules | 1 |
| Passing Tests | 110 |
| REST APIs | 2 |
| Resume Formats | 2 |
| Backend Framework | FastAPI |
| Architecture | Modular |

---

# 🗺️ Development Roadmap

The roadmap is organized into progressive milestones. Each phase builds on the previous one while maintaining a modular architecture and comprehensive automated testing.

---

## ✅ Phase 1 — Core Resume Analysis

**Completed**

This phase established the foundation of AI Resume Copilot.

### Deliverables

- Resume Parser
- ATS Engine
- Job Recommendation Engine
- Explainability Engine
- Resume Improvement Engine
- REST API Integration
- Unit Testing

---

## ✅ Phase 2 — Resume Analytics

**Completed**

This phase introduced historical resume analysis and progress tracking.

### Deliverables

- ATS Score History
- Resume Comparison
- Improvement Tracker
- Analytics Engine
- Analytics Service
- Resume Integration
- Automated Testing

---

## ✅ Phase 3 — Interview Preparation

**Completed**

This phase added interview preparation capabilities based on predicted job roles.

### Deliverables

- Technical Question Generator
- HR Question Bank
- Answer Evaluation
- Interview Feedback
- Learning Roadmap
- Interview Analyzer
- Interview Service
- Automated Testing

---

## 🚧 Phase 4 — Training Engine

**Current Phase**

The Training Engine will recommend personalized learning resources using resume analysis, interview performance, and identified skill gaps.

### Planned Deliverables

- Skill Analysis
- Course Recommendation
- Learning Planner
- Progress Tracking
- Training Service
- API Integration
- Automated Testing

---

## ⏳ Phase 5 — AI Copilot

The final phase combines every module into a unified AI-powered career assistant.

### Planned Deliverables

- Resume Chat Assistant
- Resume Review
- Resume Rewrite
- Resume Summary
- Resume vs Job Description Matching
- AI Career Guidance
- LLM Integration
- RAG Pipeline
- Vector Database Integration

---

# 📦 Version History

| Version | Highlights | Status |
|---------|------------|--------|
| v0.1.0 | Initial project setup | ✅ Released |
| v0.2.0 | Resume Parser | ✅ Released |
| v0.3.0 | ATS Engine | ✅ Released |
| v0.4.0 | Job Recommendation & Explainability | ✅ Released |
| v0.5.0 | Resume Improvement Engine | ✅ Released |
| v0.6.0 | Analytics Engine | ✅ Released |
| v0.7.0 | Interview Engine | ✅ Released |
| v0.8.0 | Training Engine | 🚧 In Development |
| v1.0.0 | AI Resume Copilot | ⏳ Planned |

---

# 📊 Development Timeline

| Milestone | Status |
|-----------|--------|
| Resume Parsing | ✅ Complete |
| ATS Evaluation | ✅ Complete |
| Career Recommendation | ✅ Complete |
| Explainability | ✅ Complete |
| Resume Improvement | ✅ Complete |
| Resume Analytics | ✅ Complete |
| Interview Preparation | ✅ Complete |
| Training Engine | 🚧 In Progress |
| AI Copilot | ⏳ Planned |

---

# 🎯 Current Development Goal

The current objective is to complete the **Training Engine**.

Planned work includes:

- Personalized learning recommendations
- Skill gap prioritization
- Course recommendation system
- Learning roadmap generation
- Progress tracking
- Service layer implementation
- REST API integration
- Automated testing

After completing the Training Engine, development will continue with the AI Copilot.

---

# 🚀 Future Enhancements

The following features are planned for future releases to transform AI Resume Copilot into a complete career assistance platform.

---

## 🤖 Artificial Intelligence

- Large Language Model (LLM) Integration
- Resume Chat Assistant
- Resume Review
- Resume Rewrite
- Resume Summary Generation
- AI Career Guidance
- Resume vs Job Description Matching
- Context-Aware Recommendations

---

## 📚 Training & Learning

- Personalized Learning Paths
- Course Recommendations
- Skill Development Plans
- Progress Tracking
- Certification Recommendations

---

## 📊 Analytics

- Resume Progress Dashboard
- ATS Score Trends
- Historical Resume Comparison
- Performance Reports
- Interactive Data Visualization

---

## 💼 Career Support

- Company-Specific Resume Optimization
- Internship Recommendations
- Placement Readiness Score
- Resume Benchmarking
- Career Growth Insights

---

## 🎤 Interview Preparation

- Technical Mock Interviews
- HR Mock Interviews
- Coding Interview Practice
- AI-Based Answer Evaluation
- Performance Analytics

---

## ☁️ Deployment

- Docker Support
- Kubernetes Deployment
- CI/CD Pipeline
- AWS Deployment
- Production Monitoring

---

## 🔐 Security

- JWT Authentication
- User Accounts
- Role-Based Access Control
- Secure Resume Storage
- API Rate Limiting

---

## 🖥️ Frontend

- React Dashboard
- Resume Upload Portal
- Analytics Dashboard
- User Profile
- Interactive Reports

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve AI Resume Copilot, follow these steps:

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Add or update tests.
5. Verify that all tests pass.
6. Commit using meaningful commit messages.
7. Open a Pull Request.

---

# 📋 Coding Standards

The project follows consistent development practices to maintain readability and long-term maintainability.

---

## Python

- Follow PEP 8 guidelines.
- Use descriptive names for variables, functions, and classes.
- Keep functions focused on a single responsibility.
- Write clear docstrings for public modules.
- Prefer reusable components over duplicated logic.

---

## Project Organization

- Keep AI modules independent.
- Separate business logic from API endpoints.
- Place reusable functionality inside the AI Engine or Service Layer.
- Validate request and response models using Pydantic.
- Add automated tests for every completed feature.

---

## Git Workflow

Recommended commit prefixes:

```text
feat(module): add new feature
fix(module): resolve issue
refactor(module): improve code structure
docs(readme): update documentation
test(module): add unit tests
```

Example:

```bash
git commit -m "feat(training): implement course recommendation engine"
```

---

# 👨‍💻 Author

**Divesh Kate**

B.Tech Artificial Intelligence & Machine Learning Student

### Connect

- GitHub: https://github.com/diveshkate11-collab
- Repository: https://github.com/diveshkate11-collab/ai-resume-analyzer

---

# 📊 Repository Status

| Category | Current Status |
|----------|----------------|
| Project Version | v0.7.0 |
| Development Status | Active Development |
| Current Milestone | Training Engine |
| Completed AI Modules | 7 |
| Module In Development | 1 |
| Planned Module | 1 |
| Total Tests | 110 Passing |
| Test Failures | 0 |
| Service Layer | Analytics & Interview |
| Backend Framework | FastAPI |
| Architecture | Modular |

---

# 📝 Changelog

## v0.7.0

### Added

- Interview Engine
- Technical Question Generator
- HR Question Bank
- Answer Evaluator
- Interview Feedback
- Interview Analyzer
- Interview Roadmap
- Interview Service
- Interview Engine Test Suite

### Improved

- Analytics integration
- Resume processing pipeline
- Service layer organization
- Test coverage
- Project architecture

### Testing

```text
110 Passed
0 Failed
1 Warning
```

---

## Previous Releases

### v0.6.0

- Analytics Engine
- ATS History
- Resume Comparison
- Improvement Tracker
- Analytics Service

### v0.5.0

- Resume Improvement Engine

### v0.4.0

- Job Recommendation Engine
- Explainability Engine

### v0.3.0

- ATS Engine

### v0.2.0

- Resume Parser

### v0.1.0

- Initial Project Setup

---

# 🏁 Project Summary

AI Resume Copilot is a modular backend platform that assists candidates throughout different stages of career preparation.

### Completed Capabilities

- Resume Parsing
- ATS Evaluation
- Job Recommendation
- Explainability
- Resume Improvement
- Resume Analytics
- Interview Preparation

### Current Focus

- Training Engine

### Long-Term Vision

- AI Copilot
- LLM Integration
- Resume Chat Assistant
- Career Guidance
- Intelligent Learning Recommendations

---

# 📚 Documentation

The documentation evolves alongside the project to reflect completed features and architectural changes.

Current documentation includes:

- Project Overview
- Installation Guide
- Architecture
- AI Modules
- Testing Guide
- API Reference
- Development Roadmap
- Version History

Future documentation will include:

- Database Design
- Deployment Guide
- Docker Setup
- Cloud Deployment
- Frontend Guide
- CI/CD Pipeline
- API Authentication
- Developer Guide

---

# 📄 License

This project is licensed under the **MIT License**.

You may use, modify, and distribute this project under the terms of the MIT License.

See the **LICENSE** file for complete license information.

<div align="center">

### ⭐ If you find this project useful, consider giving it a star on GitHub.

Thank you for visiting **AI Resume Copilot** 🚀

</div>