import requests
import config

def send_message_to_slack(payload):
    slack_url = config.url
    requests.post(slack_url, json=payload)
