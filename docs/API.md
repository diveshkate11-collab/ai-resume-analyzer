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