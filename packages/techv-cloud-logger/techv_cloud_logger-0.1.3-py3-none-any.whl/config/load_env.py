import boto3
import os
import json


def get_secret(secret_name, region_name):
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        # Retrieve the secret
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response['SecretString']
        return json.loads(secret)
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        return None


def load_secrets(aws_config):
    region_name = aws_config.get('region', 'us-west-2')
    secret_name = aws_config.get('secrets_name')  # Set this config variable to your secret's name

    if not secret_name:
        print("AWS_SECRETS_NAME environment variable not set.")
        return

    secrets = get_secret(secret_name, region_name)
    if secrets:
        os.environ['AWS_ACCESS_KEY_ID'] = secrets.get('AWS_ACCESS_KEY_ID')
        os.environ['AWS_SECRET_ACCESS_KEY'] = secrets.get('AWS_SECRET_ACCESS_KEY')