#!/usr/bin/env python3.9
import boto3
import json

sns = boto3.resource('sns', region_name=AWS_REGION)
client = boto3.client('sns')

NAME = "TESTS2234"   #Make sure to put in your Name for your SNS Topic
AWS_REGION = 'us-east-1'   #Choose your region



topic = sns.create_topic(Name=NAME)

print(topic)  #will print the ARN

response = client.subscribe(
    TopicArn=topic.arn,
    Protocol='email',
    Endpoint='devinmoreland20@gmail.com'   #Enter your email here. 
)
print("subscribing to email")