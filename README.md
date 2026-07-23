# 🚀 AI Resume Copilot

<div align="center">

### AI-Powered Resume Analysis, Career Intelligence & Interview Preparation Platform

Analyze resumes, evaluate ATS compatibility, identify skill gaps, recommend career paths, generate interview questions, create personalized learning plans, and provide AI-powered resume assistance through a modular backend architecture.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?logo=fastapi)
![Tests](https://img.shields.io/badge/Tests-127_Passed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active_Development-orange)

</div>

---

# 📖 Overview

AI Resume Copilot is a modular backend platform that helps job seekers analyze resumes, improve ATS compatibility, identify missing skills, receive career recommendations, prepare for interviews, generate personalized learning plans, and leverage AI-assisted resume guidance.

The application accepts resumes in **PDF** and **DOCX** formats, extracts structured information, evaluates Applicant Tracking System (ATS) compatibility, predicts suitable technical roles, recommends resume improvements, tracks resume progress, generates interview preparation material, creates learning roadmaps, and introduces an extensible AI Copilot layer for intelligent career assistance.

The platform follows a modular architecture where every capability is implemented as an independent AI engine. This separation of responsibilities improves maintainability, testing, scalability, and future extensibility.

The long-term objective is to evolve AI Resume Copilot into a complete AI-powered career platform supporting candidates throughout the hiring lifecycle—from resume analysis and optimization to interview preparation and continuous professional development.

---

# 🎯 Objectives

The project is being developed to achieve the following goals:

- Build a production-oriented AI resume analysis platform.
- Design reusable and independent AI engines.
- Practice scalable backend development with FastAPI.
- Follow clean architecture and separation of concerns.
- Apply Test-Driven Development (TDD).
- Develop well-documented REST APIs.
- Build a portfolio-quality software engineering project.
- Integrate Large Language Models using a provider-independent architecture.
- Prepare the system for production deployment and cloud scalability.

---

# ✨ Current Capabilities

The platform currently provides the following capabilities.

| AI Engine | Description | Status |
|-----------|-------------|--------|
| Resume Parser | Extract structured information from resumes | ✅ |
| ATS Engine | Evaluate ATS compatibility | ✅ |
| Job Recommendation | Predict suitable technical roles | ✅ |
| Explainability | Explain AI-generated decisions | ✅ |
| Resume Improvement | Recommend resume enhancements | ✅ |
| Analytics | Compare resume performance over time | ✅ |
| Interview | Generate technical and HR interview questions | ✅ |
| Training | Build personalized learning plans | ✅ |
| AI Copilot | AI-powered resume assistance foundation | 🚧 In Progress |

---

# 🌟 Key Highlights

- Modular AI Engine Architecture
- FastAPI REST Backend
- Layered Service Architecture
- Resume Parsing Pipeline
- ATS Evaluation
- Job Recommendation Engine
- Explainability Engine
- Resume Improvement Engine
- Resume Analytics
- Interview Preparation
- Personalized Training Recommendations
- AI Copilot Foundation
- Provider-Independent LLM Architecture
- Automated Unit Testing
- Production-Oriented Project Structure
- GitHub Portfolio Ready

---

# 🛠️ Technology Stack

AI Resume Copilot is built using a modern Python backend with a modular architecture focused on scalability, maintainability, and production-ready software engineering.

---

## 💻 Programming Language

| Technology | Purpose |
|------------|---------|
| Python 3.14 | Core application development |

---

## ⚡ Backend Framework

| Technology | Purpose |
|------------|---------|
| FastAPI | REST API development |
| Uvicorn | ASGI application server |

---

## ✅ Data Validation

| Technology | Purpose |
|------------|---------|
| Pydantic | Request and response validation |

---

## 📄 Resume Processing

| Technology | Purpose |
|------------|---------|
| PyPDF2 | PDF text extraction |
| python-docx | DOCX text extraction |
| Regular Expressions (Regex) | Information extraction |

---

## 🤖 AI Technologies

| Technology | Purpose |
|------------|---------|
| Prompt Manager | Centralized prompt management |
| Abstract LLM Client | Provider-independent AI integration |
| Mock LLM Client | Development and testing |

---

## 🧪 Testing

| Technology | Purpose |
|------------|---------|
| Pytest | Unit testing |
| HTTPX | API testing |
| FastAPI TestClient | Endpoint testing |

---

## 🛠️ Development Tools

| Tool | Purpose |
|------|---------|
| Visual Studio Code | Code editor |
| Git | Version control |
| GitHub | Source code hosting |

---

## 🚀 Planned Technologies

These technologies will be integrated in future releases.

| Technology | Planned Usage |
|------------|---------------|
| PostgreSQL | Persistent database |
| SQLAlchemy | ORM |
| Docker | Containerization |
| Kubernetes | Container orchestration |
| AWS | Cloud deployment |
| React | Frontend dashboard |
| LangChain | LLM orchestration |
| LangGraph | AI agent workflows |
| Ollama | Local LLM support |
| OpenAI API | AI-powered features |
| Vector Database | Semantic search |
| RAG | Retrieval-Augmented Generation |

---

# 🏛️ System Architecture

AI Resume Copilot follows a layered architecture where each layer has a single responsibility. This design improves maintainability, scalability, testing, and future extensibility.

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
                      AI Engine Layer
                            │
 ┌────────┬──────┬────────┬──────────┬────────────┬──────────┬──────────┬──────────┬──────────┐
 ▼        ▼      ▼        ▼          ▼            ▼          ▼          ▼          ▼
Parser    ATS   Jobs  Explainability Improvement Analytics Interview Training Copilot
                            │
                            ▼
                 Structured JSON Response
```

---

# 🔄 Resume Analysis Pipeline

Every uploaded resume is processed through multiple independent AI engines.

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
Analytics
      │
      ▼
Interview
      │
      ▼
Training
      │
      ▼
AI Copilot
      │
      ▼
API Response
```

---

# 📂 Project Structure

```text
AI_RESUME_COPILOT/

├── app/
│   ├── ai_engine/
│   │   ├── parser/
│   │   ├── ats/
│   │   ├── jobs/
│   │   ├── explainability/
│   │   ├── improvement/
│   │   ├── analytics/
│   │   ├── interview/
│   │   ├── training/
│   │   └── copilot/
│   │
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── prompts/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── tests/
│   ├── ai_engine/
│   ├── services/
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

# 📁 Repository Organization

| Directory | Responsibility |
|------------|----------------|
| app | Main FastAPI application |
| ai_engine | Independent AI engines |
| services | Business logic layer |
| api | REST API endpoints |
| schemas | Pydantic request and response models |
| tests | Automated test suite |
| uploads | Uploaded resume storage |
| deployment | Deployment resources |
| frontend | Future React application |
| docs | Project documentation |

---

# 🚀 Installation

Follow the steps below to run AI Resume Copilot locally.

---

## 📋 Prerequisites

Ensure the following software is installed.

| Software | Version |
|----------|----------|
| Python | 3.12 or later |
| Git | Latest |
| Visual Studio Code | Recommended |

Verify the installation.

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

Install the required packages.

```bash
python -m pip install -r requirements.txt
```

---

## ✔ Verify Installation

Verify the Python installation.

```bash
python --version
```

Verify installed packages.

```bash
python -m pip list
```

---

# ⚙️ Configuration

The current version requires minimal configuration and is ready for local development.

Future releases will introduce configurable integrations for databases, authentication, AI providers, cloud storage, and deployment environments.

---

## 🔑 Environment Variables

Future versions will include a `.env.example` file.

Example configuration:

```env
DATABASE_URL=

SECRET_KEY=

JWT_SECRET_KEY=

OPENAI_API_KEY=

OLLAMA_BASE_URL=

SMTP_USERNAME=

SMTP_PASSWORD=
```

---

# ▶️ Running the Project

Start the FastAPI development server.

```bash
uvicorn app.main:app --reload
```

If the application starts successfully, the console displays:

```text
INFO: Started server process
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

# 🌐 Access the Application

Open the following URL in your browser.

```text
http://127.0.0.1:8000
```

---

# 📘 Interactive API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 📂 Configuration Files

| File | Purpose |
|------|---------|
| requirements.txt | Project dependencies |
| pyproject.toml | Python project configuration |
| README.md | Project documentation |
| LICENSE | MIT License |
| .gitignore | Ignore generated files |

---

# 🔄 Development Workflow

Every feature follows the same engineering workflow to maintain consistency throughout the project.

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
Service Layer
      │
      ▼
Resume Pipeline Integration
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

The frontend is currently under development. Screenshots will be added after the React dashboard is implemented.

| Screen | Status |
|---------|--------|
| Dashboard | 🚧 Planned |
| Resume Upload | 🚧 Planned |
| Resume Analysis | 🚧 Planned |
| Analytics Dashboard | 🚧 Planned |
| Interview Dashboard | 🚧 Planned |
| Training Dashboard | 🚧 Planned |
| AI Copilot Dashboard | 🚧 Planned |

---

# 🎥 Live Demo

A production deployment and live demonstration will be available after the first stable release.

**Status:** 🚧 Coming Soon

---

# 🧠 AI Engines

AI Resume Copilot is built around independent AI engines. Each engine performs a single responsibility and produces structured output for the next stage of the processing pipeline.

This modular architecture improves maintainability, scalability, testing, and future feature development.

---

## 📄 Resume Parser

The Resume Parser is responsible for extracting structured information from uploaded resumes. It supports multiple document formats and prepares standardized data for downstream AI engines.

### Responsibilities

- Parse PDF resumes
- Parse DOCX resumes
- Clean extracted text
- Extract contact information
- Extract technical skills
- Extract education history
- Extract work experience
- Generate structured resume data

### Components

- PDF Parser
- DOCX Parser
- Text Cleaner
- Contact Parser
- Skills Parser
- Education Parser
- Experience Parser
- Resume Parser

### Input

```text
Resume File (.pdf / .docx)
```

### Output

```json
{
  "contact": {},
  "education": {},
  "experience": {},
  "skills": []
}
```

---

## 📊 ATS Engine

The ATS Engine evaluates resumes using rule-based analysis to estimate compatibility with Applicant Tracking Systems.

### Responsibilities

- Calculate ATS score
- Validate resume sections
- Evaluate keyword coverage
- Check formatting quality
- Identify improvement opportunities

### Components

- ATS Scorer
- Section Checker
- Keyword Matcher
- Formatting Checker
- Grammar Checker

### Output

```json
{
  "ats_score": 86
}
```

---

## 💼 Job Recommendation Engine

The Job Recommendation Engine predicts suitable technical roles based on detected skills and experience.

### Responsibilities

- Role prediction
- Technical role recommendation
- Skill gap identification
- Career recommendation

### Components

- Role Predictor
- Job Matcher
- Skill Gap Analyzer
- Recommendation Engine

### Output

```json
{
  "role": "Backend Developer",
  "recommendations": []
}
```

---

## 💡 Explainability Engine

The Explainability Engine generates human-readable explanations for AI-generated decisions, making recommendations easier to understand.

### Responsibilities

- Explain ATS scores
- Explain predicted roles
- Explain detected skills
- Explain recommendation results

### Components

- ATS Explanation
- Job Explanation
- Skill Explanation

### Output

```json
{
  "explanations": []
}
```

---

## 🛠 Resume Improvement Engine

The Resume Improvement Engine analyzes structured resume data and generates actionable improvement suggestions.

### Responsibilities

- Identify strengths
- Detect weaknesses
- Generate improvement suggestions
- Improve resume quality

### Components

- Strength Analyzer
- Weakness Analyzer
- Suggestion Generator
- Improvement Engine

### Output

```json
{
  "strengths": [],
  "weaknesses": [],
  "suggestions": []
}
```

---

## 📈 Analytics Engine

The Analytics Engine tracks resume performance across multiple analyses and provides historical insights.

### Responsibilities

- Track ATS score history
- Compare resume performance
- Monitor improvement trends
- Generate analytics reports

### Components

- ATS History
- Resume Comparison
- Improvement Tracker
- Analytics Engine

### Output

```json
{
  "ats_history": [],
  "average_score": 0
}
```

---

## 🎤 Interview Engine

The Interview Engine generates technical and HR interview preparation material tailored to predicted job roles.

### Responsibilities

- Generate technical interview questions
- Generate HR interview questions
- Map role aliases
- Build interview reports

### Components

- Technical Questions
- HR Questions
- Question Generator

### Output

```json
{
  "technical_questions": [],
  "hr_questions": []
}
```

---

## 🎓 Training Engine

The Training Engine creates personalized learning plans based on predicted roles and missing skills.

### Responsibilities

- Analyze missing skills
- Recommend learning resources
- Build learning roadmaps
- Track learning progress

### Components

- Skill Analyzer
- Course Recommender
- Learning Planner
- Progress Tracker
- Training Engine

### Output

```json
{
  "missing_skills": [],
  "recommended_courses": [],
  "learning_plan": [],
  "progress": {}
}
```

---

## 🤖 AI Copilot

The AI Copilot is the intelligent assistance layer of the platform. It builds on the existing AI engines and introduces LLM-ready capabilities through a provider-independent architecture.

### Current Components

- Prompt Manager
- Abstract LLM Client
- Mock LLM Client
- Resume Improver
- Resume Rewriter
- Job Description Matcher
- Career Advisor
- Cover Letter Generator
- Explanation Engine
- Copilot Service

### Current Capabilities

- AI-powered resume improvement
- Professional resume rewriting
- Resume vs Job Description matching
- Personalized career guidance
- Cover letter generation
- AI-generated explanations
- Centralized prompt management
- Provider-independent LLM architecture

### Planned Integrations

- OpenAI
- Ollama
- Gemini
- LangChain
- RAG Pipeline
- Vector Database
- Conversational Resume Assistant

---

# 🔄 Complete Processing Pipeline

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
Analytics
      │
      ▼
Interview
      │
      ▼
Training
      │
      ▼
AI Copilot
      │
      ▼
Final API Response
```

---

# 🧪 Testing

AI Resume Copilot follows a **Test-Driven Development (TDD)** approach. Every completed AI engine is accompanied by dedicated unit tests, service tests, and integration into the main resume analysis pipeline.

All automated tests are executed using **Pytest**.

---

## 📊 Current Test Status

| Metric | Value |
|---------|------:|
| Total Tests | **Update after latest test run** |
| Failed Tests | **0** |
| Warnings | **1** |

> Replace **"Update after latest test run"** with the actual number after running:
>
> ```bash
> python -m pytest
> ```

---

## 📂 Test Organization

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
│   ├── training/
│   └── copilot/
│
├── services/
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

## ▶️ Run With Verbose Output

```bash
python -m pytest -v
```

---

## ▶️ Run Individual AI Engine Tests

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

### Interview

```bash
python -m pytest tests/ai_engine/interview -v
```

### Training

```bash
python -m pytest tests/ai_engine/training -v
```

### AI Copilot

```bash
python -m pytest tests/ai_engine/copilot -v
```

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

## ▶️ Run Integration Tests

```bash
python -m pytest tests/integration -v
```

---

## ✅ Testing Coverage

The automated test suite validates the following components:

- Resume parsing
- ATS evaluation
- Job role prediction
- Resume recommendations
- Explainability engine
- Resume improvement
- Resume analytics
- Interview generation
- Training recommendations
- AI Copilot
- Prompt management
- LLM abstraction
- Service layer
- Resume pipeline integration
- API responses
- Error handling

---

# 🌐 REST API

The backend exposes REST APIs built with **FastAPI**.

---

## Available Endpoints

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/` | GET | Health check |
| `/resume/analyze` | POST | Complete resume analysis |
| `/jobs/recommend` | POST | Generate job recommendations |

> Additional AI Copilot endpoints will be introduced in a future release.

---

## Example Response

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
    "training": {},
    "copilot": {
      "resume_improvement": {},
      "career_advice": {}
    },
    "explainability": {},
    "text": "",
    "metadata": {}
  }
}
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## Error Handling

The API validates:

- Unsupported file formats
- Missing uploaded files
- Invalid request payloads
- Resume processing failures
- Invalid API requests

All endpoints return structured JSON responses for consistent frontend integration.

---

# 🗺️ Development Roadmap

AI Resume Copilot is being developed incrementally. Each milestone introduces a new AI capability while maintaining a modular and scalable architecture.

| Version | Milestone | Status |
|---------|-----------|--------|
| v0.1.0 | Initial Project Setup | ✅ Completed |
| v0.2.0 | Resume Parser | ✅ Completed |
| v0.3.0 | ATS Engine | ✅ Completed |
| v0.4.0 | Job Recommendation & Explainability | ✅ Completed |
| v0.5.0 | Resume Improvement | ✅ Completed |
| v0.6.0 | Analytics | ✅ Completed |
| v0.7.0 | Interview Engine | ✅ Completed |
| v0.8.0 | Training Engine | ✅ Completed |
| v0.9.0 | AI Copilot Foundation | 🚧 In Progress |
| v1.0.0 | AI Copilot Platform | ⏳ Planned |

---

# 🚀 Future Roadmap

The following capabilities are planned for future releases.

---

## 🤖 AI Copilot

- OpenAI Integration
- Ollama Integration
- Gemini Integration
- Claude Integration
- LangChain Integration
- LangGraph Workflows
- RAG Pipeline
- Vector Database Integration
- Resume Chat Assistant
- Resume Summary Generator
- Resume Review Assistant
- AI Career Mentor

---

## 💼 Career Intelligence

- Resume vs Job Description Matching Dashboard
- Company-Specific Resume Analysis
- Placement Readiness Score
- Resume Benchmarking
- Internship Recommendation Engine
- Career Path Prediction
- Skill Gap Visualization

---

## 📈 Analytics

- Interactive Analytics Dashboard
- Resume Performance Timeline
- ATS Trend Analysis
- Resume Version Comparison
- Historical Resume Reports
- Candidate Progress Tracking

---

## 🎤 Interview Preparation

- AI Mock Interviews
- Technical Interview Simulator
- HR Interview Simulator
- Coding Interview Preparation
- AI Feedback Generation
- Interview Performance Reports

---

## 🎓 Learning Platform

- Personalized Learning Dashboard
- Certification Tracking
- Learning Progress Analytics
- Daily Learning Plans
- Skill Mastery Reports

---

## 🔐 Platform Features

- User Authentication
- JWT Authorization
- Role-Based Access Control
- PostgreSQL Integration
- SQLAlchemy ORM
- Secure Resume Storage
- Resume Version History

---

## ☁️ Deployment

- Docker Support
- Docker Compose
- Kubernetes Deployment
- AWS Deployment
- CI/CD Pipeline
- Production Monitoring
- Logging & Observability

---

## 🖥️ Frontend

- React Dashboard
- Resume Upload Interface
- AI Copilot Dashboard
- Analytics Dashboard
- Interview Dashboard
- Training Dashboard
- User Profile
- Responsive UI

---

# 📋 Coding Standards

The project follows consistent engineering and software development practices.

## Development Principles

- Follow PEP 8
- Keep modules focused on a single responsibility
- Write reusable and modular code
- Follow layered architecture
- Maintain separation of concerns
- Prefer dependency injection where appropriate
- Avoid code duplication
- Keep business logic inside services and AI engines
- Write descriptive docstrings
- Use meaningful variable and function names
- Maintain consistent project structure

---

## Testing Principles

- Follow Test-Driven Development (TDD)
- Write unit tests for every module
- Validate service layer functionality
- Test integration between AI engines
- Keep tests deterministic and independent
- Maintain high code reliability

---

## Documentation Principles

- Document every completed feature
- Keep README synchronized with implementation
- Maintain clear project structure
- Use consistent formatting
- Update roadmap after each milestone

---

# 👨‍💻 Author

**Divesh Kate**

B.Tech in Artificial Intelligence & Machine Learning

### GitHub

https://github.com/diveshkate11-collab

### Repository

https://github.com/diveshkate11-collab/ai-resume-analyzer

---

# 🤝 Contributing

Contributions are welcome and appreciated.

If you would like to contribute to AI Resume Copilot, please follow these steps:

1. Fork the repository.
2. Create a new feature or bug-fix branch.
3. Follow the existing project architecture and coding standards.
4. Write or update tests for your changes.
5. Ensure the complete test suite passes successfully.
6. Use clear and meaningful commit messages.
7. Submit a Pull Request describing your changes.

### Contribution Guidelines

- Follow PEP 8 coding standards.
- Keep modules focused on a single responsibility.
- Preserve the layered architecture.
- Avoid unnecessary dependencies.
- Update documentation when functionality changes.
- Keep pull requests focused on a single feature or fix.

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to:

- Use the project for personal or commercial purposes.
- Modify and extend the source code.
- Distribute original or modified versions.
- Incorporate the project into your own applications.

All use is subject to the terms and conditions of the MIT License.

For complete license information, see the **LICENSE** file included in this repository.