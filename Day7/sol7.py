# Challenge 7: Write a script that triggers an AWS Lambda function using boto3.

import boto3
import json

AWS_REGION = "us-east-1"
LAMBDA_FUNCTION_NAME = "my_lambda_function"

lambda_client = boto3.client("lambda", region_name=AWS_REGION)

def invoke_lambda(payload={}):
    print(f"Triggering Lambda function: {LAMBDA_FUNCTION_NAME}")
    try:
        response = lambda_client.invoke(
            FunctionName=LAMBDA_FUNCTION_NAME,
            InvocationType="RequestResponse",
            Payload=json.dumps(payload)
        )
        response_payload = json.loads(response["Payload"].read().decode())
        print(f"Lambda response: {response_payload}")
    except Exception as e:
        print(f"Failed to invoke Lambda: {e}")

if __name__ == "__main__":
    payload = {"message": "Hello from Python!"}
    invoke_lambda(payload)