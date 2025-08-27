import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__slug', lookup_expr='exact')
    category_id = django_filters.NumberFilter(field_name='category__id', lookup_expr='exact')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    ordering = django_filters.OrderingFilter(
        fields=(
            ('price', 'price'),
            ('-price', '-price'),
            ('name', 'name'),
            ('-name', '-name'),
            ('created_at', 'created_at'),
            ('-created_at', '-created_at'),
        ),
        field_labels={
            'price': 'Price (low to high)',
            '-price': 'Price (high to low)',
            'name': 'Name (A-Z)',
            '-name': 'Name (Z-A)',
            'created_at': 'Oldest first',
            '-created_at': 'Newest first',
        }
    )

    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'name': ['icontains'],
        }
