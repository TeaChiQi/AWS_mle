
import json
# import sagemaker
import base64
# from sagemaker.serializers import IdentitySerializer
# from sagemaker.predictor import Predictor

import boto3


# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2022-07-14-04-04-28-813" ## TODO: fill in

def lambda_handler(event, context):
    
    
    # Decode the image data
    image = base64.b64decode(event["image_data"]) ## TODO: fill in)

    # Instantiate a Predictor
    runtime = boto3.Session().client('sagemaker-runtime')
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType = 'image/png',Body = image)
    predictions = json.loads(response['Body'].read().decode())
    
    # predictor = Predictor(ENDPOINT) ## TODO: fill in
    
    # For this model the IdentitySerializer needs to be "image/png"
    # predictor.serializer = IdentitySerializer("image/png")

    # Make a prediction:
    # inferences = predictor.predict(image) ## TODO: fill in

    # We return the data back to the Step Function    
    event["inferences"] = predictions
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
