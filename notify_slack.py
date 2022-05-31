import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from datetime import datetime
import boto3

session = boto3.session.Session()


class SlackParser:
    def __init__(self, msg):
        self.msg = msg
        self.timestamp_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        self.color = "danger"

    def slack_data(self):
        _message = {
            'text': '', 
            'attachments': [
                {
                    'title': ":awse: AWS Notification",
                    'color': self.color,
                    'fields': [
                        {
                            "title": self.msg['title'],
                            "value": self.msg['message'],
                            "short": False
                        }
                    ]
                }
            ]
        }
        return _message



def lambda_handler(event, context):
    message = event
    print(message)

    webhook_url = 'https://hooks.slack.com/services/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' # Set destination URL here

    slack_data = SlackParser(message).slack_data()
    slack_data["channel"] = 'automation'


    request = Request(
        webhook_url, 
        data=json.dumps(slack_data).encode(),
        headers={'Content-Type': 'application/json'}
        )
    response = urlopen(request)
    
    return {
        'statusCode': 200,
        'body': response.read().decode()
    }


if __name__ == "__main__":
    print(lambda_handler(None, None))