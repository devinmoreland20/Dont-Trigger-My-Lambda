#!/usr/bin/env python3.9  #This tells my file I'm using python. Its similar to a bash script
                          #Allows mo also use "./" instead of calling on python
import boto3  #Imports boto3, the SDK for python from AWS

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  #this will make a variable named DynamoDB thats calls the dynamodb resource of boto3

table = dynamodb.create_table(     #Creates our table, this is from the boto3 libary that calls the create_table 
    TableName='LambdaTest2',   #Give your table a name
    KeySchema=[    #Key schema required by dynamodb, 
        {
            'AttributeName': 'Date',  #Name of your part. key
            'KeyType': 'HASH'  #Partition key  is a must
        },
        {
            'AttributeName': 'ID',   #Name of sort key
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ID',    #Reenter your part. key and is its a S|N|B, string, number, boolean
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'Date', #Reenter your sort key and is its a S|N|B, string, number, boolean
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={    #This is how fast your table will upload data
        'ReadCapacityUnits': 1,  #if you have alot of info to upload make it like 10 RCU/WCUI
        'WriteCapacityUnits': 1
    }
)
print(table)
print("Table status:", table.table_status)  #Will print that our table is creating 