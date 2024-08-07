#!/bin/bash

# Fetch AWS Account ID dynamically using AWS CLI
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# General AWS Region
export AWS_REGION="us-east-1"

# Export AWS Account ID
export AWS_ACCOUNT_ID

# AWS Glue Environment Variables
export GLUE_CRAWLER_NAME="ens360-dashboard-crawler-dev-01"
export GLUE_ROLE="arn:aws:iam::$AWS_ACCOUNT_ID:role/sentrics"
export GLUE_DATABASE_NAME="ens360-dashboard-db-dev-01"
export GLUE_TABLE_PREFIX="crawler_output"
export GLUE_S3_PATH="s3://dashboard-sl-non-prod-345/"

# AWS Glue Job Environment Variables
export GLUE_JOB_NAME="ens360-job"
export GLUE_JOB_ROLE="arn:aws:iam::$AWS_ACCOUNT_ID:role/glue-job-role"
export GLUE_JOB_SCRIPT_PATH="s3://path-to-glue-scripts/job-script.py"
export GLUE_JOB_MAX_CAPACITY=2.0

# AWS Glue Database Environment Variables
export GLUE_DATABASE_DESCRIPTION="Provides information regarding ensure 360"

# QuickSight User Registration Environment Variables
export QS_USER_IDENTITY_TYPE="QUICKSIGHT"
export QS_USER_EMAIL="test123@gmail.com"
export QS_USER_ROLE="ADMIN"
export QS_USER_ACCOUNT_ID="$AWS_ACCOUNT_ID"
export QS_USER_NAMESPACE="default"
export QS_USER_NAME="sentrics"
export QS_USER_TAG_KEY="Environment"
export QS_USER_TAG_VALUE="Dev"

# QuickSight Data Source Environment Variables
export QS_DATA_SOURCE_ID="ensure-360"
export QS_DATA_SOURCE_NAME="ens360-dashboard-pg-dev"
export QS_DATA_SOURCE_ARN="arn:aws:quicksight:$AWS_REGION:$AWS_ACCOUNT_ID:datasource/ens-360"
export QS_DATA_SOURCE_BUCKET="aws-glue-assets-$AWS_ACCOUNT_ID-$AWS_REGION"
export QS_DATA_SOURCE_KEY="manifest.json"
export QS_DATA_SOURCE_ROLE_ARN="arn:aws:iam::$AWS_ACCOUNT_ID:role/sentrics"

# QuickSight Dataset Environment Variables
export QS_DATASET_ID="ensure-360-dataset"
export QS_DATASET_NAME="ens360-dashboard-pg-dev-01"
export QS_FORMAT_TYPE="CSV"
export QS_START_FROM_ROW=1
export QS_CONTAINS_HEADER="True"
export QS_TEXT_QUALIFIER="DOUBLE_QUOTE"
export QS_DELIMITER=","
export QS_COLUMN_NAME="column_name"
export QS_COLUMN_TYPE="STRING"
export QS_IMPORT_MODE="SPICE"

# Glue Job Permissions Environment Variables
export GLUE_JOB_PERMISSIONS_ROLE="arn:aws:iam::$AWS_ACCOUNT_ID:role/glue-job-permissions"

echo "AWS environment variables set."
