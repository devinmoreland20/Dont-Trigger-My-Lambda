#!/usr/bin/env python3.9
import boto3
s3=boto3.client('s3')
BUCKET_NAME = "devin02231993"

objects = s3.list_objects(   #listing out the contents of of the bucket and the key
    Bucket=BUCKET_NAME
)["Contents"]

for object in objects:
    key = (object["Key"])  #This chooses Key in the contents of the bucket and we are calling it a variable to delete all objets with key
    response = s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=key
    )
    print(response)