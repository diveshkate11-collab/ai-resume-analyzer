# AI Resume Copilot

An AI-powered Resume Analysis and Career Assistance platform built with **Python** and **FastAPI**.

AI Resume Copilot helps users analyze resumes, calculate ATS (Applicant Tracking System) scores, identify strengths and weaknesses, recommend suitable job roles, analyze skill gaps, generate interview questions, evaluate interview answers, and prepare for technical interviews through a modular AI-powered backend.

---

# About This Project

AI Resume Copilot is my first end-to-end AI and FastAPI project.

I built this project to learn:

- Software Engineering
- Backend Development
- REST API Development
- AI Application Architecture
- Machine Learning Integration
- Modular Project Design

This project is being developed incrementally. Every module is implemented, tested, documented, and integrated before moving to the next feature.

---

# Project Status

## ✅ Completed

### Resume Parsing

- PDF Resume Parser
- DOCX Resume Parser
- Resume Text Cleaner
- Contact Information Extraction
- Skills Extraction
- Education Extraction
- Experience Extraction
- Resume Parser Integration

### ATS Analysis

- ATS Scoring Engine
- ATS Response Validation

### Job Recommendation

- Role Prediction Engine
- Recommendation Engine
- Skill Gap Analyzer
- Job Matcher

### Resume Analysis

- Resume Improvement Engine
- Resume Strength Analysis
- Resume Weakness Analysis
- Resume Improvement Suggestions

### Explainability

- ATS Explanation
- Job Recommendation Explanation

### Analytics

- ATS History Tracker

### Interview Preparation

- Technical Interview Question Generator
- HR Interview Question Generator
- Interview Answer Evaluation

### Backend

- FastAPI Backend
- Resume Upload API
- Interview Question API
- Interview Answer Evaluation API
- Resume Improvement API
- Job Recommendation API
- Service Layer Architecture
- Pydantic Request & Response Schemas
- Swagger API Documentation
- Response Validation

---

## 🚧 Currently Working On

- Resume Upload Pipeline Integration
- End-to-End Resume Analysis Workflow
- Job Recommendation Integration
- Backend Refactoring
- Codebase Optimization

---

## 📅 Planned

### Backend

- Authentication
- Authorization
- SQL Database Integration
- User Dashboard
- Logging
- Background Tasks

### AI

- AI Resume Copilot Chatbot
- LLM Integration
- RAG Integration
- Vector Database
- Resume vs Job Description Matching
- Personalized Career Guidance

### Frontend

- React Frontend
- Dashboard
- User Authentication Pages

### Deployment

- Docker
- Kubernetes
- AWS Deployment
- CI/CD Pipeline

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
- Resume Validation
- Resume Quality Analysis

---

## Resume Improvement

- Strength Analysis
- Weakness Detection
- Resume Improvement Suggestions

---

## Job Recommendation

- Predict Suitable Job Role
- Skill Gap Analysis
- Learning Recommendations
- Job Matching

---

## Interview Preparation

- Technical Interview Questions
- HR Interview Questions
- Interview Answer Evaluation
- Answer Feedback

---

## Analytics

- ATS Score History
- Resume Analytics

---

## Explainability

- ATS Score Explanation
- Job Recommendation Explanation

---

## REST API

- Resume Upload API
- Resume Improvement API
- Job Recommendation API
- Interview Question API
- Interview Answer Evaluation API

# Tech Stack

## Backend

- Python
- FastAPI
- Pydantic

---

## AI / NLP

- Regular Expressions (Regex)

---

## Development Tools

- VS Code
- Git
- GitHub
- Swagger UI

---

## Future Technologies

- SQL
- React
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

## Resume Parsing

- [x] PDF Resume Parser
- [x] DOCX Resume Parser
- [x] Resume Text Cleaner
- [x] Contact Parser
- [x] Skills Parser
- [x] Education Parser
- [x] Experience Parser
- [x] Resume Parser Integration

---

## ATS

- [x] ATS Scoring Engine
- [x] ATS Response Validation

---

## Resume Improvement

- [x] Resume Strength Analysis
- [x] Resume Weakness Analysis
- [x] Resume Improvement Suggestions
- [x] Resume Improvement API

---

## Job Recommendation

- [x] Role Prediction
- [x] Recommendation Engine
- [x] Skill Gap Analyzer
- [x] Job Matcher
- [x] Job Recommendation API

---

## Interview

- [x] Technical Interview Questions
- [x] HR Interview Questions
- [x] Interview Answer Evaluation
- [x] Interview API

---

## Explainability

- [x] ATS Explanation
- [x] Job Recommendation Explanation

---

## Analytics

- [x] ATS History

---

## Backend

- [x] FastAPI Backend
- [x] Resume Upload API
- [x] Service Layer
- [x] Pydantic Schemas
- [x] Request Validation
- [x] Response Validation
- [x] Swagger Documentation

---

## Planned

- [ ] Authentication
- [ ] SQL Database
- [ ] User Dashboard
- [ ] AI Resume Copilot Chatbot
- [ ] Resume vs Job Description Matching
- [ ] React Frontend
- [ ] Docker
- [ ] Kubernetes
- [ ] AWS Deployment

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
                    Resume Information Parser
                              │
      ┌───────────────────────┼────────────────────────┐
      ▼                       ▼                        ▼
 Contact Parser       Education Parser       Experience Parser
                              │
                              ▼
                      Skills Extraction
                              │
                              ▼
                       ATS Scoring Engine
                              │
                              ▼
                    Resume Improvement Engine
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
      ┌───────────────────────┼────────────────────────┐
      ▼                       ▼                        ▼
Interview Questions     Answer Evaluation       Future AI Copilot
```

---

# REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Status |
| POST | `/api/resume/upload` | Upload and Analyze Resume |
| POST | `/api/improvement/analyze` | Resume Improvement Analysis |
| POST | `/api/jobs/recommend` | Job Recommendation |
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
                Request Validation
                       │
                       ▼
                 Service Layer
                       │
                       ▼
                   AI Engine
       ┌────────────┼──────────────┬──────────────┐
       ▼            ▼              ▼              ▼
    Parser         ATS      Improvement        Interview
       │            │              │              │
       └────────────┼──────────────┴──────────────┘
                    ▼
             Response Schema
                    │
                    ▼
               JSON Response
```

---

# Module Architecture

```text
app/
│
├── api/
│      Handles HTTP Requests
│
├── services/
│      Business Logic Layer
│
├── schemas/
│      Request & Response Models
│
├── ai_engine/
│      Core AI Modules
│
├── database/
│      Future SQL Integration
│
└── core/
       Project Configuration
```

---

# Backend Flow

```text
Client Request
      │
      ▼
FastAPI Endpoint
      │
      ▼
Pydantic Validation
      │
      ▼
Service Layer
      │
      ▼
AI Engine
      │
      ▼
Response Schema
      │
      ▼
JSON Response
```

---

# Current Backend Modules

## Parser

- PDF Parser
- DOCX Parser
- Resume Parser
- Contact Parser
- Skills Parser
- Education Parser
- Experience Parser

---

## ATS

- ATS Score
- Resume Validation

---

## Resume Improvement

- Strength Analysis
- Weakness Analysis
- Resume Suggestions

---

## Jobs

- Role Predictor
- Recommendation Engine
- Skill Gap Analyzer
- Job Matcher

---

## Interview

- Question Generator
- HR Questions
- Technical Questions
- Answer Evaluation

---

## Analytics

- ATS History

---

## Explainability

- ATS Explanation
- Job Recommendation Explanation

# Example API Usage

## Resume Upload API

### Request

```http
POST /api/resume/upload
```

Upload a PDF or DOCX resume using `multipart/form-data`.

---

### Example Response

```json
{
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
    "recommended_role": "Backend Developer",
    "suggestions": [
      "Build REST APIs using FastAPI.",
      "Learn Docker and containerization.",
      "Practice SQL optimization."
    ]
  }
}
```

---

# Resume Improvement API

### Request

```http
POST /api/improvement/analyze
```

### Request Body

```json
{
  "skills": [
    "Python",
    "FastAPI"
  ],
  "education": true,
  "experience": false
}
```

### Response

```json
{
  "strengths": [
    "Strong Python skills.",
    "Backend development skills identified.",
    "Education details are present."
  ],
  "weaknesses": [
    "SQL skill is missing.",
    "Docker skill is missing.",
    "Git skill is missing.",
    "Experience section is missing."
  ],
  "suggestions": [
    "Learn SQL and add it to your resume.",
    "Learn Docker for backend deployment.",
    "Add Git and GitHub experience.",
    "Include internships, projects, or freelance experience."
  ]
}
```

---

# Job Recommendation API

### Request

```http
POST /api/jobs/recommend
```

### Request Body

```json
{
  "skills": [
    "Python",
    "FastAPI"
  ],
  "education": true,
  "experience": false
}
```

### Response

```json
{
  "recommended_role": "Backend Developer",
  "skill_gap": [
    "SQL",
    "Docker",
    "Git"
  ],
  "recommendations": [
    "Build REST APIs using FastAPI.",
    "Learn Docker and containerization.",
    "Practice SQL optimization."
  ],
  "matched_jobs": [
    "Backend Developer Intern",
    "Junior Backend Developer",
    "Python Backend Developer"
  ]
}
```

---

# Interview Question API

### Request

```http
POST /api/interview/questions
```

### Request Body

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

# Interview Answer Evaluation API

### Request

```http
POST /api/interview/evaluate
```

### Request Body

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
- Resume Improvement
- Skill Gap Detection
- Job Role Recommendation
- Interview Preparation
- AI-powered Career Guidance
- Explainable AI Recommendations

---

# Learning Objectives

This project is helping me gain practical experience with:

- Python
- FastAPI
- REST API Development
- Software Engineering
- Backend Development
- AI/NLP Fundamentals
- Resume Parsing
- Service Layer Architecture
- Pydantic Models
- Modular Software Design
- Git & GitHub
- Project Documentation

---

# Future Roadmap

The next planned features for AI Resume Copilot are grouped into the following phases.

---

## Resume Analysis

- Resume Strength Analysis
- Resume Weakness Detection
- Resume Improvement Suggestions
- Resume vs Job Description Matching
- ATS Keyword Optimization
- Resume Version Comparison

---

## Career Assistance

- Direct Job Application Links
- Resume Analytics Dashboard
- Personalized Career Roadmap
- Learning Recommendations
- Skill Progress Tracking

---

## Interview Preparation

- AI-powered Interview Question Generation
- Mock Interview Simulator
- Interview Performance Analytics
- Personalized Interview Feedback

---

## AI Features

- AI Resume Copilot Chatbot
- LLM Integration
- RAG-based Resume Assistant
- Explainable AI Recommendations

---

## Backend

- Authentication & Authorization
- SQL Database Integration
- User Dashboard
- Background Tasks
- Logging
- Monitoring
- Email Notifications

---

## Frontend

- React Frontend
- Responsive Dashboard
- User Authentication
- Resume History
- Analytics Visualization

---

## Deployment

- Docker
- Kubernetes
- AWS Deployment
- CI/CD Pipeline

---

# Contributing

This project is currently under active development.

Suggestions, improvements, bug reports, and feature requests are always welcome.

If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.

---

# License

This project is licensed under the MIT License.

---

# Author

**Divesh Kate**

B.Tech – Artificial Intelligence & Machine Learning

AI Resume Copilot is my first large-scale personal project. It documents my journey of learning software engineering, backend development, FastAPI, and AI by building a real-world application step by step.

---

⭐ If you found this project useful, consider giving it a star.