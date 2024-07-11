import os

from loggers import AWSLogger, GCPLogger, LocalLogger

# from .aws_logger import AWSLogger
# from .gcp_logger import GCPLogger
# from .local_logger import LocalLogger


class LoggerFactory:
    _environment = None
    _aws_access_key_id = None
    _aws_secret_access_key = None
    _aws_region = 'us-east-1'
    _google_application_credentials = None
    _local_log_file = None

    @staticmethod
    def configure(environment,
                  aws_access_key_id=None,
                  aws_secret_access_key=None,
                  aws_region='us-east-1',
                  retention_days=30,
                  google_application_credentials=None,
                  local_log_file='my_local_log.log'):
        if not environment:
            raise ValueError("Environment must be specified. Choose from 'local', 'aws', or 'gcp'.")

        LoggerFactory._environment = environment.lower()

        os.environ['RETENTION_DAYS'] = str(retention_days)

        if environment == 'aws':
            if not aws_access_key_id or not aws_secret_access_key:
                raise ValueError("AWS credentials must be provided for the AWS environment.")
            LoggerFactory._aws_access_key_id = aws_access_key_id
            LoggerFactory._aws_secret_access_key = aws_secret_access_key
            LoggerFactory._aws_region = aws_region

        elif environment == 'gcp':
            if not google_application_credentials:
                raise ValueError("GCP credentials must be provided for the GCP environment.")
            LoggerFactory._google_application_credentials = google_application_credentials

        elif environment == 'local':
            LoggerFactory._local_log_file = local_log_file
        else:
            raise ValueError("Invalid environment specified. Choose from 'local', 'aws', or 'gcp'.")

    @staticmethod
    def _validate_configuration():
        if LoggerFactory._environment == 'aws':
            if not LoggerFactory._aws_access_key_id or not LoggerFactory._aws_secret_access_key:
                raise ValueError(
                    "AWS credentials are not fully configured. Please set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.")
        elif LoggerFactory._environment == 'gcp':
            if not LoggerFactory._google_application_credentials:
                raise ValueError("GCP credentials are not configured. Please set GOOGLE_APPLICATION_CREDENTIALS.")
        elif LoggerFactory._environment == 'local':
            if not LoggerFactory._local_log_file:
                raise ValueError("Local log file must be provided for the local environment.")

    @staticmethod
    def get_logger():
        LoggerFactory._validate_configuration()

        if LoggerFactory._environment == 'aws':
            os.environ['AWS_ACCESS_KEY_ID'] = LoggerFactory._aws_access_key_id
            os.environ['AWS_SECRET_ACCESS_KEY'] = LoggerFactory._aws_secret_access_key
            os.environ['AWS_DEFAULT_REGION'] = LoggerFactory._aws_region
            return AWSLogger(log_group='my-log-group', log_stream='my-log-stream', aws_region=LoggerFactory._aws_region)

        elif LoggerFactory._environment == 'gcp':
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = LoggerFactory._google_application_credentials
            gcp_project = 'my-gcp-project'
            credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
            return GCPLogger(log_name='my-log', project=gcp_project, credentials_path=credentials_path)

        else:  # local
            return LocalLogger(log_file=LoggerFactory._local_log_file)

    @staticmethod
    def log(level, message):
        if not LoggerFactory._environment:
            raise ValueError("Logger environment is not configured. Please call LoggerFactory.configure() first.")

        logger = LoggerFactory.get_logger()
        logger.log(level, message)
