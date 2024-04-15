# serializers.py
from rest_framework import serializers
from .models import Product, Category, Post

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'description', 'image', 'date_added']
