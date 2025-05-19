# Restart Unhealthy EC2 Instances

import boto3

def restart_unhealthy_instances():
    ec2 = boto3.client('ec2')
    statuses = ec2.describe_instance_status(IncludeAllInstances=True)
    for status in statuses['InstanceStatuses']:
        if status['InstanceStatus']['Status'] != 'ok':
            ec2.reboot_instances(InstanceIds=[status['InstanceId']])
            print(f"Rebooted instance: {status['InstanceId']}")


restart_unhealthy_instances()