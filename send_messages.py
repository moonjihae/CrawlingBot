import requests


def send_message_to_slack(payload):
    slack_url = "https://hooks.slack.com/services/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"
    requests.post(slack_url, json=payload)
