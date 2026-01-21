![CI](https://github.com/kaneezfatima11/IDS568_mlops_MS00/actions/workflows/ci.yml/badge.svg)

# IDS568-Artificial Intelligence Dev

## Milestone0: Environment reproducibility and ML Lifecyle Reliability 

Environment reproducibility is crucial for building reliable machine learning systems, especially during data preprocessing phase where results can vary due to differences in software versions and dependencies. In this project, milestone 0 setting up isolated virtual environment supports reliable data preprocessing along with pinned dependency versions in the "requirements.txt". It ensures that libraries such as NumPy and pandas behave consistently across machines and over time, preventing discrepancies in data cleaning, feature engineering and transformations. 

Further, automated validation using GitHub Actions strengthens Lifecyle reliability by building the environment in a clean runner and executing smoke tests without manual interventions. These smoke tests verify that core data processing libraries import correctly and perform basic numerical operations , providing early assurance that the preprocessing pipeline can run successfully before development begins.

In short, all these steps i.e. environment isolation, dependency pinning and continuous integration reduce the risk of data leakage, inconsistent feature transformations and "works on my machine" issues. It establishes a stable, reproducible and scalable foundation for ML Lifecyle stages in particular to model training, evaluation and deployment.