# Delete old S3 objects beyond a retention period

import boto3
from datetime import datetime, timezone

def delete_old_s3_objects(bucket_name, days=30):
    s3 = boto3.client('s3')
    objects = s3.list_objects_v2(Bucket=bucket_name)
    now = datetime.now(timezone.utc)
    for obj in objects.get('Contents', []):
        age = (now - obj['LastModified']).days
        if age > days:
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
            print(f"Deleted {obj['Key']} from {bucket_name}")


delete_old_s3_objects('my-bucket', 30)