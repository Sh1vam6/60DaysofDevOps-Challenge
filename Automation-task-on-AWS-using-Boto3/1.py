# Start, Stop, Restart & Terminate EC2 instance

import boto3 
import sys 

def manage_ec2_instance(action, instance_id):

    ec2 = boto3.client('ec2')

    actions = {
        'start': 'start_instances',
        'stop': 'stop_instances',
        'restart': 'reboot_instances',
        'terminate': 'terminate_instances'
    }

    if action not in actions:
        print(f"Invalid action: {action}. Use 'start', 'stop', 'restart', or 'terminate'.")
        return
    
    try: 
        response = getattr(ec2, actions[action])(InstanceIds=[instance_id])
        print(f"{action.capitalize()} action initiated for instance {instance_id}.")
        print(response)

    except Exception as e:
        print(f"Error: {e}")

    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <action> <instance_id>")
        sys.exit(1)
    action = sys.argv[1].lower()
    instance_id = sys.argv[2]
    manage_ec2_instance(action, instance_id)

    # Example usage:
    # python 1.py stop i-072ee71641fabef6e