import json
import boto3

# Configure the AWS DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('Books')

def lambda_handler(event, context):
    # Get the book ID from the request
    book_id = event['queryStringParameters']['id']
    
    # Retrieve the book from DynamoDB
    response = table.get_item(Key={'book_id': book_id})
    book = response.get('Item', None)
    
    # Prepare the API response
    if book:
        response = {
            'statusCode': 200,
            'body': json.dumps(book)
        }
    else:
        response = {
            'statusCode': 404,
            'body': 'Book not found'
        }
    
    return response
