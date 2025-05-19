# Challenge 5: Implement a log monitoring system that scans EC2 instances' /var/log for error messages 
# and sends alerts via email (AWS SES) and Slack.


# pip install boto3 requests paramiko

import boto3
import paramiko
import requests
import time

AWS_REGION = "us-east-1"
EC2_TAG = "log-monitor"
SES_SENDER = "alerts@example.com"
SES_RECIPIENT = "admin@example.com"
SUBJECT = "EC2 Log Monitoring Alert"
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/your/slack/webhook"

ec2_client = boto3.client("ec2", region_name=AWS_REGION)
ses_client = boto3.client("ses", region_name=AWS_REGION)

def get_ec2_instances():
    response = ec2_client.describe_instances(
        Filters=[
            {"Name": "tag:Name", "Values": [EC2_TAG]},
            {"Name": "instance-state-name", "Values": ["running"]}
        ]
    )
    instances = [
        (instance["InstanceId"], instance["PublicIpAddress"])
        for reservation in response["Reservations"]
        for instance in reservation["Instances"]
        if "PublicIpAddress" in instance
    ]
    return instances

def check_logs(instance_ip, key_file, username="ubuntu"):
    errors = []
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        private_key = paramiko.RSAKey(filename=key_file)
        ssh.connect(hostname=instance_ip, username=username, pkey=private_key)
        cmd = "grep -i 'error' /var/log/*.log | tail -n 10"
        stdin, stdout, stderr = ssh.exec_command(cmd)
        output = stdout.read().decode().strip()
        if output:
            errors.append((instance_ip, output))
        ssh.close()
    except Exception as e:
        print(f"Failed to connect to {instance_ip}: {e}")
    return errors

def send_email(subject, body):
    try:
        response = ses_client.send_email(
            Source=SES_SENDER,
            Destination={"ToAddresses": [SES_RECIPIENT]},
            Message={
                "Subject": {"Data": subject},
                "Body": {"Text": {"Data": body}}
            }
        )
        print("Email alert sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def send_slack_alert(message):
    payload = {"text": message}
    try:
        requests.post(SLACK_WEBHOOK_URL, json=payload)
        print("Slack alert sent!")
    except Exception as e:
        print(f"Failed to send Slack message: {e}")

def monitor_ec2_logs():
    print("Checking EC2 logs for errors...")
    instances = get_ec2_instances()
    if not instances:
        print("No instances found with the specified tag.")
        return
    key_file = "your-key.pem"
    all_errors = []
    for instance_id, instance_ip in instances:
        errors = check_logs(instance_ip, key_file)
        if errors:
            all_errors.extend(errors)
    if all_errors:
        message_body = "\n\n".join([f"{ip}\n{log}" for ip, log in all_errors])
        print(f"Errors Found:\n{message_body}")
        send_email(SUBJECT, message_body)
        send_slack_alert(message_body)
    else:
        print("No errors found in logs.")

if __name__ == "__main__":
    monitor_ec2_logs()