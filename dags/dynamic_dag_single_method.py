from airflow import DAG
from airflow.decorators import task
from datetime import datetime

def create_dag(filename):
    with DAG(f'process_{filename}', start_date=datetime(2026, 1, 1), schedule='@daily', catchup=False) as dag:

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
        
        send_email(process(extract(filename)))

    return dag

for file in ['file_A', 'file_B', 'file_C']:
    globals()[f"dag_{file}"] = create_dag(file)