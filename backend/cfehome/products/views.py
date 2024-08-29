from rest_framework import generics
from .models import Products
from .serializer import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()

    serializer_class = ProductSerializer
