from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Category, Product
from .serializers import (
    CategorySerializer, ProductSerializer, ProductListSerializer
)
from .filters import ProductFilter


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    @action(detail=True, methods=['get'])
    def products(self, request, slug=None):
        """Get products for a specific category"""
        category = self.get_object()
        products = Product.objects.filter(
            category=category, 
            is_published=True
        ).select_related('category').prefetch_related('images')
        
        # Apply filters
        filterset = ProductFilter(request.GET, queryset=products)
        filtered_products = filterset.qs
        
        # Apply pagination
        page = self.paginate_queryset(filtered_products)
        if page is not None:
            serializer = ProductListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = ProductListSerializer(filtered_products, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_published=True).select_related('category').prefetch_related('images')
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['price', 'name', 'created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer

    @action(detail=False, methods=['get'])
    def health(self, request):
        """Health check endpoint"""
        return Response({
            'status': 'healthy',
            'total_products': self.get_queryset().count(),
            'total_categories': Category.objects.count()
        }, status=status.HTTP_200_OK)
