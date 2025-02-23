# ETL Pipeline with Apache Airflow and Docker

## Overview
This project implements an **ETL (Extract, Transform, Load) pipeline** using **Apache Airflow** running inside **Docker**. The pipeline automates data ingestion, transformation, and storage using Airflow DAGs.

## Features
- ✅ **Containerized Airflow Setup** using Docker
- ✅ **Automated ETL Workflow** managed by Airflow
- ✅ **Modular and Scalable** pipeline design
- ✅ **Logging and Monitoring** for troubleshooting
- ✅ **Custom Operators and Tasks** for data processing

## Project Structure
```
etl_project/
│── dags/                  # Airflow DAGs for ETL pipeline
│   ├── etl_pipeline.py    # Main ETL DAG
│── scripts/               # Supporting scripts
│   ├── extract.py         # Data extraction logic
│   ├── transform.py       # Data transformation logic
│   ├── load.py            # Data loading logic
│── config/                # Configuration files
│── logs/                  # Airflow logs
│── plugins/               # Custom Airflow plugins
│── docker-compose.yaml    # Docker Compose file for Airflow setup
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
```

## Installation & Setup

### Prerequisites
- **Docker & Docker Compose** installed
- **Python 3.8+** (if running locally without Docker)

### Steps to Set Up the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/etl_project.git
   cd etl_project
   ```

2. **Start Airflow with Docker**
   ```bash
   docker-compose up -d
   ```

3. **Check Airflow UI**
   - Open **http://localhost:8080** in your browser  
   - Default **credentials**:
     - Username: `airflow`
     - Password: `airflow`

4. **Trigger the ETL Pipeline**
   - Navigate to the **DAGs** tab in Airflow UI
   - Enable and trigger `etl_pipeline` DAG

## Environment Variables
Create a `.env` file in the root directory and define:
```
DATABASE_URL=postgresql://user:password@host:port/dbname
S3_BUCKET_NAME=my-etl-bucket
```

## Airflow Commands

- **Check running containers:**
  ```bash
  docker ps
  ```
- **Restart Airflow containers:**
  ```bash
  docker-compose restart
  ```
- **View Airflow logs:**
  ```bash
  docker-compose logs -f
  ```

## Future Enhancements
🚀 Add database integration (PostgreSQL, BigQuery, etc.)  
🚀 Implement error handling & notifications  
🚀 Optimize DAG execution time  

---

This README provides all necessary details to set up and run the project. 🚀

