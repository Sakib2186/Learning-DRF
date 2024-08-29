from django.urls import path

from .import views

app_name = "products"

urlpatterns = [
    path('<int:pk>/',views.product_alt_view),
    path('',views.product_alt_view),
]
