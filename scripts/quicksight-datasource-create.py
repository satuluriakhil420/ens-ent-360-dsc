import os
import boto3

# Initialize the QuickSight client
region = os.getenv('AWS_REGION')
client = boto3.client('quicksight', region_name=region)

# Retrieve values from environment variables
aws_account_id = os.getenv('AWS_ACCOUNT_ID')
data_source_id = os.getenv('DATA_SOURCE_ID')
name = os.getenv('NAME')
bucket = os.getenv('BUCKET')
key = os.getenv('KEY')
role_arn = os.getenv('ROLE_ARN')

# Create the QuickSight data source
response = client.create_data_source(
    AwsAccountId=aws_account_id,
    DataSourceId=data_source_id,
    Name=name,
    Type='S3',
    DataSourceParameters={
        'S3Parameters': {
            'ManifestFileLocation': {
                'Bucket': bucket,
                'Key': key
            },
            'RoleArn': role_arn 
        }
    },
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)

print("QuickSight data source created successfully.")

