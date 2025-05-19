# Challenge 6: Automate DNS record updates in AWS Route 53 using Python.

import boto3
import requests

AWS_REGION = "us-east-1"
HOSTED_ZONE_ID = "ZXXXXXXXXXXXXX"
DOMAIN_NAME = "example.com"
RECORD_TYPE = "A"
TTL = 300

route53_client = boto3.client("route53", region_name=AWS_REGION)

def update_dns_record(ip_address):
    print(f"Updating DNS record {DOMAIN_NAME} → {ip_address}")
    change_batch = {
        "Changes": [
            {
                "Action": "UPSERT",
                "ResourceRecordSet": {
                    "Name": DOMAIN_NAME,
                    "Type": RECORD_TYPE,
                    "TTL": TTL,
                    "ResourceRecords": [{"Value": ip_address}]
                }
            }
        ]
    }
    try:
        response = route53_client.change_resource_record_sets(
            HostedZoneId=HOSTED_ZONE_ID,
            ChangeBatch=change_batch
        )
        print(f"DNS record updated! Change ID: {response['ChangeInfo']['Id']}")
    except Exception as e:
        print(f"Failed to update DNS record: {e}")

if __name__ == "__main__":
    ip = requests.get("https://api64.ipify.org?format=text").text
    update_dns_record(ip)