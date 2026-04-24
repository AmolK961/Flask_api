# Use official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the Flask app into the container
COPY . .

# Expose the Flask application port
EXPOSE 5000

# Run the Flask app when the container starts
CMD ["python", "app.py"]