import json

data = {'email': 'shahrukhrao55@gmail.com', 'username': 'shahru', 'name': 'Shahru', 'password': 'Raoobe11'}

# Convert dictionary to JSON string and parse it back to ensure double quotes
json_string = json.dumps(data)
converted_data = json.loads(json_string)

print(json.dumps(converted_data))