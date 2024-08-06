import boto3
 

region = 'us-west-2'

client = boto3.client('quicksight',region_name=region)
 
response = client.create_data_source(
    AwsAccountId='059643481773',
    DataSourceId='ensure-360',
    Name='ens360-dashboard-pg-dev',
    Type='S3',
    DataSourceParameters={
        'S3Parameters': {
            'ManifestFileLocation': {
                'Bucket': 'aws-glue-assets-059643481773-us-east-1',
                'Key': 'manifest.json'
            },
            'RoleArn': 'arn:aws:iam::059643481773:role/sentrics' 
        }
    },
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)
 
print(response)
