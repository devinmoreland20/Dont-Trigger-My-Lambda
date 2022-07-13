#!/usr/bin/env python3.9
import boto3
import json

lamb = boto3.client('lambda')

FUNCTION_NAME = "Lambda-Create-EC2" # Create-Ec2
S3_BUCKET_NAME = "lambdatesting2022" # Devin-1993
RUN_TIME = "ENTER YOUR RUN TIME" #python3.9
ROLE_NAME =  "ENTER YOUR ROLE NAME" #Lambda-S3-CodeBuild

response = lamb.update_function_code(
    FunctionName=FUNCTION_NAME,
    S3Bucket=S3_BUCKET_NAME,
    S3Key="Lambda_function_1_code.py"
)