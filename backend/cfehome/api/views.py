from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import *

def api_home(request):
    # data = {}
    # print(request.GET) #prints out the url qury params
    # body = request.body #byte string of JSON data
    # try:
    #     data = json.loads(body) #converts to python dictionary
    # except:
    #     pass
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    model_data = Products.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = json.loads(request.body)
        #data['params'] = request.GET
        # data['id'] = model_data.pk
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

        #easier 
        data = model_to_dict(model_data,fields=['id','title','price'])

        #so serialization is
        #converting my model into python dictionary
        #then sending it as Jsonresponse
        #which returns a JSON object
    return JsonResponse(data)