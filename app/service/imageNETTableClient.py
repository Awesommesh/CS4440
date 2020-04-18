import boto3
import json
import logging
from collections import defaultdict
import argparse

# create a DynamoDB client using boto3. The boto3 library will automatically
# use the credentials associated with our ECS task role to communicate with
# DynamoDB, so no credentials need to be stored/managed at all by our code!
client = boto3.client('dynamodb')

def getImageNETJson(items):
    # loop through the returned image and add their attributes to a new dict
    # that matches the JSON response structure expected by the frontend.
    ImageNETList = defaultdict(list)

    for item in items:
        image = {}

        image["wnid"] = item["wnid"]["S"]
        image["class"] = item["class"]["S"]
        image["link"] = item["link"]["S"]
        image["index"] = item["index"]["N"]

        ImageNETList["images"].append(image)

    return ImageNETList

def getAllImages():
    # Retrieve all Images from DynamoDB using the DynamoDB scan operation.
    # Note: The scan API can be expensive in terms of latency when a DynamoDB
    # table contains a high number of records and filters are applied to the
    # operation that require a large amount of data to be scanned in the table
    # before a response is returned by DynamoDB. For high-volume tables that
    # receive many requests, it is common to store the result of frequent/common
    # scan operations in an in-memory cache. DynamoDB Accelerator (DAX) or
    # use of ElastiCache can provide these benefits.
    response = client.scan(
        TableName='ImageNETTable'
    )

    logging.info(response["Items"])

    # loop through the returned images and add their attributes to a new dict
    # that matches the JSON response structure expected by the frontend.
    imageNETList = getImageNETJson(response["Items"])

    return json.dumps(imageNETList)

def queryImageNETItems(filter, value):
    # Use the DynamoDB API Query to retrieve images from the table that are
    # equal to the selected filter values.
    response = client.query(
        TableName='ImageNETTable',
        IndexName=filter+'Index',
        KeyConditions={
            filter: {
                'AttributeValueList': [
                    {
                        'S': value
                    }
                ],
                'ComparisonOperator': "EQ"
            }
        }
    )

    # loop through the returned images and add their attributes to a new dict
    # that matches the JSON response structure expected by the frontend.
    imageNETList = getImageNETJson(response["Items"])

    # convert the create list of dicts in to JSON
    return json.dumps(imageNETList)

def queryImageNET(queryParam):

    logging.info(json.dumps(queryParam))

    filter = queryParam['filter']
    value = queryParam['value']

    return queryImageNETItems(filter, value)

# So we can test from the command line
# So we can test from the command line
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filter')
    parser.add_argument('-v', '--value')
    args = parser.parse_args()

    filter = args.filter
    value = args.value

    if args.filter and args.value:
        print ('filter is ', args.filter)
        print ('value is ', args.value)

        print ("Getting filtered values")
        items = queryImageNETItems(args.filter, args.value)
    else:
        print ("Getting all values")
        items = getAllImages()

    print (items)