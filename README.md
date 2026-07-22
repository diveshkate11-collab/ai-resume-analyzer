# 🚀 AI Resume Copilot

<div align="center">

### AI-Powered Resume Analysis, Career Intelligence & Interview Preparation Platform

Analyze resumes, evaluate ATS compatibility, identify skill gaps, recommend career paths, generate interview questions, create personalized learning plans, and prepare candidates for technical hiring through a modular AI-powered backend.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?logo=fastapi)
![Tests](https://img.shields.io/badge/Tests-127_Passed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active_Development-orange)

</div>

---

# 📖 Overview

AI Resume Copilot is a backend application designed to help job seekers improve their resumes and prepare for technical recruitment using Artificial Intelligence techniques and modern software engineering practices.

The platform accepts resumes in **PDF** and **DOCX** formats, extracts structured information, evaluates Applicant Tracking System (ATS) compatibility, predicts suitable technical roles, identifies missing skills, explains AI-generated decisions, recommends resume improvements, tracks resume progress, generates interview preparation material, and creates personalized learning plans.

The application follows a **modular architecture**, where each capability is implemented as an independent AI engine. This design makes the project scalable, reusable, and easier to maintain as new functionality is added.

The long-term vision is to evolve AI Resume Copilot into a complete AI-powered career assistant that supports candidates throughout the hiring journey—from resume creation to interview preparation and continuous skill development.

---

# 🎯 Objectives

The project is being developed to achieve the following goals:

- Build a production-oriented AI resume analysis platform.
- Design independent and reusable AI engines.
- Practice scalable backend development using FastAPI.
- Follow clean architecture and separation of concerns.
- Apply Test-Driven Development (TDD).
- Develop well-documented REST APIs.
- Create a portfolio-quality software engineering project.
- Gradually integrate Machine Learning and Large Language Models.
- Prepare the system for cloud deployment and production use.

---

# ✨ Current Capabilities

The platform currently provides the following capabilities:

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
| AI Copilot | Intelligent career assistant | ⏳ Planned |

---

# 🌟 Key Highlights

- Modular AI Engine Architecture
- FastAPI REST Backend
- Service-Oriented Design
- Resume Parsing Pipeline
- ATS Evaluation
- Career Recommendation Engine
- Resume Improvement System
- Resume Analytics
- Interview Preparation
- Personalized Learning Recommendations
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

AI Resume Copilot follows a layered architecture where every responsibility is isolated into its own layer.

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
 ┌─────────┬────────┬────────┬────────┬────────┬────────┬────────┬────────┐
 ▼         ▼        ▼        ▼        ▼        ▼        ▼        ▼
Parser     ATS     Jobs   Explain  Improve Analytics Interview Training
                       │
                       ▼
              Structured JSON Response
```

---

# 🔄 Resume Analysis Pipeline

The application processes every uploaded resume through a sequence of independent AI engines.

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
| schemas | Pydantic models |
| tests | Automated test suite |
| uploads | Uploaded resume storage |
| deployment | Deployment resources |
| frontend | Future React application |
| docs | Project documentation |

---

# 🚀 Installation

Follow the steps below to set up AI Resume Copilot on your local machine.

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

Install all required packages.

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

The current release requires minimal configuration.

Future releases will support configurable services such as:

- PostgreSQL Database
- Authentication
- Email Notifications
- Cloud Storage
- AI Providers
- Logging
- Environment Profiles

---

## 🔑 Environment Variables

Future versions will include a `.env.example` file.

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

If the application starts successfully, the console will display:

```text
INFO: Started server process
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

# 🌐 Access the Application

Open the following address in your browser.

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

Every new feature follows the same development process.

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
Service Integration
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

Frontend screenshots will be added after the React dashboard is implemented.

| Screen | Status |
|---------|--------|
| Dashboard | 🚧 Planned |
| Resume Upload | 🚧 Planned |
| Resume Analysis | 🚧 Planned |
| Analytics Dashboard | 🚧 Planned |
| Interview Dashboard | 🚧 Planned |
| Training Dashboard | 🚧 Planned |

---

# 🎥 Live Demo

A live demonstration will be available after the production deployment.

**Status:** 🚧 Coming Soon

---

# 🧠 AI Engines

AI Resume Copilot is built as a collection of independent AI engines. Each engine performs a single responsibility and produces structured output that becomes the input for the next stage of the pipeline.

This modular approach makes the application easier to maintain, test, and extend.

---

## 📄 Resume Parser

The Resume Parser converts uploaded resumes into structured information.

### Responsibilities

- Parse PDF resumes
- Parse DOCX resumes
- Clean extracted text
- Extract contact details
- Extract technical skills
- Extract education
- Extract experience
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

```
Resume File
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

Evaluates resume quality using rule-based analysis.

### Responsibilities

- ATS score calculation
- Resume section validation
- Technical keyword matching
- Formatting checks
- Grammar checks

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

Predicts suitable technical roles from resume skills.

### Responsibilities

- Role prediction
- Job matching
- Skill gap analysis
- Career recommendations

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

Provides human-readable explanations for AI-generated results.

### Responsibilities

- Explain ATS scores
- Explain role predictions
- Explain detected skills
- Explain missing skills

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

Generates practical recommendations to improve resume quality.

### Responsibilities

- Strength analysis
- Weakness analysis
- Improvement suggestions

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

Tracks resume improvement across multiple analyses.

### Responsibilities

- ATS history
- Resume comparison
- Progress tracking
- Analytics report generation

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

Generates interview preparation material.

### Responsibilities

- Technical interview questions
- HR interview questions
- Role alias mapping
- Interview report generation

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

Builds personalized learning recommendations.

### Responsibilities

- Skill analysis
- Course recommendation
- Learning roadmap generation
- Progress tracking

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

## 🤖 AI Copilot (Planned)

AI Copilot will become the central intelligent assistant for the platform.

Planned capabilities include:

- Resume chat assistant
- Resume review
- Resume rewriting
- Resume summarization
- Resume vs Job Description matching
- Career guidance
- Interview coaching
- LLM integration
- RAG pipeline

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
Final API Response
```

--- 

# 🧪 Testing

AI Resume Copilot follows a **Test-Driven Development (TDD)** approach. Every completed AI engine is accompanied by dedicated unit tests, service tests, and integration into the main resume analysis pipeline.

All tests are executed using **Pytest**.

---

## 📊 Current Test Status

| Metric | Value |
|---------|------:|
| Total Tests | **127 Passed** |
| Failed Tests | **0** |
| Warnings | **1** |

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
│   └── training/
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

## ✅ Testing Coverage

The automated test suite verifies:

- Resume parsing
- ATS evaluation
- Job role prediction
- Skill gap analysis
- Resume improvement
- Resume analytics
- Interview generation
- Training recommendations
- Service layer
- API responses
- Integration workflow
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
        "interview": {},
        "training": {},
        "explainability": {},
        "text": "",
        "metadata": {}
    }
}
```

---

## API Documentation

FastAPI automatically generates interactive documentation.

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
- Processing failures

All endpoints return structured JSON responses for consistent frontend integration.

---

# 🗺️ Development Roadmap

The project is developed incrementally, with each milestone introducing new capabilities while preserving the modular architecture.

| Version | Milestone | Status |
|---------|-----------|--------|
| v0.1.0 | Initial Project Setup | ✅ Completed |
| v0.2.0 | Resume Parser | ✅ Completed |
| v0.3.0 | ATS Engine | ✅ Completed |
| v0.4.0 | Job Recommendation & Explainability | ✅ Completed |
| v0.5.0 | Resume Improvement | ✅ Completed |
| v0.6.0 | Analytics | ✅ Completed |
| v0.7.0 | Interview | ✅ Completed |
| v0.8.0 | Training | ✅ Completed |
| v1.0.0 | AI Copilot | ⏳ Planned |

---

# 🚀 Future Work

The following enhancements are planned after the AI Copilot module is completed:

- Authentication & User Accounts
- PostgreSQL Integration
- SQLAlchemy ORM
- Docker Support
- Kubernetes Deployment
- AWS Deployment
- React Frontend
- CI/CD Pipeline
- Production Monitoring
- Cloud Storage Integration

---

# 📋 Coding Standards

This project follows the following development principles:

- Follow PEP 8
- Write modular, reusable code
- Keep functions focused on a single responsibility
- Prefer composition over duplication
- Add tests for every new feature
- Keep business logic inside services and AI engines
- Maintain clear project structure

---

# 👨‍💻 Author

**Divesh Kate**

B.Tech Artificial Intelligence & Machine Learning 

### GitHub

https://github.com/diveshkate11-collab

### Repository

https://github.com/diveshkate11-collab/ai-resume-analyzer

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve AI Resume Copilot:

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Add or update tests where necessary.
5. Ensure the complete test suite passes.
6. Commit using meaningful commit messages.
7. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, distribute, and study the source code under the terms of the MIT License.

See the **LICENSE** file for complete details.

---

<div align="center">

### ⭐ If you find this project useful, consider giving it a star on GitHub.

Thank you for visiting **AI Resume Copilot**.

</div>