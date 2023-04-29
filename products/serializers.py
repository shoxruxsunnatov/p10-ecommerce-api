from rest_framework import serializers

from products.models import Product, Category


class ProductListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug']


class ProductDetailSerializer(ProductSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'slug', 'category']
