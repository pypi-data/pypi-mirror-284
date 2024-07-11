import os
import boto3

from config.util import install_and_import
from .base_logger import BaseLogger


class AWSLogger(BaseLogger):
    def __init__(self, log_group: str, log_stream: str, aws_region: str):
        self.log_group = log_group
        self.log_stream = log_stream
        self.aws_region = aws_region

        # Check if required SDK installed already if not then install it
        install_and_import('boto3')

        aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.retention_days = os.getenv('RETENTION_DAYS')

        self.client = boto3.client(
            'logs',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=self.aws_region
        )

        self._create_log_group()
        self._create_log_stream()

    def _create_log_group(self):
        try:
            self.client.create_log_group(logGroupName=self.log_group)
        except self.client.exceptions.ResourceAlreadyExistsException:
            pass

    def _create_log_stream(self):
        try:
            self.client.create_log_stream(logGroupName=self.log_group, logStreamName=self.log_stream)
        except self.client.exceptions.ResourceAlreadyExistsException:
            pass

    def log(self, level: str, message: str):
        import time
        timestamp = int(time.time() * 1000)
        log_event = {
            'logGroupName': self.log_group,
            'logStreamName': self.log_stream,
            'logEvents': [
                {
                    'timestamp': timestamp,
                    'message': f"{level.upper()}: {message}"
                },
            ],
        }

        self.client.put_retention_policy(
            logGroupName=self.log_group,
            retentionInDays= int(self.retention_days)
        )

        response = self.client.describe_log_streams(
            logGroupName=self.log_group,
            logStreamNamePrefix=self.log_stream
        )
        sequence_token = response['logStreams'][0].get('uploadSequenceToken')
        if sequence_token:
            log_event['sequenceToken'] = sequence_token
        self.client.put_log_events(**log_event)
        print(log_event)
