
import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""

    # Get the s3 address from the Step Function event input
    key = event['s3_key'] ## TODO: fill in
    bucket = event['s3_bucket'] ## TODO: fill in

    # Download the data from s3 to /tmp/image.png
    ## TODO: fill in
    s3.download_file(bucket, key, '/tmp/image.png')

    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }

# response
# {
#   "statusCode": 200,
#   "body": {
#     "image_data": "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",
#     "s3_bucket": "sagemaker-studio-741682700515-7evegs5hn7",
#     "s3_key": "test/bicycle_s_000513.png",
#     "inferences": []
#   }
# }
