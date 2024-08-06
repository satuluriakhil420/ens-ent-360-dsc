import boto3

region = 'us-east-1'

client = boto3.client('quicksight',region_name=region)
 
response = client.create_account_subscription(
    Edition='ENTERPRISE',  
    AuthenticationMethod='IAM_AND_QUICKSIGHT',  
    AwsAccountId='059643481773',
    AccountName='enrich-dev',
    NotificationEmail='satulakhil@gmail.com',
)
