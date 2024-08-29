import requests

#an API client has a lot of endpoint
endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint,params={'abc':123}#query params like /api/?abc=123
    ,json={
    'content':'Hello World'
}) # HTTP GET Request
#print(get_response.text)
print(get_response.json())

#sending as raw data which will be sent as form data
#get_response = requests.get(endpoint,data={
#    'query':'Hello World'
#}) # HTTP GET Request
#print(get_response.text)

#converting the data from JSON to python dic
#print(get_response.json())

#normal HTTP request returns HTML, design for humans to look at
#REST API HTTP REsuqest returns JSON, not design for humans to look at