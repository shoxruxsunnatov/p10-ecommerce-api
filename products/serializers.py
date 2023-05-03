from rest_framework import serializers

from products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)


    class Meta:
        model = Product
        fields = ["id", "title", "slug", "category"]
