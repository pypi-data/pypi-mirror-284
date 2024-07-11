import os

from config.util import install_and_import
from .base_logger import BaseLogger
import logging


class GCPLogger(BaseLogger):
    def __init__(self, log_name: str, project: str, application_credentials: str):
        if not application_credentials:
            raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set")

        # Check if required SDK installed already if not then install it
        install_and_import('google-cloud-logging')

        self.log_name = log_name
        self.project = project
        self.application_credentials_path = application_credentials

        from google.oauth2 import service_account
        # Load credentials from the specified path
        credentials = service_account.Credentials.from_service_account_file(self.application_credentials_path)

        # Initialize the client with the provided credentials
        from google.cloud import logging as gcp_logging
        from google.cloud.logging.handlers import CloudLoggingHandler
        self.client = gcp_logging.Client(project=project, credentials=credentials)
        self.handler = CloudLoggingHandler(self.client, name=log_name)
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self.handler)

    def log(self, level: str, message: str):
        # self.logger.log_text(f"{level.upper()}: {message}")
        if level == "critical":
            self.logger.critical(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        else:
            self.logger.info(message)
