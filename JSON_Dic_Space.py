import requests

response = requests.get('http://api.open-notify.org/astros.json')
jsonformat = response.json()
print("list in JSON format about the web app's response")
print(jsonformat)

print("list the astronauts:")
for data in jsonformat['people']:
    print(data['name'])


