import sys
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import sys
sys.path.append("/opt/airflow/scripts")

from etl_pipeline import (
    download_dataset,
    untar_dataset,
    extract_data_from_csv,
    extract_data_from_fixed_width,
    consolidate_data,
    transform_data
)

# Default arguments for Airflow
default_args = {
    'owner': 'saladi ',
    'start_date': datetime.today(),
    'email': ['saladisairamteja@gmail.com'],
    'email_on_failure': False,
    'retries': 1,
}

# Define the DAG
with DAG(
    dag_id='ETL_toll_data',
    schedule='@daily',  # Runs once daily
    default_args=default_args,
    description='First ETL pipeline',
    catchup=False # Prevent tasks from backfilling
) as dag:
    
    download_task = PythonOperator(
        task_id='download_dataset',  # Task ID
        python_callable=download_dataset # Function to be called
    )
    
    untar_task = PythonOperator(
        task_id='untar_dataset',
        python_callable=untar_dataset
    )
    
    extract_csv_task = PythonOperator(
        task_id='extract_data_from_csv',
        python_callable=extract_data_from_csv
    )
    
    extract_fixed_width_task = PythonOperator(
        task_id='extract_data_from_fixed_width',
        python_callable=extract_data_from_fixed_width
    )
    
    consolidate_task = PythonOperator(
        task_id='consolidate_data',
        python_callable=consolidate_data
    )
    
    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    # Define task dependencies
    download_task >> untar_task >> extract_csv_task >> extract_fixed_width_task >> consolidate_task >> transform_task
    