from rest_framework import serializers
from .models import Category, Product, ProductImage, ProductProperty


class ProductPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProperty
        fields = ['id', 'key', 'value', 'order']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text', 'is_primary']


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'products_count', 'created_at']

    def get_products_count(self, obj):
        return obj.products.filter(is_published=True).count()


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    properties = ProductPropertySerializer(many=True, read_only=True)
    primary_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price', 
            'category', 'stock_quantity', 'images', 'properties', 'primary_image', 
            'created_at'
        ]

    def get_primary_image(self, obj):
        primary_image = obj.images.filter(is_primary=True).first()
        if primary_image:
            return ProductImageSerializer(primary_image).data
        return None


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    properties = ProductPropertySerializer(many=True, read_only=True)
    primary_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'price', 'category', 
            'properties', 'primary_image', 'created_at'
        ]

    def get_primary_image(self, obj):
        primary_image = obj.images.filter(is_primary=True).first()
        if primary_image:
            return ProductImageSerializer(primary_image).data
        return None
