# dbt Orchestration DAG
# Apache Airflow DAG for orchestrating dbt models

from datetime import datetime, timedelta
from airflow import DAG
from airflow.bash_operator import BashOperator

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
    'dbt_orchestration_dag',
    default_args=default_args,
    description='dbt model orchestration DAG',
    schedule_interval='@daily',
    catchup=False,
)

# Define dbt tasks here
