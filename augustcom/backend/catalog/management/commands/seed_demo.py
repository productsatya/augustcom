from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from catalog.models import Category, Product, ProductImage, ProductProperty
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Seed the database with demo categories and products'

    def handle(self, *args, **options):
        self.stdout.write('Seeding demo data...')

        # Create categories
        categories_data = [
            {
                'name': 'Electronics',
                'description': 'Latest electronic gadgets and devices'
            },
            {
                'name': 'Clothing',
                'description': 'Fashionable clothing for all ages'
            },
            {
                'name': 'Books',
                'description': 'Books for all interests and ages'
            },
            {
                'name': 'Home & Garden',
                'description': 'Everything for your home and garden'
            }
        ]

        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create products
        products_data = [
            # Electronics
            {
                'name': 'Smartphone X1',
                'description': 'Latest smartphone with advanced features',
                'price': Decimal('699.99'),
                'category': categories[0],
                'stock_quantity': 50,
                'is_published': True,
                'properties': [
                    {'key': 'Color', 'value': 'Black', 'order': 1},
                    {'key': 'Storage', 'value': '128GB', 'order': 2},
                    {'key': 'RAM', 'value': '8GB', 'order': 3},
                    {'key': 'Screen Size', 'value': '6.1 inches', 'order': 4},
                ]
            },
            {
                'name': 'Laptop Pro',
                'description': 'Professional laptop for work and gaming',
                'price': Decimal('1299.99'),
                'category': categories[0],
                'stock_quantity': 25,
                'is_published': True,
                'properties': [
                    {'key': 'Processor', 'value': 'Intel i7-12700H', 'order': 1},
                    {'key': 'RAM', 'value': '16GB DDR4', 'order': 2},
                    {'key': 'Storage', 'value': '512GB SSD', 'order': 3},
                    {'key': 'Graphics', 'value': 'RTX 3060', 'order': 4},
                ]
            },
            {
                'name': 'Wireless Headphones',
                'description': 'High-quality wireless headphones',
                'price': Decimal('199.99'),
                'category': categories[0],
                'stock_quantity': 100,
                'is_published': True,
                'properties': [
                    {'key': 'Color', 'value': 'White', 'order': 1},
                    {'key': 'Battery Life', 'value': '30 hours', 'order': 2},
                    {'key': 'Connectivity', 'value': 'Bluetooth 5.0', 'order': 3},
                ]
            },
            # Clothing
            {
                'name': 'Classic T-Shirt',
                'description': 'Comfortable cotton t-shirt',
                'price': Decimal('24.99'),
                'category': categories[1],
                'stock_quantity': 200,
                'is_published': True,
                'properties': [
                    {'key': 'Color', 'value': 'Navy Blue', 'order': 1},
                    {'key': 'Size', 'value': 'Medium', 'order': 2},
                    {'key': 'Material', 'value': '100% Cotton', 'order': 3},
                    {'key': 'Fit', 'value': 'Regular', 'order': 4},
                ]
            },
            {
                'name': 'Denim Jeans',
                'description': 'Stylish denim jeans for everyday wear',
                'price': Decimal('59.99'),
                'category': categories[1],
                'stock_quantity': 150,
                'is_published': True,
                'properties': [
                    {'key': 'Color', 'value': 'Dark Blue', 'order': 1},
                    {'key': 'Size', 'value': '32x32', 'order': 2},
                    {'key': 'Material', 'value': 'Denim', 'order': 3},
                    {'key': 'Style', 'value': 'Straight Leg', 'order': 4},
                ]
            },
            {
                'name': 'Winter Jacket',
                'description': 'Warm winter jacket for cold weather',
                'price': Decimal('89.99'),
                'category': categories[1],
                'stock_quantity': 75,
                'is_published': True,
                'properties': [
                    {'key': 'Color', 'value': 'Black', 'order': 1},
                    {'key': 'Size', 'value': 'Large', 'order': 2},
                    {'key': 'Material', 'value': 'Polyester', 'order': 3},
                    {'key': 'Insulation', 'value': 'Synthetic', 'order': 4},
                ]
            },
            # Books
            {
                'name': 'Python Programming Guide',
                'description': 'Complete guide to Python programming',
                'price': Decimal('39.99'),
                'category': categories[2],
                'stock_quantity': 80,
                'is_published': True,
                'properties': [
                    {'key': 'Author', 'value': 'John Smith', 'order': 1},
                    {'key': 'Pages', 'value': '450', 'order': 2},
                    {'key': 'Language', 'value': 'English', 'order': 3},
                    {'key': 'Format', 'value': 'Paperback', 'order': 4},
                ]
            },
            {
                'name': 'Mystery Novel',
                'description': 'Bestselling mystery thriller',
                'price': Decimal('19.99'),
                'category': categories[2],
                'stock_quantity': 120,
                'is_published': True,
                'properties': [
                    {'key': 'Author', 'value': 'Jane Doe', 'order': 1},
                    {'key': 'Pages', 'value': '320', 'order': 2},
                    {'key': 'Genre', 'value': 'Mystery/Thriller', 'order': 3},
                    {'key': 'Format', 'value': 'Hardcover', 'order': 4},
                ]
            },
            {
                'name': 'Cookbook Collection',
                'description': 'Delicious recipes from around the world',
                'price': Decimal('29.99'),
                'category': categories[2],
                'stock_quantity': 60,
                'is_published': True,
                'properties': [
                    {'key': 'Author', 'value': 'Chef Maria', 'order': 1},
                    {'key': 'Pages', 'value': '280', 'order': 2},
                    {'key': 'Cuisine', 'value': 'International', 'order': 3},
                    {'key': 'Format', 'value': 'Hardcover', 'order': 4},
                ]
            },
            # Home & Garden
            {
                'name': 'Garden Tool Set',
                'description': 'Complete set of essential garden tools',
                'price': Decimal('79.99'),
                'category': categories[3],
                'stock_quantity': 40,
                'is_published': True,
                'properties': [
                    {'key': 'Material', 'value': 'Stainless Steel', 'order': 1},
                    {'key': 'Pieces', 'value': '8', 'order': 2},
                    {'key': 'Handle', 'value': 'Wooden', 'order': 3},
                    {'key': 'Warranty', 'value': '2 years', 'order': 4},
                ]
            },
            {
                'name': 'Kitchen Mixer',
                'description': 'Professional kitchen mixer for baking',
                'price': Decimal('149.99'),
                'category': categories[3],
                'stock_quantity': 30,
                'is_published': True,
                'properties': [
                    {'key': 'Color', 'value': 'Red', 'order': 1},
                    {'key': 'Power', 'value': '300W', 'order': 2},
                    {'key': 'Speed Settings', 'value': '5', 'order': 3},
                    {'key': 'Material', 'value': 'Metal', 'order': 4},
                ]
            },
            {
                'name': 'LED Desk Lamp',
                'description': 'Modern LED desk lamp with adjustable brightness',
                'price': Decimal('49.99'),
                'category': categories[3],
                'stock_quantity': 90,
                'is_published': True,
                'properties': [
                    {'key': 'Color', 'value': 'Silver', 'order': 1},
                    {'key': 'Brightness', 'value': 'Adjustable', 'order': 2},
                    {'key': 'Power Source', 'value': 'USB-C', 'order': 3},
                    {'key': 'Material', 'value': 'Aluminum', 'order': 4},
                ]
            }
        ]

        for prod_data in products_data:
            properties_data = prod_data.pop('properties', [])
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    'description': prod_data['description'],
                    'price': prod_data['price'],
                    'category': prod_data['category'],
                    'stock_quantity': prod_data['stock_quantity'],
                    'is_published': prod_data['is_published']
                }
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')
                
                # Create properties for the product
                for prop_data in properties_data:
                    ProductProperty.objects.create(
                        product=product,
                        key=prop_data['key'],
                        value=prop_data['value'],
                        order=prop_data['order']
                    )
                self.stdout.write(f'  - Added {len(properties_data)} properties')

        # Create some unpublished products for testing
        unpublished_products = [
            {
                'name': 'Coming Soon Product',
                'description': 'This product will be available soon',
                'price': Decimal('99.99'),
                'category': categories[0],
                'stock_quantity': 0,
                'is_published': False
            },
            {
                'name': 'Discontinued Item',
                'description': 'This item is no longer available',
                'price': Decimal('29.99'),
                'category': categories[1],
                'stock_quantity': 0,
                'is_published': False
            }
        ]

        for prod_data in unpublished_products:
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    'description': prod_data['description'],
                    'price': prod_data['price'],
                    'category': prod_data['category'],
                    'stock_quantity': prod_data['stock_quantity'],
                    'is_published': prod_data['is_published']
                }
            )
            if created:
                self.stdout.write(f'Created unpublished product: {product.name}')

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully seeded demo data! '
                f'Created {Category.objects.count()} categories, '
                f'{Product.objects.count()} products, and '
                f'{ProductProperty.objects.count()} properties'
            )
        )
