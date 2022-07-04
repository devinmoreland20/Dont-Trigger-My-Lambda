#!/usr/bin/env python3.9
# Standard Imports
import argparse
import json

# 3rd Party Imports
import boto3

# Arguments
parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True)

args = parser.parse_args()

# Functions
def open_input():
    with open(args.filename) as file_object:
        contents = json.load(file_object)
        return contents['Input'][0]

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

# Main Function - use to call other functions
def main():
    kwargs = open_input()
    translate_text(**kwargs)

if __name__ == "__main__":
    main()









# json_string = """
# {
#     "Input":[
#         {
#         "Text":"I am learning to code in AWS",
#         "SourceLanguageCode":"en",
#         "TargetLanguageCode":"fr",
#         "Required": true
#         }
#     ]
# }
# """

# def main():
#     json_input = json.loads(json_string)
#     indented_format = json.dumps(json_input, indent=2)
#     print(indented_format)

# if __name__=="__main__":
#     main()
