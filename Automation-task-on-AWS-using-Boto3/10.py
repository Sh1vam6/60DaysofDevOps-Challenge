# DynamoDB Data Export to S3

import boto3

def export_dynamodb_to_s3(table_name, bucket_name, file_name):
    dynamodb = boto3.resource('dynamodb')
    s3 = boto3.client('s3')
    table = dynamodb.Table(table_name)
    data = table.scan()['Items']
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=str(data))
    print(f"Data exported to s3://{bucket_name}/{file_name}")

# Example usage:
export_dynamodb_to_s3('my-table', 'my-bucket', 'backup.json')