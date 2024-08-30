from django.urls import path

from .import views

app_name = "products"

urlpatterns = [
    path('',views.product_alt_view),
    path('<int:pk>/',views.product_alt_view),
    path('<int:pk>/update/',views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/',views.ProductDeleteAPIView.as_view()),
]
