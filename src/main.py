import json
import boto3

from enum import Enum
from botocore.exceptions import ClientError

BUCKET_NAME = 'svcomp-tracks'
YEAR_KEY = 'year'
CATEGORY_KEY = 'category'
POSITION_KEY = 'position'

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=BUCKET_NAME, Key='2023')
    categories_json = json.loads(response['Body'].read().decode('utf-8'))
    
    # Check we have all our values
    if not all(key in event for key in [YEAR_KEY, CATEGORY_KEY, POSITION_KEY]):
        return {
        'statusCode': 400,
        'body': f'Bad request. Missing required parameters {json.dumps(event)}'
    }
    
    year = event['year']
    category = event['category']
    position_number = event['position']
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=str(year))
    except ClientError:
        return {
            'statusCode': 404,
            'body': 'A year with that specific value was not found'
        }
    categories_json = json.loads(response['Body'].read().decode('utf-8'))
    categories = categories_json['categories']
    
    try:
        position = Position(position_number)
    except ValueError:
        return {
            'statusCode': 400,
            'body': 'Bad request. Position must be 1, 2, or 3'
        }
        
    if category not in categories:
         return {
            'statusCode': 400,
            'body': f'Bad request. Category: {category} was not present in this year'
        }
    
    # Validation succeeded, construct formatting
    return  generate_format_json(year, category, position)
    
def generate_format_json(year, category, position):
    format = {}
    format['schemaVersion'] = 1
    format['message'] = f'SVCOMP\'{year % 100}-{category}'
    format['color'] = '5a5a5a'
    format['label'] = ''
    format['labelColor'] = position.colour
    return format
    

class Position(Enum):
    FIRST = 1, "FFD700"
    SECOND = 2, "C0C0C0"
    THIRD = 3, "CD7F32"

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: int, colour: str = None):
        self._colour = colour

    def __str__(self):
        return self.value

    # this makes sure that the description is read-only
    @property
    def colour(self):
        return self._colour