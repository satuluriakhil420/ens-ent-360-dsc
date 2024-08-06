import os
import boto3

# Initialize the Glue client
region = os.getenv('AWS_REGION')
glue_client = boto3.client('glue', region_name=region)

# Retrieve values from environment variables
database_name = os.getenv('DATABASE_NAME')
database_description = os.getenv('DATABASE_DESCRIPTION')

# Update the Glue database
response = glue_client.update_database(
    Name=database_name,
    DatabaseInput={
        'Name': database_name,
        'Description': database_description
    }
)

print("Glue database updated successfully.")

