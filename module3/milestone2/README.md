![CI](https://github.com/kaneezfatima11/IDS568_mlops_MS00/actions/workflows/ci.yml/badge.svg)

# IDS568-Artificial Intelligence Dev

## Milestone 0: Environment reproducibility and ML Lifecyle Reliability:
Environment reproducibility is critical for building reliable machine learning systems, particularly during data preprocessing and early development stages where results can vary due to differences in software versions and dependencies.
In this milestone, an isolated Python virtual environment is used together with pinned dependency versions specified in requirements.txt. This ensures consistent behavior of core libraries such as NumPy and pandas across machines and over time, preventing discrepancies in data cleaning, feature engineering, and transformations.
Automated validation is implemented using GitHub Actions. The continuous integration pipeline recreates the environment in a clean runner and executes smoke tests on every commit. These tests verify that essential libraries import correctly and perform basic numerical operations, providing early assurance that the pipeline is functional before further development.
Together, environment isolation, dependency pinning, and automated CI reduce the risk of data leakage, inconsistent feature transformations, and “works on my machine” failures. This establishes a stable and reproducible foundation for downstream ML lifecycle stages.

**Milestone 1: Cloud Deployment and Serving Comparison**

Milestone 1 extends the machine learning lifecycle from local inference to cloud-based deployment using two distinct serving paradigms:
container-based services and serverless functions.
The same trained model artifact is reused across all deployment patterns to ensure consistent inference behavior and reliable lifecycle management.

**Model Training and Artifact Management**
The machine learning model is trained using a dedicated training script and serialized into a reusable artifact (model.pkl). This artifact represents a deterministic snapshot of the trained model and is treated as a first-class lifecycle object.
The same artifact is reused for:
Local FastAPI inference
Cloud Run container deployment
Google Cloud Functions deployment
This guarantees consistent predictions across all serving environments.

**Local API Serving with FastAPI**
A FastAPI application exposes the trained model through REST endpoints. The model artifact is loaded once at application startup, ensuring deterministic behavior and efficient request handling.
The API includes:
A /health endpoint for service monitoring
A /predict endpoint that accepts numerical feature vectors and returns predictions in JSON format
Pydantic request and response schemas enforce strict input validation and output consistency.

**Automated Testing and Continuous Integration**
Automated tests validate both the health and prediction endpoints. These tests are executed locally and within a GitHub Actions workflow.
The CI pipeline ensures:
Environment reproducibility
Deterministic artifact loading
API correctness in a clean execution environment
A passing CI badge confirms the reliability of the codebase.

**Cloud Deployment Using Google Cloud Run**
The FastAPI application is containerized using Docker and deployed to Google Cloud Run. This deployment represents a stateful, container-based serving approach, where the model artifact is loaded at container startup and reused for all incoming requests.
Cloud Run provides:
HTTPS-accessible endpoints
Controlled runtime environments
Horizontal scalability
Explicit dependency and artifact management
Successful inference is verified using the deployed public service URL.

**Serverless Deployment Using Google Cloud Functions**
In parallel, a stateless serverless inference endpoint is implemented using Google Cloud Functions. The trained model artifact is packaged with the function and loaded during invocation.
This approach demonstrates:
Event-driven execution
Minimal infrastructure management
Automatic scaling
The function endpoint is successfully invoked and returns valid predictions, confirming correct deployment.

**ML Lifecycle Stage Explanation**
This project spans multiple stages of the machine learning lifecycle, including:
Environment setup and reproducibility
Model training and artifact creation
Validation and testing
Serving and deployment
Monitoring and comparison of deployment patterns
The consistent reuse of the trained artifact across environments ensures lifecycle continuity and reliability.

**Model–API Interaction**
The API receives feature vectors in JSON format, converts them into the appropriate numerical structure, and passes them to the trained model for inference. Predictions are returned as structured JSON responses, enabling seamless integration with downstream consumers.

**Deployment Pattern Comparison**
Two deployment patterns are compared:
**Cloud Run (Container-based, Stateful)**
Greater control over runtime and dependencies
Model loaded once at startup
Suitable for complex or long-running services
**Cloud Functions (Serverless, Stateless)**
Lightweight and event-driven
Model loaded per invocation
Reduced operational overhead with simpler deployment
This comparison highlights trade-offs in cold-start behavior, scalability, state management, and reproducibility within modern MLOps systems.

**Conclusion**
Milestone 1 demonstrates how a trained machine learning model can be reliably deployed across local, containerized, and serverless environments. By combining reproducible environments, automated testing, and cloud-native serving strategies, this project showcases best practices for building robust and scalable MLOps pipelines.

