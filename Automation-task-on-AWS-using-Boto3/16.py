# Check for open security groups

import boto3

def check_open_security_groups():
    ec2 = boto3.client('ec2')
    groups = ec2.describe_security_groups()['SecurityGroups']
    for group in groups:
        for permission in group['IpPermissions']:
            for ip_range in permission.get('IpRanges', []):
                if ip_range['CidrIp'] == '0.0.0.0/0':
                    print(f"Security Group {group['GroupId']} has open access!")

check_open_security_groups()