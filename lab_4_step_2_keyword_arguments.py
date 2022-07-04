#!/usr/bin/env python3.9
import boto3

def translate_text(**kwargs): #you may use other names in place of kwargs
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

# def main():
#     translate_text(Text='I am learning to code in AWS',SourceLanguageCode='en',TargetLanguageCode='fr')

# if __name__=="__main__":
#     main()

kwargs={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()

