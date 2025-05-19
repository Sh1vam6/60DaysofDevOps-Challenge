# Cleanup Old Lambda Function Versions

import boto3

def cleanup_old_lambda_versions(function_name):
    lambda_client = boto3.client('lambda')
    versions = lambda_client.list_versions_by_function(FunctionName=function_name)['Versions']
    for version in versions:
        if version['Version'] not in ['$LATEST']:
            lambda_client.delete_function(FunctionName=function_name, Qualifier=version['Version'])
            print(f"Deleted Lambda version {version['Version']}")

# Example usage:
cleanup_old_lambda_versions('my-lambda-function')