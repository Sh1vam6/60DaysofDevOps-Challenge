# Automatically tag EC2 resources

import boto3

def tag_ec2_instance(instance_id, tags):
    ec2 = boto3.client('ec2')
    ec2.create_tags(Resources=[instance_id], Tags=tags)
    print(f"Tagged instance {instance_id} with {tags}")

# Example usage:
tag_ec2_instance('i-1234567890abcdef0', [{'Key': 'Owner', 'Value': 'DevOps'}])