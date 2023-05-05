from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.serializers import ProductListSerializer



class ProductListCreateView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        prodcuts = Product.objects.order_by("-id")
        serializer = ProductListSerializer(prodcuts, many=True)
        return Response(serializer.data)


    def post(self, request):

        serializer = ProductListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)


    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        serializer = ProductListSerializer(self.get_object(pk))
        return Response(serializer.data)


    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        serializer = ProductListSerializer(instance=self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        category = self.get_object(pk)
        category.delete()
        return Response("Deleted.", status=status.HTTP_204_NO_CONTENT)





