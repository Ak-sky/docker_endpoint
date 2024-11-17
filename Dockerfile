# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY wifi_api.py /app/

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "wifi_api.py"]