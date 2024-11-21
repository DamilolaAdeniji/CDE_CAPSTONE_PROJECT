# Core Data Engineering Bootcamp: Capstone project

#### This project exports data from the Country REST API to a cloud-based Object Storage and Database/Data Warehouse. 
#### The raw data is stored in Parquet format for performance and future scalability. Specific fields required for predictive analytics are extracted and loaded into the Database/Data Warehouse. 
#### The entire workflow is automated using Apache Airflow, with infrastructure provisioned through Terraform and packaged into a Docker image for deployment.

## Setup
### **1. Prerequisites**
- Terraform, Docker, Airflow and Python 3.10
- Access to AWS with permissions to provision an s3 bucket, IAM, and RDS services.

### **2. Infrastructure Setup**
- Use the Terraform configuration files in this repository to provision the s3 bucket and RDS (without the backend.tf):

` 
terraform init
`

` 
terraform plan
`

` 
terraform apply
`
- Then import the `backend.tf` file into the terraform dir and re-initialize terraform to move the statefile to s3

### **3. Docker setup**
- Use the provided `Dockerfile` to rebuild the airflow base image with all packages in the `requirements.txt` file by running the command below

- `
docker build -t cde-airflow:latest .
`

- Start the containers defined in the `docker-compose.yml`

- `
docker compose up
`


### **4. Workflow Deployment**
- Use the provided Airflow DAG in the `dags` directory to orchestrate:
  1. API data extraction.
  2. Raw data storage in s3.
  3. Data transformation and staging in s3
  4. Final loading into RDS.

