import os
import boto3

# Initialize the Glue client
glue_client = boto3.client('glue')

# Retrieve values from environment variables
crawler_name = os.getenv('CRAWLER_NAME')
role = os.getenv('ROLE')
database_name = os.getenv('DATABASE_NAME')
table_prefix = os.getenv('TABLE_PREFIX')
s3_path = os.getenv('S3_PATH')

description = f"description for {crawler_name}"

# Define the S3 target
s3_target = {
    'Path': s3_path,
    'Exclusions': []
}

# Update the crawler
response = glue_client.update_crawler(
    Name=crawler_name,
    Role=role,
    DatabaseName=database_name,
    Description=description,
    Targets={
        'S3Targets': [s3_target],
        'JdbcTargets': [],
        'MongoDBTargets': [],
        'DynamoDBTargets': [],
        'CatalogTargets': []
    },
    TablePrefix=table_prefix
)

print("Crawler updated successfully.")
