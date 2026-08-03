# 🤖 AI Resume Copilot

> An AI-powered backend application that helps job seekers analyze, improve, and optimize resumes using Artificial Intelligence, Large Language Models (LLMs), modern backend engineering practices, and PostgreSQL-powered data persistence.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-FF9900?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![AI](https://img.shields.io/badge/AI-Ollama-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

---

# 📖 Overview

AI Resume Copilot is a production-inspired backend application built with **FastAPI** that uses **Large Language Models (LLMs)** to analyze resumes, improve ATS compatibility, rewrite resume content, generate cover letters, provide career guidance, recommend learning resources, and assist job seekers throughout their placement journey.

The project follows modern backend engineering practices including:

- Modular Architecture
- Provider-Based AI Design
- Dependency Injection
- Shared Prompt Management
- Shared Response Parsing
- Environment-Based Configuration
- SQLAlchemy ORM
- PostgreSQL Integration
- Alembic Database Migrations
- Automated Testing
- Docker Containerization
- Continuous Integration using GitHub Actions

The application currently integrates **Ollama** with the **Llama 3.2** model for local AI inference while supporting a **Mock Provider** for automated testing and Continuous Integration.

Configuration is managed using **environment variables (`.env`)**, allowing the same codebase to run across local development, Docker containers, CI pipelines, and future cloud deployments without changing the application source code.

The backend now includes a fully configured **PostgreSQL** database with **SQLAlchemy ORM** and **Alembic** migration support. The initial database schema has been created successfully, providing the foundation for persistent resume storage and future user-related features.

The project also includes a fully automated CI pipeline with **154 passing Pytest tests**, ensuring reliability and maintainability as new features are added.

---

# ✨ Features

## 📄 Resume Intelligence

- Resume Parsing
- ATS Analysis
- Resume Improvement
- Resume Rewriting
- Resume Analytics
- Resume Explainability

### Resume Processing

- Extract text from PDF resumes
- Extract text from DOCX resumes
- Normalize extracted resume content
- Prepare structured resume data for AI processing

### ATS Optimization

- ATS Compatibility Analysis
- Resume Quality Evaluation
- Keyword Matching
- Missing Skills Detection
- AI-Based Resume Suggestions

---

## 🤖 AI Copilot

- Career Advisor
- Cover Letter Generator
- Resume Rewriter
- Resume Improver
- Job Description Matcher
- AI Explanation Engine

### Planned AI Capabilities

- AI Resume Builder
- Portfolio Generator
- LinkedIn Profile Analysis
- GitHub Profile Analysis
- Career Roadmap Generator

---

## 🧠 AI Infrastructure

- Prompt Manager
- LLM Factory
- Provider-Based Architecture
- Ollama Integration
- Mock Provider
- Shared Response Parser
- Environment-Based Configuration

### Current Providers

- Ollama
- Mock Provider

### Planned Providers

- OpenAI
- Google Gemini
- Claude
- Azure OpenAI

---

## 🗄️ Database Infrastructure

The application now includes a dedicated persistence layer powered by PostgreSQL.

Current capabilities include:

- PostgreSQL 18
- SQLAlchemy ORM
- Alembic Migration Management
- Declarative ORM Models
- Database Session Management
- Environment-Based Database Configuration
- Resume Model
- Migration Version Control

Current database tables:

- resumes
- alembic_version

---

## 🚀 Additional AI Engines

- Resume Analytics
- Interview Preparation
- Job Recommendation
- Training Recommendation

### Future AI Engines

- Salary Prediction
- Career Progress Tracking
- AI Career Coach

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

Current deployment workflow supports:

- Local Development
- PostgreSQL Integration
- Database Migrations
- Automated Testing
- Continuous Integration

---

# 🏗️ Project Architecture

AI Resume Copilot follows a layered architecture where each component has a single responsibility. This separation makes the application easier to maintain, test, and extend as new AI features are added.

```text
                           Client
                              │
                              ▼
                     FastAPI REST API
                              │
                              ▼
                    API Routes / Endpoints
                              │
                              ▼
                      Business Services
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   Resume Engine         AI Copilot         Career Services
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              ▼
                      Prompt Management
                              │
                              ▼
                         LLM Factory
                    ┌─────────┴─────────┐
                    ▼                   ▼
             Ollama Provider      Mock Provider
                    │
                    ▼
                Llama 3.2 Model

────────────────────────────────────────────────────

Configuration Layer
        │
        ▼
Environment Variables (.env)

────────────────────────────────────────────────────

Persistence Layer
        │
        ▼
SQLAlchemy ORM
        │
        ▼
PostgreSQL Database
        │
        ▼
Alembic Migrations
```

---

# 📂 Project Structure

```text
AI-RESUME-COPILOT
│
├── .github/
│   └── workflows/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── app/
│   ├── ai_engine/
│   │   ├── analytics/
│   │   ├── ats/
│   │   ├── copilot/
│   │   ├── explainability/
│   │   ├── improvement/
│   │   ├── interview/
│   │   ├── jobs/
│   │   ├── parser/
│   │   ├── training/
│   │   └── utils/
│   │
│   ├── api/
│   ├── core/
│   ├── database/
│   │   ├── base.py
│   │   ├── connection.py
│   │   ├── migrations.py
│   │   └── seed.py
│   │
│   ├── models/
│   ├── prompts/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── __init__.py
│   └── main.py
│
├── data/
├── deployment/
├── docs/
├── frontend/
├── notebooks/
├── storage/
├── tests/
├── uploads/
│
├── .dockerignore
├── .env
├── .gitignore
├── alembic.ini
├── Dockerfile
├── LICENSE
├── pyproject.toml
├── README.md
└── requirements.txt
```

---

# 💻 Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.12 |
| Backend Framework | FastAPI |
| Database | PostgreSQL 18 |
| ORM | SQLAlchemy 2.x |
| Database Migration | Alembic |
| Database Driver | psycopg2-binary |
| AI Framework | Ollama |
| LLM | Llama 3.2 |
| Data Validation | Pydantic |
| Testing | Pytest |
| API Testing | HTTPX |
| PDF Processing | PyMuPDF |
| DOCX Processing | python-docx |
| Configuration | python-dotenv |
| Containerization | Docker |
| Version Control | Git & GitHub |
| CI/CD | GitHub Actions |
| Operating System | Ubuntu (WSL2) |

---

# 🏛️ Design Principles

The project is developed using modern software engineering and backend development practices.

### Software Engineering

- Modular Design
- Separation of Concerns
- High Cohesion
- Low Coupling
- Scalable Architecture

### Backend Engineering

- RESTful API Design
- Environment-Based Configuration
- Database Version Control
- ORM-Based Database Access
- Layered Application Structure

### AI Engineering

- Provider-Based Architecture
- Prompt Management
- Shared Response Parsing
- Extensible LLM Factory

### Database Engineering

- PostgreSQL as the primary relational database
- SQLAlchemy Declarative ORM
- Alembic Versioned Database Migrations
- Environment-based database configuration
- Persistent resume data storage

---

# ⚙️ Configuration Management

Application configuration is centralized through environment variables.

Sensitive information such as database credentials, API keys, and provider settings are stored inside the local `.env` file and are never committed to version control.

Current configurable components include:

- LLM Provider
- LLM Model
- Ollama Base URL
- Database Host
- Database Port
- Database Name
- Database Username
- Database Password
- LLM Temperature
- Request Timeout

This approach allows the same application to run across local development, Docker containers, CI pipelines, and future production deployments without modifying the source code.

---

# 🎯 Architecture Highlights

- Modular FastAPI backend
- Provider-based AI architecture
- SQLAlchemy ORM integration
- PostgreSQL persistence layer
- Alembic migration management
- Environment-driven configuration
- Docker-ready development environment
- GitHub Actions Continuous Integration
- Production-inspired project organization

---

# 🧩 Core Project Modules

The project is organized into multiple independent modules, each responsible for a specific functionality. This modular design improves maintainability, scalability, readability, and testing.

---

## 📄 Resume Parser

The Resume Parser is responsible for extracting structured information from uploaded resumes.

### Responsibilities

- Extract text from PDF resumes
- Extract text from DOCX resumes
- Clean extracted content
- Normalize formatting
- Prepare text for AI processing

### Planned Improvements

- OCR Support
- Multi-language Resume Parsing
- Image Resume Parsing
- Better Formatting Detection

---

## 🎯 ATS Analysis Engine

The ATS Analysis Engine evaluates resumes based on Applicant Tracking System (ATS) standards.

### Current Capabilities

- ATS Compatibility Analysis
- Resume Quality Evaluation
- Keyword Detection
- Missing Skills Identification
- Improvement Suggestions

### Future Enhancements

- Company-Specific ATS Rules
- Industry-Based Resume Scoring
- Job Description Comparison
- ATS Score Prediction

---

## ✍️ Resume Improvement Engine

This module generates actionable suggestions to improve resume quality.

Current objectives include:

- Improve grammar
- Improve readability
- Improve professional wording
- Remove unnecessary content
- Optimize formatting recommendations
- Enhance ATS compatibility

Future enhancements include:

- Industry-specific recommendations
- Role-based resume optimization
- Experience-based improvement suggestions

---

## 🔄 Resume Rewriter

The Resume Rewriter uses the configured LLM provider to rewrite resume content while preserving meaning.

Capabilities include:

- Professional language enhancement
- Improved sentence structure
- Better impact statements
- ATS-friendly wording
- Consistent formatting recommendations

Future enhancements:

- Senior-level resume rewriting
- Fresher resume templates
- Executive resume optimization

---

## 🧠 AI Copilot

The AI Copilot acts as the central intelligent assistant within the application.

Current modules include:

- Career Advisor
- Resume Improvement
- Resume Rewriting
- Cover Letter Generation
- Resume Explanation
- Job Description Matching

Planned capabilities include:

- AI Career Coach
- Personalized Learning Recommendations
- Resume Builder
- Portfolio Assistant

---

## 📊 Resume Analytics

The analytics module provides deeper insights into resume quality.

Current capabilities:

- Resume Quality Analysis
- ATS Readiness
- Skill Identification
- Section Completeness
- Improvement Recommendations

Future capabilities:

- Resume Trend Analysis
- Historical Resume Comparison
- Skill Gap Visualization
- Career Growth Tracking

---

## 💼 Job Recommendation Engine

The project includes a dedicated module for job-related recommendations.

Current focus:

- Resume-to-Job Matching
- Skill-Based Recommendations
- Job Description Comparison

Future roadmap:

- Personalized Job Recommendations
- Company Recommendation Engine
- Location-Based Jobs
- Salary Estimation

---

## 🎤 Interview Preparation

The Interview module helps users prepare for technical and HR interviews.

Planned features include:

- HR Interview Questions
- Technical Interview Questions
- AI-Based Interview Practice
- Mock Interviews
- Answer Evaluation
- Personalized Feedback

---

## 📚 Training Recommendation

The Training module recommends learning resources based on identified skill gaps.

Future recommendations may include:

- Online Courses
- Certifications
- Practice Platforms
- Books
- Interview Preparation Resources
- Personalized Learning Paths

---

# 🗄️ Database Layer

The project now includes a fully configured relational database layer.

Current implementation includes:

- PostgreSQL database
- SQLAlchemy ORM
- Declarative Base
- Session Management
- Resume ORM Model
- Alembic Migration System
- Version-Controlled Database Schema

### Database Tables

Current tables:

- `resumes`
- `alembic_version`

Future tables may include:

- users
- resumes_history
- cover_letters
- interview_sessions
- job_matches
- activity_logs

---

# 🔄 Application Workflow

The current backend workflow follows this sequence:

```text
User
 │
 ▼
Upload Resume
 │
 ▼
Resume Parser
 │
 ▼
Resume Processing
 │
 ▼
AI Engine
 │
 ├── ATS Analysis
 ├── Resume Improvement
 ├── Resume Rewriting
 ├── Resume Analytics
 └── Career Guidance
 │
 ▼
Database Storage (PostgreSQL)
 │
 ▼
FastAPI Response
 │
 ▼
Client
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Resume-Copilot.git

cd AI-Resume-Copilot
```

---

## 2️⃣ Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Linux / macOS

```bash
python3 -m venv .venv
```

---

## 3️⃣ Activate Virtual Environment

Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

Windows (CMD)

```cmd
.venv\Scripts\activate.bat
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install -e .
```

---

# 🐘 PostgreSQL Setup

Install PostgreSQL 18 and create a database.

```sql
CREATE DATABASE ai_resume_copilot;
```

Verify the database:

```sql
\l
```

Connect to the database:

```sql
\c ai_resume_copilot
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

Example:

```env
LLM_PROVIDER=ollama
LLM_MODEL=llama3.2
LLM_TIMEOUT=60
LLM_TEMPERATURE=0.3

OLLAMA_BASE_URL=http://localhost:11434

DB_HOST=localhost
DB_PORT=5432
DB_NAME=ai_resume_copilot
DB_USER=postgres
DB_PASSWORD=YOUR_PASSWORD
```

> **Important:** Never commit the `.env` file or database password to GitHub. Sensitive credentials should remain local and `.env` should be included in `.gitignore`.

---

# 🗄️ Database Configuration

The application uses SQLAlchemy for database access and Alembic for migration management.

Current database components include:

- SQLAlchemy Engine
- Session Factory
- Declarative Base
- Resume ORM Model
- Alembic Migration Environment
- PostgreSQL Connection Management

The first migration creates:

- `resumes`
- `alembic_version`

---

# 🔄 Database Migration Commands

Generate a migration:

```bash
alembic revision --autogenerate -m "create resumes table"
```

Apply migrations:

```bash
alembic upgrade head
```

Check the current migration version:

```bash
alembic current
```

View migration history:

```bash
alembic history
```

---

# 🤖 Running Ollama

Start the Ollama service:

```bash
ollama serve
```

Download the model:

```bash
ollama pull llama3.2
```

Verify installed models:

```bash
ollama list
```

---

# 🚀 Running the Application

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

Default application URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

# 📦 Current Development Status

The following components have been completed:

- FastAPI project setup
- AI engine architecture
- Prompt management
- Ollama integration
- Mock provider
- Shared response parser
- Docker support
- GitHub Actions CI
- Automated testing
- PostgreSQL integration
- SQLAlchemy ORM
- Alembic migration system
- Resume ORM model
- Database connectivity
- Initial database schema
- Environment-based configuration

The project is now ready for implementing persistent resume upload APIs, resume storage services, and AI-powered resume processing using the configured PostgreSQL backend.

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Resume-Copilot.git

cd AI-Resume-Copilot
```

---

## 2️⃣ Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Linux / macOS

```bash
python3 -m venv .venv
```

---

## 3️⃣ Activate Virtual Environment

Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

Windows (CMD)

```cmd
.venv\Scripts\activate.bat
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install -e .
```

---

# 🐘 PostgreSQL Setup

Install PostgreSQL 18 and create a database.

```sql
CREATE DATABASE ai_resume_copilot;
```

Verify the database:

```sql
\l
```

Connect to the database:

```sql
\c ai_resume_copilot
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

Example:

```env
LLM_PROVIDER=ollama
LLM_MODEL=llama3.2
LLM_TIMEOUT=60
LLM_TEMPERATURE=0.3

OLLAMA_BASE_URL=http://localhost:11434

DB_HOST=localhost
DB_PORT=5432
DB_NAME=ai_resume_copilot
DB_USER=postgres
DB_PASSWORD=YOUR_PASSWORD
```

> **Important:** Never commit the `.env` file or database password to GitHub. Sensitive credentials should remain local and `.env` should be included in `.gitignore`.

---

# 🗄️ Database Configuration

The application uses SQLAlchemy for database access and Alembic for migration management.

Current database components include:

- SQLAlchemy Engine
- Session Factory
- Declarative Base
- Resume ORM Model
- Alembic Migration Environment
- PostgreSQL Connection Management

The first migration creates:

- `resumes`
- `alembic_version`

---

# 🔄 Database Migration Commands

Generate a migration:

```bash
alembic revision --autogenerate -m "create resumes table"
```

Apply migrations:

```bash
alembic upgrade head
```

Check the current migration version:

```bash
alembic current
```

View migration history:

```bash
alembic history
```

---

# 🤖 Running Ollama

Start the Ollama service:

```bash
ollama serve
```

Download the model:

```bash
ollama pull llama3.2
```

Verify installed models:

```bash
ollama list
```

---

# 🚀 Running the Application

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

Default application URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

# 📦 Current Development Status

The following components have been completed:

- FastAPI project setup
- AI engine architecture
- Prompt management
- Ollama integration
- Mock provider
- Shared response parser
- Docker support
- GitHub Actions CI
- Automated testing
- PostgreSQL integration
- SQLAlchemy ORM
- Alembic migration system
- Resume ORM model
- Database connectivity
- Initial database schema
- Environment-based configuration

The project is now ready for implementing persistent resume upload APIs, resume storage services, and AI-powered resume processing using the configured PostgreSQL backend.

---

# 🚀 API Overview

AI Resume Copilot is designed as a RESTful backend application using **FastAPI**. Every feature is exposed through clean, modular API endpoints, making the backend suitable for web, mobile, and desktop applications.

The API architecture separates routing, business logic, AI processing, and database operations into independent layers.

Current API architecture:

```text
Client
   │
   ▼
FastAPI Routes
   │
   ▼
Service Layer
   │
   ▼
AI Engine
   │
   ▼
Database Layer
   │
   ▼
PostgreSQL
```

---

# 📡 Planned API Modules

The backend is structured so each feature can have its own dedicated API router.

Current and planned modules include:

- Resume APIs
- ATS Analysis APIs
- Resume Improvement APIs
- Resume Rewrite APIs
- Career Guidance APIs
- Interview Preparation APIs
- Job Recommendation APIs
- Training Recommendation APIs

Future modules:

- Authentication APIs
- User Management APIs
- Dashboard APIs
- Analytics APIs

---

# 📄 Resume API

The Resume module will become the central component of the application.

Planned capabilities include:

- Upload Resume
- View Resume
- Update Resume
- Delete Resume
- Resume History
- Resume Metadata
- Resume Processing Status

Future workflow:

```text
Upload Resume
      │
      ▼
Validate File
      │
      ▼
Extract Resume Text
      │
      ▼
Store in PostgreSQL
      │
      ▼
Run AI Analysis
      │
      ▼
Return Results
```

---

# 🤖 AI Processing Pipeline

Once a resume is uploaded, it will pass through multiple AI processing stages.

Processing pipeline:

```text
Resume Upload
      │
      ▼
Parser
      │
      ▼
Resume Cleaning
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
Structured Output
      │
      ▼
Database Storage
```

Current supported provider:

- Ollama (Llama 3.2)

Current testing provider:

- Mock Provider

Future providers:

- OpenAI
- Google Gemini
- Claude
- Azure OpenAI

---

# 📁 File Processing

The application supports structured resume processing.

Supported formats:

- PDF
- DOCX

Processing stages:

- File Upload
- Validation
- Text Extraction
- Content Cleaning
- AI Processing
- Database Storage

Future support:

- Image Resume Parsing
- OCR Processing
- Multi-language Resume Support

---

# 📊 Resume Analysis Pipeline

The ATS analysis workflow consists of several independent stages.

```text
Resume
   │
   ▼
Extract Content
   │
   ▼
Skill Detection
   │
   ▼
Keyword Matching
   │
   ▼
Missing Skill Detection
   │
   ▼
Resume Scoring
   │
   ▼
Improvement Suggestions
```

Future additions:

- Company-specific ATS Rules
- Industry Benchmarks
- AI Resume Ranking
- Resume Comparison

---

# 🗄️ Database Workflow

The project now includes a fully functional PostgreSQL persistence layer.

Current workflow:

```text
FastAPI Request
      │
      ▼
SQLAlchemy Session
      │
      ▼
ORM Model
      │
      ▼
PostgreSQL Database
      │
      ▼
Commit Transaction
      │
      ▼
Return Response
```

Current database technologies:

- PostgreSQL
- SQLAlchemy ORM
- Alembic
- psycopg2

---

# 📦 Dependency Management

The project manages dependencies using modern Python tooling.

Current dependencies include:

Core

- FastAPI
- SQLAlchemy
- Alembic
- psycopg2-binary
- Pydantic
- python-dotenv

AI

- Ollama

Resume Processing

- PyMuPDF
- python-docx

Testing

- Pytest
- HTTPX

Development

- Uvicorn

Future dependencies may include:

- Redis
- Celery
- JWT Authentication
- LangChain
- OpenTelemetry

---

# 📈 Current Project Status

Completed

- FastAPI Backend
- AI Architecture
- Prompt Management
- LLM Factory
- Ollama Integration
- Mock Provider
- Docker Support
- GitHub Actions
- Automated Testing
- PostgreSQL Installation
- Database Connection
- SQLAlchemy ORM
- Alembic Setup
- Resume ORM Model
- Initial Database Migration
- Database Schema Versioning

Current Progress

- Resume Persistence Layer
- Backend Infrastructure
- AI Processing Foundation

Next Development Targets

- Resume Upload API
- Resume CRUD APIs
- Resume Storage Service
- ATS Analysis API
- Resume Improvement API
- Authentication System

---

# 🛣️ Development Roadmap

The project is being developed incrementally, with each phase building upon a stable and tested foundation. The objective is to create a production-inspired AI-powered backend application for resume analysis and career assistance.

---

# ✅ Completed Foundation

The following components have been successfully implemented:

### Backend

- FastAPI Project Setup
- Modular Project Structure
- API Layer
- Service Layer
- Configuration Management
- Environment Variable Support

### Artificial Intelligence

- Ollama Integration
- Llama 3.2 Support
- Mock Provider
- Provider-Based Architecture
- LLM Factory
- Prompt Management
- Shared Response Parsing

### Database

- PostgreSQL Installation
- PostgreSQL Database Creation
- SQLAlchemy ORM Configuration
- Database Engine
- Session Management
- Declarative Base
- Resume ORM Model
- Alembic Configuration
- Initial Database Migration
- Database Version Control
- Resume Table Creation

### Development Tools

- Docker Support
- GitHub Actions CI
- Automated Testing
- Pytest Configuration
- Project Documentation

---

# 🚧 Current Development Phase

The current focus is building the backend features on top of the completed database infrastructure.

Current tasks include:

- Resume Upload APIs
- Resume CRUD Operations
- Resume Storage Services
- Resume Retrieval
- Resume Processing Pipeline
- ATS Analysis Integration

---

# 📅 Upcoming Development

The following modules are planned for future implementation.

## Resume Management

- Resume Upload
- Resume Download
- Resume Update
- Resume Delete
- Resume Version History

---

## ATS Analysis

- ATS Score Generation
- Keyword Matching
- Missing Skill Detection
- Resume Quality Analysis
- Improvement Suggestions

---

## Resume Improvement

- Resume Rewriting
- Professional Language Enhancement
- Achievement Optimization
- Grammar Improvements
- ATS Optimization

---

## AI Career Assistant

- Career Guidance
- Learning Recommendations
- Interview Preparation
- Career Roadmaps
- Resume Review Assistant

---

## Job Intelligence

- Job Description Analysis
- Resume Matching
- Skill Gap Analysis
- Company Recommendations
- Career Suggestions

---

# 📈 Long-Term Vision

The long-term objective is to transform AI Resume Copilot into a comprehensive career development platform.

Future capabilities may include:

- User Authentication
- Personal Dashboards
- Resume Versioning
- Portfolio Analysis
- LinkedIn Analysis
- GitHub Profile Analysis
- AI Career Coach
- Personalized Learning Plans
- Company-Specific ATS Analysis
- Recruiter Dashboard

---

# 🔄 Development Workflow

Every new feature follows a structured workflow.

```text
Plan Feature
      │
      ▼
Design Module
      │
      ▼
Implement Code
      │
      ▼
Test Feature
      │
      ▼
Verify Database
      │
      ▼
Create Migration (if required)
      │
      ▼
Run All Tests
      │
      ▼
Commit Changes
      │
      ▼
Push to GitHub
      │
      ▼
Continuous Integration
```

---

# 📊 Project Progress

## Completed

- FastAPI Backend
- AI Engine Architecture
- Prompt Management
- Ollama Integration
- Mock Provider
- Docker Support
- GitHub Actions
- Automated Testing
- PostgreSQL Integration
- SQLAlchemy ORM
- Alembic Migration System
- Resume Database Model
- Database Connectivity
- Initial Database Schema

---

## In Progress

- Resume CRUD APIs
- Resume Storage Layer
- AI Processing Services
- Resume Upload Workflow

---

## Planned

- ATS Analysis APIs
- Resume Improvement APIs
- Authentication System
- User Management
- Dashboard APIs
- Analytics APIs
- Deployment Preparation

---

# 🎯 Project Goals

The primary goals of AI Resume Copilot are:

- Build a scalable AI-powered backend.
- Apply modern backend engineering practices.
- Follow production-inspired software architecture.
- Integrate Large Language Models effectively.
- Maintain a clean, modular, and testable codebase.
- Support continuous integration and future cloud deployment.
- Provide an extensible foundation for AI-powered career services.

---

# 📚 Learning Outcomes

Developing AI Resume Copilot provides practical experience across multiple domains of software engineering, artificial intelligence, backend development, and database management.

---

## Backend Development

Skills gained:

- FastAPI Application Development
- REST API Design
- Modular Project Architecture
- Dependency Injection
- Service Layer Design
- Configuration Management
- Environment Variable Management
- Error Handling
- Request Validation
- Response Modeling

---

## Artificial Intelligence

Skills gained:

- Large Language Model Integration
- Ollama Deployment
- Prompt Engineering
- Provider-Based AI Architecture
- Response Parsing
- AI Service Design
- Resume Intelligence
- ATS Analysis Concepts

---

## Database Engineering

Skills gained:

- PostgreSQL Database Design
- SQLAlchemy ORM
- Declarative Models
- Database Sessions
- Database Connectivity
- Alembic Migration Management
- Schema Version Control
- Persistent Data Storage

Current implementation includes:

- Resume ORM Model
- Database Engine
- Session Factory
- Migration Environment
- Initial Database Schema

---

## DevOps

Current DevOps practices include:

- Docker
- GitHub Actions
- Automated Testing
- Continuous Integration
- Environment Configuration

Future DevOps goals include:

- Docker Compose
- Production Deployment
- Monitoring
- Logging
- Cloud Deployment

---

## Software Engineering Principles

The project follows several software engineering best practices.

Current principles:

- Separation of Concerns
- Modular Design
- Reusable Components
- Clean Architecture
- Maintainable Code
- Version Control
- Database Versioning

---

# 📈 Performance Goals

The application is designed with scalability in mind.

Target characteristics:

- Fast API Response
- Modular AI Components
- Scalable Database Design
- Independent Service Layer
- Extensible AI Providers
- Production-Ready Architecture

Future optimization areas:

- Background Task Processing
- Response Caching
- Database Query Optimization
- Asynchronous Processing

---

# 🔮 Future Enhancements

The roadmap includes several planned enhancements.

## Backend

- Authentication
- Authorization
- User Profiles
- Resume Versioning
- File Management
- Activity History

---

## Artificial Intelligence

- Multi-LLM Support
- AI Career Coach
- Personalized Resume Suggestions
- Company-Specific Resume Optimization
- AI Interview Simulator
- AI Skill Gap Detection

---

## Database

Future tables may include:

- users
- resumes_history
- cover_letters
- interview_sessions
- job_matches
- activity_logs

Future improvements:

- Database Index Optimization
- Backup Strategy
- Soft Deletes
- Audit Logs
- Relationship Mapping

---

## Frontend

Planned frontend features:

- Resume Upload Dashboard
- ATS Score Visualization
- Resume History
- Analytics Dashboard
- User Authentication
- Profile Management

---

# 🤝 Contribution Guidelines

Contributions are welcome.

Recommended workflow:

1. Fork the repository.
2. Create a feature branch.
3. Implement the feature.
4. Run all tests.
5. Commit changes.
6. Push the branch.
7. Open a Pull Request.

All contributions should:

- Follow the existing project structure.
- Maintain code readability.
- Include tests where applicable.
- Keep documentation updated.

---

# 📝 Coding Standards

Development follows consistent coding practices.

- PEP 8 Compliance
- Type Hints
- Clear Naming Conventions
- Modular Functions
- Reusable Components
- Proper Documentation
- Consistent Formatting

Database standards:

- SQLAlchemy ORM
- Alembic Migrations
- Environment-Based Configuration
- No Hardcoded Credentials

---

# 📊 Current Project Snapshot

| Category | Status |
|----------|--------|
| FastAPI Backend | ✅ Completed |
| AI Architecture | ✅ Completed |
| Ollama Integration | ✅ Completed |
| Prompt Management | ✅ Completed |
| Mock Provider | ✅ Completed |
| PostgreSQL Integration | ✅ Completed |
| SQLAlchemy ORM | ✅ Completed |
| Alembic Migration | ✅ Completed |
| Resume Database Model | ✅ Completed |
| Docker Support | ✅ Completed |
| GitHub Actions CI | ✅ Completed |
| Automated Testing | ✅ Completed |
| Resume Upload API | 🚧 In Progress |
| Resume CRUD APIs | 🚧 In Progress |
| ATS Analysis API | 📅 Planned |
| Authentication | 📅 Planned |
| Dashboard | 📅 Planned |

---

# 📖 Documentation

AI Resume Copilot is documented to make development, maintenance, and future enhancements straightforward.

Current documentation includes:

- Project Overview
- Architecture Overview
- Project Structure
- Technology Stack
- Installation Guide
- PostgreSQL Setup
- Database Configuration
- Alembic Migration Guide
- Environment Variables
- Docker Setup
- Testing Guide
- Development Roadmap

Future documentation will include:

- API Documentation
- Database Schema Documentation
- Deployment Guide
- Developer Guide
- Contribution Guide
- Architecture Diagrams

---

# 🔍 Quality Assurance

The project emphasizes reliability through structured development and testing practices.

Current quality measures:

- Automated Testing
- GitHub Actions Continuous Integration
- Modular Code Structure
- Environment-Based Configuration
- Database Version Control
- ORM-Based Database Access

Every completed feature is verified before being committed to the repository.

---

# 📦 Current Repository Contents

The repository currently contains:

- FastAPI Backend
- AI Engine
- PostgreSQL Integration
- SQLAlchemy ORM
- Alembic Migration System
- Docker Configuration
- GitHub Actions Workflow
- Automated Tests
- Project Documentation
- Environment Configuration

Supporting directories include:

- Application Source Code
- Database Layer
- AI Modules
- Documentation
- Test Suite
- Deployment Files
- Upload Storage
- Frontend
- Notebooks

---

# 📈 Repository Evolution

The project has progressed through multiple development stages.

### Phase 1

- Backend Project Initialization
- FastAPI Configuration
- Project Architecture
- Environment Configuration

### Phase 2

- AI Engine Development
- Ollama Integration
- Prompt Management
- Mock Provider
- Testing Infrastructure

### Phase 3

- Docker Integration
- GitHub Actions
- Automated Testing
- Documentation Improvements

### Phase 4

- PostgreSQL Installation
- SQLAlchemy Integration
- Database Connection
- Resume ORM Model
- Alembic Configuration
- Initial Database Migration
- Database Schema Versioning

### Upcoming Phase

- Resume Upload APIs
- Resume CRUD Operations
- Resume Storage Services
- ATS Analysis APIs
- Resume Improvement APIs

---

# 🎯 Why This Project?

AI Resume Copilot combines several important software engineering concepts into a single production-inspired application.

The project demonstrates practical knowledge of:

- Backend Development
- REST API Design
- Artificial Intelligence Integration
- Large Language Models
- Database Engineering
- Object Relational Mapping
- Database Migration Management
- Automated Testing
- Docker
- Continuous Integration
- Software Architecture

Rather than being a single-feature project, it is designed as a scalable platform that can continuously evolve as additional AI services and backend capabilities are implemented.

---

# 🏆 Key Achievements

Current milestones achieved:

- Production-inspired FastAPI Architecture
- Modular AI Engine
- Provider-Based LLM Design
- Ollama Integration
- Prompt Management System
- Automated Testing
- Docker Support
- GitHub Actions CI
- PostgreSQL Database Integration
- SQLAlchemy ORM Configuration
- Alembic Migration System
- Resume Database Model
- Environment-Based Configuration
- Initial Database Schema Creation

---

# 🌟 Future Vision

The long-term vision is to transform AI Resume Copilot into a complete AI-powered career platform.

Planned capabilities include:

- Resume Management
- AI Resume Builder
- ATS Optimization
- Cover Letter Generator
- AI Career Coach
- Job Recommendation System
- Interview Preparation
- Learning Recommendations
- Portfolio Analysis
- LinkedIn Analysis
- GitHub Profile Analysis
- Recruiter Dashboard
- Analytics Dashboard

The architecture has been intentionally designed to support these future modules without requiring major structural changes.

---

# ⭐ Support

If you find this project useful:

- Star the repository.
- Fork the repository.
- Report issues.
- Suggest improvements.
- Contribute new features.
- Share feedback.

Community contributions are welcome and help improve the project for everyone.

---

# 👨‍💻 Author

**Divesh Kate**

B.Tech in Artificial Intelligence & Machine Learning

AI Resume Copilot is a long-term backend engineering project focused on applying modern software engineering principles, artificial intelligence, and scalable backend development practices.

GitHub: https://github.com/diveshkate11-collab

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve the project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes with meaningful commit messages.
4. Push the branch to your fork.
5. Open a Pull Request.

Please ensure that:

- Code follows the existing project structure.
- New features include appropriate tests where applicable.
- Documentation is updated alongside code changes.

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for additional information.

---

# 🧑‍💻 Developer Notes

AI Resume Copilot is being developed as a production-inspired backend application that combines Artificial Intelligence, FastAPI, PostgreSQL, SQLAlchemy, and modern backend engineering practices.

The project emphasizes:

- Clean Architecture
- Modular Design
- Scalable Development
- Maintainable Code
- Test-Driven Development
- Database Version Control
- Environment-Based Configuration

Every completed feature is integrated into the existing architecture before new functionality is introduced, ensuring the project remains organized, scalable, and easy to extend.

---

# 🚀 Recent Development Progress

The latest development cycle introduced the complete database foundation.

Recently completed:

- PostgreSQL 18 Installation
- PostgreSQL Database Creation
- SQLAlchemy ORM Integration
- Database Engine Configuration
- Session Factory Configuration
- Declarative Base Setup
- Resume ORM Model
- Alembic Initialization
- Alembic Configuration
- Automatic Migration Generation
- Initial Database Migration
- Resume Table Creation
- Database Connection Verification

These additions establish the persistence layer required for future resume management and AI-powered analysis.

---

# 🎯 Next Development Targets

Current focus:

- Resume Upload API
- Resume CRUD Operations
- Resume Storage Service
- Resume Processing Pipeline
- ATS Analysis API
- Resume Improvement API

Upcoming features:

- Authentication
- JWT Authorization
- User Profiles
- Resume History
- Dashboard
- AI Career Coach
- Portfolio Analysis
- GitHub Profile Analysis
- LinkedIn Profile Analysis

---

# 📊 Current Project Statistics

| Category | Status |
|----------|--------|
| FastAPI Backend | ✅ Completed |
| AI Architecture | ✅ Completed |
| Ollama Integration | ✅ Completed |
| PostgreSQL Integration | ✅ Completed |
| SQLAlchemy ORM | ✅ Completed |
| Alembic Migration System | ✅ Completed |
| Resume ORM Model | ✅ Completed |
| Docker Support | ✅ Completed |
| GitHub Actions CI | ✅ Completed |
| Automated Testing | ✅ 154 Passing Tests |
| Resume Upload API | 🚧 In Progress |
| Resume CRUD APIs | 🚧 In Progress |
| ATS Analysis API | 📅 Planned |
| Authentication | 📅 Planned |

---

# 🎓 Educational Objectives

This project demonstrates practical implementation of:

- Backend Engineering
- REST API Development
- Artificial Intelligence Integration
- Large Language Models
- PostgreSQL Database Engineering
- SQLAlchemy ORM
- Alembic Database Migrations
- Docker
- GitHub Actions
- Automated Testing
- Environment-Based Configuration
- Production-Inspired Software Architecture

---

# 🌟 Final Note

AI Resume Copilot is an ongoing project designed to demonstrate modern backend engineering, AI integration, and scalable software architecture.

As development progresses, additional AI capabilities, database features, and production-ready services will continue to be added while maintaining a clean, modular, and maintainable codebase.

If you find this project useful, consider giving it a ⭐ on GitHub.

---

**Built with ❤️ by Divesh Kate using FastAPI, PostgreSQL, SQLAlchemy, Alembic, Ollama, and Python.**