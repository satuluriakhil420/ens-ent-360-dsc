import boto3
from datetime import datetime

region = 'us-east-1'
 
client = boto3.client('quicksight',region_name=region)
 
dataset_params = {
    'AwsAccountId': '059643481773',
    'DataSetId': 'ensure-360-dataset',
    'Name': 'ens360-dashboard-pg-dev-01',
    'PhysicalTableMap': {
        'string': {
            'S3Source': {
                'DataSourceArn': 'arn:aws:quicksight:us-east-1:059643481773:datasource/ens-360',  
                'UploadSettings': {
                    'Format': 'CSV',  
                    'StartFromRow': 1,  
                    'ContainsHeader': True,
                    'TextQualifier': 'DOUBLE_QUOTE',  
                    'Delimiter': ','  
                },
                'InputColumns': [
                    {
                        'Name': 'column_name',
                        'Type': 'STRING',  
                    },
                ]
            }
        }
    },
    'ImportMode': 'SPICE',  
}
 
response = client.create_data_set(**dataset_params)
 
print(response)
