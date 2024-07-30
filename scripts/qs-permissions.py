import boto3

client = boto3.client('quicksight', region_name='us-east-1')

response = client.register_user(
    IdentityType='QUICKSIGHT',
    Email='test@gmail.com',
    UserRole='ADMIN',
    AwsAccountId='059643481773',
    Namespace='default',
    UserName='test-user',
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'Dev'
        }
    ]
)
