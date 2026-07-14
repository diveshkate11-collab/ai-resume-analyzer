# AI Resume Copilot

An AI-powered Resume Analysis and Interview Preparation platform built with Python and FastAPI.

AI Resume Copilot helps users analyze resumes, calculate ATS (Applicant Tracking System) scores, identify strengths and weaknesses, recommend suitable job roles, generate interview questions, evaluate interview answers, and prepare for technical interviews through a modular AI-powered backend.

> **About This Project**
>
> AI Resume Copilot is my first end-to-end AI and FastAPI project. I built this project to learn software engineering, backend development, machine learning integration, REST API development, and real-world AI application architecture.
>
> This project is being developed incrementally. Every module is implemented, tested, documented, and integrated before moving to the next feature.

---

# Project Status

## ✅ Completed

- PDF Resume Parser
- DOCX Resume Parser
- Resume Text Cleaner
- Contact Information Extraction
- Skills Extraction
- Education Extraction
- Experience Extraction
- Resume Parser Integration
- ATS Scoring Engine
- Role Prediction Engine
- Recommendation Engine
- Skill Gap Analyzer
- Explainability Module
- Analytics Module
- Resume Upload API
- Interview Question Generator API
- Interview Answer Evaluation API
- Resume Service Layer
- Interview Service Layer
- FastAPI Backend
- Pydantic Schemas
- Swagger API Documentation
- Response Validation
- Resume Upload & Analysis Workflow

---

## 🚧 Currently Working On

- ATS Improvement Engine
- Resume Strength Analysis
- Resume Weakness Analysis
- Resume Improvement Suggestions
- Job Matching Engine

---

## 📅 Planned

- Authentication
- Database Integration
- Resume Dashboard
- React Frontend
- AI Resume Copilot Chatbot
- LLM Integration
- RAG Integration
- Docker
- Kubernetes
- AWS Deployment

---

# Features

## Resume Parsing

- Upload PDF Resume
- Upload DOCX Resume
- Resume Text Cleaning
- Contact Extraction
- Skills Extraction
- Education Extraction
- Experience Extraction

---

## ATS Analysis

- ATS Score Calculation
- Section Validation
- Keyword Matching
- Resume Formatting Check
- Grammar Check

---

## Job Recommendation

- Role Prediction
- Resume Recommendation Engine
- Skill Gap Analysis
- Job Role Matching

---

## Interview Preparation

- Technical Interview Questions
- HR Interview Questions
- Interview Answer Evaluation
- Answer Feedback
- Improvement Suggestions

---

## Analytics

- Resume Comparison
- Resume Improvement Tracker
- ATS Score History

---

## Explainability

- ATS Score Explanation
- Job Recommendation Explanation
- Skill Gap Explanation

---

## REST API

- FastAPI Backend
- Resume Upload API
- Interview Question API
- Interview Answer Evaluation API
- Pydantic Validation
- Request Validation
- HTTP Exception Handling
- Interactive API Documentation

---

# Tech Stack

## Backend

- Python
- FastAPI
- Pydantic

## AI / NLP

- Regular Expressions (Regex)

## Development Tools

- VS Code
- Git
- GitHub

## Future Technologies

- React
- SQL Database
- Docker
- Kubernetes
- AWS
- LangChain
- LangGraph
- Vector Database
- LLM
- RAG

---

# Project Structure

```text
AI_RESUME_COPILOT/
│
├── app/
│   │
│   ├── ai_engine/
│   │   ├── analytics/
│   │   ├── ats/
│   │   ├── copilot/
│   │   ├── explainability/
│   │   ├── interview/
│   │   ├── jobs/
│   │   ├── parser/
│   │   ├── training/
│   │   └── utils/
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
├── data/
├── deployment/
├── docs/
├── frontend/
├── notebooks/
├── storage/
├── tests/
├── uploads/
│
├── README.md
├── requirements.txt
├── pyproject.toml
├── LICENSE
└── .gitignore
```

---

# Development Progress

- [x] PDF Resume Parser
- [x] DOCX Resume Parser
- [x] Resume Text Cleaner
- [x] Contact Parser
- [x] Skills Parser
- [x] Education Parser
- [x] Experience Parser
- [x] Resume Parser Integration
- [x] ATS Scoring Engine
- [x] Role Prediction
- [x] Recommendation Engine
- [x] Skill Gap Analyzer
- [x] Explainability Module
- [x] Analytics Module
- [x] Resume Upload API
- [x] Interview Question API
- [x] Interview Answer Evaluation API
- [x] Resume Service Layer
- [x] Interview Service Layer
- [x] Pydantic Schemas
- [x] Swagger Documentation
- [x] API Response Validation
- [ ] Resume Improvement Engine
- [ ] Resume Strength Analysis
- [ ] Resume Weakness Analysis
- [ ] Job Matching Engine
- [ ] Resume Dashboard
- [ ] Authentication
- [ ] Database Integration
- [ ] AI Resume Copilot Chatbot
- [ ] React Frontend
- [ ] Docker
- [ ] Kubernetes
- [ ] AWS Deployment

---

# Latest Update (14 July 2026)

Today's milestone focused on completing the first fully functional backend for AI Resume Copilot.

### Completed

- Integrated the Resume Parser pipeline.
- Connected ATS Scoring with Resume Analysis.
- Connected Role Prediction.
- Integrated Recommendation Engine.
- Integrated Skill Gap Analysis.
- Added Explainability Module.
- Added Analytics Module.
- Fixed FastAPI response validation.
- Fixed backend import issues.
- Successfully tested Resume Upload API.
- Successfully analyzed PDF resumes through Swagger UI.

---

# Current Workflow

```text
                         Resume
                            │
                            ▼
                  Upload API (FastAPI)
                            │
                            ▼
                  Resume Service Layer
                            │
                            ▼
                  PDF / DOCX Resume Parser
                            │
                            ▼
                   Resume Text Cleaner
                            │
                            ▼
                    Resume Information
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
  Contact Parser     Education Parser   Experience Parser
                            │
                            ▼
                     Skills Extraction
                            │
                            ▼
                       ATS Scoring Engine
                            │
                            ▼
                  Role Prediction Engine
                            │
                            ▼
                  Recommendation Engine
                            │
                            ▼
                     Skill Gap Analyzer
                            │
                            ▼
                  Explainability Module
                            │
                            ▼
                    Analytics Module
                            │
                            ▼
                Resume Analysis Response
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
 Interview Question   Answer Evaluation   Future Improvements
     Generator              Engine
```

---

# REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Check API Status |
| POST | `/api/resume/upload` | Upload and Analyze Resume |
| POST | `/api/interview/questions` | Generate Interview Questions |
| POST | `/api/interview/evaluate` | Evaluate Interview Answers |

---

# API Architecture

```text
                Client
                  │
                  ▼
             FastAPI Router
                  │
                  ▼
            Service Layer
                  │
                  ▼
             AI Engine
      ┌───────────┼────────────┐
      ▼           ▼            ▼
    Parser       ATS         Interview
      │           │            │
      └───────────┼────────────┘
                  ▼
            Response Schema
                  │
                  ▼
             JSON Response
```
---

# Example API Response

## Resume Analysis

```json
{
  "success": true,
  "filename": "resume.pdf",
  "analysis": {
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
    "ats": {
      "ats_score": 85
    },
    "recommendation": {
      "recommended_roles": [
        "Python Developer",
        "Backend Developer"
      ]
    }
  }
}
```

---

## Interview Question API

### Request

```json
{
  "role": "python developer"
}
```

### Response

```json
{
  "role": "python developer",
  "technical_questions": [
    "What is Python?",
    "Explain decorators.",
    "What is FastAPI?"
  ],
  "hr_questions": [
    "Tell me about yourself.",
    "Why should we hire you?"
  ]
}
```

---

## Interview Answer Evaluation API

### Request

```json
{
  "question": "What is Python?",
  "answer": "Python is a high-level interpreted programming language."
}
```

### Response

```json
{
  "score": 9,
  "strengths": [
    "Detailed explanation."
  ],
  "weaknesses": [
    "Minor improvements possible."
  ],
  "improvements": [
    "Use more technical terminology.",
    "Add practical examples."
  ]
}
```

---

# Project Goals

The objective of AI Resume Copilot is to build a complete AI-powered career assistant capable of:

- Resume Parsing
- ATS Score Analysis
- Resume Strength & Weakness Detection
- Resume Improvement Suggestions
- Skill Gap Detection
- Job Role Recommendation
- Direct Job Application Links
- Interview Preparation
- AI-powered Resume Assistant
- Explainable AI Recommendations

---

# Learning Objectives

This project is helping me gain practical experience with:

- Python
- FastAPI
- REST API Development
- Software Architecture
- AI/NLP Fundamentals
- Resume Parsing
- Backend Development
- Service Layer Architecture
- Pydantic Models
- Git & GitHub
- Project Documentation
- Modular Software Design

---

# Future Roadmap

The next planned features for AI Resume Copilot are:

### Resume Analysis

- Resume Strength Analysis
- Resume Weakness Detection
- Resume Improvement Suggestions
- Resume vs Job Description Matching
- ATS Keyword Optimization
- Resume Version Comparison

---

### Career Assistance

- Direct Job Apply Links
- Resume Analytics Dashboard
- Career Roadmap Generator
- Personalized Learning Recommendations

---

### Interview Preparation

- AI-powered Interview Question Generation
- Mock Interview Simulator
- Advanced Answer Evaluation
- Interview Performance Analytics

---

### AI Features

- AI Resume Copilot Chatbot
- LLM Integration
- RAG-based Resume Assistant
- Explainable AI Recommendations

---

### Backend

- Authentication & Authorization
- SQL Database Integration
- User Dashboard
- Background Tasks
- Logging & Monitoring

---

### Deployment

- React Frontend
- Docker
- Kubernetes
- AWS Deployment
- CI/CD Pipeline

---

# Contributing

This project is currently under active development.

Suggestions, issues, and improvements are always welcome.

If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.

---

# License

This project is licensed under the MIT License.

---

# Author

**Divesh Kate**

B.Tech – Artificial Intelligence & Machine Learning

This repository documents my journey of building an end-to-end AI-powered Resume Analysis and Interview Preparation platform using Python and FastAPI while continuously learning software engineering, backend development, and applied AI.

---

⭐ If you found this project interesting, consider giving it a star.