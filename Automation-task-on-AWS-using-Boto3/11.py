# Automate AWS Lambda function deployments
# It updates an existing AWS Lambda function's code by uploading a .zip file
#  containing your Lambda code and dependencies.

import boto3

def deploy_lambda_function(function_name, zip_file_path):
    lambda_client = boto3.client('lambda')
    with open(zip_file_path, 'rb') as f:
        lambda_client.update_function_code(FunctionName=function_name, ZipFile=f.read())
    print(f"Lambda function {function_name} updated successfully")

# Example usage:
deploy_lambda_function('my-function', '/path/to/your/lambda.zip')