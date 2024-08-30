import requests

product_id = input("Enter product id")

try:
    product_id = int(product_id)
except:
    product_id = f'{product_id} not a valid ID'
if product_id:
    #an API client has a lot of endpoint
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint) # HTTP GET Request
    #print(get_response.text)
    print(get_response.json())
