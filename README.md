

!\[C](https://github.com/kaneezfatima11/IDS568\_mlops\_MS00/actions/workflows/ci.yml/badge.svg)



\# IDS568 – MLOPs



\## Milestone 0: Environment Reproducibility and ML Lifecycle Reliability



Environment reproducibility is critical for building reliable machine learning systems, especially during data preprocessing, where results can vary significantly due to differences in software versions and dependencies. In this project, the Milestone 0 environment setup supports reliable data preprocessing by using an isolated Python virtual environment and pinned dependency versions in requirements.txt. This ensures that libraries such as NumPy and pandas behave consistently across machines and over time, preventing discrepancies in data cleaning, feature engineering, and transformation steps.



Automated validation using GitHub Actions further strengthens lifecycle reliability by rebuilding the environment in a clean runner and executing smoke tests without manual intervention. These smoke tests verify that core data-processing libraries import correctly and perform basic numerical operations, providing early assurance that the preprocessing pipeline can run successfully before model development begins.



Together, environment isolation, dependency pinning, and continuous integration reduce the risk of data leakage, inconsistent feature transformations, and “works on my machine” issues. This establishes a stable, reproducible, and scalable foundation for downstream stages of the ML lifecycle, including model training

