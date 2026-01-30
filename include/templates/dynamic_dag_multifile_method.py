from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(f'process_DAG_ID_HOLDER', start_date=datetime(2026, 1, 1), schedule='SCHEDULER_INTERVAL_HOLDER', catchup=False) as dag:

    @task
    def extract(filename):
        return filename

    @task
    def process(filename):
        return filename
    
    @task
    def send_email(filename):
        print(filename)
        return filename
    
    send_email(process(extract('INPUT_HOLDER')))
