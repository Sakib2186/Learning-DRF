from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

urlpatterns = [
    path('auth/',obtain_auth_token),
    path('',views.api_home,name='api_home'),
]
