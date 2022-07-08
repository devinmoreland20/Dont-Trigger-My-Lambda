#!/usr/bin/env python3.9
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Federation')

GET_RAW_PATH = "/planet/query"
GET_RAW_PATH_SCAN = "/planet"
GET_PATH_DELETE = "/delete"

def lambda_handler(event, context): 
    print(event)
       
       
    if event['path'] == GET_RAW_PATH_SCAN:
        tablename=event['queryStringParameters']['tablename']
        table = dynamodb.Table(tablename)
        body = table.scan()
        scan_items = body['Items']
        return {'body': json.dumps(scan_items)}
    
    elif event['path'] == GET_RAW_PATH:
        planetname=event['queryStringParameters']['planetname']
        table = dynamodb.Table('Federation')
        response = table.query(
            KeyConditionExpression=Key('PlanetName').eq(planetname) 
            )
        items = response['Items']
        return {'body': json.dumps(items)}
    
    elif event['path'] == GET_PATH_DELETE:
        planetname=event['queryStringParameters']['planetname']
        table = dynamodb.Table('Federation')
        response = table.query(
            KeyConditionExpression=Key('PlanetName').eq(planetname) 
        )
        items = response['Items'][0]
        print(items)
        responses = table.delete_item(
            Key=items
            )
        list_items=str(responses)  
        print("Item delete from table: " + planetname)
        return {'body': json.dumps(list_items)}
        
    else:
        print("Table/Item not found") #######