# Challenge 3: Create a script that starts or stops all EC2 instances in a specific AWS region.

import boto3

AWS_REGION = "us-east-1"
ec2_client = boto3.client("ec2", region_name=AWS_REGION)

def get_all_instances():
    response = ec2_client.describe_instances()
    instances = [
        instance["InstanceId"]
        for reservation in response["Reservations"]
        for instance in reservation["Instances"]
    ]
    return instances

def manage_instances(action):
    instances = get_all_instances()
    if not instances:
        print("No EC2 instances found.")
        return
    if action == "start":
        ec2_client.start_instances(InstanceIds=instances)
        print(f"Started instances: {instances}")
    elif action == "stop":
        ec2_client.stop_instances(InstanceIds=instances)
        print(f"Stopped instances: {instances}")
    else:
        print("Invalid action! Use 'start' or 'stop'.")

if __name__ == "__main__":
    action = input("Enter action (start/stop): ").strip().lower()
    manage_instances(action)