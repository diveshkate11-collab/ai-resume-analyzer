# AI Resume Copilot

An AI-powered Resume Analysis platform built with Python.

AI Resume Copilot analyzes resumes, calculates ATS (Applicant Tracking System) scores, recommends suitable job roles, tracks resume improvements, explains every recommendation, and exposes a production-ready REST API built with FastAPI.

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
- Job Recommendation Engine
- Analytics Module
- Explainability Module
- FastAPI Backend
- Resume Upload API
- Resume Service Layer
- Pydantic Response Schemas
- API Validation & Error Handling

## 🚧 In Progress

- Interview Preparation Module

## 📅 Planned

- Resume Analytics Dashboard
- Resume Improvement Suggestions
- Authentication & Authorization
- Database Integration
- React Frontend
- AI Resume Copilot Chatbot (LLM)
- RAG-based Resume Assistant
- Docker Support
- Kubernetes Deployment
- AWS Deployment

---

# Features

## Resume Parsing

- Parse PDF resumes
- Parse DOCX resumes
- Resume Text Cleaning
- Contact Information Extraction
- Skills Extraction
- Education Extraction
- Experience Extraction

---

## ATS Analysis

- ATS Score Calculator
- Section Checker
- Keyword Matching
- Resume Formatting Checker
- Grammar Checker (V1)

---

## Job Recommendation

- Role Predictor
- Skill Gap Analysis
- Resume Recommendation Engine
- Job Matcher

---

## Analytics

- Resume Comparison
- Resume Improvement Tracker
- ATS History Tracker

---

## Explainability

- ATS Score Explanation
- Job Recommendation Explanation
- Skill Gap Explanation

---

## REST API

- FastAPI Backend
- Resume Upload API
- Resume Analysis API
- Pydantic Response Models
- Request Validation
- HTTP Exception Handling
- Interactive Swagger Documentation

---

# Tech Stack

## Backend

- Python
- FastAPI
- Pydantic

## AI / NLP

- Regular Expressions (Regex)

## Data

- Text-based Skills Database

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
│   │   ├── explainability/
│   │   ├── interview/
│   │   ├── jobs/
│   │   ├── parser/
│   │   ├── copilot/
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

- [x] PDF Parser
- [x] DOCX Parser
- [x] Resume Text Cleaner
- [x] Contact Parser
- [x] Skills Parser
- [x] Education Parser
- [x] Experience Parser
- [x] Resume Parser
- [x] ATS Engine
- [x] Job Recommendation Engine
- [x] Skill Gap Analyzer
- [x] Resume Recommendation Engine
- [x] Analytics Module
- [x] Explainability Module
- [x] FastAPI Backend
- [x] Resume Upload API
- [x] Service Layer
- [x] Pydantic Schemas
- [x] HTTP Exception Handling
- [ ] Interview Module
- [ ] AI Copilot
- [ ] Authentication
- [ ] Database Integration
- [ ] React Frontend
- [ ] Docker
- [ ] Kubernetes
- [ ] AWS Deployment

---

# Current Workflow

```text
Resume
   │
   ▼
Upload API (FastAPI)
   │
   ▼
Resume Service
   │
   ▼
PDF / DOCX Parser
   │
   ▼
Text Cleaner
   │
   ▼
Resume Parser
   │
   ├── Contact Parser
   ├── Skills Parser
   ├── Education Parser
   └── Experience Parser
   │
   ▼
ATS Engine
   ├── Section Checker
   ├── Keyword Matcher
   ├── Formatting Checker
   └── Grammar Checker
   │
   ▼
Job Recommendation Engine
   ├── Role Predictor
   ├── Skill Gap Analyzer
   ├── Recommendation Engine
   └── Job Matcher
   │
   ▼
Analytics Module
   ├── Resume Comparison
   ├── Improvement Tracker
   └── ATS History
   │
   ▼
Explainability Module
   ├── ATS Explanation
   ├── Job Recommendation Reason
   └── Skill Gap Explanation
   │
   ▼
REST API Response
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Status |
| POST | `/api/resume/upload` | Upload and Analyze Resume |

Interactive API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Future Roadmap

- Resume Analytics Dashboard
- Resume Improvement Suggestions
- Resume vs Job Description Matching
- AI Resume Copilot Chatbot
- Interview Question Generator
- Mock Interview Evaluation
- Explainable AI Recommendations
- Authentication
- SQL Database Integration
- User Dashboard
- LLM Integration
- RAG Integration
- Vector Database
- LangChain
- LangGraph
- React Frontend
- Docker Deployment
- Kubernetes Deployment
- AWS Cloud Deployment

---

# License

This project is licensed under the MIT License.