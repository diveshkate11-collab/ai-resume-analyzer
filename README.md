# 🤖 AI Resume Copilot

> An AI-powered backend application that helps job seekers analyze, improve, and optimize resumes using Artificial Intelligence and Large Language Models (LLMs).

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-154%20Passed-success?style=for-the-badge)
![AI](https://img.shields.io/badge/AI-Ollama-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

---

# 📖 Overview

AI Resume Copilot is a modular backend application built with **FastAPI** that leverages **Large Language Models (LLMs)** to assist job seekers throughout the recruitment process. It provides resume analysis, ATS evaluation, AI-powered resume rewriting, career guidance, interview preparation, and personalized learning recommendations.

The project follows clean software engineering principles, including modular architecture, provider abstraction, dependency injection, centralized prompt management, and automated testing. AI providers can be switched without changing business logic, making the application easy to maintain and extend.

Currently, the project integrates with **Ollama** using the **Llama 3.2** model for local AI inference while supporting a mock provider for testing.

---

# ✨ Features

## 📄 Resume Intelligence

- Resume Parsing
- ATS Analysis
- Resume Improvement
- Resume Rewriting
- Explainability

## 🤖 AI Copilot

- Career Advisor
- Cover Letter Generator
- Resume Rewriter
- Resume Improver
- Job Description Matcher
- Explanation Engine

## 🧠 AI Infrastructure

- Prompt Manager
- LLM Factory
- Provider-Based Architecture
- Ollama Integration
- Mock Provider
- Shared Response Parser

## 🚀 Additional AI Engines

- Resume Analytics
- Interview Preparation
- Job Recommendation
- Training Recommendation

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Backend | Python, FastAPI, Uvicorn, Pydantic |
| AI | Ollama, Llama 3.2 |
| Document Processing | PyPDF2, python-docx |
| Testing | Pytest, HTTPX |
| Development | Git, GitHub, VS Code |

---

# 📊 Project Status

| Component | Status |
|-----------|--------|
| Resume Parser | ✅ Completed |
| AI Engines | ✅ Completed |
| AI Copilot | ✅ Completed |
| Ollama Integration | ✅ Completed |
| Provider Architecture | ✅ Completed |
| Response Parser | ✅ Completed |
| Automated Tests | ✅ 154 Passed |

---

# 🎯 Project Goals

- Build a production-inspired AI backend.
- Improve resumes using AI-powered analysis.
- Support multiple LLM providers through a common interface.
- Maintain clean, modular, and scalable architecture.
- Demonstrate backend engineering and AI integration skills.

---

# 📁 Project Structure

```text
AI-Resume-Copilot/
│
├── app/
│   ├── ai_engine/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   └── main.py
│
├── tests/
├── requirements.txt
├── README.md
└── .env
```

---

# 🌟 Highlights

- ✅ Modular AI architecture
- ✅ Local LLM support with Ollama
- ✅ Provider abstraction for multiple AI models
- ✅ Centralized prompt management
- ✅ Shared AI response parser
- ✅ RESTful API with FastAPI
- ✅ Automated testing (**154 passing tests**)
- ✅ Clean and scalable project structure

---

# ⚙️ Installation & Setup

Follow these steps to run AI Resume Copilot locally.

---

# 📋 Prerequisites

Install the following software before starting:

| Software | Version |
|----------|---------|
| Python | 3.11+ |
| Git | Latest |
| Ollama | Latest |
| pip | Latest |
| VS Code | Recommended |

Supported Operating Systems:

- Windows
- Linux
- macOS

---

# 📥 Clone the Repository

```bash
git clone https://github.com/your-username/AI-Resume-Copilot.git

cd AI-Resume-Copilot
```

---

# 🐍 Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Main dependencies:

- FastAPI
- Uvicorn
- Pydantic
- PyPDF2
- python-docx
- Requests
- Pytest
- HTTPX

---

# 🤖 Install Ollama

Download and install the latest version of **Ollama**.

Verify installation:

```bash
ollama --version
```

---

# 📥 Download the AI Model

Pull the **Llama 3.2** model:

```bash
ollama pull llama3.2
```

Verify the model:

```bash
ollama list
```

Expected output:

```text
NAME
llama3.2:latest
```

---

# 🚀 Test Ollama

Run the model:

```bash
ollama run llama3.2
```

Example:

```text
>>> Hello

Hello! How can I help you today?
```

If you receive a response, Ollama is configured correctly.

---

# ⚙️ Configure AI Provider

Open:

```text
app/core/settings.py
```

Set the provider:

```python
LLM_PROVIDER = "ollama"
```

Available providers:

| Provider | Purpose |
|----------|---------|
| mock | Unit Testing |
| ollama | Local AI |

---

# ▶️ Run the Application

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

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

# 🧪 Running Tests

Run the complete test suite:

```bash
python -m pytest
```

Current Status:

```text
154 Passed
```

Run only Copilot tests:

```bash
python -m pytest tests/ai_engine/copilot -v
```

---

# 📂 Important Files

| File | Purpose |
|------|---------|
| `main.py` | FastAPI Entry Point |
| `settings.py` | Application Configuration |
| `requirements.txt` | Project Dependencies |
| `README.md` | Project Documentation |

---

# 🔧 Troubleshooting

### Ollama Not Found

```bash
ollama --version
```

Reinstall Ollama if the command is unavailable.

---

### Model Missing

```bash
ollama pull llama3.2
```

---

### API Not Starting

Restart FastAPI:

```bash
uvicorn app.main:app --reload
```

---

### Tests Failing

Run:

```bash
python -m pytest
```

If failures occur, verify:

- Virtual environment is activated
- Dependencies are installed
- Ollama is configured correctly

---

# 🧠 AI Engines

The AI Engine layer contains the core business logic of AI Resume Copilot. Each engine is designed with a **single responsibility**, making the project modular, maintainable, and easy to extend.

---

# 📄 Resume Parser

Extracts text from uploaded **PDF** and **DOCX** resumes.

### Responsibilities

- Read uploaded resumes
- Extract textual content
- Clean formatting
- Return structured text

### Workflow

```text
Resume Upload
      │
      ▼
PDF / DOCX Reader
      │
      ▼
Text Extraction
      │
      ▼
Structured Resume Text
```

**Example Response**

```json
{
    "success": true,
    "text": "Extracted resume content..."
}
```

---

# 📊 ATS Engine

Evaluates resume compatibility with Applicant Tracking Systems (ATS).

### Features

- ATS Score
- Keyword Analysis
- Skill Matching
- Improvement Suggestions

### Workflow

```text
Resume
   │
   ▼
Keyword Analysis
   │
   ▼
Score Generation
   │
   ▼
Recommendations
```

**Example Response**

```json
{
    "success": true,
    "score": 87,
    "recommendations": [
        "Add measurable achievements",
        "Include more technical keywords"
    ]
}
```

---

# 💼 Job Recommendation Engine

Analyzes resume skills and recommends suitable career paths.

### Features

- Skill Analysis
- Career Suggestions
- Technology Recommendations
- Growth Guidance

**Example Response**

```json
{
    "success": true,
    "recommended_roles": [
        "Backend Developer",
        "Machine Learning Engineer",
        "Data Analyst"
    ]
}
```

---

# 🔍 Explainability Engine

Converts AI-generated results into clear, human-readable explanations.

### Features

- Explain ATS Scores
- Explain Recommendations
- Identify Strengths
- Highlight Weaknesses

**Example Response**

```json
{
    "success": true,
    "explanation": "Your resume scores well due to relevant technical skills and project experience."
}
```

---

# ✨ Resume Improvement Engine

Provides AI-powered suggestions to strengthen resume content.

### Features

- Improve wording
- Recommend stronger achievements
- Detect missing skills
- Enhance readability

**Example Response**

```json
{
    "success": true,
    "suggestions": [
        "Use action verbs",
        "Quantify achievements",
        "Expand project descriptions"
    ]
}
```

---

# 📈 Analytics Engine

Generates insights from resume data.

### Features

- Skill Statistics
- ATS Analytics
- Experience Summary
- Resume Metrics

**Example Response**

```json
{
    "success": true,
    "analytics": {
        "technical_skills": 18,
        "projects": 5,
        "ats_score": 89
    }
}
```

---

# 🎤 Interview Engine

Creates personalized interview questions based on the resume.

### Features

- Technical Questions
- HR Questions
- Project-Based Questions
- Resume Discussions

**Example Response**

```json
{
    "success": true,
    "questions": [
        "Explain your FastAPI architecture.",
        "Describe your machine learning workflow."
    ]
}
```

---

# 📚 Training Engine

Generates personalized learning recommendations.

### Features

- Learning Roadmaps
- Skill Gap Analysis
- Technology Recommendations
- Career Planning

**Example Response**

```json
{
    "success": true,
    "learning_plan": [
        "Advanced FastAPI",
        "Docker",
        "System Design"
    ]
}
```

---

# 🔗 AI Engine Workflow

```text
Resume Upload
      │
      ▼
Resume Parser
      │
      ▼
ATS Engine
      │
      ├──────────────┐
      ▼              ▼
Analytics      Job Recommendation
      │              │
      ├──────────────┤
      ▼
Resume Improvement
      │
      ▼
Explainability
      │
      ▼
Interview & Training
```

Each engine is independent, making it easy to add new features without affecting existing modules.

---

# 🤖 AI Copilot

The AI Copilot layer provides AI-powered features for resume enhancement, career guidance, and job preparation. Each module focuses on a single task while sharing the same AI provider architecture.

---

# 📝 Resume Rewriter

Rewrites resume content to improve professionalism while preserving the original meaning.

### Features

- Professional wording
- Grammar correction
- ATS-friendly writing
- Better readability

**Example Response**

```json
{
    "success": true,
    "feature": "resume_rewriter",
    "response": "Professional version of the resume..."
}
```

---

# ✨ Resume Improver

Analyzes resumes and suggests targeted improvements instead of rewriting the entire document.

### Features

- Improve achievements
- Better action verbs
- Missing skills
- Content enhancement

**Example Response**

```json
{
    "success": true,
    "feature": "resume_improver",
    "response": [
        "Add measurable achievements",
        "Improve project descriptions"
    ]
}
```

---

# 📄 Cover Letter Generator

Generates professional cover letters based on resume information, company, and job role.

### Features

- Personalized content
- Professional formatting
- Company-specific writing
- Role-focused cover letters

**Example Response**

```json
{
    "success": true,
    "feature": "cover_letter",
    "response": "Generated cover letter..."
}
```

---

# 💼 Career Advisor

Provides AI-generated career guidance based on resume content.

### Features

- Career path recommendations
- Skills to learn
- Certification suggestions
- Next career steps

**Example Response**

```json
{
    "success": true,
    "feature": "career_advisor",
    "response": {
        "career_path": "Backend Developer",
        "skills_to_learn": [
            "Docker",
            "System Design"
        ],
        "certifications": [
            "AWS Cloud Practitioner"
        ],
        "next_steps": [
            "Build production projects",
            "Apply for internships"
        ]
    }
}
```

---

# 📑 Job Description Matcher

Compares resumes against job descriptions to identify compatibility.

### Features

- Match percentage
- Missing skills
- Resume improvement suggestions
- Skill comparison

**Example Response**

```json
{
    "success": true,
    "feature": "jd_matcher",
    "response": {
        "match_percentage": 82,
        "missing_skills": [
            "Docker",
            "Kubernetes"
        ]
    }
}
```

---

# 🔍 Explanation Engine

Converts AI-generated results into simple, easy-to-understand explanations.

### Features

- Human-readable summaries
- Better transparency
- Clear recommendations
- Improved understanding

**Example Response**

```json
{
    "success": true,
    "feature": "explanation_engine",
    "response": "Your resume is strong in backend development but can be improved by adding measurable achievements and cloud experience."
}
```

---

# 🔄 AI Copilot Workflow

```text
Client Request
      │
      ▼
FastAPI Endpoint
      │
      ▼
Copilot Module
      │
      ▼
Prompt Manager
      │
      ▼
LLM Factory
      │
      ▼
Selected Provider
      │
      ▼
Ollama / Mock
      │
      ▼
Response Parser
      │
      ▼
Structured JSON Response
```

---

# ✅ Current AI Copilot Features

| Feature | Status |
|---------|--------|
| Resume Rewriter | ✅ Completed |
| Resume Improver | ✅ Completed |
| Cover Letter Generator | ✅ Completed |
| Career Advisor | ✅ Completed |
| Job Description Matcher | ✅ Completed |
| Explanation Engine | ✅ Completed |
| Ollama Integration | ✅ Completed |
| Shared Response Parser | ✅ Completed |


The AI Copilot follows a modular architecture where every feature uses a common **PromptManager**, **LLMFactory**, and **ResponseParser**. This design minimizes code duplication, simplifies maintenance, and allows new AI providers or Copilot modules to be added with minimal changes.

---

# 🏗️ AI Architecture

AI Resume Copilot follows a modular and provider-based architecture. Business logic is separated from AI providers, allowing the application to switch between different LLMs without changing the core implementation.

---

# 🧠 Prompt Manager

The **PromptManager** centralizes all AI prompts used throughout the application.

### Responsibilities

- Centralized prompt templates
- Reusable prompts
- Consistent AI instructions
- Easier maintenance

Instead of embedding prompts inside multiple modules, every Copilot feature retrieves its prompt from a single location.

---

# 🏭 LLM Factory

The **LLMFactory** creates the appropriate AI client based on the application configuration.

Current providers:

- MockLLMClient
- OllamaLLMClient

Future providers:

- OpenAI
- Google Gemini
- Anthropic Claude
- Azure OpenAI

### Factory Workflow

```text
Application
      │
      ▼
 LLM Factory
      │
      ├───────────────┐
      ▼               ▼
 Mock Provider   Ollama Provider
      │               │
      └───────┬───────┘
              ▼
        AI Response
```

---

# 🔌 Provider Architecture

Every AI provider follows the same interface.

```text
          LLM Client
              │
      ┌───────┴────────┐
      ▼                ▼
MockLLMClient   OllamaLLMClient
```

This abstraction allows providers to be replaced without modifying business logic.

---

# 🤖 Ollama Integration

The project integrates **Ollama** for running Large Language Models locally.

Current Model:

```text
llama3.2
```

### Benefits

- Local AI execution
- No API costs
- Offline support
- Better privacy
- Easy provider switching

---

# 📦 Response Parser

The **ResponseParser** converts raw AI responses into structured Python objects.

### Responsibilities

- Parse JSON responses
- Handle invalid JSON safely
- Return Python dictionaries
- Centralize response parsing

Instead of each Copilot module handling JSON parsing individually, all modules now use a shared parser.

```text
AI Response
     │
     ▼
ResponseParser
     │
     ▼
Python Object
```

---

# 🔄 Complete AI Workflow

```text
Client Request
      │
      ▼
FastAPI Endpoint
      │
      ▼
Copilot Module
      │
      ▼
PromptManager
      │
      ▼
LLMFactory
      │
      ▼
Selected Provider
      │
      ▼
Ollama / Mock
      │
      ▼
ResponseParser
      │
      ▼
Structured JSON Response
```

---

# 🏛️ Design Principles

The project follows several software engineering principles:

- Single Responsibility Principle (SRP)
- Separation of Concerns
- Dependency Injection
- Factory Pattern
- Provider Abstraction
- Reusable Components
- Modular Architecture

---

# 🚀 Advantages

- Clean and maintainable code
- Easy to add new AI providers
- Minimal code duplication
- Consistent AI responses
- Simplified testing
- Scalable architecture
- Production-ready design


This architecture enables AI Resume Copilot to support multiple language models while keeping the application modular, testable, and easy to extend.

---

# 🌐 REST API

AI Resume Copilot exposes RESTful APIs built with **FastAPI**. All endpoints accept and return **JSON**, making integration with web and mobile applications straightforward.

---

# 📚 API Documentation

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

# 📄 API Endpoints

## Resume Parser

```http
POST /parser/parse
```

Extracts text from uploaded PDF or DOCX resumes.

---

## ATS Analysis

```http
POST /ats/analyze
```

Calculates ATS score and provides resume recommendations.

---

## Job Recommendation

```http
POST /recommendation/jobs
```

Suggests suitable job roles based on resume skills.

---

## Explainability

```http
POST /explainability/explain
```

Explains AI-generated scores and recommendations.

---

## Resume Improvement

```http
POST /resume-improver/improve
```

Provides suggestions to strengthen resume content.

---

## Analytics

```http
POST /analytics/analyze
```

Generates resume statistics and insights.

---

## Interview Preparation

```http
POST /interview/questions
```

Creates personalized interview questions.

---

## Training Recommendation

```http
POST /training/recommend
```

Generates personalized learning roadmaps.

---

# 🤖 AI Copilot APIs

## Resume Rewriter

```http
POST /copilot/rewrite-resume
```

Professionally rewrites resume content.

---

## Resume Improver

```http
POST /copilot/improve-resume
```

Suggests improvements without rewriting the entire resume.

---

## Cover Letter Generator

```http
POST /copilot/cover-letter
```

Generates professional cover letters.

---

## Career Advisor

```http
POST /copilot/career-advice
```

Provides AI-powered career guidance.

---

## Job Description Matcher

```http
POST /copilot/jd-match
```

Compares resumes against job descriptions.

---

## Explanation Engine

```http
POST /copilot/explain
```

Simplifies AI-generated outputs into human-readable explanations.

---

# 🔄 API Workflow

```text
Client
   │
   ▼
FastAPI Route
   │
   ▼
Request Validation
   │
   ▼
Business Logic
   │
   ▼
AI Engine
   │
   ▼
LLM Provider
   │
   ▼
Response Parser
   │
   ▼
JSON Response
```

---

# ✅ Standard Success Response

```json
{
    "success": true,
    "feature": "career_advisor",
    "response": {}
}
```

---

# ❌ Error Response

```json
{
    "detail": [
        {
            "loc": ["body"],
            "msg": "Field required",
            "type": "missing"
        }
    ]
}
```

---

# 📌 HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 404 | Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# 🔒 Validation

The API uses **Pydantic** models for request validation, ensuring:

- Required fields
- Correct data types
- Consistent JSON responses
- Automatic error handling


The REST API follows a consistent design across all modules, making it easy to integrate with frontend applications while maintaining clean architecture and predictable responses.

---

# 🧪 Testing & Development

AI Resume Copilot follows a **test-driven and modular development approach**. Automated testing ensures that new features do not break existing functionality.

---

# 📊 Test Status

| Category | Status |
|----------|--------|
| Total Tests | ✅ 154 Passed |
| Unit Tests | ✅ Passed |
| API Tests | ✅ Passed |
| AI Engine Tests | ✅ Passed |
| AI Copilot Tests | ✅ Passed |
| Ollama Tests | ✅ Passed |

---

# 🧩 Testing Strategy

The project includes multiple testing layers:

### Unit Tests

Verify individual modules independently.

Examples:

- Resume Parser
- ATS Engine
- Prompt Manager
- Career Advisor
- Resume Improver
- Resume Rewriter
- Cover Letter Generator
- JD Matcher
- Explanation Engine

---

### API Tests

Validate FastAPI endpoints.

- Request validation
- Response validation
- HTTP status codes
- Route functionality

---

### Integration Tests

Verify complete workflows.

```text
API Route
    │
    ▼
Business Logic
    │
    ▼
Prompt Manager
    │
    ▼
LLM Factory
    │
    ▼
AI Provider
    │
    ▼
Response Parser
```

---

# ▶️ Running Tests

Run all tests:

```bash
python -m pytest
```

Expected output:

```text
154 passed
```

Run a specific test:

```bash
python -m pytest tests/ai_engine/copilot -v
```

Verbose mode:

```bash
python -m pytest -v
```

---

# 🤖 AI Provider Testing

### Mock Provider

Used for:

- Unit testing
- Fast execution
- Consistent responses

### Ollama Provider

Used for:

- Real AI integration
- Local LLM testing
- End-to-end verification

Requirements:

- Ollama installed
- Llama 3.2 downloaded
- Ollama server running

---

# 📂 Test Structure

```text
tests/
│
├── api/
├── ai_engine/
│   ├── analytics/
│   ├── ats/
│   ├── copilot/
│   ├── explainability/
│   ├── interview/
│   ├── parser/
│   ├── recommendation/
│   ├── resume_improver/
│   └── training/
│
└── conftest.py
```

---

# 🛠 Development Workflow

```text
Develop Feature
      │
      ▼
Write Tests
      │
      ▼
Run Pytest
      │
      ▼
Fix Issues
      │
      ▼
Commit Changes
      │
      ▼
Push to GitHub
```

---

# 📋 Coding Standards

The project follows modern software engineering practices:

- Modular Architecture
- Clean Code
- Type Hints
- Dependency Injection
- Factory Pattern
- Single Responsibility Principle
- Provider Abstraction
- Reusable Components

---

# 🔒 Security & Performance

Current implementation includes:

- Request validation with Pydantic
- Structured API responses
- Local AI execution with Ollama
- Error handling
- Provider abstraction

Future improvements:

- JWT Authentication
- OAuth2
- Rate Limiting
- CI/CD Pipeline
- Performance Testing
- Load Testing


This testing strategy ensures that AI Resume Copilot remains reliable, maintainable, and scalable as new features are added.

---

# 🗺️ Roadmap

The project is actively evolving toward a production-ready AI platform.

## ✅ Completed

### Backend Foundation
- FastAPI Project Setup
- Modular Project Structure
- REST API Development
- Configuration Management

### AI Engines
- Resume Parser
- ATS Engine
- Job Recommendation
- Resume Improvement
- Explainability
- Analytics
- Interview Engine
- Training Engine

### AI Copilot
- Resume Rewriter
- Resume Improver
- Cover Letter Generator
- Career Advisor
- Job Description Matcher
- Explanation Engine

### AI Infrastructure
- Prompt Manager
- LLM Factory
- Mock Provider
- Ollama Provider
- Provider-Based Architecture
- Shared Response Parser
- Local Llama 3.2 Integration

### Testing
- Unit Tests
- API Tests
- Integration Tests
- **154 Passing Tests**

---

# 🚧 Upcoming Features

The next development milestones include:

- Docker Support
- PostgreSQL Integration
- SQLAlchemy ORM
- Alembic Migrations
- User Authentication
- Resume History
- File Storage
- Logging
- Background Tasks
- CI/CD Pipeline

---

# ☁️ Deployment Targets

Planned deployment platforms:

- Docker
- Railway
- Render
- Azure
- AWS
- Google Cloud Platform
- DigitalOcean

---

# 🎯 Long-Term Vision

AI Resume Copilot aims to become a complete AI-powered career assistant by expanding beyond resume analysis.

Future capabilities may include:

- AI Resume Builder
- Portfolio Generator
- LinkedIn Profile Optimizer
- GitHub Profile Analyzer
- Mock Interview Simulator
- Salary Insights
- Career Progress Tracking
- AI Career Coach

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Add or update tests.
5. Ensure all tests pass.
6. Submit a Pull Request.

Please follow the existing project structure and coding standards.

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to:

- Use
- Modify
- Learn
- Extend
- Distribute

Please include the original license when redistributing this project.

---

# 👨‍💻 Author

**Divesh Kate**

Bachelor of Technology (Artificial Intelligence & Machine Learning)

### Interests

- Backend Development
- Artificial Intelligence
- Machine Learning
- FastAPI
- Software Engineering

---

# ⭐ Project Summary

AI Resume Copilot demonstrates the development of a modern AI-powered backend application using FastAPI and Large Language Models.

### Highlights

- Modular AI Architecture
- Provider-Based LLM Design
- Ollama (Llama 3.2) Integration
- Shared Response Parser
- RESTful APIs
- Automated Testing (**154 Passing Tests**)
- Clean, Scalable Project Structure

The project is designed as a learning journey toward building production-quality AI applications while following clean architecture and software engineering best practices.

---

⭐ If you find this project useful, consider giving the repository a star.

Thank you for exploring **AI Resume Copilot**.