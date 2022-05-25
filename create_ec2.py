import boto3

def lambda_handler(event, context):

    client = boto3.client('ec2')

    resp = client.run_instances(
        ImageId = 'your image id',
        InstanceType = 't2.micro',
        MinCount = 1,
        MaxCount = 1,
        KeyName = 'your key name',
        SecurityGroupIds = ['your Security Group ID'],
        TagSpecifications = [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'key': 'Name', 'value': 'Linux server'},
                    {'Key': 'Env', 'value': 'Dev'}
                ]
            },
        ],
    )