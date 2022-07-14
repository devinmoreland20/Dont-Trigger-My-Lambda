#!/usr/bin/env python3.9
import boto3

sqs = boto3.resource('sqs')
queue = sqs.create_queue(QueueName='DevinsLambda')
print(queue.url )
