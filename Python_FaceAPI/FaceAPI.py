import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("image_url", help="image you want to identify faces")
args = parser.parse_args()

print(args.image_url)

data = {'url' : args.image_url}
headers = {'Content-Type' : 'application/json', 'Ocp-Apim-Subscription-Key' : ''}

r = requests.post('https://westus.api.cognitive.microsoft.com/face/v1.0/detect', json=data, headers=headers)

json_response = r.json()

print("There are " + str(len(json_response)) + " faces on this image")

#https://st2.depositphotos.com/1000904/11984/i/950/depositphotos_119849996-stock-photo-young-happy-family-having-fun.jpg