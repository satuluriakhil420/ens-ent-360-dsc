import os
import boto3
from datetime import datetime

# Initialize the QuickSight client
region = os.getenv('AWS_REGION')
client = boto3.client('quicksight', region_name=region)

# Retrieve values from environment variables
aws_account_id = os.getenv('AWS_ACCOUNT_ID')
data_set_id = os.getenv('DATA_SET_ID')
name = os.getenv('NAME')
data_source_arn = os.getenv('DATA_SOURCE_ARN')
format_type = os.getenv('FORMAT_TYPE', 'CSV')
start_from_row = int(os.getenv('START_FROM_ROW', 1))
contains_header = os.getenv('CONTAINS_HEADER', 'True') == 'True'
text_qualifier = os.getenv('TEXT_QUALIFIER', 'DOUBLE_QUOTE')
delimiter = os.getenv('DELIMITER', ',')
column_name = os.getenv('COLUMN_NAME')
column_type = os.getenv('COLUMN_TYPE', 'STRING')
import_mode = os.getenv('IMPORT_MODE', 'SPICE')

dataset_params = {
    'AwsAccountId': aws_account_id,
    'DataSetId': data_set_id,
    'Name': name,
    'PhysicalTableMap': {
        'string': {
            'S3Source': {
                'DataSourceArn': data_source_arn,
                'UploadSettings': {
                    'Format': format_type,
                    'StartFromRow': start_from_row,
                    'ContainsHeader': contains_header,
                    'TextQualifier': text_qualifier,
                    'Delimiter': delimiter
                },
                'InputColumns': [
                    {
                        'Name': column_name,
                        'Type': column_type,
                    },
                ]
            }
        }
    },
    'ImportMode': import_mode,
}

# Create the QuickSight data set
response = client.create_data_set(**dataset_params)

print("Data set created successfully.")
print(response)

