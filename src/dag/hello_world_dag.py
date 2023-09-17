from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from script.alert_sender import slack_alert_sender

default_args = {
    "start_date": datetime(2023, 8, 1),
    "on_failure_callback": slack_alert_sender,
    "catchup": True,
    "responsible": "<@U01MM7PKX1A>",
}

dag = DAG(
    dag_id="hello_world_dag",
    schedule_interval=None,
    default_args=default_args,
)


def print_hello():
    "Função para reproduzir o erro"
    print("Hello, World!")

    print(dict()[23])


hello_task = PythonOperator(
    task_id="print_hello_task",
    python_callable=print_hello,
    dag=dag,
)

hello_task
