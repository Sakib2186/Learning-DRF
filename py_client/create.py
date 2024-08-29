import requests

#an API client has a lot of endpoint
endpoint = "http://localhost:8000/api/products/"

data = {
    'title':"This field is done"
}
get_response = requests.post(endpoint,json=data) # HTTP GET Request
#print(get_response.text)
print(get_response.json())
