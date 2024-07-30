import boto3
 
glue_client = boto3.client('glue')
 
crawler_name = 
role = 
database_name = 
table_prefix = 
 

description = "description for ens360-dashboard-crawler"

s3_target = {
    'Path': ,
    'Exclusions': []
}
 
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
 
print("Crawler created successfully.")
