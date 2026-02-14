![CI](https://github.com/kaneezfatima11/IDS568_mlops_MS00/actions/workflows/ci.yml/badge.svg)

# IDS568 – Artificial Intelligence Dev

## Repository Overview

This repository contains structured deliverables for IDS 568 (MLOps / AI Dev).  
Each milestone demonstrates reliability, reproducibility, and deployment practices across the machine learning lifecycle.

---

## How to Navigate

Key locations:

- **Root README (this file):** High-level overview of all milestones  
- **module3/milestone2/:** Module 3 Milestone 2 deliverables (app, tests, Docker, workflow, runbook)  
- **.github/workflows/:** GitHub Actions workflows (CI automation)  

---

# Milestone 0: Environment Reproducibility and ML Lifecycle Reliability

Environment reproducibility is critical for building reliable machine learning systems, particularly during data preprocessing and early development stages where results can vary due to differences in software versions and dependencies.

In this milestone:

- An isolated Python virtual environment is used  
- Dependencies are pinned in `requirements.txt`  
- Core libraries (NumPy, pandas) behave consistently across machines  

Automated validation is implemented using GitHub Actions. The CI pipeline recreates the environment in a clean runner and executes smoke tests on every commit. These tests verify that essential libraries import correctly and perform basic numerical operations.

Together, environment isolation, dependency pinning, and automated CI reduce the risk of inconsistent feature transformations and “works on my machine” failures.

---

# Milestone 1: Cloud Deployment and Serving Comparison

Milestone 1 extends the machine learning lifecycle from local inference to cloud-based deployment using two distinct serving paradigms:

- Container-based services  
- Serverless functions  

The same trained model artifact (`model.pkl`) is reused across all deployment patterns to ensure consistent inference behavior and lifecycle reliability.

---

## Model Training and Artifact Management

The model is trained using a dedicated script and serialized into a reusable artifact (`model.pkl`).  
This artifact represents a deterministic snapshot of the trained model and is treated as a first-class lifecycle object.

It is reused for:

- Local FastAPI inference  
- Cloud Run container deployment  
- Google Cloud Functions deployment  

---

## Local API Serving with FastAPI

A FastAPI application exposes the trained model through REST endpoints.

The API includes:

- `/health` endpoint for service monitoring  
- `/predict` endpoint for inference  

Pydantic schemas enforce strict input validation and output consistency.

---

## Automated Testing and Continuous Integration

Automated tests validate both the health and prediction endpoints.

The CI pipeline ensures:

- Environment reproducibility  
- Deterministic artifact loading  
- API correctness in a clean execution environment  

---

## Deployment Pattern Comparison

Two deployment patterns are compared:

- **Cloud Run (Container-based, Stateful):**  
  - Greater control over runtime and dependencies  
  - Model loaded once at startup  
  - Suitable for complex services  

- **Cloud Functions (Serverless, Stateless):**  
  - Lightweight and event-driven  
  - Model loaded per invocation  
  - Reduced operational overhead  

---

# Milestone 2: FastAPI + Docker + CI/CD + GHCR

Module 3 Milestone 2 builds a standalone FastAPI microservice that is:

- Containerized using Docker  
- Tested via GitHub Actions  
- Released using semantic version tags  
- Published to GitHub Container Registry (GHCR)  

📍 Location: `module3/milestone2/`  
📄 Detailed documentation: `module3/milestone2/README.md`


---

## Release Trigger

Publishing is triggered only on semantic version tags (`v*`), for example:

```bash
git tag v1.0.3
git push origin v1.0.3
```