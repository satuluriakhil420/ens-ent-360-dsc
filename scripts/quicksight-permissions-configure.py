import os
import boto3

# Initialize the QuickSight client
region = os.getenv('AWS_REGION')
client = boto3.client('quicksight', region_name=region)

# Retrieve values from environment variables
identity_type = os.getenv('IDENTITY_TYPE')
email = os.getenv('EMAIL')
user_role = os.getenv('USER_ROLE')
aws_account_id = os.getenv('AWS_ACCOUNT_ID')
namespace = os.getenv('NAMESPACE')
user_name = os.getenv('USER_NAME')
tag_key = os.getenv('TAG_KEY')
tag_value = os.getenv('TAG_VALUE')

# Register the QuickSight user
response = client.register_user(
    IdentityType=identity_type,
    Email=email,
    UserRole=user_role,
    AwsAccountId=aws_account_id,
    Namespace=namespace,
    UserName=user_name,
    Tags=[
        {
            'Key': tag_key,
            'Value': tag_value
        }
    ]
)

print("User registered:", response)

