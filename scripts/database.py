import boto3

region = 'us-east-2'

# Initialize the Glue client
glue_client = boto3.client('glue')

response = glue_client.update_database(
    Name='ens360-dashboard-db-dev-01',
    DatabaseInput={
        'Name': 'ens360-dashboard-db-dev-01',
        'Description': 'Provides information regarding ensure 360'
    }
)


