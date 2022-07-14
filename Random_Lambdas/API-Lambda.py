#Gotta have boto3 imported here because it is the laugange we are using
#Import datetime allows us to get our time and send it in the message
#!/usr/bin/env python3.9
import boto3
import json
import datetime

#This is where the function starts
def lambda_handler(event, context):
    sqs_client = boto3.client("sqs", region_name="us-east-1")

#you can change your message to what ever you want, so now is going to call
#the date and time then we will make the variable message equal to the date and
#time in hour, minutes,seconds
    now = datetime.datetime.now()
    message = now.strftime("%H:%M:%S")
    
    
    #MessageBody is what is sending to our SQS queue, and it can only be one
    #argument, so we much add the time by putting our varible messages in
    response = sqs_client.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/AWSAccount#/ENTER-YOUR-QUEUE-NAME",
        MessageBody=json.dumps(message)
    )
    #The return is what will be returned on our lambda execution result page
    #showing that it worked correctly. 
    return {
        'statusCode': 200,
        'body': "You just triggered my lambda"
    }
    print("Print sending message to Queue: " + response)