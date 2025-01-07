# Use a base image
FROM python:3.11-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Set up environment variables
WORKDIR /app/backend/core
RUN cp .env.example .env

# Set the working directory for the application
WORKDIR /app/backend

# Expose the application port
EXPOSE 8000

# Command to run migrations and start the application
CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000"]
