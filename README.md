# 🤖 AI Resume Copilot

> An AI-powered backend application that helps job seekers analyze, improve, and optimize resumes using Artificial Intelligence, Large Language Models (LLMs), and modern backend engineering practices.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-154%20Passed-success?style=for-the-badge)
![AI](https://img.shields.io/badge/AI-Ollama-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

---

# 📖 Overview

AI Resume Copilot is a modular backend application built with **FastAPI** that leverages **Large Language Models (LLMs)** to help job seekers improve resumes, analyze ATS compatibility, generate career guidance, prepare for interviews, and receive personalized learning recommendations.

The project follows modern software engineering practices including modular architecture, provider abstraction, dependency injection, centralized prompt management, shared response parsing, automated testing, and containerized deployment.

Currently, the project integrates **Ollama** with the **Llama 3.2** model for local AI inference while supporting a mock provider for testing. The backend is fully containerized using **Docker**, enabling consistent development and deployment across different operating systems.

---

# ✨ Features

## 📄 Resume Intelligence

- Resume Parsing
- ATS Analysis
- Resume Improvement
- Resume Rewriting
- Resume Analytics
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

## 🐳 Deployment

- Docker Desktop
- Docker Compose
- Docker Containerization
- WSL2 Integration
- FastAPI Container Deployment

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Backend | Python 3.12, FastAPI, Uvicorn, Pydantic |
| Artificial Intelligence | Ollama, Llama 3.2 |
| Document Processing | PyPDF2, PyMuPDF, python-docx |
| Containerization | Docker, Docker Compose |
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
| Shared Response Parser | ✅ Completed |
| Docker Integration | ✅ Completed |
| Docker Compose | ✅ Completed |
| Automated Tests | ✅ 154 Passed |

---

# 🎯 Project Goals

- Build a production-inspired AI backend.
- Improve resumes using AI-powered analysis.
- Support multiple AI providers through a common interface.
- Follow clean, modular, and scalable architecture.
- Demonstrate backend engineering, AI integration, and deployment practices.
- Prepare the project for future cloud deployment.

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
├── deployment/
│   ├── docker-compose.yml
│   └── nginx.conf
│
├── tests/
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── README.md
└── .env
```

---

# 🌟 Highlights

- ✅ Modular AI Architecture
- ✅ Provider-Based AI Design
- ✅ Local LLM Support (Ollama)
- ✅ Shared Response Parser
- ✅ Docker Containerization
- ✅ RESTful API Development
- ✅ Automated Testing (**154 Passing Tests**)
- ✅ Clean & Scalable Project Structure

---

# ⚙️ Installation & Setup

Follow these steps to run AI Resume Copilot on your local machine.

---

# 📋 Prerequisites

Install the following software before starting:

| Software | Version |
|----------|---------|
| Python | 3.12+ |
| Git | Latest |
| Docker Desktop | Latest |
| Ollama | Latest |
| pip | Latest |
| VS Code | Recommended |

Supported Operating Systems

- Windows
- Linux
- macOS

---

# 📥 Clone Repository

```bash
git clone https://github.com/your-username/AI-Resume-Copilot.git

cd AI-Resume-Copilot
```

---

# 🐍 Create Virtual Environment

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

Main dependencies

- FastAPI
- Uvicorn
- Pydantic
- PyPDF2
- PyMuPDF
- python-docx
- python-multipart
- Requests
- Pytest
- HTTPX

---

# 🤖 Install Ollama

Download and install the latest version of **Ollama** from the official website.

Verify the installation:

```bash
ollama --version
```

---

# 📥 Download the AI Model

Pull the **Llama 3.2** model:

```bash
ollama pull llama3.2
```

Verify the downloaded model:

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

If the model responds successfully, Ollama has been configured correctly.

---

# ⚙️ Configure AI Provider

Open:

```text
app/core/settings.py
```

Configure the provider:

```python
LLM_PROVIDER = "ollama"
```

Supported providers:

| Provider | Purpose |
|----------|---------|
| mock | Unit Testing |
| ollama | Local AI Inference |

---

# ▶️ Run the Application (Local)

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

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

# 🧪 Running Tests

Run the complete test suite:

```bash
python -m pytest
```

Current Status:

```text
154 Passed
```

Run only AI Copilot tests:

```bash
python -m pytest tests/ai_engine/copilot -v
```

---

# 🐳 Docker Integration

AI Resume Copilot is fully containerized using **Docker**, allowing the backend to run consistently across different operating systems without manual dependency installation.

## Docker Features

- Docker Desktop Support
- Docker Compose
- Containerized FastAPI Backend
- WSL2 Integration
- Consistent Development Environment
- Production-Oriented Deployment Structure

---

# 📂 Docker Files

| File | Purpose |
|------|---------|
| Dockerfile | Builds the backend image |
| deployment/docker-compose.yml | Runs and manages containers |
| .dockerignore | Excludes unnecessary files during image creation |

---

# 🚀 Build Docker Image

```bash
docker compose -f deployment/docker-compose.yml build
```

---

# ▶️ Start Docker Container

```bash
docker compose -f deployment/docker-compose.yml up
```

Run in detached mode:

```bash
docker compose -f deployment/docker-compose.yml up -d
```

---

# 🛑 Stop Docker Container

```bash
docker compose -f deployment/docker-compose.yml down
```

---

# 🌐 Docker Application URLs

| Service | URL |
|----------|-----|
| FastAPI | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

---

# 🏗 Docker Workflow

```text
Source Code
      │
      ▼
Docker Build
      │
      ▼
Docker Image
      │
      ▼
Docker Container
      │
      ▼
FastAPI Application
      │
      ▼
Browser / API Client
```

---

# ✅ Docker Verification

Docker integration has been successfully verified.

Completed:

- Docker Desktop Installation
- WSL2 Configuration
- Ubuntu Integration
- Dockerfile Creation
- Docker Compose Configuration
- Dependency Installation
- FastAPI Container Startup
- Swagger UI Verification
- REST API Verification

Current Status:

```text
AI Resume Copilot is running successfully inside a Docker container.
```

---

# 📂 Important Files

| File | Purpose |
|------|---------|
| main.py | FastAPI Entry Point |
| settings.py | Application Configuration |
| requirements.txt | Python Dependencies |
| Dockerfile | Docker Image Configuration |
| deployment/docker-compose.yml | Container Orchestration |
| README.md | Project Documentation |

---

# 🔧 Troubleshooting

## Ollama Not Found

```bash
ollama --version
```

If the command is unavailable, reinstall Ollama and restart your terminal.

---

## Model Missing

```bash
ollama pull llama3.2
```

---

## Docker Build Failed

Rebuild without cache:

```bash
docker compose -f deployment/docker-compose.yml build --no-cache
```

---

## Container Not Starting

Check container logs:

```bash
docker compose -f deployment/docker-compose.yml up
```

Verify:

- Docker Desktop is running.
- WSL2 integration is enabled.
- Required ports are available.
- Dependencies are installed successfully.

---

## Tests Failing

Run:

```bash
python -m pytest
```

Verify:

- Virtual environment is activated.
- Dependencies are installed.
- Ollama server is running.
- Docker services are functioning correctly.

---

# 🧠 AI Engines

The AI Engine layer contains the core business logic of AI Resume Copilot. Each engine is designed with a **single responsibility**, making the application modular, maintainable, testable, and easy to extend.

Each engine can operate independently while sharing common project infrastructure such as configuration management, API routing, and response formatting.

---

# 📄 Resume Parser Engine

The Resume Parser extracts textual information from uploaded PDF and DOCX resumes.

### Responsibilities

- Read uploaded resumes
- Support PDF documents
- Support DOCX documents
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

### Example Response

```json
{
    "success": true,
    "text": "Extracted resume content..."
}
```

---

# 📊 ATS Analysis Engine

The ATS Engine evaluates resume compatibility with Applicant Tracking Systems.

### Features

- ATS Score
- Keyword Analysis
- Skill Matching
- Missing Skills Detection
- Improvement Suggestions

### Workflow

```text
Resume
   │
   ▼
Keyword Analysis
   │
   ▼
ATS Scoring
   │
   ▼
Recommendations
```

### Example Response

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

The Job Recommendation Engine analyzes resume skills and recommends suitable career opportunities.

### Features

- Skill Analysis
- Recommended Job Roles
- Technology Suggestions
- Career Guidance

### Example Response

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

# ✨ Resume Improvement Engine

Provides AI-powered suggestions to strengthen resume quality without rewriting the entire document.

### Features

- Better wording
- Achievement improvements
- Missing skill detection
- Readability enhancement

### Example Response

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

# 📈 Resume Analytics Engine

Generates useful insights from resume content.

### Features

- Resume Statistics
- Skill Distribution
- ATS Metrics
- Experience Summary
- Resume Score

### Example Response

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

# 🎤 Interview Preparation Engine

Creates personalized interview questions using resume content.

### Features

- Technical Questions
- HR Questions
- Resume Discussion
- Project-Based Questions

### Example Response

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

# 📚 Training Recommendation Engine

Generates personalized learning recommendations based on resume analysis.

### Features

- Learning Roadmaps
- Skill Gap Analysis
- Technology Recommendations
- Career Planning

### Example Response

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

# 🔍 Explainability Engine

Transforms AI-generated outputs into clear and understandable explanations.

### Features

- Explain ATS Scores
- Explain Recommendations
- Highlight Strengths
- Identify Weaknesses
- Human-Friendly Responses

### Example Response

```json
{
    "success": true,
    "explanation": "Your resume demonstrates strong backend development skills but would benefit from measurable achievements and cloud technologies."
}
```

---

# 🔄 AI Engine Workflow

```text
Resume Upload
      │
      ▼
Resume Parser
      │
      ▼
ATS Analysis
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
Interview Preparation
      │
      ▼
Training Recommendation
```

---

# 🎯 AI Engine Design Principles

Each AI Engine follows a common design philosophy.

### Principles

- Single Responsibility Principle
- Modular Architecture
- Reusable Components
- Clear Separation of Concerns
- Independent Business Logic
- Easy Testing
- Scalable Design

---

# ✅ Current AI Engine Modules

| Engine | Status |
|---------|--------|
| Resume Parser | ✅ Completed |
| ATS Analysis | ✅ Completed |
| Resume Improvement | ✅ Completed |
| Resume Analytics | ✅ Completed |
| Explainability | ✅ Completed |
| Job Recommendation | ✅ Completed |
| Interview Preparation | ✅ Completed |
| Training Recommendation | ✅ Completed |


The AI Engine layer serves as the foundation of AI Resume Copilot. Every module is implemented independently, allowing new capabilities to be added with minimal changes while maintaining clean architecture and high test coverage.

---

# 🤖 AI Copilot

The AI Copilot layer provides intelligent AI-powered features that help users improve resumes, prepare job applications, receive career guidance, and better understand AI-generated recommendations.

Unlike traditional AI applications, every Copilot module shares the same underlying architecture through a centralized **PromptManager**, **LLMFactory**, and **ResponseParser**, ensuring consistency, maintainability, and minimal code duplication.

---

# 📝 Resume Rewriter

Professionally rewrites resume content while preserving its original meaning.

### Features

- Professional language
- Grammar improvement
- ATS-friendly wording
- Better readability
- Strong action verbs

### Workflow

```text
Resume
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
   │
   ▼
Professional Resume
```

### Example Response

```json
{
    "success": true,
    "feature": "resume_rewriter",
    "response": "Professional version of the resume..."
}
```

---

# ✨ Resume Improver

Analyzes resume content and provides targeted suggestions without completely rewriting it.

### Features

- Achievement improvement
- Stronger action verbs
- Skill recommendations
- Content enhancement
- ATS optimization

### Example Response

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

Generates personalized cover letters using resume content, company name, and job role.

### Features

- Personalized writing
- Company-specific content
- Professional formatting
- Role-focused writing
- Ready-to-use cover letters

### Example Response

```json
{
    "success": true,
    "feature": "cover_letter",
    "response": "Generated professional cover letter..."
}
```

---

# 💼 Career Advisor

Provides AI-generated career guidance based on the user's resume.

### Features

- Career path recommendations
- Skills to learn
- Certification suggestions
- Internship guidance
- Long-term career planning

### Example Response

```json
{
    "success": true,
    "feature": "career_advisor",
    "response": {
        "career_path": "Backend Developer",
        "skills_to_learn": [
            "Docker",
            "System Design"
        ]
    }
}
```

---

# 📑 Job Description Matcher

Compares a resume with a job description to evaluate compatibility.

### Features

- Resume match percentage
- Missing skills detection
- Skill comparison
- Improvement suggestions
- ATS compatibility

### Example Response

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

Transforms AI-generated responses into simple and easy-to-understand explanations.

### Features

- Human-readable summaries
- Simple explanations
- Better transparency
- Easier interpretation
- Improved user understanding

### Example Response

```json
{
    "success": true,
    "feature": "explanation_engine",
    "response": "Your resume demonstrates strong backend skills but would benefit from measurable achievements and cloud technologies."
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
Selected AI Provider
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

# 🧩 Shared Components

Every AI Copilot module uses the same shared infrastructure.

### Prompt Manager

Responsible for:

- Centralized prompt templates
- Consistent AI instructions
- Reusable prompts
- Easy prompt maintenance

---

### LLM Factory

Responsible for:

- Creating AI provider instances
- Switching providers
- Dependency abstraction
- Future provider support

Current Providers

- Ollama
- Mock Provider

Future Providers

- OpenAI
- Google Gemini
- Anthropic Claude
- Azure OpenAI

---

### Response Parser

Responsible for:

- Parsing AI responses
- JSON validation
- Error handling
- Returning structured Python dictionaries

Instead of implementing response parsing separately in every Copilot module, a single shared parser is reused throughout the application.

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
| Prompt Manager | ✅ Completed |
| LLM Factory | ✅ Completed |
| Response Parser | ✅ Completed |
| Ollama Integration | ✅ Completed |

---

# 🎯 AI Copilot Highlights

- Modular AI Architecture
- Shared Prompt Management
- Provider-Based Design
- Reusable Response Parsing
- Local LLM Support
- Easily Extensible Features
- Consistent JSON Responses
- Minimal Code Duplication


The AI Copilot demonstrates how multiple AI-powered capabilities can be developed using a common architecture while maintaining clean code, modularity, and scalability. New Copilot modules can be added with minimal changes by reusing the shared infrastructure.

---

# 🏗️ AI Architecture

AI Resume Copilot follows a modular, provider-based architecture that separates business logic from AI providers. This design improves maintainability, scalability, testing, and future extensibility while minimizing code duplication.

The architecture allows AI providers to be replaced without modifying the application's core business logic.

---

# 🧠 Architecture Overview

```text
                Client
                   │
                   ▼
           FastAPI REST API
                   │
                   ▼
            AI Copilot Module
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
 PromptManager  LLMFactory  ResponseParser
                   │
                   ▼
            Selected Provider
          ┌────────┴────────┐
          ▼                 ▼
     Ollama Provider    Mock Provider
                   │
                   ▼
              AI Response
                   │
                   ▼
          Structured JSON Output
```

---

# 📝 Prompt Manager

The **PromptManager** centralizes all AI prompts used throughout the application.

Instead of embedding prompts inside every module, prompts are maintained in one location, making updates simple and ensuring consistency.

### Responsibilities

- Centralized prompt templates
- Reusable AI prompts
- Consistent instructions
- Easier maintenance
- Reduced duplication

---

# 🏭 LLM Factory

The **LLMFactory** is responsible for creating AI provider instances based on application configuration.

Business logic never communicates directly with a provider. Instead, every module requests an AI client from the factory.

### Current Providers

| Provider | Purpose |
|----------|---------|
| Ollama | Local AI inference |
| Mock Provider | Unit testing |

### Planned Providers

- OpenAI
- Google Gemini
- Anthropic Claude
- Azure OpenAI

---

# 🔌 Provider Architecture

Every AI provider follows the same interface.

```text
             LLM Client
                 │
      ┌──────────┴──────────┐
      ▼                     ▼
Mock Provider       Ollama Provider
```

Because every provider follows the same contract, switching providers requires only a configuration change.

### Advantages

- Easy provider replacement
- Cleaner business logic
- Better testing
- Future extensibility

---

# 🤖 Ollama Integration

The project currently uses **Ollama** as its AI backend.

Current model:

```text
llama3.2
```

### Benefits

- Local execution
- Offline support
- No API cost
- Better privacy
- Faster experimentation

---

# 📦 Response Parser

The **ResponseParser** standardizes AI responses before they are returned to the application.

Instead of every Copilot module parsing responses individually, all modules now reuse a shared parser.

### Responsibilities

- Parse JSON responses
- Handle invalid JSON safely
- Return Python dictionaries
- Centralize response processing
- Improve consistency

### Workflow

```text
Raw AI Response
        │
        ▼
 ResponseParser
        │
        ▼
 Structured Python Object
```

---

# ⚙️ Configuration Layer

Application behavior is controlled through centralized configuration.

Current configuration includes:

- AI Provider Selection
- Ollama Configuration
- Application Settings
- Environment Variables

This approach keeps configuration separate from business logic.

---

# 🔄 Complete AI Workflow

```text
Client Request
       │
       ▼
FastAPI Endpoint
       │
       ▼
Request Validation
       │
       ▼
Business Logic
       │
       ▼
PromptManager
       │
       ▼
LLMFactory
       │
       ▼
Selected AI Provider
       │
       ▼
Ollama / Mock
       │
       ▼
ResponseParser
       │
       ▼
Structured JSON Response
       │
       ▼
Client
```

---

# 🏛️ Design Principles

AI Resume Copilot follows modern software engineering principles.

### Principles Used

- Single Responsibility Principle (SRP)
- Separation of Concerns
- Dependency Injection
- Factory Pattern
- Provider Abstraction
- Reusable Components
- Modular Architecture
- Low Coupling
- High Cohesion

---

# 🚀 Architectural Advantages

The current architecture provides several long-term benefits.

### Benefits

- Easy to maintain
- Easy to extend
- Supports multiple AI providers
- Consistent AI responses
- Minimal code duplication
- Simplified testing
- Cleaner project structure
- Production-oriented design

---

# 📈 Future Architecture

The current architecture is designed to support future expansion.

Planned improvements include:

- OpenAI Integration
- Google Gemini Integration
- Claude Integration
- Azure OpenAI Support
- Multi-provider Selection
- Response Caching
- Streaming Responses
- AI Usage Analytics


The architecture of AI Resume Copilot emphasizes modularity, maintainability, and scalability. By separating AI providers from business logic and introducing shared components such as the **PromptManager**, **LLMFactory**, and **ResponseParser**, the project is well prepared for future enhancements while keeping the codebase clean and easy to maintain.

---

# 🌐 REST API

AI Resume Copilot exposes a RESTful API built with **FastAPI**. Every endpoint accepts structured requests and returns standardized JSON responses, making integration with web, desktop, or mobile applications straightforward.

The API follows a modular architecture where each feature is implemented as an independent endpoint while sharing common validation, AI infrastructure, and response formatting.

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

These interfaces allow developers to explore and test every endpoint without additional tools.

---

# 📄 Resume Parser APIs

### Parse Resume

```http
POST /parser/parse
```

Extracts text from uploaded PDF or DOCX resumes.

---

# 📊 ATS APIs

### Analyze Resume

```http
POST /ats/analyze
```

Calculates ATS compatibility, analyzes keywords, and generates improvement recommendations.

---

# 💼 Job Recommendation APIs

### Recommend Jobs

```http
POST /recommendation/jobs
```

Suggests suitable career opportunities based on resume skills and experience.

---

# ✨ Resume Improvement APIs

### Improve Resume

```http
POST /resume-improver/improve
```

Provides AI-powered suggestions to strengthen resume quality.

---

# 📈 Analytics APIs

### Analyze Resume

```http
POST /analytics/analyze
```

Generates resume statistics, skill analysis, and ATS metrics.

---

# 🎤 Interview APIs

### Generate Interview Questions

```http
POST /interview/questions
```

Creates personalized interview questions from resume content.

---

# 📚 Training APIs

### Recommend Learning Path

```http
POST /training/recommend
```

Generates personalized learning recommendations and skill-development roadmaps.

---

# 🤖 AI Copilot APIs

### Resume Rewriter

```http
POST /copilot/rewrite-resume
```

Professionally rewrites resume content.

---

### Resume Improver

```http
POST /copilot/improve-resume
```

Suggests improvements while preserving the original content.

---

### Cover Letter Generator

```http
POST /copilot/cover-letter
```

Creates personalized cover letters based on the resume, company, and job role.

---

### Career Advisor

```http
POST /copilot/career-advice
```

Provides AI-generated career guidance and recommendations.

---

### Job Description Matcher

```http
POST /copilot/jd-match
```

Compares resumes with job descriptions and identifies missing skills.

---

### Explanation Engine

```http
POST /copilot/explain
```

Transforms AI-generated outputs into clear, human-readable explanations.

---

# 🔄 API Request Workflow

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
AI Engine / Copilot
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

Every successful endpoint follows a consistent response format.

```json
{
    "success": true,
    "feature": "career_advisor",
    "response": {}
}
```

---

# ❌ Standard Error Response

Validation errors are automatically handled by FastAPI and Pydantic.

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
| 201 | Resource Created |
| 400 | Bad Request |
| 404 | Resource Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# 🔒 Request Validation

The API uses **Pydantic** for request validation.

### Validation Features

- Required field validation
- Automatic type checking
- JSON schema generation
- Consistent error responses
- Built-in documentation support

---

# 🚀 API Highlights

- RESTful architecture
- FastAPI framework
- Automatic OpenAPI documentation
- Interactive Swagger UI
- ReDoc support
- Standardized JSON responses
- Request validation with Pydantic
- Modular endpoint design
- Easy frontend integration
- Docker-compatible deployment



The REST API serves as the communication layer between clients and the AI engine, providing a clean, consistent, and scalable interface for all resume analysis and AI-powered career assistance features.

---

# 🧪 Testing & Development

AI Resume Copilot follows a **test-driven and modular development approach**. Automated testing ensures that new features remain reliable and do not break existing functionality.

The project currently contains **154 passing automated tests**, covering AI engines, AI Copilot modules, API routes, and shared infrastructure.

---

# 📊 Test Status

| Category | Status |
|----------|--------|
| Total Tests | ✅ 154 Passed |
| Unit Tests | ✅ Passed |
| API Tests | ✅ Passed |
| AI Engine Tests | ✅ Passed |
| AI Copilot Tests | ✅ Passed |
| Ollama Integration | ✅ Passed |
| Docker Deployment | ✅ Verified |

---

# 🧩 Testing Strategy

The project uses multiple testing layers to validate different parts of the application.

## Unit Testing

Unit tests verify individual modules independently.

Covered modules:

- Resume Parser
- ATS Engine
- Resume Improvement
- Analytics Engine
- Job Recommendation
- Interview Engine
- Training Engine
- Prompt Manager
- LLM Factory
- Response Parser
- Resume Rewriter
- Resume Improver
- Cover Letter Generator
- Career Advisor
- JD Matcher
- Explanation Engine

---

## API Testing

API tests validate FastAPI endpoints.

Coverage includes:

- Request validation
- Response validation
- HTTP status codes
- Route functionality
- Error handling

---

## Integration Testing

Integration tests verify complete workflows from API request to AI response.

```text
Client Request
      │
      ▼
FastAPI Endpoint
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
      │
      ▼
JSON Response
```

---

## Docker Verification

The application has been tested successfully inside a Docker container.

Verified components:

- Docker Image Build
- Docker Compose
- FastAPI Startup
- REST API
- Swagger UI
- ReDoc
- Dependency Installation

---

# ▶️ Running Tests

Run the complete test suite:

```bash
python -m pytest
```

Expected output:

```text
154 passed
```

Run AI Copilot tests only:

```bash
python -m pytest tests/ai_engine/copilot -v
```

Run with verbose output:

```bash
python -m pytest -v
```

---

# 🐳 Running with Docker

Build the Docker image:

```bash
docker compose -f deployment/docker-compose.yml build
```

Start the application:

```bash
docker compose -f deployment/docker-compose.yml up
```

Stop the application:

```bash
docker compose -f deployment/docker-compose.yml down
```

---

# 🤖 AI Provider Testing

### Mock Provider

Used for:

- Unit Testing
- Fast Execution
- Predictable Responses
- Offline Development

---

### Ollama Provider

Used for:

- Local AI Inference
- End-to-End Testing
- Real AI Responses
- Feature Validation

Requirements:

- Ollama Installed
- Llama 3.2 Downloaded
- Ollama Service Running

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

# 🔄 Development Workflow

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
Run Docker
      │
      ▼
Verify APIs
      │
      ▼
Commit Changes
      │
      ▼
Push to GitHub
```

---

# 📋 Coding Standards

The project follows modern backend engineering practices.

### Standards

- Modular Architecture
- Clean Code
- Type Hints
- Dependency Injection
- Factory Pattern
- Provider Abstraction
- Reusable Components
- Docker-Based Development

---

# 🔒 Security & Reliability

Current implementation includes:

- Request Validation
- Structured API Responses
- Local AI Execution
- Error Handling
- Provider Abstraction
- Docker Isolation

Planned improvements:

- JWT Authentication
- OAuth2
- PostgreSQL
- SQLAlchemy
- Alembic
- CI/CD Pipeline
- Performance Testing
- Load Testing

---

# 🚀 Development Highlights

Current project achievements:

- 154 Passing Automated Tests
- Fully Modular Architecture
- Shared AI Infrastructure
- Provider-Based AI Design
- Dockerized Backend
- Interactive API Documentation
- Clean Project Structure
- Production-Oriented Development Workflow



The testing and development strategy ensures that AI Resume Copilot remains reliable, maintainable, and scalable while supporting continuous feature development and future production deployment.

---

# 🗺️ Roadmap

AI Resume Copilot is being developed as a production-inspired AI backend application. The project continues to evolve with new AI capabilities, backend improvements, and deployment features.

---

# ✅ Completed

## Backend Foundation

- FastAPI Project Setup
- Modular Project Structure
- REST API Development
- Configuration Management

---

## AI Engines

- Resume Parser
- ATS Analysis
- Resume Improvement
- Resume Analytics
- Explainability Engine
- Job Recommendation Engine
- Interview Preparation Engine
- Training Recommendation Engine

---

## AI Copilot

- Resume Rewriter
- Resume Improver
- Cover Letter Generator
- Career Advisor
- Job Description Matcher
- Explanation Engine

---

## AI Infrastructure

- Prompt Manager
- LLM Factory
- Mock Provider
- Ollama Provider
- Provider-Based Architecture
- Shared Response Parser
- Local Llama 3.2 Integration

---

## Deployment

- Docker Desktop Integration
- Dockerfile
- Docker Compose
- Dockerized FastAPI Backend
- WSL2 Integration
- Ubuntu Configuration
- Containerized Development Environment

---

## Testing

- Unit Testing
- API Testing
- Integration Testing
- Docker Verification
- **154 Passing Automated Tests**

---

# 🚧 Upcoming Features

The next development milestones include:

- PostgreSQL Integration
- SQLAlchemy ORM
- Alembic Database Migrations
- JWT Authentication
- User Management
- Resume History
- File Storage
- Logging
- Background Tasks
- Environment Configuration
- CI/CD Pipeline
- Production Deployment
- API Versioning
- Monitoring & Health Checks

---

# ☁️ Deployment Targets

Planned deployment platforms:

- Railway
- Render
- Azure App Service
- AWS
- Google Cloud Platform
- DigitalOcean
- Self-Hosted Docker Server

---

# 🎯 Long-Term Vision

AI Resume Copilot aims to become a complete AI-powered career platform that helps users throughout their professional journey.

Future capabilities include:

- AI Resume Builder
- Portfolio Generator
- LinkedIn Profile Optimizer
- GitHub Profile Analyzer
- Mock Interview Simulator
- Salary Insights
- Career Progress Tracker
- AI Career Coach
- Multi-Language Support
- Team Collaboration
- Recruiter Dashboard

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Add or update tests.
5. Ensure all tests pass.
6. Submit a Pull Request.

Please follow the existing project structure, coding standards, and development workflow.

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
- Docker
- Software Engineering
- System Design

---

# ⭐ Project Summary

AI Resume Copilot is a modern AI-powered backend application built using **FastAPI**, **Ollama**, and **Docker**. The project demonstrates modular backend architecture, AI integration, provider abstraction, automated testing, and containerized deployment.

## Key Highlights

- 🤖 AI-Powered Resume Analysis
- 📝 Resume Rewriter & Improver
- 💼 Career Advisor
- 📄 Cover Letter Generator
- 🎯 ATS Analysis
- 📊 Resume Analytics
- 🧠 Provider-Based AI Architecture
- ⚙️ Shared Prompt Management
- 🔄 Shared Response Parser
- 🐳 Dockerized Backend
- 📚 Interactive API Documentation
- ✅ 154 Passing Automated Tests
- 🏗️ Modular & Scalable Architecture

---

## Project Statistics

| Category | Status |
|----------|--------|
| AI Engines | ✅ 8 Modules |
| AI Copilot Features | ✅ 6 Modules |
| REST APIs | ✅ Available |
| Docker Support | ✅ Completed |
| AI Provider | ✅ Ollama |
| Tests | ✅ 154 Passed |
| Documentation | ✅ Complete |

---

### Thank You

Thank you for exploring **AI Resume Copilot**.

This project represents an ongoing journey of learning backend engineering, Artificial Intelligence, software architecture, testing, and deployment while following modern development practices.

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!