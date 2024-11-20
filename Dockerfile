# Use the official Apache Airflow image as the base image
FROM apache/airflow:2.5.1-python3.10

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install the packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the Airflow environment variables are set
ENV AIRFLOW_HOME=/opt/airflow