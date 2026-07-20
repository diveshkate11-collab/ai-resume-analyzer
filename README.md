# 🚀 AI Resume Copilot

<div align="center">

### AI-Powered Resume Analysis, ATS Optimization & Career Assistant

Analyze resumes, evaluate ATS compatibility, identify skill gaps, recommend career paths, improve resume quality, and support interview preparation through a modular AI-powered backend.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?logo=fastapi)
![Tests](https://img.shields.io/badge/Tests-77_Passed-success)
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
  - Analytics Module
  - Interview Module
  - Training Module
  - AI Copilot
- Testing
- API Overview
- Version History
- Roadmap
- Future Enhancements
- Contributing
- License
- Author
- Changelog

---

# 📚 About

AI Resume Copilot is a modular backend application that helps candidates evaluate and improve their resumes using Artificial Intelligence and Machine Learning techniques.

The system analyzes resumes uploaded in **PDF** or **DOCX** format, extracts structured information, evaluates Applicant Tracking System (ATS) compatibility, predicts suitable job roles, explains AI-generated decisions, identifies resume weaknesses, and provides personalized improvement suggestions.

The project is being developed as a production-oriented software engineering project with a strong emphasis on:

- Modular Architecture
- Clean Code
- Scalability
- Test-Driven Development
- Deployment Readiness
- API-First Design

The long-term vision is to build a complete AI-powered career assistance platform that supports candidates throughout the placement journey.

---

# 🎯 Project Objectives

The primary objectives of AI Resume Copilot are:

- Build an industry-ready AI Resume Analyzer.
- Learn production-grade FastAPI backend development.
- Design reusable AI modules.
- Implement scalable software architecture.
- Follow clean coding principles.
- Practice Test-Driven Development using Pytest.
- Build deployment-ready REST APIs.
- Develop a portfolio-quality software engineering project.
- Continuously extend the platform with AI-driven career assistance.

---

# ✨ Current Features

## 📄 Resume Parsing

- PDF Resume Parsing
- DOCX Resume Parsing
- Resume Text Cleaning
- Contact Information Extraction
- Skills Extraction
- Education Extraction
- Experience Extraction
- Structured Resume Output

---

## 📊 ATS Analysis

- ATS Score Calculation
- Resume Section Validation
- Technical Keyword Matching
- Resume Formatting Analysis
- Grammar Analysis

---

## 💼 Job Recommendation

- Role Prediction
- Job Matching
- Skill Gap Detection
- Career Recommendations

---

## 💡 Explainability

- ATS Score Explanation
- Job Recommendation Explanation
- Skill Gap Explanation

---

## 🛠️ Resume Improvement

- Strength Analysis
- Weakness Analysis
- Resume Improvement Suggestions
- Resume Improvement Engine

---

# 📊 Current Project Status

| Module | Status |
|---------|--------|
| Resume Parser | ✅ Completed |
| ATS Engine | ✅ Completed |
| Job Recommendation | ✅ Completed |
| Explainability | ✅ Completed |
| Resume Improvement | ✅ Completed |
| Analytics | 🚧 In Development |
| Interview | ⏳ Planned |
| Training | ⏳ Planned |
| AI Copilot | ⏳ Planned |

---

# 🏆 Latest Milestone

### Current Version

```text
v0.5.0
```

### Latest Achievement

```text
77 Passing Unit Tests
```

### Current Focus

```text
Analytics Module
```

---

# ⭐ Project Highlights

- Modular AI Engine Architecture
- FastAPI Backend
- RESTful API Design
- Automated Unit Testing
- Resume Parsing Pipeline
- ATS Compatibility Analysis
- AI-Based Job Recommendation
- Resume Explainability
- Resume Improvement Engine
- Production-Oriented Project Structure
- GitHub Portfolio Ready

---

# 🛠️ Technology Stack

AI Resume Copilot is built using a modern Python backend with a modular architecture designed for scalability, maintainability, and production deployment.

---

## 💻 Programming Language

| Technology | Purpose |
|------------|---------|
| Python 3.14 | Core Programming Language |

---

## ⚡ Backend Framework

| Technology | Purpose |
|------------|---------|
| FastAPI | REST API Development |
| Uvicorn | ASGI Application Server |

---

## ✅ Data Validation

| Technology | Purpose |
|------------|---------|
| Pydantic | Request & Response Validation |

---

## 📄 Resume Parsing

| Technology | Purpose |
|------------|---------|
| PyPDF2 | PDF Text Extraction |
| python-docx | DOCX Text Extraction |
| Regular Expressions (Regex) | Contact & Information Extraction |

---

## 🧪 Testing

| Technology | Purpose |
|------------|---------|
| Pytest | Unit Testing |
| HTTPX | API Testing |
| FastAPI TestClient | Endpoint Testing |

---

## 🛠️ Development Tools

| Tool | Purpose |
|------|---------|
| Visual Studio Code | Code Editor |
| Git | Version Control |
| GitHub | Repository Hosting |

---

## 🚀 Planned Technologies

These technologies will be integrated as the project evolves.

| Technology | Planned Usage |
|------------|---------------|
| PostgreSQL | Persistent Database |
| SQLAlchemy | ORM |
| Docker | Containerization |
| Kubernetes | Container Orchestration |
| AWS | Cloud Deployment |
| React | Frontend Dashboard |
| LangChain | LLM Workflow |
| LangGraph | Agent Workflow |
| Vector Database | Semantic Search |
| Ollama | Local LLM Support |
| OpenAI API | AI Features |
| RAG | Retrieval-Augmented Generation |

---

# 🏛️ System Architecture

AI Resume Copilot follows a layered architecture that separates API endpoints, business logic, AI processing, and future storage components. This design keeps modules independent, testable, and easy to extend.

```text
                    Client
                       │
                       ▼
               FastAPI REST API
                       │
                       ▼
             Request Validation
                  (Pydantic)
                       │
                       ▼
                 Service Layer
                       │
                       ▼
                  AI Engine Core
                       │
 ┌──────────┬──────────┬──────────┬──────────┬──────────┐
 ▼          ▼          ▼          ▼          ▼
Parser      ATS       Jobs   Explainability Improvement
 │           │          │          │            │
 └───────────┴──────────┴──────────┴────────────┘
                       │
                       ▼
              Structured JSON Response
```

---

## 🧩 AI Engine Design

Every AI module is designed as an independent component.

```text
Resume Upload
      │
      ▼
 Resume Parser
      │
      ▼
Structured Resume Data
      │
      ├─────────────── ATS Engine
      │
      ├─────────────── Job Recommendation
      │
      ├─────────────── Explainability
      │
      ├─────────────── Resume Improvement
      │
      ├─────────────── Analytics (Upcoming)
      │
      ├─────────────── Interview (Upcoming)
      │
      └─────────────── AI Copilot (Upcoming)
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

## 📁 Repository Overview

| Directory | Description |
|-----------|-------------|
| app | Main backend application |
| ai_engine | AI modules for resume processing |
| api | REST API endpoints |
| services | Business logic layer |
| schemas | Pydantic request & response models |
| tests | Automated unit and API tests |
| uploads | Uploaded resumes |
| storage | Future persistent storage |
| deployment | Deployment resources |
| frontend | Planned React frontend |

---

## 📌 Current Development Stage

```text
Completed
────────────
✔ Resume Parser
✔ ATS Engine
✔ Job Recommendation
✔ Explainability
✔ Resume Improvement

Currently Developing
────────────────────
▶ Analytics Module

Upcoming
────────
• Interview Module
• Training Module
• AI Copilot
• Database Integration
• Authentication
• Frontend
• Deployment
```

---

# 🚀 Installation

Follow the steps below to set up **AI Resume Copilot** on your local machine.

---

## 📋 Prerequisites

Ensure the following software is installed before proceeding.

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

Clone the project from GitHub.

```bash
git clone https://github.com/diveshkate11-collab/ai-resume-analyzer.git
```

Navigate into the project directory.

```bash
cd ai-resume-analyzer
```

---

## 🐍 Create a Virtual Environment

### Windows

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

```bash
.venv\Scripts\activate
```

---

### Linux / macOS

Create a virtual environment.

```bash
python3 -m venv .venv
```

Activate it.

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

## ✔ Verify Installation

Check the installed Python version.

```bash
python --version
```

Check installed packages.

```bash
python -m pip list
```

---

# ⚙️ Configuration

The current version requires minimal configuration.

Future releases will introduce configurable services such as:

- Database Connection
- Authentication
- Cloud Storage
- Logging
- AI Model Configuration
- Email Notifications

---

## 🔑 Environment Variables

A sample environment file will be introduced in future releases.

Example:

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

If the application starts successfully, you should see output similar to:

```text
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## 🌐 Local Server

Open the application:

```text
http://127.0.0.1:8000
```

---

## 📘 Interactive API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# 📂 Configuration Files

| File | Purpose |
|------|---------|
| `requirements.txt` | Python dependencies |
| `pyproject.toml` | Project configuration |
| `.gitignore` | Ignore unnecessary files |
| `README.md` | Project documentation |
| `LICENSE` | Project license |

---

# 🚦 Development Workflow

Every feature in AI Resume Copilot follows a consistent development lifecycle to ensure code quality and maintainability.

```text
Requirement
      │
      ▼
Planning
      │
      ▼
Architecture Design
      │
      ▼
Implementation
      │
      ▼
Unit Testing
      │
      ▼
Integration Testing
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

Screenshots will be added as frontend development progresses.

| Screen | Status |
|---------|--------|
| Home Dashboard | 🚧 Planned |
| Resume Upload | 🚧 Planned |
| Resume Analysis | 🚧 Planned |
| ATS Report | 🚧 Planned |
| Job Recommendation | 🚧 Planned |
| Resume Improvement | 🚧 Planned |
| Analytics Dashboard | 🚧 Planned |

---

# 🎥 Live Demo

A live demonstration will be available after deployment.

**Status:** 🚧 Coming Soon

---

# 🌐 API Documentation

Once the server is running, FastAPI automatically generates interactive API documentation.

| Documentation | URL |
|---------------|-----|
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |

---

# 📄 Resume Parser Module

The **Resume Parser** is the first stage of the AI Resume Copilot pipeline. It converts an uploaded resume into structured data that can be processed by the remaining AI modules.

The parser currently supports both **PDF** and **DOCX** resume formats.

---

## 🎯 Responsibilities

The Resume Parser performs the following tasks:

- Extract text from PDF resumes
- Extract text from DOCX resumes
- Clean unnecessary characters
- Parse contact information
- Identify technical skills
- Detect educational qualifications
- Extract work experience
- Generate structured resume data

---

## 📦 Supported Formats

| Format | Status |
|---------|--------|
| PDF | ✅ Supported |
| DOCX | ✅ Supported |

---

## 🧩 Parser Components

| Component | Description | Status |
|-----------|-------------|--------|
| PDF Parser | Extracts text from PDF resumes | ✅ |
| DOCX Parser | Extracts text from DOCX resumes | ✅ |
| Text Cleaner | Cleans extracted resume text | ✅ |
| Contact Parser | Extracts contact details | ✅ |
| Skills Parser | Identifies technical skills | ✅ |
| Education Parser | Extracts education information | ✅ |
| Experience Parser | Extracts experience information | ✅ |
| Resume Parser | Integrates all parser modules | ✅ |

---

# 🔄 Resume Parsing Workflow

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

# 📊 Extracted Information

The parser generates structured information in the following format.

```text
Resume
│
├── Contact
│      ├── Name
│      ├── Email
│      └── Phone
│
├── Skills
│
├── Education
│
├── Experience
│
└── Metadata
```

---

# 📤 Sample Output

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
  "metadata": {
    "characters": 1824
  }
}
```

---

# 🧪 Unit Testing

The Resume Parser is fully covered with automated unit tests.

Current parser tests validate:

- PDF parsing
- DOCX parsing
- Text cleaning
- Contact extraction
- Skill extraction
- Education extraction
- Experience extraction
- Complete parser integration

---

## Test Command

```bash
python -m pytest tests/ai_engine/parser -v
```

---

## Current Status

| Category | Status |
|----------|--------|
| Module | ✅ Completed |
| Integration | ✅ Completed |
| Unit Tests | ✅ Passed |
| API Integration | ✅ Completed |

---

# 📈 Parser Statistics

| Metric | Value |
|---------|-------|
| Supported Formats | 2 |
| Parser Components | 8 |
| API Integrated | Yes |
| Unit Tested | Yes |
| Production Ready | Yes |

---

# 🔗 Position in AI Pipeline

The Resume Parser is the entry point of the complete AI processing pipeline.

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
      ├────────► Explainability
      │
      ├────────► Resume Improvement
      │
      └────────► Analytics (Upcoming)
```

---

# 🎯 ATS Engine

The **Applicant Tracking System (ATS) Engine** evaluates resume quality by analyzing resume structure, technical keywords, formatting, and grammar. It generates an ATS score that estimates how well a resume aligns with common ATS screening practices.

The ATS Engine operates on the structured data produced by the Resume Parser and returns detailed scoring information rather than a single numeric score.

---

## 🎯 Responsibilities

The ATS Engine performs the following tasks:

- Calculate ATS Score
- Validate Resume Sections
- Match Technical Keywords
- Analyze Resume Formatting
- Perform Basic Grammar Checks
- Generate ATS Analysis Report

---

## 🧩 ATS Components

| Component | Description | Status |
|-----------|-------------|--------|
| ATS Scorer | Calculates the final ATS score | ✅ |
| Section Checker | Detects required resume sections | ✅ |
| Keyword Matcher | Matches technical skills | ✅ |
| Formatting Checker | Checks resume formatting | ✅ |
| Grammar Checker | Performs grammar analysis | ✅ |

---

# ⚙️ ATS Evaluation Pipeline

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

# 📊 ATS Scoring Criteria

| Category | Maximum Score |
|----------|--------------:|
| Resume Sections | 40 |
| Technical Keywords | 30 |
| Formatting | 20 |
| Grammar | 10 |
| **Total** | **100** |

---

## 📑 Resume Sections Checked

The Section Checker validates the presence of essential resume sections.

- Education
- Skills
- Experience
- Projects

Each detected section contributes to the overall ATS score.

---

## 💻 Technical Keyword Matching

The Keyword Matcher scans the resume for relevant technical skills.

Examples include:

- Python
- FastAPI
- SQL
- Docker
- Git
- Machine Learning
- Deep Learning
- PyTorch
- TensorFlow
- NumPy
- Pandas

Additional keywords can be added as the project evolves.

---

## 📄 Formatting Analysis

The Formatting Checker validates basic formatting quality by checking for:

- Empty resumes
- Very short resumes
- Basic structural quality

---

## ✍️ Grammar Analysis

The Grammar Checker performs lightweight grammar validation and contributes to the final ATS score.

Current implementation focuses on simple quality checks and can be extended with advanced NLP models in future releases.

---

# 📤 Sample ATS Output

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

# 🧪 Unit Testing

The ATS Engine is fully covered by automated unit tests.

The following components are verified:

- ATS Scorer
- Section Checker
- Keyword Matcher
- Formatting Checker
- Grammar Checker

---

## Test Command

```bash
python -m pytest tests/ai_engine/ats -v
```

---

## Current Status

| Category | Status |
|----------|--------|
| Module | ✅ Completed |
| Unit Tests | ✅ Passed |
| API Integration | ✅ Completed |
| Resume Parser Integration | ✅ Completed |

---

# 📈 Module Statistics

| Metric | Value |
|---------|-------|
| Components | 5 |
| Maximum Score | 100 |
| Resume Sections Evaluated | 4 |
| Testing Status | Passed |
| Integration Status | Completed |

---

# 🔗 Position in AI Pipeline

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
      ▼
Resume Response
```

---

# 💼 Job Recommendation Engine

The **Job Recommendation Engine** analyzes the extracted skills from a resume and predicts suitable job roles. It also identifies missing skills required for those roles and generates practical recommendations to help candidates improve their employability.

The module works after ATS analysis and provides role-specific career guidance.

---

## 🎯 Responsibilities

The Job Recommendation Engine performs the following tasks:

- Predict suitable job roles
- Match candidate skills with predefined roles
- Detect missing technical skills
- Recommend learning paths
- Generate career recommendations

---

## 🧩 Components

| Component | Description | Status |
|-----------|-------------|--------|
| Role Predictor | Predicts suitable job roles | ✅ |
| Job Matcher | Matches candidate with predefined roles | ✅ |
| Skill Gap Analyzer | Detects missing technical skills | ✅ |
| Recommendation Engine | Generates career recommendations | ✅ |

---

# ⚙️ Job Recommendation Workflow

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
Final Job Recommendation
```

---

# 👨‍💻 Supported Job Roles

The current version supports prediction for the following roles:

- Backend Developer
- Python Developer
- AI / ML Engineer
- Data Analyst
- Software Developer

Additional roles will be introduced in future releases.

---

# 📤 Sample Output

```json
{
  "role": "Backend Developer",
  "recommendations": [
    "Build REST APIs using FastAPI.",
    "Learn Docker and containerization.",
    "Practice SQL optimization."
  ]
}
```

---

## 🧪 Unit Testing

The Job Recommendation Engine includes automated tests for:

- Role Predictor
- Job Matcher
- Skill Gap Analyzer
- Recommendation Engine

Run the tests using:

```bash
python -m pytest tests/ai_engine/jobs -v
```

---

## Current Status

| Category | Status |
|----------|--------|
| Module | ✅ Completed |
| Unit Tests | ✅ Passed |
| Resume Parser Integration | ✅ Completed |
| API Integration | ✅ Completed |

---

# 📈 Module Statistics

| Metric | Value |
|---------|-------|
| Components | 4 |
| Supported Job Roles | 5 |
| Integration | Completed |
| Testing | Passed |

---

# 💡 Explainability Engine

The **Explainability Engine** provides human-readable explanations for AI-generated outputs. Instead of returning only predictions, it explains why a resume received a particular ATS score, why a role was recommended, and which skills influenced the recommendation.

The objective is to make AI decisions transparent and easier to understand.

---

## 🎯 Responsibilities

The Explainability Engine performs the following tasks:

- Explain ATS score
- Explain recommended job roles
- Explain matched skills
- Explain missing skills

---

## 🧩 Components

| Component | Description | Status |
|-----------|-------------|--------|
| ATS Explanation | Explains ATS score | ✅ |
| Job Reason | Explains recommended role | ✅ |
| Skill Reason | Explains matched and missing skills | ✅ |

---

# ⚙️ Explainability Workflow

```text
ATS Analysis
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
Skill Gap Analysis
      │
      ▼
Skill Reason
      │
      ▼
Final Explainability Report
```

---

# 📤 Sample Output

```json
{
  "ats_score": 85,
  "explanation": [
    "Your resume has a strong ATS score.",
    "Education section is present.",
    "Skills section is present.",
    "Matched 5 technical skills."
  ]
}
```

---

## 🧪 Unit Testing

The Explainability Engine is covered with automated tests for all components.

Run the tests using:

```bash
python -m pytest tests/ai_engine/explainability -v
```

---

## Current Status

| Category | Status |
|----------|--------|
| Module | ✅ Completed |
| Unit Tests | ✅ Passed |
| Resume Parser Integration | ✅ Completed |
| API Integration | ✅ Completed |

---

# 📈 Module Statistics

| Metric | Value |
|---------|-------|
| Components | 3 |
| Integration | Completed |
| Testing | Passed |
| Production Ready | Yes |

---

# 🔗 AI Processing Pipeline

```text
Resume Upload
      │
      ▼
Resume Parser
      │
      ▼
ATS Engine
      │
      ▼
Job Recommendation
      │
      ▼
Explainability
      │
      ▼
Resume Improvement
      │
      ▼
Analytics (Next Module)
```

---

# 🛠️ Resume Improvement Engine

The **Resume Improvement Engine** analyzes resume quality and provides actionable recommendations to help candidates strengthen their resumes before applying for jobs.

Unlike the ATS Engine, which evaluates compatibility, the Improvement Engine focuses on identifying strengths, weaknesses, and practical improvements that increase resume quality.

---

## 🎯 Responsibilities

The Resume Improvement Engine performs the following tasks:

- Analyze resume strengths
- Detect resume weaknesses
- Generate personalized improvement suggestions
- Produce a structured improvement report

---

## 🧩 Components

| Component | Description | Status |
|-----------|-------------|--------|
| Strength Analyzer | Identifies positive aspects of the resume | ✅ |
| Weakness Analyzer | Detects missing skills and sections | ✅ |
| Suggestion Generator | Generates improvement suggestions | ✅ |
| Improvement Engine | Combines all improvement modules | ✅ |

---

# ⚙️ Resume Improvement Workflow

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

# 📤 Sample Output

```json
{
    "strengths": [
        "Strong Python skills.",
        "Backend development skills identified.",
        "Education details are present."
    ],
    "weaknesses": [
        "Docker skill is missing.",
        "Git skill is missing."
    ],
    "suggestions": [
        "Learn Docker for backend deployment.",
        "Add Git and GitHub experience.",
        "Include internships, projects, or freelance experience."
    ]
}
```

---

## 🧪 Unit Testing

The Resume Improvement Engine includes automated unit tests covering all analyzers and the integrated engine.

Run the tests using:

```bash
python -m pytest tests/ai_engine/improvement -v
```

---

## Current Status

| Category | Status |
|----------|--------|
| Module | ✅ Completed |
| Unit Tests | ✅ Passed |
| Resume Parser Integration | ✅ Completed |
| API Integration | ✅ Completed |

---

# 📈 Module Statistics

| Metric | Value |
|---------|-------|
| Components | 4 |
| Integration | Completed |
| Unit Tests | Passed |
| Production Ready | Yes |

---

# 📊 Analytics Module

The **Analytics Module** will enable users to compare multiple resume analyses and monitor improvement over time.

Instead of evaluating only a single resume, Analytics will provide historical insights, score tracking, and resume comparison reports.

---

## 🎯 Planned Responsibilities

- Store ATS score history
- Compare resume versions
- Track improvements
- Generate analytics summary
- Visualize resume progress

---

## 🧩 Planned Components

| Component | Description | Status |
|-----------|-------------|--------|
| ATS History | Stores ATS score history | 🚧 |
| Resume Compare | Compares multiple resumes | 🚧 |
| Improvement Tracker | Tracks resume improvements | 🚧 |
| Analytics Engine | Generates analytics report | 🚧 |

---

# Planned Analytics Workflow

```text
Resume Analysis
        │
        ▼
Store ATS History
        │
        ▼
Resume Comparison
        │
        ▼
Improvement Tracking
        │
        ▼
Analytics Engine
        │
        ▼
Analytics Report
```

---

# 🎤 Interview Module

The Interview Module will help candidates prepare for placement interviews by generating technical and HR interview questions based on their resume and predicted job role.

---

## Planned Features

- Technical Interview Questions
- HR Interview Questions
- Coding Interview Questions
- Answer Evaluation
- Interview Feedback
- Performance Analysis

---

## Planned Workflow

```text
Resume Analysis
        │
        ▼
Predicted Job Role
        │
        ▼
Interview Question Generator
        │
        ▼
Candidate Answers
        │
        ▼
Answer Evaluation
        │
        ▼
Interview Feedback
```

---

# 🎓 Training Module

The Training Module will recommend learning resources based on the candidate's missing skills and career goals.

---

## Planned Features

- Personalized Learning Roadmap
- Recommended Courses
- Skill Development Suggestions
- Career Growth Guidance
- Learning Progress Tracking

---

# 🤖 AI Copilot

AI Copilot represents the long-term vision of the project.

It will function as an intelligent career assistant capable of guiding users throughout the complete placement journey, from resume preparation to interview success.

---

## Planned Features

- Resume Chat Assistant
- Resume Review
- Resume Rewrite
- Resume Summary Generator
- Resume vs Job Description Matching
- Career Guidance
- AI Career Mentor
- Interview Coaching
- LLM Integration
- RAG Pipeline

---

# 📍 Development Progress

| Module | Progress |
|---------|----------|
| Resume Parser | ✅ Completed |
| ATS Engine | ✅ Completed |
| Job Recommendation | ✅ Completed |
| Explainability | ✅ Completed |
| Resume Improvement | ✅ Completed |
| Analytics | 🚧 In Development |
| Interview | ⏳ Planned |
| Training | ⏳ Planned |
| AI Copilot | ⏳ Planned |

---

# 🧪 Testing

AI Resume Copilot follows a test-driven development approach. Every completed module includes dedicated unit tests to verify functionality before integration.

---

## 📊 Current Test Status

| Category | Status |
|----------|--------|
| Total Tests | ✅ 77 Passed |
| Failed Tests | ✅ 0 |
| API Tests | ✅ Passed |
| AI Engine Tests | ✅ Passed |
| Parser Tests | ✅ Passed |
| ATS Tests | ✅ Passed |
| Job Recommendation Tests | ✅ Passed |
| Explainability Tests | ✅ Passed |
| Resume Improvement Tests | ✅ Passed |

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

## ▶️ Run Tests with Verbose Output

```bash
python -m pytest -v
```

---

## ▶️ Run Individual Module Tests

### Resume Parser

```bash
python -m pytest tests/ai_engine/parser -v
```

### ATS Engine

```bash
python -m pytest tests/ai_engine/ats -v
```

### Job Recommendation

```bash
python -m pytest tests/ai_engine/jobs -v
```

### Explainability

```bash
python -m pytest tests/ai_engine/explainability -v
```

### Resume Improvement

```bash
python -m pytest tests/ai_engine/improvement -v
```

### Analytics

```bash
python -m pytest tests/ai_engine/analytics -v
```

### API Tests

```bash
python -m pytest tests/api -v
```

---

## ✅ Testing Goals

The testing suite verifies:

- Resume parsing accuracy
- ATS score generation
- Job role prediction
- Skill gap analysis
- Resume improvement suggestions
- API responses
- Module integration
- Error handling

---

# 🌐 API Overview

AI Resume Copilot exposes REST APIs built using FastAPI.

The APIs are designed to be modular, scalable, and easy to integrate with web or mobile frontends.

---

## 📦 Current API Modules

| Module | Status |
|---------|--------|
| Resume API | ✅ Completed |
| ATS API | 🚧 Planned |
| Jobs API | ✅ Completed |
| Interview API | ⏳ Planned |
| Analytics API | 🚧 Planned |
| Authentication API | ⏳ Planned |

---

## 📡 Available Endpoints

| Endpoint | Method | Purpose |
|-----------|--------|---------|
| `/` | GET | Health Check |
| `/resume/analyze` | POST | Analyze uploaded resume |
| `/jobs/recommend` | POST | Get job recommendations |

---

## 📤 Resume Analysis Response

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

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 🔒 Error Handling

The API currently validates:

- Unsupported file formats
- Missing upload files
- Invalid request data
- Internal processing failures

All API responses follow a consistent JSON response structure for easier frontend integration.

---

# 📈 Current Project Metrics

| Metric | Value |
|---------|-------|
| AI Modules Completed | 5 |
| AI Modules Planned | 4 |
| Total Passing Tests | 77 |
| REST APIs | 2 |
| Supported Resume Formats | 2 |
| Programming Language | Python |
| Backend Framework | FastAPI |
| Architecture | Modular |

---

# 🗺️ Development Roadmap

The roadmap outlines the planned development phases for AI Resume Copilot. Each phase builds on the previous one, ensuring a modular and maintainable architecture.

---

## ✅ Phase 1 — Core AI Engine (Completed)

- Resume Parser
- ATS Engine
- Job Recommendation Engine
- Explainability Engine
- Resume Improvement Engine
- REST API Integration
- Unit Testing
- Project Documentation

**Status:** ✅ Completed

---

## 🚧 Phase 2 — Resume Analytics (In Progress)

Current development focuses on tracking resume improvements across multiple analyses.

### Planned Features

- ATS Score History
- Resume Comparison
- Improvement Tracking
- Analytics Engine
- Resume Progress Summary

**Status:** 🚧 In Development

---

## ⏳ Phase 3 — Interview Preparation

This phase will assist candidates in preparing for placement interviews.

### Planned Features

- Technical Interview Questions
- HR Interview Questions
- Coding Questions
- AI Answer Evaluation
- Interview Feedback
- Performance Analysis

**Status:** ⏳ Planned

---

## ⏳ Phase 4 — AI Career Training

This module will recommend learning paths based on missing skills and career goals.

### Planned Features

- Personalized Learning Roadmap
- Course Recommendations
- Skill Development Plans
- Career Growth Suggestions
- Learning Progress Tracking

**Status:** ⏳ Planned

---

## ⏳ Phase 5 — AI Copilot

The final phase transforms AI Resume Copilot into a complete AI-powered career assistant.

### Planned Features

- Resume Chat Assistant
- Resume Rewrite
- Resume Review
- Resume Summary Generator
- Resume vs Job Description Matching
- AI Career Mentor
- LLM Integration
- RAG Pipeline
- Vector Database Integration

**Status:** ⏳ Planned

---

# 📦 Version History

| Version | Description | Status |
|---------|-------------|--------|
| v0.1.0 | Initial Project Setup | ✅ Released |
| v0.2.0 | Resume Parser Module | ✅ Released |
| v0.3.0 | ATS Engine | ✅ Released |
| v0.4.0 | Job Recommendation & Explainability | ✅ Released |
| v0.5.0 | Resume Improvement Engine | ✅ Released |
| v0.6.0 | Analytics Module | 🚧 In Development |
| v0.7.0 | Interview Module | ⏳ Planned |
| v0.8.0 | Training Module | ⏳ Planned |
| v1.0.0 | AI Resume Copilot | ⏳ Planned |

---

# 🚀 Future Enhancements

The following enhancements are planned for future releases.

---

## 🤖 Artificial Intelligence

- Large Language Model Integration
- Resume Chat Assistant
- Resume Rewrite
- Resume Summary Generator
- AI Career Mentor
- Personalized Career Guidance

---

## 📊 Analytics

- Resume Progress Dashboard
- ATS Score Trends
- Historical Resume Comparison
- Resume Growth Timeline
- Interactive Charts

---

## 💼 Career Support

- Job Description Matching
- Internship Recommendation
- Resume Benchmarking
- Company-Specific Resume Optimization
- Placement Readiness Score

---

## 🎤 Interview Preparation

- Technical Mock Interviews
- HR Mock Interviews
- Coding Interview Preparation
- AI Feedback
- Interview Analytics

---

## ☁️ Deployment

- Docker Support
- Kubernetes Deployment
- AWS Deployment
- CI/CD Pipeline
- Production Monitoring

---

## 🔐 Security

- JWT Authentication
- User Accounts
- Role-Based Access Control
- Secure Resume Storage
- Rate Limiting

---

## 🖥️ Frontend

- React Dashboard
- Resume Upload Interface
- Analytics Dashboard
- User Profile
- Interactive Reports

---

# 📈 Project Progress

| Area | Progress |
|------|----------|
| Resume Parser | ✅ 100% |
| ATS Engine | ✅ 100% |
| Job Recommendation | ✅ 100% |
| Explainability | ✅ 100% |
| Resume Improvement | ✅ 100% |
| Analytics | 🚧 In Progress |
| Interview | ⏳ Planned |
| Training | ⏳ Planned |
| AI Copilot | ⏳ Planned |

---

# 🎯 Current Development Goal

The immediate goal is to complete the **Analytics Module**, including:

- ATS Score History
- Resume Comparison
- Improvement Tracking
- Analytics Engine
- Analytics API Integration
- Unit Testing
- Resume Parser Integration
- Documentation Update

After completing Analytics, development will move to the Interview Module.

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve AI Resume Copilot, please follow these steps:

1. Fork the repository.
2. Create a new feature branch.
3. Implement the feature or bug fix.
4. Add or update unit tests.
5. Ensure all tests pass.
6. Commit your changes with meaningful commit messages.
7. Open a Pull Request.

---

# 📋 Coding Standards

The project follows a consistent coding style to ensure readability and maintainability.

## Python

- Follow PEP 8 guidelines.
- Use meaningful variable and function names.
- Write descriptive docstrings.
- Keep functions focused on a single responsibility.
- Avoid duplicate code.

---

## Project Structure

- Keep every AI module independent.
- Maintain separation between API, services, and AI logic.
- Place reusable logic inside the AI Engine.
- Write tests for every completed module.

---

## Git Workflow

Recommended commit style:

```text
feat(module): add new feature
fix(module): resolve issue
refactor(module): improve code structure
docs(readme): update documentation
test(module): add unit tests
```

Example:

```bash
git commit -m "feat(analytics): implement ATS history tracker"
```

---

# 📚 Documentation

The documentation is continuously updated throughout development.

Current documentation includes:

- Project Overview
- Installation Guide
- Architecture
- AI Modules
- Testing Guide
- API Overview
- Roadmap
- Version History

Future documentation will include:

- Deployment Guide
- Docker Setup
- AWS Deployment
- Frontend Documentation
- Database Design
- CI/CD Pipeline

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to:

- Use
- Modify
- Distribute
- Study

the source code under the terms of the MIT License.

See the **LICENSE** file for complete details.

---

# 👨‍💻 Author

**Divesh Kate**

B.Tech Artificial Intelligence & Machine Learning Student

### Connect

- GitHub: https://github.com/diveshkate11-collab
- Repository: https://github.com/diveshkate11-collab/ai-resume-analyzer

---

# 📊 Current Repository Status

| Category | Status |
|----------|--------|
| Project Version | v0.5.0 |
| Development Status | Active |
| Current Focus | Analytics Module |
| AI Modules Completed | 5 |
| AI Modules In Development | 1 |
| Planned AI Modules | 3 |
| Total Passing Tests | 77 |
| API Status | Operational |

---

# 📝 Changelog

## v0.5.0

### Added

- Resume Improvement Engine
- Strength Analyzer
- Weakness Analyzer
- Suggestion Generator
- Improvement Engine Integration
- Resume Parser Integration
- Resume Improvement API Integration

### Improved

- Resume parsing workflow
- Project architecture
- API response structure
- Module integration
- Documentation

### Fixed

- Job Recommendation Service integration
- Resume API response validation
- Recommendation schema consistency
- Parser integration issues

### Testing

- Added Improvement Engine unit tests.
- Updated parser tests.
- Updated API tests.
- Verified complete project functionality.

**Current Test Result**

```text
77 Passed
0 Failed
1 Warning
```

---

# 🏁 Project Summary

AI Resume Copilot is a modular backend application designed to simplify resume analysis and career preparation using Artificial Intelligence.

The project currently provides:

- Resume Parsing
- ATS Analysis
- Job Recommendation
- Explainability
- Resume Improvement

Upcoming development focuses on:

- Resume Analytics
- Interview Preparation
- AI Training
- AI Copilot
- Frontend Development
- Cloud Deployment

The project continues to evolve with a strong emphasis on clean architecture, modular design, automated testing, and production-ready development practices.

---

<div align="center">

### ⭐ If you find this project useful, consider giving it a star on GitHub.

**Thank you for visiting AI Resume Copilot! 🚀**

</div>