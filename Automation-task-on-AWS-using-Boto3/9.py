# S3 Bucket Backup and Synchronization

import boto3

def sync_s3_buckets(source_bucket, destination_bucket):
    s3 = boto3.resource('s3')
    for obj in s3.Bucket(source_bucket).objects.all():
        copy_source = {'Bucket': source_bucket, 'Key': obj.key}
        s3.Object(destination_bucket, obj.key).copy(copy_source)
        print(f"Data synced from {source_bucket} to {destination_bucket}")

# Example usage:
sync_s3_buckets('source-bucket-name', 'destination-bucket-name')