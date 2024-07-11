# Techv Cloud Logger

A logger implementation for AWS, GCP, and local logging.

## Installation

```bash
pip install techv-cloud-logger

## Usage

from logger_factory import LoggerFactory

# Configure logger for local, aws or gcp by passing respective name such as 'local', 'aws' and 'gcp'
LoggerFactory.configure('local')

# Then logs messages
LoggerFactory.log('Critical', 'This is critical log message')
LoggerFactory.log("info", "This is a test log message")
LoggerFactory.log("error", "This is an error message")
