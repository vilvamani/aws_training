import boto3
import json
import argparse
from os import environ
from botocore.exceptions import ClientError

print('Loading function')

AWS_REGION = environ.get("AWS_REGION")

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("--bucket_name", help="Name of the S3 Bucket", type=str, default='aws-training-lambda-bucket')
parser.add_argument("--image_name", help="Name of the key stored in S3 Bucket", type=str, default='car_man.jpg')
parser.add_argument("--table_name", help="DynamoDB table name", type=str, default='gpu_queue')

args = parser.parse_args()

# AWS clients
rekognition_client = boto3.client('rekognition', region_name=AWS_REGION)
dynamodb_client = boto3.client('dynamodb', region_name=AWS_REGION)

def image_processing():
    print('Invoking Rekognition: {}'.format(args))

    try:
        response = rekognition_client.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': args.bucket_name,
                    'Name': args.image_name
                }
            }
        )

        print("Image Label::: {}".format(response))
        return response
    except ClientError as err:
        print("Error::: {}".format(err))
        raise ClientError(err)

def record_label(label):
    try:
        label_name = label['Labels'][0]['Name']
        label_confidence = label['Labels'][0]['Confidence']

        operations = {
            'DELETE': lambda dynamo, x: dynamo.delete_item(**x),
            'POST': lambda dynamo, x: dynamo.put_item(**x),
            'PUT': lambda dynamo, x: dynamo.update_item(**x),
            'GET': lambda dynamo, x: dynamo.get_item(**x),
            'GET_ALL': lambda dynamo, x: dynamo.scan(**x),
            'BATCH_WRITE': lambda dynamo, x: dynamo.batch_write_item(**x),
        }

        message = {
            'TableName': args.table_name,
            'Item':
                {
                    'bucket':
                        {
                            'S': args.bucket_name
                        },
                    'key':
                        {
                            'S': args.image_name
                        },
                    'label_name':
                        {
                            'S': label_name
                        },
                    'confidence':
                        {
                            'S': str(label_confidence)
                        }
                }
            }
        
        operations['POST'](dynamodb_client, message)
        print('{} method successful'.format('POST'))
        return True
    except ClientError as err:
        print("Error::: {}".format(err))
        raise ClientError(err)

if __name__ == "__main__":
    image_label = image_processing()
    
    if image_label is not None:
        record_label(image_label)
