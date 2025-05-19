# List all IAM users and their attached policies

import boto3

def list_iam_users_and_policies():
    iam = boto3.client('iam')
    users = iam.list_users()['Users']
    for user in users:
        print(f"User: {user['UserName']}")
        policies = iam.list_attached_user_policies(UserName=user['UserName'])['AttachedPolicies']
        for policy in policies:
            print(f"  Policy: {policy['PolicyName']}")

# Example usage:
list_iam_users_and_policies()