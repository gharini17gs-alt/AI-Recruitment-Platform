FROM python:3.11-slim

# Install Tesseract OCR
RUN apt-get update \
    && apt-get install -y --no-install-recommends tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# App folder
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Render uses the PORT environment variable
CMD gunicorn app:app --bind 0.0.0.0:$PORT