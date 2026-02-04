![CI](https://github.com/kaneezfatima11/IDS568_mlops_MS00/actions/workflows/ci.yml/badge.svg)

# IDS568-Artificial Intelligence Dev

## Milestone 0: Environment reproducibility and ML Lifecyle Reliability: 

Environment reproducibility is crucial for building reliable machine learning systems, especially during data preprocessing phase where results can vary due to differences in software versions and dependencies. In this project, milestone 0 setting up isolated virtual environment supports reliable data preprocessing along with pinned dependency versions in the "requirements.txt". It ensures that libraries such as NumPy and pandas behave consistently across machines and over time, preventing discrepancies in data cleaning, feature engineering and transformations. 

Further, automated validation using GitHub Actions strengthens Lifecyle reliability by building the environment in a clean runner and executing smoke tests without manual interventions. These smoke tests verify that core data processing libraries import correctly and perform basic numerical operations , providing early assurance that the preprocessing pipeline can run successfully before development begins.

In short, all these steps i.e. environment isolation, dependency pinning and continuous integration reduce the risk of data leakage, inconsistent feature transformations and "works on my machine" issues. It establishes a stable, reproducible and scalable foundation for ML Lifecyle stages in particular to model training, evaluation and deployment.

## Milestone 1: Cloud Deployment and Serving Comparison:

This milestone extends the ML lifecycle from local inference to cloud-based deployment using two serving paradigms.

The FastAPI application was containerized using Docker and deployed to Google Cloud Run, enabling a stateful, container-based inference service that loads the trained model artifact at startup and serves predictions via a REST API.

In parallel, a stateless serverless inference endpoint was implemented using Google Cloud Functions. The same trained model artifact is packaged with the function and loaded on invocation, demonstrating a lightweight, event-driven serving approach.

Cloud Run offers greater flexibility and control over dependencies and runtime configuration, while Cloud Functions provide simpler deployment with minimal infrastructure management. Both approaches highlight trade-offs in cold-start behavior, scalability, and lifecycle management within modern MLOps systems.

**Project Overview**
This project demonstrates an end-to-end MLOps workflow that transitions a trained machine learning model from local development to production-ready inference services. The goal of Milestone 1 is to ensure reproducibility, reliable serving, and scalable deployment using both container-based and serverless cloud platforms.

**Setup and Deployment Instructions**
The project is developed in an isolated Python virtual environment to ensure consistent dependency management and reproducibility across systems. All required libraries are pinned in a requirements file. Docker Desktop is used to containerize the application, and the Google Cloud CLI is used for cloud deployment and service management.

**Model Training**
The machine learning model is trained using a dedicated training script. The trained model is serialized into a reusable artifact file and stored in the project repository. This artifact is reused across all serving environments to guarantee consistent inference behavior.

**Local API Serving with FastAPI**
A FastAPI application exposes the trained model through REST endpoints. The model artifact is loaded once at application startup to ensure deterministic predictions and efficient request handling. The application includes a health endpoint for service monitoring and a prediction endpoint that accepts numerical feature inputs and returns model predictions in JSON format.

**API Usage Examples**
Clients interact with the service by sending HTTP requests containing numerical feature vectors. The prediction endpoint processes the input features and returns a structured prediction response. The health endpoint confirms service availability and readiness
Automated Testing and Continuous Integration
Automated tests validate the health and prediction endpoints. A continuous integration pipeline runs these tests in a clean environment on every commit, ensuring reproducible behavior and preventing environment-specific failures.

**Cloud Deployment using Google Cloud Run**
The FastAPI application is containerized using Docker and deployed to Google Cloud Run. This deployment represents a stateful, container-based serving approach where the model artifact is loaded at startup. Cloud Run provides scalability, runtime flexibility, and controlled dependency management.

**Serverless Deployment using Google Cloud Functions**
A stateless inference endpoint is implemented using Google Cloud Functions. The same trained model artifact is packaged with the function and executed on demand. This approach demonstrates an event-driven serving model with minimal infrastructure management.

**ML Lifecycle Stage Explanation**
This milestone spans multiple stages of the machine learning lifecycle, including training, packaging, validation, serving, and deployment. The consistent reuse of the trained model artifact across all environments ensures reliability and reproducibility throughout the lifecycle.

**Model–API Interaction**
The API receives feature vectors in JSON format, transforms them into the appropriate numerical structure, and passes them to the trained model for inference. Predictions are returned as structured JSON responses, enabling seamless integration with downstream systems.

**Deployment Pattern Comparison**
The Cloud Run deployment provides greater control over runtime configuration and is suitable for complex, stateful services. Cloud Functions offer a lightweight, stateless deployment model with reduced operational overhead. This comparison highlights trade-offs related to scalability, cold-start behavior, and lifecycle management.

**Conclusion**
Milestone 1 demonstrates how a trained machine learning model can be reliably deployed across local, containerized, and serverless environments. By combining reproducible environments, automated testing, and cloud-native serving strategies, the project showcases best practices in modern MLOps.