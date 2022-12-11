import json
import boto3

HEADERS = {
    'Access-Control-Allow-Origin': 'https://tictac.t79.app',
    'Access-Control-Allow-Headers': '*'
}

DATA_STRUCTUR_IN = {
    'player': '',
    'move': {'x': '', 'y': ''}
}

DATA_STRUCTURE_OUT = {
    'next-player': '',
    'board': {
        'A': {'0': '', '1': '', '2': ''},
        'B': {'0': '', '1': '', '2': ''},
        'C': {'0': '', '1': '', '2': ''}
    }
}

bucketName = "tictac.t79.app"

def lambda_handler(event, context):
    
    data = { 'player': 'X', 'board': '0 0 0 0 0 0 0 0 0' }
    
    s3Client = boto3.client('s3')
    
    try:
        fileRes = s3Client.get_object(Bucket=bucketName, Key='tictac.json')
        file = json.loads(fileRes['Body'].read().decode('utf-8'))
        print(file)
        
        file['Test'] = "Dette er en test"
        
        s3Client.put_object(Bucket=bucketName, Key='tictac.json', Body=bytes(json.dumps(file).encode('UTF-8')))
        
    except Exception as e:
        raise e
    
    return {
        'statusCode': 200,
        'headers': HEADERS,
        'body': json.dumps(file)
    }
