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

AI Resume Copilot is a production-inspired backend application built with **FastAPI** that uses **Large Language Models (LLMs)** to analyze resumes, improve ATS compatibility, rewrite resume content, generate cover letters, provide career guidance, recommend learning paths, and assist users throughout the job application process.

The project follows modern backend engineering practices, including:

- Modular Architecture
- Provider-Based AI Design
- Dependency Injection
- Shared Prompt Management
- Shared Response Parsing
- Environment-Based Configuration
- Automated Testing
- Docker Containerization
- Continuous Integration using GitHub Actions

The application currently integrates **Ollama** with the **Llama 3.2** model for local AI inference while supporting a **Mock Provider** for testing. Application configuration is now managed through **environment variables (`.env`)**, improving portability and making the project more production-ready. The backend is fully containerized using Docker and includes an automated GitHub Actions workflow that validates the project on every push.

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
- Environment-Based Configuration
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
- Environment Variable Management

---

# 🏗️ Project Architecture

The project follows a modular backend architecture where every component has a single responsibility. This improves maintainability, scalability, testing, and future feature development.

```
                +----------------------+
                |      FastAPI API     |
                +----------+-----------+
                           |
                           ▼
                 API Routes / Controllers
                           |
                           ▼
                 Business Logic Services
                           |
                           ▼
                  AI Engine Modules
                           |
                           ▼
               LLM Factory (Provider Layer)
                    /                \
                   /                  \
          Ollama Provider      Mock Provider
                   |
                   ▼
              Llama 3.2 Model

Configuration
      │
      ▼
 Environment Variables (.env)

Deployment
      │
      ▼
 Docker • Docker Compose

Automation
      │
      ▼
 GitHub Actions (CI)
```

---

# 📂 Project Structure

```text
AI-RESUME-COPILOT
│
├── app/
│   ├── ai_engine/
│   │   ├── analytics/
│   │   ├── copilot/
│   │   ├── interview/
│   │   ├── parser/
│   │   ├── recommender/
│   │   ├── training/
│   │   └── prompts/
│   │
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   └── services/
│
├── tests/
├── uploads/
├── deployment/
├── docs/
├── frontend/
├── notebooks/
├── storage/
├── .github/
│   └── workflows/
├── Dockerfile
├── requirements.txt
├── pyproject.toml
├── README.md
└── .env (Local Only)
```

---

# ⚙️ Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12 |
| Backend Framework | FastAPI |
| AI Model | Llama 3.2 |
| AI Provider | Ollama |
| Testing | Pytest |
| API Validation | Pydantic |
| PDF Parser | PyMuPDF, PyPDF2 |
| DOCX Parser | python-docx |
| HTTP Client | Requests |
| Containerization | Docker |
| CI | GitHub Actions |
| Configuration | python-dotenv |
| Version Control | Git & GitHub |

---

# 🎯 Design Principles

The application follows several backend engineering principles:

- Modular Design
- Separation of Concerns
- Provider-Based AI Architecture
- Dependency Injection
- Environment-Based Configuration
- Test-Driven Development
- Containerized Deployment
- Continuous Integration
- Scalable Project Structure

---

# 🌍 Configuration Management

Application configuration is managed using **environment variables** instead of hardcoded values.

Current configuration includes:

- LLM Provider
- LLM Model
- Ollama Base URL
- Request Timeout
- Temperature Settings

This approach makes the application portable across local development, Docker containers, and CI environments without changing the source code.

---

# 🚀 Getting Started

Follow these steps to set up AI Resume Copilot on your local machine.

---

# 📋 Prerequisites

Before starting, ensure the following software is installed:

- Python 3.12 or later
- Git
- Docker Desktop
- WSL2 (Windows)
- Ubuntu (WSL)
- Ollama
- Visual Studio Code

---

# 📥 Clone the Repository

```bash
git clone https://github.com/diveshkate11-collab/ai-resume-analyzer.git
cd ai-resume-analyzer
```

---

# 🐍 Create a Virtual Environment

```bash
python -m venv .venv
```

---

# ▶️ Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

# ⚙️ Environment Configuration

Create a local **`.env`** file in the project root.

```env
LLM_PROVIDER=ollama
LLM_MODEL=llama3.2
LLM_TIMEOUT=60
LLM_TEMPERATURE=0.3
OLLAMA_BASE_URL=http://localhost:11434
```

> **Note:** The `.env` file is ignored by Git and should never be committed.

---

# 🤖 Start Ollama

Ensure Ollama is installed.

Pull the model:

```bash
ollama pull llama3.2
```

Start Ollama:

```bash
ollama serve
```

---

# ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# 🐳 Run with Docker

Build and start the project:

```bash
docker compose -f deployment/docker-compose.yml up --build
```

Run in detached mode:

```bash
docker compose -f deployment/docker-compose.yml up -d
```

Stop containers:

```bash
docker compose -f deployment/docker-compose.yml down
```

---

# 🧪 Run Automated Tests

Execute all tests locally:

```bash
pytest
```

or

```bash
python -m pytest
```

Current local status:

```text
154 Passed
```

---

# 🔄 Continuous Integration

GitHub Actions automatically executes the test suite whenever code is pushed to the repository.

Current CI status:

- ✅ Workflow Configured
- ✅ Dependencies Installed
- ✅ Tests Running Automatically
- ⚠️ Remaining integration tests depend on a running Ollama instance

---

# 📌 Development Workflow

```text
Write Code
     │
     ▼
Run Local Tests
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

# 🐳 Docker & Deployment

AI Resume Copilot is fully containerized using Docker, allowing the application to run consistently across Windows, Linux, and macOS without manual dependency management.

---

# 🚀 Docker Features

- Docker Desktop Integration
- Docker Compose Support
- FastAPI Containerization
- WSL2 Compatibility
- Ubuntu Development Environment
- Consistent Development Workflow
- Production-Ready Deployment

---

# 📂 Docker Files

| File | Purpose |
|------|---------|
| Dockerfile | Builds the application image |
| deployment/docker-compose.yml | Runs the application container |
| .dockerignore | Excludes unnecessary files during image creation |

---

# 🔨 Build Docker Image

```bash
docker compose -f deployment/docker-compose.yml build
```

---

# ▶️ Start Application

```bash
docker compose -f deployment/docker-compose.yml up
```

Run in detached mode:

```bash
docker compose -f deployment/docker-compose.yml up -d
```

---

# 🛑 Stop Application

```bash
docker compose -f deployment/docker-compose.yml down
```

---

# 🌐 Application URLs

| Service | URL |
|----------|-----|
| FastAPI | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

---

# 📦 Deployment Workflow

```text
Developer
    │
    ▼
Git Repository
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
FastAPI Backend
    │
    ▼
Browser / API Client
```

---

# ✅ Docker Verification

Successfully completed:

- Docker Desktop Installation
- WSL2 Configuration
- Ubuntu Integration
- Dockerfile Creation
- Docker Compose Setup
- FastAPI Container Deployment
- Swagger API Verification
- REST API Verification

Current Status

```text
Docker Environment Ready
FastAPI Running Successfully
Container Build Successful
```

---

# ⚙️ Environment Configuration

Application settings are loaded from a local `.env` file.

Current configuration:

```env
LLM_PROVIDER=ollama
LLM_MODEL=llama3.2
LLM_TIMEOUT=60
LLM_TEMPERATURE=0.3
OLLAMA_BASE_URL=http://localhost:11434
```

Benefits:

- No hardcoded configuration
- Easy environment switching
- Docker-friendly configuration
- Production-ready setup
- Git-safe local configuration

> The `.env` file is ignored using `.gitignore` and is never committed to GitHub.

---

# 🔄 Continuous Integration

The project includes an automated GitHub Actions workflow.

Every push automatically:

- Checks out the repository
- Sets up Python
- Installs project dependencies
- Runs the complete pytest suite
- Reports CI results

Workflow:

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
Run Tests
      │
      ▼
Publish Results
```

---

# 📊 Current CI Status

| Component | Status |
|-----------|--------|
| GitHub Actions | ✅ Configured |
| Workflow | ✅ Running |
| Docker Support | ✅ Verified |
| Dependency Installation | ✅ Successful |
| Local Configuration | ✅ Environment Variables |
| Passing Tests | ✅ 140 |
| Remaining Tests | ⚠️ 14 (Require Ollama) |

---

# 🔧 Troubleshooting

## Docker Build Issues

```bash
docker compose -f deployment/docker-compose.yml build --no-cache
```

---

## Container Not Starting

Check:

- Docker Desktop is running
- WSL2 is enabled
- Port **8000** is available
- Dependencies installed successfully

---

## Ollama Connection Error

If you receive:

```text
Connection refused: localhost:11434
```

Run:

```bash
ollama serve
```

Verify installed models:

```bash
ollama list
```

---

## GitHub Actions Failure

Current GitHub Actions failures are limited to integration tests requiring a live Ollama server.

Planned solution:

- Replace live Ollama calls with the Mock Provider during CI.
- Keep Ollama for local development.
- Achieve a fully passing GitHub Actions pipeline.

---

# 🧠 AI Engine

The AI Engine is the intelligence layer of AI Resume Copilot. It is responsible for processing resumes, interacting with Large Language Models (LLMs), generating AI-powered responses, and providing career-related assistance.

The engine is designed using a modular architecture where every component has a single responsibility, making the system scalable, maintainable, and easy to test.

---

# 🏗️ AI Engine Architecture

```text
                  Resume
                     │
                     ▼
              Resume Parser
                     │
                     ▼
              Extracted Text
                     │
        ┌────────────┼─────────────┐
        ▼            ▼             ▼
 ATS Analysis   Resume Analytics  Job Matching
        │            │             │
        └────────────┼─────────────┘
                     ▼
              Prompt Manager
                     │
                     ▼
               LLM Factory
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
   Ollama Provider         Mock Provider
                     │
                     ▼
             Response Parser
                     │
                     ▼
              JSON Response
```

---

# 📄 Resume Parser

Extracts structured text from uploaded resumes.

### Supported Formats

- PDF
- DOCX

### Responsibilities

- Read uploaded resumes
- Extract text content
- Remove unnecessary formatting
- Prepare data for AI processing

---

# 📊 ATS Analysis

Evaluates resume quality for Applicant Tracking Systems (ATS).

### Features

- ATS Score
- Keyword Matching
- Missing Skills Detection
- Resume Suggestions
- Resume Quality Analysis

---

# ✨ Resume Improvement

Generates AI-powered recommendations to improve resume quality.

### Capabilities

- Grammar Improvements
- Professional Writing
- Better Action Verbs
- ATS Optimization
- Readability Enhancement

---

# 💼 Job Matching

Compares resumes with job descriptions.

### Output

- Match Percentage
- Missing Skills
- Strength Analysis
- Improvement Suggestions

---

# 📈 Resume Analytics

Provides statistical insights about resumes.

### Metrics

- Technical Skills
- Soft Skills
- Experience Summary
- Projects
- ATS Metrics

---

# 🎤 Interview Preparation

Generates personalized interview questions based on resume content.

### Categories

- Technical Questions
- HR Questions
- Behavioral Questions
- Project-Based Questions

---

# 📚 Training Recommendation

Suggests learning resources based on missing skills.

### Recommendations

- Technologies
- Certifications
- Learning Paths
- Career Development

---

# 🧩 Shared AI Components

All AI modules use a common infrastructure.

## Prompt Manager

Responsible for:

- Prompt Templates
- Prompt Organization
- Reusable Prompt Library

---

## LLM Factory

Creates the appropriate AI provider during runtime.

### Supported Providers

- Ollama
- Mock Provider

### Planned Providers

- OpenAI
- Google Gemini
- Claude
- Azure OpenAI

---

## Response Parser

Processes AI responses into a standardized format.

### Responsibilities

- Response Parsing
- JSON Formatting
- Error Handling
- Output Validation

---

# 🔄 AI Processing Workflow

```text
Resume Upload
      │
      ▼
Resume Parser
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
Generated Response
      │
      ▼
Response Parser
      │
      ▼
Structured JSON Response
```

---

# ✅ Current Status

| Module | Status |
|---------|--------|
| Resume Parser | ✅ Completed |
| ATS Analysis | ✅ Completed |
| Resume Improvement | ✅ Completed |
| Resume Analytics | ✅ Completed |
| Job Matching | ✅ Completed |
| Interview Preparation | ✅ Completed |
| Training Recommendation | ✅ Completed |
| Prompt Manager | ✅ Completed |
| LLM Factory | ✅ Completed |
| Response Parser | ✅ Completed |
| Ollama Integration | ✅ Completed |
| Mock Provider | 🚧 CI Integration in Progress |


The AI Engine follows a modular and provider-based architecture, allowing new AI providers and intelligent features to be integrated with minimal changes to the existing codebase. It is designed for scalability, maintainability, automated testing, and future production deployment.

---

# 🏗️ AI Architecture

AI Resume Copilot follows a provider-based architecture that separates business logic from AI providers. This design keeps the application modular, scalable, testable, and easy to maintain.

The business logic never communicates directly with an AI model. Instead, every request passes through shared infrastructure before reaching the selected provider.

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
 Prompt Manager  LLM Factory  Response Parser
                    │
                    ▼
           Selected AI Provider
          ┌─────────┴─────────┐
          ▼                   ▼
  Ollama Provider      Mock Provider
          │
          ▼
      AI Response
          │
          ▼
 Structured JSON Response
```

---

# 📝 Prompt Manager

The Prompt Manager stores and organizes all AI prompts used throughout the application.

Instead of writing prompts inside every AI module, prompts are managed from one location.

### Responsibilities

- Centralized Prompt Templates
- Reusable Prompts
- Consistent AI Instructions
- Easy Prompt Maintenance
- Reduced Code Duplication

---

# 🏭 LLM Factory

The LLM Factory creates the appropriate AI provider during runtime.

Application services never communicate directly with an AI provider.

### Supported Providers

- Ollama
- Mock Provider

### Planned Providers

- OpenAI
- Google Gemini
- Claude
- Azure OpenAI

---

# 🤖 Ollama Provider

The project currently uses Ollama for local AI inference.

Current model:

- Llama 3.2

### Benefits

- Local AI Execution
- Offline Capability
- No API Cost
- Better Privacy
- Fast Development

---

# 🧪 Mock Provider

A Mock Provider is included to support automated testing.

It allows AI-related features to be tested without requiring a running AI server.

### Advantages

- Faster Testing
- Deterministic Responses
- CI Compatibility
- Independent Test Execution

---

# 📦 Response Parser

The Response Parser converts AI responses into a consistent format before returning them to the application.

### Responsibilities

- Response Parsing
- JSON Formatting
- Error Handling
- Response Validation
- Consistent Output Structure

---

# 🔄 AI Request Lifecycle

```text
User Request
      │
      ▼
FastAPI Endpoint
      │
      ▼
Business Service
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
AI Response
      │
      ▼
Response Parser
      │
      ▼
JSON Response
```

---

# 🏛️ Software Design Principles

The project follows modern software engineering principles.

### Principles

- Single Responsibility Principle
- Separation of Concerns
- Dependency Injection
- Factory Pattern
- Provider Abstraction
- Modular Architecture
- Low Coupling
- High Cohesion

---

# 🔄 Continuous Integration

GitHub Actions automatically validates the project whenever new code is pushed to the repository.

Current workflow:

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

Current status:

- ✅ Workflow Configured
- ✅ Automatic Test Execution
- ✅ Dependency Installation
- ✅ 140 Tests Passing
- ⚠️ Remaining integration tests require a running Ollama server

---

# 🚀 Future Improvements

Planned architecture enhancements include:

- OpenAI Provider
- Google Gemini Provider
- Claude Provider
- Azure OpenAI Provider
- Response Caching
- Streaming Responses
- Database Integration
- Background Task Processing
- Production CI/CD Pipeline
- Complete Mock-Based CI Testing


The provider-based architecture allows AI Resume Copilot to support multiple LLM providers while keeping business logic independent from implementation details. This design improves scalability, maintainability, automated testing, and future extensibility.

---

# 🌐 REST API

AI Resume Copilot exposes a RESTful API built with **FastAPI**. The API is organized into independent modules, allowing each feature to be developed, tested, and maintained separately.

All endpoints return structured JSON responses and are documented automatically using the OpenAPI specification.

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

# 📄 Resume APIs

### Upload Resume

```http
POST /api/resume/upload
```

Uploads and parses PDF or DOCX resumes for further processing.

---

# 📊 Resume Improvement APIs

### Analyze Resume

```http
POST /api/improvement/analyze
```

Analyzes resume quality and provides AI-powered improvement suggestions.

---

# 💼 Job Recommendation APIs

### Recommend Jobs

```http
POST /api/jobs/recommend
```

Generates job recommendations based on resume content and extracted skills.

---

# 🎤 Interview APIs

### Generate Interview Questions

```http
POST /api/interview/questions
```

Creates personalized interview questions based on the uploaded resume.

---

### Evaluate Interview Answer

```http
POST /api/interview/evaluate
```

Evaluates user answers and provides AI-generated feedback.

---

# 🤖 AI Copilot APIs

### Rewrite Resume

```http
POST /api/copilot/rewrite
```

Professionally rewrites resume sections while maintaining the original meaning.

---

### Improve Resume

```http
POST /api/copilot/improve
```

Provides AI-driven suggestions to improve clarity, impact, and ATS compatibility.

---

### Generate Cover Letter

```http
POST /api/copilot/cover-letter
```

Creates a personalized cover letter using resume information and job details.

---

### Career Advice

```http
POST /api/copilot/career-advice
```

Provides AI-powered career guidance and learning recommendations.

---

### Job Description Match

```http
POST /api/copilot/job-match
```

Compares a resume against a job description and identifies missing skills.

---

### Explain Resume

```http
POST /api/copilot/explain
```

Explains resume improvements and AI-generated suggestions in simple language.

---

# 🔄 API Request Lifecycle

```text
Client
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
    "message": "Request processed successfully",
    "data": {}
}
```

---

# ❌ Standard Error Response

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

# 🧪 Automated Testing

The REST API is validated using **Pytest** through unit tests, API tests, and integration tests.

Current testing status:

| Category | Status |
|----------|--------|
| Local Testing | ✅ 154 Passed |
| GitHub Actions | ✅ Configured |
| CI Passing Tests | ✅ 140 |
| Remaining CI Tests | ⚠️ 14 (Require Ollama) |

---

# 🔄 Continuous Integration

Every push to the **main** branch automatically triggers GitHub Actions.

The workflow performs:

- Repository Checkout
- Python Environment Setup
- Dependency Installation
- Automated Test Execution
- CI Status Reporting

This ensures code quality is continuously validated before future deployments.

---

# 🚀 API Highlights

- RESTful API Design
- FastAPI Framework
- Automatic OpenAPI Documentation
- Swagger UI
- ReDoc Documentation
- Pydantic Request Validation
- Modular Route Structure
- Docker Ready
- GitHub Actions Integration
- Automated Testing

---

# 🗺️ Roadmap

AI Resume Copilot is being developed as a production-inspired AI backend application. The project will continue to evolve with additional AI capabilities, backend improvements, DevOps practices, and deployment features.

---

# ✅ Completed

## Backend

- FastAPI REST API
- Modular Project Structure
- Service Layer Architecture
- Request Validation
- Error Handling

---

## AI Features

- Resume Parser
- ATS Analysis
- Resume Improvement
- Resume Rewriter
- Resume Analytics
- Career Advisor
- Cover Letter Generator
- Job Description Matcher
- Interview Preparation
- Training Recommendation

---

## AI Infrastructure

- Prompt Manager
- LLM Factory
- Ollama Provider
- Mock Provider
- Response Parser
- Provider-Based Architecture

---

## Testing

- Unit Testing
- API Testing
- Integration Testing
- Pytest Configuration
- GitHub Actions Workflow
- Local Test Verification

---

## DevOps

- Git
- GitHub
- Docker
- Docker Compose
- WSL2
- Ubuntu Development Environment
- Continuous Integration

---

# 🚧 In Progress

The following improvements are currently under development:

- Mock Provider Integration for CI
- GitHub Actions Test Improvements
- Complete CI Compatibility
- Production Deployment Preparation

---

# 📌 Upcoming Features

Future development includes:

- PostgreSQL Integration
- SQLAlchemy ORM
- Alembic Migrations
- JWT Authentication
- User Accounts
- Resume History
- File Management
- Background Tasks
- Logging
- Monitoring
- API Versioning
- Role-Based Authorization

---

# ☁️ Deployment Targets

Planned deployment platforms:

- Railway
- Render
- Microsoft Azure
- AWS
- Google Cloud Platform
- DigitalOcean

---

# 🎯 Long-Term Vision

The goal of AI Resume Copilot is to become a complete AI-powered career platform.

Planned capabilities include:

- AI Resume Builder
- Portfolio Generator
- LinkedIn Profile Analyzer
- GitHub Profile Analyzer
- AI Mock Interview
- Salary Insights
- Career Progress Tracking
- AI Career Coach
- Multi-Language Support
- Recruiter Dashboard

---

# 📊 Current Project Status

| Category | Status |
|----------|--------|
| Backend | ✅ Completed |
| AI Engine | ✅ Completed |
| REST APIs | ✅ Completed |
| Docker | ✅ Configured |
| GitHub Actions | ✅ Configured |
| Local Testing | ✅ 154 Tests Passed |
| GitHub CI | ⚠️ 140 Tests Passed |
| Remaining Work | Mock Ollama Integration |

---

# 📅 Latest Development

## Day 10 — Environment Configuration & CI Preparation

### Completed

- Added support for environment-based application configuration.
- Installed and configured **python-dotenv**.
- Refactored application settings to load values from environment variables.
- Created a local `.env` configuration for development.
- Verified that the `.env` file is ignored by Git.
- Added GitHub Actions workflow for automated testing.
- Fixed the missing sample resume file required by the test suite.
- Investigated GitHub Actions failures and identified the remaining dependency on a running Ollama server.

### Current Status

```text
Local Development
✔ Docker Running
✔ FastAPI Running
✔ Swagger Verified
✔ Environment Configuration Working
✔ 154 Tests Passed

GitHub Actions
✔ Workflow Configured
✔ Automatic Testing Enabled
✔ 140 Tests Passed
⚠ 14 Integration Tests Require Ollama
```

### Next Milestone

- Configure the Mock Provider for GitHub Actions.
- Remove the dependency on a live Ollama server during CI.
- Achieve 154 / 154 passing tests in GitHub Actions.

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Run the test suite.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

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

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Feedback, suggestions, and contributions are always welcome.

---

**Thank you for exploring AI Resume Copilot! 🚀**