# Example Pipeline DAG
# Apache Airflow DAG definition for data pipeline orchestration

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'data-eng',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'example_pipeline_dag',
    default_args=default_args,
    description='Example data pipeline DAG',
    schedule_interval='@daily',
    catchup=False,
)

# Define tasks here
