from airflow.sdk import dag, task, Context

@dag
def xcom_dag_manual_multiple_values():

    @task
    def task_a(ti):
        val = 42
        ti.xcom_push(key='my_key', value=val)

    @task
    def task_b(ti):
        val = 43
        ti.xcom_push(key='my_key', value=val)

    @task
    def task_c(ti):
        vals = ti.xcom_pull(task_ids=['task_a', 'task_b'], key='my_key')
        print(vals)

    task_a() >> task_b() >> task_c()

xcom_dag_manual_multiple_values()