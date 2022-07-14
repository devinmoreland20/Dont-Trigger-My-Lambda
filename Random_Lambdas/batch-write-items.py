
#!/usr/bin/env python3.9

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
#Variables that we are using to put items into our tables.
Planets = [
    {'PlanetName': "Earth", "Quadrant": "Alpha"},
    {'PlanetName': "Vulcan", "Quadrant": "Alpha"},
    {'PlanetName': "Cardassia", "Quadrant": "Alpha"},
    {'PlanetName': "Qo'noS", "Quadrant": "Beta"},
    {'PlanetName': "Talos IV", "Quadrant": "Alpha"},
    {'PlanetName': "Risa", "Quadrant": "Alpha"},
    {'PlanetName': "Bajor", "Quadrant": "Alpha"},
    {'PlanetName': "Saturn", "Quadrant": "Alpha"},
    {'PlanetName': "Ferenginar", "Quadrant": "Alpha"},
    {'PlanetName': "Talaxia", "Quadrant": "Delta"},
]

table = dynamodb.Table("Federation")  #Creates a variable that will call our table name.
with table.batch_writer() as batch:   #Batch writer statement that will upload a batch of items to dynamoDB. 
    for planet in Planets:
        batch.put_item(    
        Item=planet
        )