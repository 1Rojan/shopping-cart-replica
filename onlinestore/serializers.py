from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ['id','title', 'slug', 'description', 'products']

    def create(self, validated_data):
        albums_data = validated_data.pop('products')
        category = Category.objects.create(**validated_data)
        for album_data in albums_data:
            Product.objects.create(artist=category, **album_data)
        return category



