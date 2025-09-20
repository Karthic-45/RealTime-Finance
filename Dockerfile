FROM python:3.11-slim

WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download TextBlob corpora for sentiment analysis
RUN python -m textblob.download_corpora

# Copy all project files
COPY . .

# Expose port for Flask
EXPOSE 8000

# Run the backend app
CMD ["python", "backend/app.py"]
