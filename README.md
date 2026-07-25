# 🚀 AI Resume Copilot

<div align="center">

### AI-Powered Resume Analysis, Career Intelligence & Interview Preparation Platform

Analyze resumes, evaluate ATS compatibility, identify skill gaps, recommend career paths, generate interview questions, create personalized learning plans, and provide AI-powered resume assistance through a modular backend architecture.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?logo=fastapi)
![Tests](https://img.shields.io/badge/Tests-153_Passed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active_Development-orange)

</div>

---

# 📖 Overview

AI Resume Copilot is a modular backend platform that helps job seekers analyze resumes, improve ATS compatibility, identify missing skills, receive career recommendations, prepare for interviews, generate personalized learning plans, and leverage AI-assisted resume guidance.

The application accepts resumes in **PDF** and **DOCX** formats, extracts structured information, evaluates Applicant Tracking System (ATS) compatibility, predicts suitable technical roles, recommends resume improvements, tracks resume progress, generates interview preparation material, creates learning roadmaps, and provides an extensible AI Copilot layer through REST APIs.

The platform follows a modular architecture where every capability is implemented as an independent AI engine. This separation of responsibilities improves maintainability, testing, scalability, and future extensibility.

The AI Copilot module now follows a **provider-independent LLM architecture** using centralized configuration and the Factory design pattern, allowing different AI providers to be integrated without modifying business logic.

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
- Design extensible AI provider integration using the Factory Pattern.
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
| AI Copilot | AI-powered resume assistance with REST API integration | ✅ |
| Provider-Based LLM Architecture | Dynamic AI provider selection | ✅ |

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
- AI Copilot Module
- AI Copilot REST API
- Provider-Independent LLM Architecture
- LLM Factory Pattern
- Centralized LLM Configuration
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
| Abstract LLM Client | Common interface for AI providers |
| Mock LLM Client | Development and testing |
| Ollama LLM Client | Local LLM provider integration (Architecture Ready) |
| LLM Factory | Dynamic AI provider selection |
| Centralized LLM Settings | Provider configuration management |

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

The AI Copilot module adopts a provider-independent architecture where business logic communicates with an abstract LLM interface instead of a specific AI provider.

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
 ┌────────┬──────┬────────┬────────────┬────────────┬──────────┬──────────┬──────────┬──────────┐
 ▼        ▼      ▼        ▼            ▼            ▼          ▼          ▼          ▼
Parser    ATS   Jobs  Explainability Improvement Analytics Interview Training Copilot
                            │
                            ▼
                    Structured JSON Response
```

---

# 🤖 AI Provider Architecture

The AI Copilot follows a provider-based architecture that separates AI providers from application logic. Business modules communicate only with the abstract client interface while the factory dynamically selects the configured provider.

```text
                 Copilot Services
                        │
                        ▼
                  LLM Factory
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
 Mock LLM Client               Ollama LLM Client
        │                               │
        └───────────────┬───────────────┘
                        ▼
                  LLM Client Interface
```

---

# ⚙️ LLM Configuration Flow

Application-wide AI configuration is centralized so the provider can be changed without modifying business logic.

```text
settings.py
      │
      ▼
LLM Provider Configuration
      │
      ▼
LLM Factory
      │
      ▼
Selected AI Provider
      │
      ▼
Copilot Services
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
REST API
      │
      ▼
Final API Response
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
│   │       ├── llm_client.py
│   │       ├── ollama_client.py
│   │       ├── llm_factory.py
│   │       ├── prompt_manager.py
│   │       ├── resume_improver.py
│   │       ├── resume_rewriter.py
│   │       ├── career_advisor.py
│   │       ├── cover_letter.py
│   │       ├── jd_matcher.py
│   │       └── explanation_engine.py
│   │
│   ├── api/
│   ├── core/
│   │   └── settings.py
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
| copilot | AI Copilot module and LLM provider layer |
| services | Business logic layer |
| api | REST API endpoints |
| core | Centralized application configuration |
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

The AI Copilot now uses centralized application settings to manage AI provider selection. Future releases will extend this configuration to support multiple AI providers, cloud services, databases, authentication, and deployment environments.

---

## 🤖 Current LLM Configuration

The project currently supports a configurable provider architecture.

```text
Provider : Mock LLM
Architecture : Provider Independent
Selection : LLM Factory
Configuration : app/core/settings.py
```

Future versions will allow switching providers by changing the application configuration instead of modifying business logic.

---

## 🔑 Future Environment Variables

Future releases will move application configuration into environment variables.

Example:

```env
LLM_PROVIDER=ollama

LLM_MODEL=llama3.2

LLM_TEMPERATURE=0.3

LLM_TIMEOUT=60

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
| app/core/settings.py | Centralized application configuration |
| app/ai_engine/copilot/llm_factory.py | Dynamic LLM provider selection |
| app/ai_engine/copilot/llm_client.py | Abstract LLM interface |
| app/ai_engine/copilot/ollama_client.py | Ollama provider implementation |

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
API Integration
      │
      ▼
LLM Provider Integration
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

The AI Copilot is the intelligent assistance layer of AI Resume Copilot. It extends the resume analysis pipeline by providing AI-powered resume enhancement, career guidance, job description matching, resume rewriting, cover letter generation, and explainability.

The Copilot module is designed using a **provider-independent architecture**, allowing different Large Language Model (LLM) providers to be integrated without changing the business logic.

---

### Architecture Overview

The Copilot follows the Factory Pattern for provider selection.

```text
                  Copilot Services
                         │
                         ▼
                   LLM Factory
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
   Mock LLM Client              Ollama LLM Client
          │                             │
          └──────────────┬──────────────┘
                         ▼
                  LLM Client Interface
```

---

### Current Components

- Prompt Manager
- Abstract LLM Client
- Mock LLM Client
- Ollama LLM Client
- LLM Factory
- Centralized LLM Settings
- Resume Improver
- Resume Rewriter
- Job Description Matcher
- Career Advisor
- Cover Letter Generator
- Explanation Engine
- Copilot Service
- REST API

---

### Current Capabilities

- AI-powered resume improvement
- Professional resume rewriting
- Resume vs Job Description matching
- Personalized career guidance
- Cover letter generation
- AI-generated explanations
- REST API endpoints
- Centralized prompt management
- Provider-based LLM architecture
- Dynamic AI provider selection
- Centralized LLM configuration

---

### Current Provider

| Component | Status |
|-----------|--------|
| Mock LLM Client | ✅ Active |
| Ollama Client | 🚧 Architecture Ready |
| OpenAI | ⏳ Planned |
| Gemini | ⏳ Planned |
| Claude | ⏳ Planned |

---

### LLM Configuration

The active AI provider is selected from a centralized configuration.

```text
settings.py
      │
      ▼
LLM Provider
      │
      ▼
LLM Factory
      │
      ▼
Selected Provider
      │
      ▼
Copilot Modules
```

Changing the provider only requires updating the application configuration. The Copilot modules remain unchanged because they communicate through the abstract LLM interface.

---

### Current Workflow

```text
Client Request
      │
      ▼
REST API
      │
      ▼
Copilot Service
      │
      ▼
Prompt Manager
      │
      ▼
LLM Factory
      │
      ▼
Selected AI Provider
      │
      ▼
Generated Response
```

---

### Provider Selection Flow

```text
Application Starts
        │
        ▼
Load Settings
        │
        ▼
Read LLM Provider
        │
        ▼
LLM Factory
        │
 ┌──────┴─────────┐
 ▼                ▼
Mock          Ollama
        │
        ▼
Return LLM Client
```

---

### Design Principles

- Provider-independent architecture
- Factory Pattern
- Dependency Injection
- Single Responsibility Principle
- Open/Closed Principle
- Centralized configuration
- Extensible AI provider integration
- Modular service design

---

### Planned Integrations

- OpenAI API
- Ollama Local Models
- Google Gemini
- Anthropic Claude
- LangChain
- LangGraph
- RAG Pipeline
- Vector Database
- Resume Chat Assistant
- Resume Summary Generator
- AI Interview Coach
- AI Career Mentor
- Multi-provider fallback support
- Streaming AI responses

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
REST API
      │
      ▼
Final API Response
```

---

# 🧪 Testing

AI Resume Copilot follows a **Test-Driven Development (TDD)** approach. Every completed AI engine, service, API endpoint, and Copilot component is validated through automated testing.

The project currently includes unit tests, API tests, service tests, and integration tests executed using **Pytest**.

---

## 📊 Current Test Status

| Metric | Value |
|---------|------:|
| Total Tests | **153 Passed** |
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

The automated test suite validates:

- Resume parsing
- ATS evaluation
- Job recommendation
- Explainability engine
- Resume improvement
- Resume analytics
- Interview generation
- Training recommendations
- AI Copilot services
- AI Copilot REST APIs
- Prompt management
- LLM abstraction layer
- LLM Factory
- Provider selection
- Centralized settings
- Service layer
- Resume analysis pipeline
- API request validation
- API responses
- Error handling

---

# 🌐 REST API

AI Resume Copilot exposes RESTful APIs built with **FastAPI**. Each endpoint is responsible for a specific feature and returns structured JSON responses suitable for frontend or third-party integration.

---

## Available Endpoints

### Core APIs

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/` | GET | Health Check |
| `/resume/analyze` | POST | Complete Resume Analysis |
| `/jobs/recommend` | POST | Generate Job Recommendations |

---

### AI Copilot APIs

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/copilot/improve` | POST | Generate Resume Improvement Suggestions |
| `/copilot/rewrite` | POST | Rewrite Resume Professionally |
| `/copilot/job-match` | POST | Compare Resume with Job Description |
| `/copilot/career-advice` | POST | Generate Personalized Career Guidance |
| `/copilot/cover-letter` | POST | Generate Professional Cover Letter |
| `/copilot/explain` | POST | Explain AI-generated Recommendations |

---

## API Architecture

```text
Client
   │
   ▼
FastAPI Router
   │
   ▼
Request Validation
(Pydantic)
   │
   ▼
Copilot Service
   │
   ▼
Prompt Manager
   │
   ▼
LLM Factory
   │
   ▼
Selected AI Provider
   │
   ▼
JSON Response
```

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

## Request Validation

All endpoints use **Pydantic** models for request validation.

Validation includes:

- Required field validation
- Data type validation
- Request body validation
- Automatic HTTP `422 Unprocessable Entity` responses for invalid requests
- Schema-based AI Copilot request validation

---

## Error Handling

The API validates and handles:

- Unsupported file formats
- Missing uploaded files
- Invalid request payloads
- Missing required fields
- Resume processing failures
- Invalid API requests
- Unsupported LLM providers
- Internal processing errors

All endpoints return structured JSON responses for consistent frontend integration.

---

# 🗺️ Development Roadmap

AI Resume Copilot is being developed incrementally. Each milestone introduces new capabilities while preserving the modular architecture, maintaining backward compatibility, and improving AI extensibility.

| Version | Milestone | Status |
|---------|-----------|--------|
| v0.1.0 | Initial Project Setup | ✅ Completed |
| v0.2.0 | Resume Parser | ✅ Completed |
| v0.3.0 | ATS Engine | ✅ Completed |
| v0.4.0 | Job Recommendation & Explainability | ✅ Completed |
| v0.5.0 | Resume Improvement | ✅ Completed |
| v0.6.0 | Analytics Engine | ✅ Completed |
| v0.7.0 | Interview Engine | ✅ Completed |
| v0.8.0 | Training Engine | ✅ Completed |
| v0.9.0 | AI Copilot Backend & REST APIs | ✅ Completed |
| v0.9.5 | Provider-Based LLM Architecture | ✅ Completed |
| v1.0.0 | Real Ollama Integration | 🚧 Next Milestone |

---

# 🚀 Future Roadmap

The following enhancements are planned for future releases.

---

## 🤖 AI Copilot

- Real Ollama Integration
- OpenAI Integration
- Google Gemini Integration
- Anthropic Claude Integration
- LangChain Integration
- LangGraph Workflows
- RAG Pipeline
- Vector Database Integration
- Multi-provider AI Support
- Automatic Provider Selection
- AI Response Streaming
- Resume Chat Assistant
- Resume Summary Generator
- Resume Review Assistant
- AI Career Mentor

---

## 💼 Career Intelligence

- Resume vs Job Description Dashboard
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
- JWT Authentication
- Role-Based Access Control
- PostgreSQL Integration
- SQLAlchemy ORM
- Resume History
- Secure Resume Storage
- User Dashboard
- Resume Version Management

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
- Resume Upload Portal
- Resume Analysis Dashboard
- AI Copilot Dashboard
- Analytics Dashboard
- Interview Dashboard
- Training Dashboard
- User Profile
- Responsive User Interface

---

# 📋 Coding Standards

AI Resume Copilot follows modern software engineering practices to ensure maintainability, scalability, extensibility, and code quality.

---

## Development Principles

- Follow PEP 8
- Apply the Single Responsibility Principle
- Follow the Open/Closed Principle
- Write reusable and modular components
- Follow layered architecture
- Maintain separation of concerns
- Keep business logic inside services and AI engines
- Prefer dependency injection where appropriate
- Use the Factory Pattern for provider selection
- Centralize application configuration
- Design components for provider independence
- Avoid code duplication
- Write descriptive docstrings
- Use meaningful naming conventions
- Keep the project structure consistent

---

## AI Architecture Principles

- Provider-independent LLM architecture
- Abstract AI provider interface
- Factory-based provider selection
- Centralized AI configuration
- Extensible provider integration
- Replaceable AI backends
- Modular Copilot services
- Scalable AI architecture

---

## Testing Principles

- Follow Test-Driven Development (TDD)
- Write unit tests for every new module
- Validate service layer functionality
- Test REST API endpoints
- Test integration between AI engines
- Test provider selection logic
- Keep tests deterministic and independent
- Maintain high code reliability

---

## Documentation Principles

- Keep documentation synchronized with implementation
- Document every completed feature
- Maintain a consistent README structure
- Update API documentation after new endpoints
- Update architecture diagrams after structural changes
- Update the development roadmap after every milestone

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
2. Create a feature or bug-fix branch.
3. Follow the existing project architecture and coding standards.
4. Write or update tests for your changes.
5. Ensure the complete test suite passes successfully.
6. Use clear and meaningful commit messages.
7. Submit a Pull Request describing your changes.

---

## Contribution Guidelines

- Follow PEP 8 coding standards.
- Keep modules focused on a single responsibility.
- Follow the layered architecture.
- Maintain provider-independent AI integration.
- Use the Factory Pattern for new AI providers.
- Keep configuration centralized.
- Preserve dependency injection where applicable.
- Write clean, reusable, and maintainable code.
- Add tests for newly introduced functionality.
- Ensure all tests pass before opening a Pull Request.
- Update documentation whenever implementation changes.
- Keep pull requests focused on a single feature or bug fix.

---

## Contributing Workflow

```text
Fork Repository
       │
       ▼
Create Feature Branch
       │
       ▼
Implement Feature
       │
       ▼
Run Tests
       │
       ▼
Update Documentation
       │
       ▼
Commit Changes
       │
       ▼
Push Branch
       │
       ▼
Open Pull Request
```

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

---

<div align="center">

### ⭐ If you find this project useful, consider giving it a star on GitHub.

**AI Resume Copilot** is continuously evolving with new AI capabilities, provider integrations, and production-ready features.

Thank you for visiting the project!

</div>