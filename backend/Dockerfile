# Use an official Python runtime as a parent image.
# This gives you a pre-built environment with Python installed.
FROM python:3.10-slim

# Set the working directory inside the container.
# All subsequent commands will be run from this directory.
WORKDIR /app

# Install system dependencies required for OpenCV
# These libraries are needed even for headless OpenCV processing
RUN apt-get update && apt-get install -y \
    libgl1 \
    libgl1-mesa-dri \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgthread-2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory's contents into the container at /app.
# This brings your app.py file into the container.
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the command to execute your application.
# This is the last thing that happens when the container starts.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
