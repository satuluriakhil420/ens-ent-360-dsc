import os
import boto3

# Initialize the QuickSight client
region = os.getenv('AWS_REGION')
client = boto3.client('quicksight', region_name=region)

# Retrieve values from environment variables
aws_account_id = os.getenv('AWS_ACCOUNT_ID')
account_name = os.getenv('ACCOUNT_NAME')
notification_email = os.getenv('NOTIFICATION_EMAIL')

# Create the QuickSight account subscription
response = client.create_account_subscription(
    Edition='ENTERPRISE',  
    AuthenticationMethod='IAM_AND_QUICKSIGHT',  
    AwsAccountId=aws_account_id,
    AccountName=account_name,
    NotificationEmail=notification_email,
)

print("QuickSight account subscription created successfully.")
