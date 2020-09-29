#!/usr/bin/env python

import boto3
import json
import logging
import os
import random 
import string
from uuid import uuid4
from botocore.exceptions import ClientError

from aws_xray_sdk.core import xray_recorder

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.info('Loading function')

# Environment variables (set by SAM template)
JOB_DEFINITION = os.environ['JOB_DEFINITION']
JOB_QUEUE = os.environ['JOB_QUEUE']
IMAGES_TABLE = os.environ['IMAGES_TABLE']

# AWS clients
batch_client = boto3.client('batch')

@xray_recorder.capture('## aws_batch_lambda_handler')
def lambda_handler(event,context):
    logger.debug('Received event: {}'.format(event))

    IMAGES_BUCKET = event['Records'][0]['s3']['bucket']['name']
    IMAGES_NAME = event['Records'][0]['s3']['object']['key']

    try:
        # Submit the job to AWS Batch
        job = batch_client.submit_job(
            jobDefinition= JOB_DEFINITION,
            jobName= 'job_' + str(uuid4()), # Create unique name for the job
            jobQueue= JOB_QUEUE,
            parameters= {
                'bucketName': IMAGES_BUCKET,
                'imageName': IMAGES_NAME,
                'dynamoTable': IMAGES_TABLE
            }
        )

        logger.debug("Started Job: {}".format(job))
    except ClientError as e:
        logger.error(e)
        return None
