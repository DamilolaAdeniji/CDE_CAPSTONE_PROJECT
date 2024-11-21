# Use the official Apache Airflow image as the base image
FROM apache/airflow:2.5.1-python3.10

# Set the Airflow home environment
ENV AIRFLOW_HOME=/opt/airflow

# Copy dag into the Airflow DAGs directory
COPY ./dags $AIRFLOW_HOME/dags

# Copy Python dependencies
COPY ./requirements.txt $AIRFLOW_HOME/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r $AIRFLOW_HOME/requirements.txt