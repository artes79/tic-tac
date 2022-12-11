import json

HEADERS = {
    'Access-Control-Allow-Origin': 'https://tictac.t79.app',
    'Access-Control-Allow-Headers': '*'
}

def lambda_handler(event, context):
    
    data = { 'player': 'X', 'board': '0 0 0 0 0 0 0 0 0' }
    
    return {
        'statusCode': 200,
        'headers': HEADERS,
        'body': json.dumps(data)
    }