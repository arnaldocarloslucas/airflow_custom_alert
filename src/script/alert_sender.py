from airflow.hooks.base_hook import BaseHook
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator
from datetime import date

SLACK_CONN_ID = 'slack'


def slack_alert_sender(context):
    """Function to deliver error messages to slack."""

    slack_webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password
    if not context.get('task_instance').previous_start_date_success:
        custom_message = """:eyes: DAG nunca finalizou com sucesso.
        :cop: Realize a correção do código.
        :warning: DAG será desligada até que a correção seja realizada."""

    else:
        last_success_date = context.get('task_instance').previous_start_date_success.date()
        custom_message = f"""
        :calendar: *Última execução com sucesso:* {last_success_date}
        :bug: *Dias quebrando consecutivamente:* {
            (date.today() - last_success_date).days
        }
    """


    slack_msg = f"""
        :rotating_light: TASK FAILED.
        *Task*: {context.get('task_instance').task_id}
        *Dag*: {context.get('task_instance').dag_id}
        *Execution Time*: {context.get('execution_date')}
        *Log Url*: {context.get('task_instance').log_url}
        *Responsible*: {context["dag"].default_args.get("responsible")}
        {custom_message}
    """

    failed_alert = SlackWebhookOperator(
        task_id='slack_test',
        http_conn_id='slack',
        webhook_token=slack_webhook_token,
        message=slack_msg,
        username='airflow')
    return failed_alert.execute(context=context)
