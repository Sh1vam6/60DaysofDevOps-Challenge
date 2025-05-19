# Enable versioning on all S3 buckets

import boto3

def enable_s3_bucket_versioning():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']
    for bucket in buckets:
        bucket_name = bucket['Name']
        s3.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={'Status': 'Enabled'}
        )
        print(f"Enabled versioning on bucket: {bucket_name}")

# Example usage:
enable_s3_bucket_versioning()