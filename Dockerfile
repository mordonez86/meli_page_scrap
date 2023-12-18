# Use a base Python image from Docker Hub
FROM python:3.9

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# read the arguments
ARG arg1

# Define the command to run your Python script
CMD ["python", "main.py"]