# ---------- builder ----------
FROM python:3.11-slim AS builder

WORKDIR /build

# Create and use a venv for dependencies
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---------- runtime ----------
FROM python:3.11-slim

# Non-root user (security best practice)
RUN useradd -m appuser

WORKDIR /app

# Copy venv from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy only the app code needed at runtime
COPY app ./app

ENV PORT=8080
EXPOSE 8080

USER appuser

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8080"]
