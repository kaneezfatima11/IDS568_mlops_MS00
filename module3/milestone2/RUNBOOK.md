## Image Optimization Strategy

### Before Optimization
Initial image build:
- Base image: python:3.14-slim
- Single-stage build
- Image content size: ~159MB

### After Optimization
Updated image build:
- Multi-stage Docker build (builder + runtime)
- Base image: python:3.11-slim
- Dependencies installed in virtual environment
- Non-root user in runtime stage
- Only application code copied into runtime image
- Image content size: ~166MB

### Observations
The optimized image separates build and runtime environments and improves security posture. Although content size remained similar (since base image was already slim), the multi-stage design follows production-grade best practices and aligns with MLOps container optimization guidelines.
