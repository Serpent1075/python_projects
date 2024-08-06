from melon import Melon
import json

def lambda_handler(event, context):
    return {
        'statusCode':200,
        'body':json.dumps(Melon().page_parse())
    }