# Rotate AWS Access Keys for IAM Users

import boto3

def rotate_iam_keys(username):
    iam = boto3.client('iam')
    old_keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
    for key in old_keys:
        iam.delete_access_key(UserName=username, AccessKeyId=key['AccessKeyId'])
    new_key = iam.create_access_key(UserName=username)
    print(f"Secret Access Key: {new_key['AccessKey']['SecretAccessKey']}")

# Example usage:
rotate_iam_keys('existing-user')