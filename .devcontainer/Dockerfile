# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the prediction directory into the container
COPY prediction/ .

# Define the command to run your application
CMD ["python", "main.py"]
