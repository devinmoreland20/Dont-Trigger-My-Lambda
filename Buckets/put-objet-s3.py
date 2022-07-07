#!/usr/bin/env python3.9
import os
import glob
import boto3
s3 = boto3.client('s3')
cwd = os.getcwd()
BUCKET_NAME = "devin02231993"
#FILE_NAME = "text.txt"
#KEY = file.split("/")[-1]

cwd=cwd+"/"  #use / if ur in ur cwd... you can use pwd to find ur cwd on mac. cwd is from python
files = glob.glob(cwd+"*.txt")  #allows us to upload any files with this as the ending

for file in files:
    response = s3.upload_file(
        Bucket=BUCKET_NAME,
        Key=file.split("/")[-1], 
        Filename=file
)