from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(f'process_file_c_dag', start_date=datetime(2026, 1, 1), schedule='@daily', catchup=False) as dag:

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
    
    send_email(process(extract('file_c.csv')))
