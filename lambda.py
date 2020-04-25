import boto3

client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    # TODO implement
    # print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    image_name = event['Records'][0]['s3']['object']['key']
    url = "https://$BUCKET_NAME$.$REGION_NAME$.amazonaws.com/" + image_name
    metadata = client.head_object(Bucket=bucket, Key=image_name)['Metadata']
    table = dynamodb.Table('$TABLE_NAME$')
    table.put_item(Item={
        'index': int(metadata['index']),
        'link': url,
        'class': metadata['class'],
        'wnid': metadata['wnid']
    })
    return 'test'