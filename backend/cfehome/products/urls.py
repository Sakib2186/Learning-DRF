from django.urls import path

from .import views

app_name = "products"

urlpatterns = [
    path('<int:pk>/',views.ProductDetailAPIView.as_view()),
    path('',views.ProductListCreateAPIView.as_view()),
]
