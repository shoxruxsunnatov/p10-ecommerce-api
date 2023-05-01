from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductListSerializer, ProductSerializer, ProductDetailSerializer, CategorySerializer
from products.models import Product, Category


@api_view(['GET'])
def get_products_list(req):
    
    products = Product.objects.all().order_by('-id')
    serializer = ProductListSerializer(products, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_product_detail(req, pk):
    
    product = get_object_or_404(Product, id=pk)
    serializer = ProductDetailSerializer(product)

    return Response(serializer.data)


@api_view(['GET'])
def get_products_list_by_category(req, pk):

    category = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=category)
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def categories(req):

    category = Category.objects.order_by('position')
    serializer_class = CategorySerializer

    serializer = serializer_class(category, many=True)

    if req.method == 'POST':
        serializer = serializer_class(data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return Response(serializer.data)

