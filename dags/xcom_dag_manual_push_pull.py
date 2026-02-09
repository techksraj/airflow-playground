from airflow.sdk import dag, task, Context

@dag
def xcom_dag_manual_push_pull():

    @task
    def task_a(**context: Context):
        val = 42
        context['ti'].xcom_push(key='my_key', value=val)

    @task
    def task_b(**context: Context):
        val = context['ti'].xcom_pull(task_ids='task_a', key='my_key')
        print(val)

    task_a() >> task_b()

xcom_dag_manual_push_pull()