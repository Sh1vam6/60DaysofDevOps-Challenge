# Update Route53 DNS record

import boto3

def update_dns_record(domain_name, ip_address, hosted_zone_id):
    route53 = boto3.client('route53')
    response = route53.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': domain_name,
                        'Type': 'A',
                        'TTL': 300,
                        'ResourceRecords': [{'Value': ip_address}]
                    }
                }
            ]
        }
    )
    print(f"DNS Record Updated: {domain_name} -> {ip_address}")

# Example usage:
update_dns_record('example.com', '192.168.1.1', 'ZXXXXXXXXXXXXX')
