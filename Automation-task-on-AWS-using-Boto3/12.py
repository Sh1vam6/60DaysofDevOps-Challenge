# Create CloudWatch alarm for EC2

import boto3

def create_cloudwatch_alarm(instance_id, threshold=70.0):
    cloudwatch = boto3.client('cloudwatch')
    cloudwatch.put_metric_alarm(
        AlarmName=f'CPU_Utilization_{instance_id}',
        MetricName='CPUUtilization',
        Namespace='AWS/EC2',
        Statistic='Average',
        Period=300,
        EvaluationPeriods=1,
        Threshold=threshold,
        ComparisonOperator='GreaterThanThreshold',
        AlarmActions=['<SNS_TOPIC_ARN>'],
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}]
    )
    print(f"CloudWatch alarm created for {instance_id}")

# Example usage:
create_cloudwatch_alarm('i-1234567890abcdef0')