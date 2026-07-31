# 🤖 AI Resume Copilot

> An AI-powered backend application that helps job seekers analyze, improve, and optimize resumes using Artificial Intelligence, Large Language Models (LLMs), and modern backend engineering practices.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![AI](https://img.shields.io/badge/AI-Ollama-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

---

# 📖 Overview

AI Resume Copilot is a modular backend application built with **FastAPI** that leverages **Large Language Models (LLMs)** to help job seekers analyze resumes, improve ATS compatibility, generate career guidance, prepare for interviews, and receive personalized learning recommendations.

The project follows modern backend engineering practices including:

- Modular Architecture
- Provider-Based AI Design
- Dependency Injection
- Shared Prompt Management
- Shared Response Parsing
- Automated Testing
- Docker Containerization
- Continuous Integration using GitHub Actions

The application currently integrates **Ollama** with the **Llama 3.2** model for local AI inference while supporting a **Mock Provider** for testing. The backend is fully containerized using Docker and includes an automated GitHub Actions workflow that validates the project on every push.

---

# ✨ Features

## 📄 Resume Intelligence

- Resume Parsing
- ATS Analysis
- Resume Improvement
- Resume Rewriting
- Resume Analytics
- Explainability

---

## 🤖 AI Copilot

- Career Advisor
- Cover Letter Generator
- Resume Rewriter
- Resume Improver
- Job Description Matcher
- Explanation Engine

---

## 🧠 AI Infrastructure

- Prompt Manager
- LLM Factory
- Provider-Based Architecture
- Ollama Integration
- Mock Provider
- Shared Response Parser

---

## 🚀 Additional AI Engines

- Resume Analytics
- Interview Preparation
- Job Recommendation
- Training Recommendation

---

## 🐳 Deployment & DevOps

- Docker Desktop
- Docker Compose
- Dockerized FastAPI Backend
- WSL2 Integration
- Ubuntu Development Environment
- GitHub Actions CI
- Automated Testing Pipeline

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Backend | Python 3.12, FastAPI, Uvicorn, Pydantic |
| Artificial Intelligence | Ollama, Llama 3.2 |
| Document Processing | PyPDF2, PyMuPDF, python-docx |
| Containerization | Docker, Docker Compose |
| Testing | Pytest, HTTPX |
| CI/CD | GitHub Actions |
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
| GitHub Actions | ✅ Configured |
| Continuous Integration | ✅ Running |
| Automated Testing | ✅ 140 Passing (CI) |

> **Note:** GitHub Actions currently passes **140 automated tests**. The remaining **14 integration tests** require a running Ollama server and will be replaced with mocked responses in a future update to make the CI pipeline fully self-contained.

---

# 🎯 Project Goals

- Build a production-inspired AI backend.
- Improve resumes using AI-powered analysis.
- Support multiple AI providers through a common interface.
- Follow clean, modular, and scalable architecture.
- Demonstrate backend engineering, AI integration, testing, and deployment practices.
- Implement Continuous Integration and prepare the project for cloud deployment.

---

# 📁 Project Structure

```text
AI-Resume-Copilot/
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
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
├── uploads/
├── Dockerfile
├── .dockerignore
├── .gitignore
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
- ✅ Docker Compose Support
- ✅ GitHub Actions CI
- ✅ RESTful API Development
- ✅ Automated Testing
- ✅ Clean & Scalable Project Structure

---

# ⚙️ Installation & Setup

Follow the steps below to set up AI Resume Copilot on your local machine.

---

# 📋 Prerequisites

Install the following software before getting started.

| Software | Version |
|----------|---------|
| Python | 3.12+ |
| Git | Latest |
| Docker Desktop | Latest |
| Ollama | Latest |
| VS Code | Recommended |
| pip | Latest |

---

## Supported Operating Systems

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

Main dependencies:

- FastAPI
- Uvicorn
- Pydantic
- PyPDF2
- PyMuPDF
- python-docx
- python-multipart
- Requests
- HTTPX
- Pytest

---

# 🤖 Install Ollama

Download and install the latest version of **Ollama**.

Verify installation:

```bash
ollama --version
```

---

# 📥 Download AI Model

Pull the required model:

```bash
ollama pull llama3.2
```

Verify installation:

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

If you receive a response, Ollama has been configured successfully.

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
| ollama | Local AI Inference |
| mock | Unit Testing |

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

For local development with Ollama running:

```text
154 Passed
```

For GitHub Actions CI:

```text
140 Passed
14 Integration Tests Pending
```

The remaining CI failures are integration tests that require a running Ollama server. These will be migrated to mocked responses in a future update to allow the full suite to run in GitHub Actions without external AI services.

---

# 🐳 Docker Integration

AI Resume Copilot is fully containerized using **Docker**, providing a consistent development environment across Windows, Linux, and macOS. Docker eliminates manual dependency installation and simplifies project setup.

---

# 🚀 Docker Features

- Docker Desktop Support
- Docker Compose
- Dockerized FastAPI Backend
- WSL2 Integration
- Ubuntu Development Environment
- Consistent Development Workflow
- Production-Oriented Project Structure

---

# 📂 Docker Files

| File | Purpose |
|------|---------|
| Dockerfile | Builds the FastAPI application image |
| deployment/docker-compose.yml | Starts and manages the application container |
| .dockerignore | Excludes unnecessary files during Docker image creation |

---

# 🔨 Build Docker Image

Build the Docker image:

```bash
docker compose -f deployment/docker-compose.yml build
```

---

# ▶️ Start Docker Container

Start the application:

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

The Docker environment has been successfully verified.

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

# ⚙️ Continuous Integration (GitHub Actions)

The project now includes **GitHub Actions** to automate testing whenever changes are pushed to GitHub.

Current workflow automatically:

- Triggers on every push to the `main` branch
- Creates a fresh Ubuntu runner
- Installs Python 3.12
- Installs project dependencies
- Executes the complete pytest suite
- Reports the test results

---

# 🔄 CI Pipeline

```text
Developer Push
      │
      ▼
GitHub Repository
      │
      ▼
GitHub Actions
      │
      ▼
Ubuntu Runner
      │
      ▼
Install Dependencies
      │
      ▼
Run Pytest
      │
      ▼
Publish Results
```

---

# 📊 Current CI Status

| Component | Status |
|-----------|--------|
| GitHub Actions Workflow | ✅ Configured |
| Workflow Execution | ✅ Running |
| Dependency Installation | ✅ Successful |
| Docker Support | ✅ Verified |
| Test Execution | ✅ Running |
| Passing Tests | ✅ 140 |
| Pending Tests | ⚠️ 14 |

---

# ⚠️ Current CI Limitation

The remaining **14 tests** are integration tests that communicate directly with a locally running **Ollama** server.

Since GitHub Actions runners do not include Ollama by default, these tests currently fail during CI.

Planned improvement:

- Replace live Ollama calls with mocked responses during automated testing.
- Keep real Ollama integration for local development.
- Achieve a fully passing CI pipeline without external AI dependencies.

---

# 📂 Important Files

| File | Purpose |
|------|---------|
| Dockerfile | Docker Image Configuration |
| deployment/docker-compose.yml | Docker Compose Configuration |
| .github/workflows/python-tests.yml | GitHub Actions Workflow |
| requirements.txt | Python Dependencies |
| app/main.py | FastAPI Entry Point |
| app/core/settings.py | Application Configuration |
| README.md | Project Documentation |

---

# 🔧 Troubleshooting

## Docker Build Failed

Rebuild the image without using cache:

```bash
docker compose -f deployment/docker-compose.yml build --no-cache
```

---

## Container Not Starting

Start the container with logs:

```bash
docker compose -f deployment/docker-compose.yml up
```

Verify:

- Docker Desktop is running.
- WSL2 integration is enabled.
- Required ports are available.
- Dependencies are installed correctly.

---

## GitHub Actions Failed

If the GitHub Actions workflow fails:

- Verify all dependencies are listed in `requirements.txt`.
- Ensure required project files are committed.
- Review the workflow logs in the **Actions** tab.
- Check whether failures are caused by external services such as Ollama.

---

## Ollama Connection Error

If you see:

```text
Connection refused: localhost:11434
```

Make sure Ollama is running locally:

```bash
ollama serve
```

Then verify the installed model:

```bash
ollama list
```

If running inside GitHub Actions, this limitation is expected until the AI provider is mocked for CI.

---

# 🧠 AI Engines

The AI Engine layer contains the core business logic of AI Resume Copilot. Each engine follows the **Single Responsibility Principle (SRP)**, making the application modular, reusable, maintainable, and easy to extend.

Every engine operates independently while sharing common infrastructure such as configuration management, provider abstraction, prompt management, and response parsing.

---

# 📄 Resume Parser Engine

The Resume Parser extracts text from uploaded PDF and DOCX resumes.

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

The ATS Engine evaluates resume compatibility with Applicant Tracking Systems (ATS).

### Features

- ATS Score
- Keyword Analysis
- Skill Matching
- Missing Skills Detection
- Resume Recommendations

### Workflow

```text
Resume
   │
   ▼
Keyword Analysis
   │
   ▼
ATS Score
   │
   ▼
Recommendations
```

### Example Response

```json
{
    "success": true,
    "score": 89,
    "recommendations": [
        "Use measurable achievements",
        "Add missing technical keywords"
    ]
}
```

---

# 💼 Job Recommendation Engine

Analyzes resume skills and recommends suitable job roles.

### Features

- Skill Analysis
- Recommended Roles
- Technology Suggestions
- Career Guidance

### Example Response

```json
{
    "success": true,
    "recommended_roles": [
        "Backend Developer",
        "Machine Learning Engineer",
        "AI Engineer"
    ]
}
```

---

# ✨ Resume Improvement Engine

Provides AI-powered suggestions to improve resumes without rewriting the complete document.

### Features

- Better wording
- Achievement improvements
- Skill recommendations
- ATS optimization
- Readability enhancement

### Example Response

```json
{
    "success": true,
    "suggestions": [
        "Use stronger action verbs",
        "Quantify project outcomes",
        "Improve project descriptions"
    ]
}
```

---

# 📈 Resume Analytics Engine

Generates meaningful insights from resume content.

### Features

- Resume Statistics
- ATS Metrics
- Skill Distribution
- Experience Summary
- Resume Score

### Example Response

```json
{
    "success": true,
    "analytics": {
        "technical_skills": 18,
        "projects": 5,
        "ats_score": 90
    }
}
```

---

# 🎤 Interview Preparation Engine

Generates personalized interview questions using resume content.

### Features

- Technical Questions
- HR Questions
- Project-Based Questions
- Resume Discussion

### Example Response

```json
{
    "success": true,
    "questions": [
        "Explain your FastAPI architecture.",
        "Describe your Docker workflow."
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

Converts AI-generated outputs into simple, human-readable explanations.

### Features

- Explain ATS Scores
- Explain AI Suggestions
- Highlight Resume Strengths
- Identify Weaknesses
- Human-Friendly Responses

### Example Response

```json
{
    "success": true,
    "explanation": "Your resume demonstrates strong backend development skills but would benefit from quantified achievements and cloud technologies."
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
 ┌────┴────────────┐
 ▼                 ▼
Analytics     Job Recommendation
      │
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

Every AI Engine follows the same architectural principles.

### Principles

- Single Responsibility Principle (SRP)
- Modular Architecture
- Provider Abstraction
- Reusable Components
- Low Coupling
- High Cohesion
- Independent Business Logic
- Easy Unit Testing
- Scalable Design

---

# ✅ Current AI Engine Status

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


The AI Engine layer serves as the foundation of AI Resume Copilot. Each module is implemented independently, making the application easier to test, maintain, and extend. The provider-based architecture also allows future AI providers to be added with minimal changes to the business logic.

---

# 🤖 AI Copilot

The AI Copilot layer provides intelligent AI-powered capabilities that help users improve resumes, prepare job applications, receive career guidance, and better understand AI-generated recommendations.

Unlike traditional AI applications, every Copilot module shares the same infrastructure through a centralized **Prompt Manager**, **LLM Factory**, and **Response Parser**, ensuring consistency, maintainability, and minimal code duplication.

---

# 📝 Resume Rewriter

Professionally rewrites resume content while preserving its original meaning.

### Features

- Professional wording
- Grammar improvement
- ATS-friendly formatting
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
Selected AI Provider
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

Analyzes resume content and provides targeted suggestions without rewriting the entire document.

### Features

- Achievement improvement
- Stronger action verbs
- Skill recommendations
- ATS optimization
- Better readability

### Example Response

```json
{
    "success": true,
    "feature": "resume_improver",
    "response": [
        "Use measurable achievements",
        "Improve project descriptions"
    ]
}
```

---

# 📄 Cover Letter Generator

Generates personalized cover letters using resume content, company information, and job role.

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

Provides AI-generated career guidance based on resume content.

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

Compares a resume against a job description to evaluate compatibility.

### Features

- Resume match percentage
- Missing skills detection
- Skill comparison
- ATS compatibility
- Improvement suggestions

### Example Response

```json
{
    "success": true,
    "feature": "job_match",
    "response": {
        "match_percentage": 85,
        "missing_skills": [
            "Docker",
            "Kubernetes"
        ]
    }
}
```

---

# 🔍 Explanation Engine

Transforms AI-generated responses into simple and understandable explanations.

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
    "feature": "explanation",
    "response": "Your resume demonstrates strong backend development skills but would benefit from measurable achievements and cloud technologies."
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
Ollama / Mock Provider
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

## Prompt Manager

Responsible for:

- Centralized prompt templates
- Consistent AI instructions
- Reusable prompts
- Easy prompt maintenance

---

## LLM Factory

Responsible for:

- Creating AI provider instances
- Switching providers
- Dependency abstraction
- Future provider support

### Current Providers

- Ollama
- Mock Provider

### Planned Providers

- OpenAI
- Google Gemini
- Anthropic Claude
- Azure OpenAI

---

## Response Parser

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
| Mock Provider | ✅ Completed |

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
- Production-Oriented Backend Design


The AI Copilot demonstrates how multiple AI-powered capabilities can be developed using a common architecture while maintaining clean code, modularity, scalability, and testability. Future AI providers can be integrated with minimal changes by reusing the shared infrastructure.

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

The **Prompt Manager** centralizes every AI prompt used throughout the application.

Instead of embedding prompts inside every Copilot module, prompts are maintained in a single location, making updates simple while ensuring consistent AI instructions.

### Responsibilities

- Centralized prompt templates
- Reusable AI prompts
- Consistent instructions
- Easier maintenance
- Reduced duplication

---

# 🏭 LLM Factory

The **LLM Factory** is responsible for creating AI provider instances based on the current application configuration.

Business logic never communicates directly with an AI provider. Instead, every module requests an AI client through the factory.

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
Mock Provider        Ollama Provider
```

Because every provider follows the same contract, switching AI providers requires only a configuration change.

### Advantages

- Easy provider replacement
- Cleaner business logic
- Better testing
- Future extensibility
- Low coupling

---

# 🤖 Ollama Integration

The project currently uses **Ollama** as the primary local AI provider.

Current model:

```text
llama3.2
```

### Benefits

- Local execution
- Offline support
- No API costs
- Better privacy
- Faster experimentation

---

# 📦 Response Parser

The **Response Parser** standardizes AI responses before they are returned to the application.

Instead of implementing response parsing inside every Copilot module, all modules reuse one shared parser.

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
Response Parser
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
- API Timeouts
- Model Configuration

Keeping configuration separate from business logic improves maintainability and flexibility.

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
      │
      ▼
Client
```

---

# 🏛️ Design Principles

AI Resume Copilot follows modern backend engineering principles.

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

# 🔄 Continuous Integration Architecture

The project also follows modern DevOps practices through **GitHub Actions**.

Current CI workflow:

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ▼
Ubuntu Runner
    │
    ▼
Install Dependencies
    │
    ▼
Run Pytest
    │
    ▼
Publish Results
```

Current Status

- ✅ Workflow configured
- ✅ Automatic execution on every push
- ✅ Dependency installation successful
- ✅ Test execution successful
- ✅ 140 automated tests passing
- ⚠️ 14 integration tests depend on a running Ollama server

---

# 📈 Future Architecture

The architecture is designed for future expansion.

Planned improvements include:

- OpenAI Integration
- Google Gemini Integration
- Anthropic Claude Integration
- Azure OpenAI Support
- Multi-provider Selection
- Response Caching
- Streaming Responses
- AI Usage Analytics
- Mocked AI Integration for CI
- Production CI/CD Pipeline



The architecture of AI Resume Copilot emphasizes modularity, maintainability, scalability, and testability. By separating AI providers from business logic and introducing shared components such as the **Prompt Manager**, **LLM Factory**, and **Response Parser**, the project remains easy to extend while supporting modern backend engineering practices.

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

Provides AI-powered improvement suggestions while preserving the original content.

---

### Cover Letter Generator

```http
POST /copilot/cover-letter
```

Generates personalized cover letters based on resume, company, and job role.

---

### Career Advisor

```http
POST /copilot/career-advice
```

Provides AI-generated career guidance and learning recommendations.

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

Converts AI-generated outputs into clear and human-readable explanations.

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
- Interactive API documentation

---

# 🚀 API Highlights

- RESTful Architecture
- FastAPI Framework
- Automatic OpenAPI Documentation
- Swagger UI Support
- ReDoc Support
- Standardized JSON Responses
- Request Validation with Pydantic
- Modular Endpoint Design
- Docker-Compatible Deployment

---

# 🧪 Testing & Development

AI Resume Copilot follows a **test-driven** and **container-first** development workflow. Every major feature is validated through automated testing before being committed.

Current testing status:

| Category | Status |
|----------|--------|
| Total Tests (Local) | ✅ 154 Passed |
| GitHub Actions | ✅ Configured |
| GitHub CI Tests | ✅ 140 Passed |
| Remaining Tests | ⚠️ 14 (Ollama Integration) |
| Docker Verification | ✅ Completed |

---

# 🔄 Development Workflow

```text
Develop Feature
      │
      ▼
Write Tests
      │
      ▼
Run Local Pytest
      │
      ▼
Run Docker
      │
      ▼
Commit Changes
      │
      ▼
Push to GitHub
      │
      ▼
GitHub Actions
      │
      ▼
Automatic Test Execution
```

---

# 🎯 Continuous Integration

GitHub Actions automatically validates the project whenever code is pushed to the repository.

Current workflow performs:

- Repository Checkout
- Python Setup
- Dependency Installation
- Automated Test Execution
- CI Status Reporting

### Current CI Result

```text
GitHub Actions

✔ Workflow Created
✔ Dependencies Installed
✔ 140 Tests Passed
⚠ 14 Tests Waiting for Ollama Mocking
```

These remaining integration tests will be updated in a future revision by mocking the Ollama provider so that the entire CI pipeline becomes independent of external AI services.

---

# 🗺️ Roadmap

AI Resume Copilot is being developed as a production-inspired AI backend application. The project will continue to evolve with new AI capabilities, backend improvements, deployment features, and DevOps practices.

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

## DevOps

- GitHub Repository
- GitHub Actions Workflow
- Automated CI Pipeline
- Automatic Pytest Execution
- Continuous Integration Setup

---

## Testing

- Unit Testing
- API Testing
- Integration Testing
- Docker Verification
- GitHub Actions Integration
- 154 Passing Tests (Local)
- 140 Passing Tests (GitHub Actions)

---

# 🚧 Upcoming Features

The next development milestones include:

- Mock Ollama for GitHub Actions
- 154 Passing Tests in CI
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
- Production CI/CD Pipeline
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

AI Resume Copilot aims to become a complete AI-powered career platform that assists users throughout their professional journey.

Future capabilities include:

- AI Resume Builder
- Portfolio Generator
- LinkedIn Profile Analyzer
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
- DevOps

---

# ⭐ Project Summary

AI Resume Copilot is a production-inspired AI backend application built using **FastAPI**, **Ollama**, **Docker**, and **GitHub Actions**. The project demonstrates modern backend engineering through modular architecture, AI integration, provider abstraction, automated testing, Docker-based deployment, and Continuous Integration.

---

## 🚀 Current Achievements

- 🤖 AI-Powered Resume Analysis
- 📝 Resume Rewriter & Resume Improver
- 💼 Career Advisor
- 📄 Cover Letter Generator
- 🎯 ATS Analysis
- 📊 Resume Analytics
- 🎤 Interview Preparation
- 📚 Training Recommendation
- 🧠 Provider-Based AI Architecture
- ⚙️ Shared Prompt Management
- 🔄 Shared Response Parser
- 🐳 Dockerized Backend
- 🐧 WSL2 Development Environment
- 📚 Interactive API Documentation
- 🔄 GitHub Actions CI Pipeline
- 🧪 Automated Testing
- 🏗️ Modular & Scalable Architecture

---

# 📊 Project Statistics

| Category | Status |
|----------|--------|
| AI Engines | ✅ 8 Modules |
| AI Copilot Features | ✅ 6 Modules |
| REST APIs | ✅ Available |
| Docker Support | ✅ Completed |
| GitHub Actions | ✅ Configured |
| AI Provider | ✅ Ollama |
| Local Tests | ✅ 154 Passed |
| GitHub CI | ✅ 140 Passed |
| Documentation | ✅ Complete |

---

# 📅 Latest Development Update

## Day 09 – Docker & Continuous Integration

### Completed

- Installed Docker Desktop
- Configured WSL2
- Installed Ubuntu
- Built Docker Image
- Configured Docker Compose
- Successfully ran FastAPI inside Docker
- Added GitHub Actions workflow
- Configured automated testing on every push
- Fixed missing sample resume file in Git tracking
- Investigated GitHub Actions failures
- Identified Ollama dependency as the remaining CI limitation

### Current Status

```text
Local Development
✔ 154 / 154 Tests Passed

GitHub Actions
✔ Workflow Running
✔ Dependencies Installed
✔ 140 Tests Passed
⚠ 14 Integration Tests Require Ollama
```

### Next Milestone

- Mock Ollama during automated testing
- Achieve **154 / 154 passing tests** in GitHub Actions
- Continue production-ready CI/CD improvements

---

### Thank You

Thank you for exploring **AI Resume Copilot**.

This project represents an ongoing journey of learning **Backend Development**, **Artificial Intelligence**, **Software Architecture**, **Docker**, **Testing**, **GitHub Actions**, and **DevOps** while following modern software engineering practices.

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!