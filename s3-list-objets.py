#!/usr/bin/env python3.9
import boto3
s3=boto3.client('s3')
BUCKET_NAME = "devin02231993"

response = s3.list_objects(Bucket=BUCKET_NAME)["Contents"]#returns just the contents of the bucket

length = len(response)

if length > 0:
    print(length)

for res in response:
    print(res)