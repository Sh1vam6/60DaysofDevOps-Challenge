# Delete outdated snapshots

import boto3
from datetime import datetime, timezone

def cleanup_snapshots(retention_days=30):
    ec2 = boto3.client('ec2')
    now = datetime.now(timezone.utc)
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    for snapshot in snapshots:
        age = (now - snapshot['StartTime']).days
        if age > retention_days:
            ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
            print(f"Deleted snapshot {snapshot['SnapshotId']}")

cleanup_snapshots()