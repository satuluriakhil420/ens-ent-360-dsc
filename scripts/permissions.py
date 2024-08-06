import boto3
 
client = boto3.client('quicksight', region_name='us-east-1')
 
response = client.register_user(
    IdentityType='QUICKSIGHT',
    Email='test123@gmail.com',
    UserRole='ADMIN',
    AwsAccountId='059643481773',
    Namespace='default',
    UserName='sentrics',
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'Dev'
        }
    ]
)
 
print("User registered:", response)
