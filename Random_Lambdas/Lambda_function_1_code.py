#!/usr/bin/env python3.9

#Funtion that will create EC2 instances.
import boto3
ec2 = boto3.resource('ec2')
IMAGE_ID = "ami-0cff7528ff583bf9a"
INSTANCE_TYPE = "t2.micro"
KEY_NAME = "Mac"

instance = ec2.create_instances(
    ImageId=IMAGE_ID,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_NAME,
    MaxCount=1,
    MinCount=1
)

print(instance)