# Create RDS snapshot

import boto3

def create_rds_snapshot(db_instance_identifier, snapshot_id):
    rds = boto3.client('rds')
    rds.create_db_snapshot(DBSnapshotIdentifier=snapshot_id, DBInstanceIdentifier=db_instance_identifier)
    print(f"Snapshot {snapshot_id} created for {db_instance_identifier}")

# Example usage:
create_rds_snapshot('my-db-instance', 'my-db-snapshot')