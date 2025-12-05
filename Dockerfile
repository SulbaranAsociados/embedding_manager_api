# Use an official Python runtime as a parent image
FROM python:3.11-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 80

# Define environment variable for Python
ENV PYTHONUNBUFFERED=1

# Run the uvicorn server when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
