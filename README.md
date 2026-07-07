# AI Resume Copilot

An AI-powered Resume Analysis platform built with Python.

The project extracts information from resumes, calculates an ATS (Applicant Tracking System) score, recommends suitable job roles, identifies skill gaps, and lays the foundation for AI-powered career guidance.

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

## 🚧 In Progress

- Analytics Module

## 📅 Planned

- Resume Analytics Dashboard
- Resume Improvement Suggestions
- FastAPI REST API
- React Frontend
- Authentication
- Database Integration
- Docker Support
- Kubernetes Deployment
- AWS Deployment
- AI Resume Copilot (LLM)
- RAG-based Resume Assistant

---

# Features

## Resume Parsing

- Parse PDF resumes
- Parse DOCX resumes
- Clean extracted text
- Extract Contact Information
- Extract Skills
- Extract Education
- Extract Experience

---

## ATS Analysis

- Section Checker
- Keyword Matching
- Resume Formatting Checker
- Grammar Checker (V1)
- ATS Score Calculator

---

## Job Recommendation

- Role Predictor
- Skill Gap Analysis
- Resume Recommendation Engine
- Job Matcher

---

# Tech Stack

## Backend

- Python

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
│   ├── ai_engine/
│   │   ├── ats/
│   │   ├── jobs/
│   │   ├── parser/
│   │   ├── analytics/
│   │   ├── copilot/
│   │   ├── explainability/
│   │   ├── interview/
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
- [ ] Analytics Module
- [ ] Explainability Module
- [ ] Interview Module
- [ ] AI Copilot
- [ ] FastAPI Backend
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
   ├── Experience Parser
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
Recommended Roles & Suggestions
```

---

# Future Roadmap

- Resume Analytics Dashboard
- AI-powered Resume Analysis
- Resume vs Job Description Matching
- Skill Gap Detection
- Resume Improvement Suggestions
- Interview Question Generator
- Explainable AI Recommendations
- LLM Integration
- RAG Integration
- Vector Database
- LangChain
- LangGraph
- FastAPI REST API
- React Frontend
- Docker Deployment
- Kubernetes Deployment
- AWS Cloud Deployment

---

# License

This project is licensed under the MIT License.