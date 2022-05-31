import json
import boto3

def lambda_handler(event, context): 


    ec2_client = boto3.client("ec2", region_name=event['region'])
    reservations = ec2_client.describe_instances(InstanceIds=[event['instance']]).get("Reservations")

    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            reason = instance['StateTransitionReason']
            instanceName = "No Name Found"
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    instanceName = tag['Value']
            
    
    message = "The EC2 Instance (*" + instanceName + "*) has changed to *" + event['state'] + "* \n \n Instance ID: *"+ instance_id + "* \n" + " Instance Type: *" + instance_type + "* \n" + "Reason: *" + reason + "* " 
    
    return { 
        'message' : message,
        'title': 'ec2 state change'
    }