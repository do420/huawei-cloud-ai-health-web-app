# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install any required dependencies
RUN pip install flask
RUN pip install pillow
RUN pip install requests


# Expose a port (if your app listens on a specific port)
EXPOSE 5000

# Define the command to run your application
CMD ["python", "app/app.py"]
