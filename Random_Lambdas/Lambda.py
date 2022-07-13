#!/usr/bin/env python3.9
import boto3
import json

lamb = boto3.client('lambda')


response = lamb.create_function(
    FunctionName='Stop-Instances',
    Runtime='python3.9',
    Role = 'Lambda-S3-CodeBuild'
    Handler = "handler.handler_name"
    code={
        "S3Bucket" : "Devin-1993"
    }
)

print(response["FunctionName"])