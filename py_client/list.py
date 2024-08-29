import requests

#an API client has a lot of endpoint
endpoint = "http://localhost:8000/api/products/1"

get_response = requests.get(endpoint) # HTTP GET Request
#print(get_response.text)
print(get_response.json())
