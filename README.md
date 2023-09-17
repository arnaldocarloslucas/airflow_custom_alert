# airflow_custom_alert
A custom script to better Airflow alerts on Slack

# What this script offers?
This repository aims to provide a customized script for Airflow DAG failure alerts to notify messages such as DAG name, task, execution time and url to the error log in Slack.

# What makes this alert different?
In addition to these components, we have the main differences from common alerts on the market, such as the team/person responsible for the code that broke as well as a counter of days that have been breaking since the first error.

# How to use?

> 1 - Copy the script into your project where the DAG that you want to customize the alert is located.

>2 - Change the "responsible" parameter that is in the default_args within the main DAG file, adding the ID that can be collected by going to the user's slack profile, click on the 3 vertical dots and copy the member's ID. Add the ID in the following format <@ID>.

Example:
<@U01MM7QPKT1A>

```python
default_args = {
    "start_date": datetime(2023, 8, 1),
    "on_failure_callback": slack_alert_sender,
    "catchup": True,
    "responsible": "<@U01MM7QPKT1A>",
}
```

> 3 - Import the "slack_alert_sender" function that is in the "alert_sender" script into the main DAG file and add the "on_failure_callback" parameter to the default_args with the function.
