from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [

    path('api/',views.api_home,name='api_home'),
]
