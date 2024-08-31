import requests
from getpass import getpass

#an API client has a lot of endpoint
auth_endpoint = "http://localhost:8000/auth/"
username = input("What is your username")
password = getpass("What is your password")

auth_reponse = requests.get(auth_endpoint,json={
    "username":username,
    "password":password,
})
#get_response = requests.get(endpoint) # HTTP GET Request
#print(get_response.text)
print(auth_reponse.json())

if auth_reponse.status_code == 200:
    endpoint = "http://localhost:8000/api/products/"
    token = auth_reponse.json()['token']
    headers = {
        # "Authorization":f"Token {token}"
        "Authorization":f"Bearer {token}"
    }
    get_response = requests.get(endpoint,headers=headers)
    print(get_response.json())