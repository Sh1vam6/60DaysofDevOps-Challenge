# Identify and stop underutilized instances

import boto3

def stop_idle_instances():
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            if instance['CpuOptions']['CoreCount'] < 5:
                ec2.stop_instances(InstanceIds=[instance['InstanceId']])
                print(f"Stopped idle instance {instance['InstanceId']}")


stop_idle_instances()