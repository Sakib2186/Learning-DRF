import requests

#an API client has a lot of endpoint
endpoint = "http://localhost:8000/api/products/1/update/"

data ={
    'title':'Hello World my old friend',
    'price':0.00
}

get_response = requests.put(endpoint,json=data) # HTTP GET Request
#print(get_response.text)
print(get_response.json())
