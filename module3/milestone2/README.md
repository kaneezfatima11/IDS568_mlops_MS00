![Module3-M2 CI](https://github.com/kaneezfatima11/IDS568_mlops_MS00/actions/workflows/module3-milestone2.yml/badge.svg)

# Module 3 – Milestone 2
Containerized FastAPI Application with CI/CD and Secure Image Publishing

## Project Overview

This milestone implements a production-ready FastAPI application that:

- Exposes a health endpoint  
- Includes unit tests  
- Is containerized using Docker  
- Uses multi-stage image optimization  
- Implements a CI pipeline with GitHub Actions  
- Builds and pushes versioned Docker images to GitHub Container Registry (GHCR)

The workflow is triggered on semantic version tags (`v*`).
---

## Architecture Overview

```text
Developer → Git tag (v1.0.x)
        → GitHub Repository
        → GitHub Actions (Test → Build → Push)
        → GitHub Container Registry (GHCR)
        → Deployable Container Image
```

---

## Dockerization

- Base image: `python:3.14-slim`
- Multi-stage optimization
- Dependencies installed from `requirements.txt`
- `.dockerignore` excludes unnecessary files
- Image published to GHCR

---

## CI/CD Workflow

Workflow file: `.github/workflows/module3-milestone2.yml`

**Trigger:** Push tags matching `v*`

### Stages

1. **Test Stage**
   - Set up Python  
   - Install dependencies  
   - Run `pytest`

2. **Build & Push Stage**
   - Authenticate to GHCR  
   - Build Docker image  
   - Tag and push versioned image  

---

## Security & Best Practices

1. Minimal base image reduces attack surface  
2. Multi-stage build separates build and runtime layers  
3. Dependencies controlled via `requirements.txt`  
4. CI runs in a clean, isolated runner environment  
5. Version-controlled releases (`v*` tags only)  
6. Secure authentication using GitHub-provided `GITHUB_TOKEN` (no hardcoded secrets)

---

## Project Structure

```
module3/milestone2/
├── app/
│   ├── __init__.py
│   └── app.py
├── tests/
│   └── test_app.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── RUNBOOK.md
└── README.md
```

---

## Running Locally

### Run App
```bash
uvicorn app.app:app --host 0.0.0.0 --port 8080
```

### Run Tests
```bash
python -m pytest -q
```

### Build Docker Image
```bash
docker build -t ids568-m2:test .
```

### Run Container
```bash
docker run -p 8080:8080 ids568-m2:test
```
