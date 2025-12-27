# Use Python 3.8 slim image
FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .

# Expose port (adjust if your Flask app uses different port)
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]
