from rest_framework import generics,mixins,permissions,authentication
from .models import Products
from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import Http404
from .permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    #authentication class and permission classes
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication]
    
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission] #Ordering matters here

    

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()

    serializer_class = ProductSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Products.objects.all()

    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Products.objects.all()

    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instacnce):
        super().perform_destroy()




#creting all API view in a single view function
@api_view(["GET","POST"])
def product_alt_view(request,pk = None,*args,**kwargs):

    method = request.method

    if method == "GET":

        if pk is not None:
            #detail view
            obj = get_object_or_404(Products,pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)
                
        else:
            #list view
            queryset = Products.objects.all()
            data = ProductSerializer(queryset,many = True).data
            return Response(data)

    if method == "POST":

        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            instance = serializer.save()
            data = serializer.data
            return Response(data,status = 201)
        else:
            return Response({'message':'Error Occured'},status=400)

#alternative to product alt view using rest frmawork class 
class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'     
    
    def get(self,request,*args,**kwargs):
        print(args,kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)