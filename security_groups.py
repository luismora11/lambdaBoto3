import json
import urllib3
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("----------------")
    # Required Variables from Event ---
    slack_webHook_URL = <-----Your Slack Incoming Webhook------>
    userName = str(event['detail']['userIdentity']['userName'])
    awsRegion = str(event['detail']['awsRegion'])
    groupId = str(event['detail']['requestParameters']['groupId'])
    eventName = str(event['detail']['eventName'])
    eventTime = str(event['detail']['eventTime'])
    security_group_URL = "https://"+awsRegion+".console.aws.amazon.com/ec2/v2/home?region="+awsRegion+"#SecurityGroup:group-id="+groupId
    security_group_URL_text = "<"+security_group_URL+"|"+groupId+">"
    data = {"text": "*Security Group Modification Alert!*\n*UserName*:  "+userName+"\n*Security Group ID*:  "+security_group_URL_text+"\n*Event Name*:  "+eventName+"\n*Event Time*:  "+eventTime+"\n*Region*:  "+awsRegion}
    
    # Calling Slack API ---
    http = urllib3.PoolManager()
    req = http.request("POST",slack_webHook_URL, body = json.dumps(data), headers = {"Content-Type": "application/json"})
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Done Posting Message!')
    }