from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from decimal import Decimal
from .models import Category, Product, ProductImage, ProductProperty


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Electronics",
            description="Test electronics category"
        )

    def test_slug_auto_generation(self):
        """Test that slug is automatically generated from name"""
        self.assertEqual(self.category.slug, "test-electronics")

    def test_slug_uniqueness(self):
        """Test that slug is unique"""
        category2 = Category.objects.create(
            name="Test Electronics 2",
            description="Another test category"
        )
        self.assertNotEqual(self.category.slug, category2.slug)

    def test_string_representation(self):
        """Test string representation of category"""
        self.assertEqual(str(self.category), "Test Electronics")


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            description="Test category description"
        )
        self.product = Product.objects.create(
            name="Test Product",
            description="Test product description",
            price=Decimal("99.99"),
            category=self.category,
            is_published=True,
            stock_quantity=10
        )

    def test_slug_auto_generation(self):
        """Test that slug is automatically generated from name"""
        self.assertEqual(self.product.slug, "test-product")

    def test_slug_uniqueness(self):
        """Test that slug is unique"""
        product2 = Product.objects.create(
            name="Test Product 2",
            description="Another test product",
            price=Decimal("149.99"),
            category=self.category,
            is_published=True,
            stock_quantity=5
        )
        self.assertNotEqual(self.product.slug, product2.slug)

    def test_string_representation(self):
        """Test string representation of product"""
        self.assertEqual(str(self.product), "Test Product")


class ProductPropertyModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            description="Test category description"
        )
        self.product = Product.objects.create(
            name="Test Product",
            description="Test product description",
            price=Decimal("99.99"),
            category=self.category,
            is_published=True,
            stock_quantity=10
        )

    def test_product_property_creation(self):
        """Test creating product properties"""
        property1 = ProductProperty.objects.create(
            product=self.product,
            key="Color",
            value="Red",
            order=1
        )
        property2 = ProductProperty.objects.create(
            product=self.product,
            key="Size",
            value="Large",
            order=2
        )
        
        self.assertEqual(property1.key, "Color")
        self.assertEqual(property1.value, "Red")
        self.assertEqual(property2.key, "Size")
        self.assertEqual(property2.value, "Large")

    def test_product_property_ordering(self):
        """Test that properties are ordered correctly"""
        ProductProperty.objects.create(
            product=self.product,
            key="Third",
            value="Value3",
            order=3
        )
        ProductProperty.objects.create(
            product=self.product,
            key="First",
            value="Value1",
            order=1
        )
        ProductProperty.objects.create(
            product=self.product,
            key="Second",
            value="Value2",
            order=2
        )
        
        properties = list(self.product.properties.all())
        self.assertEqual(properties[0].key, "First")
        self.assertEqual(properties[1].key, "Second")
        self.assertEqual(properties[2].key, "Third")

    def test_string_representation(self):
        """Test string representation of product property"""
        property_obj = ProductProperty.objects.create(
            product=self.product,
            key="Color",
            value="Red"
        )
        self.assertEqual(str(property_obj), "Test Product - Color: Red")

    def test_unique_together_constraint(self):
        """Test that product and key combination must be unique"""
        ProductProperty.objects.create(
            product=self.product,
            key="Color",
            value="Red"
        )
        
        # Should not be able to create another property with same key for same product
        with self.assertRaises(Exception):
            ProductProperty.objects.create(
                product=self.product,
                key="Color",
                value="Blue"
            )


class ProductImageModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            description="Test category description"
        )
        self.product = Product.objects.create(
            name="Test Product",
            description="Test product description",
            price=Decimal("99.99"),
            category=self.category,
            is_published=True,
            stock_quantity=10
        )

    def test_string_representation(self):
        """Test string representation of product image"""
        image = ProductImage.objects.create(
            product=self.product,
            alt_text="Test image"
        )
        self.assertEqual(str(image), "Test Product - Test image")


class CategoryAPITest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Electronics",
            description="Test electronics category"
        )

    def test_category_list(self):
        """Test category list endpoint"""
        url = reverse('catalog:category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], "Test Electronics")

    def test_category_detail(self):
        """Test category detail endpoint"""
        url = reverse('catalog:category-detail', kwargs={'slug': self.category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Electronics")

    def test_category_products(self):
        """Test category products endpoint"""
        # Create a published product
        Product.objects.create(
            name="Test Product",
            description="Test product",
            price=Decimal("99.99"),
            category=self.category,
            is_published=True,
            stock_quantity=10
        )
        
        url = reverse('catalog:category-products', kwargs={'slug': self.category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)


class ProductAPITest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            description="Test category description"
        )
        self.product = Product.objects.create(
            name="Test Product",
            description="Test product description",
            price=Decimal("99.99"),
            category=self.category,
            is_published=True,
            stock_quantity=10
        )
        self.unpublished_product = Product.objects.create(
            name="Unpublished Product",
            description="Unpublished product description",
            price=Decimal("149.99"),
            category=self.category,
            is_published=False,
            stock_quantity=5
        )

    def test_product_list_published_only(self):
        """Test that only published products are returned"""
        url = reverse('catalog:product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], "Test Product")

    def test_product_detail_published_only(self):
        """Test that unpublished products are not accessible"""
        url = reverse('catalog:product-detail', kwargs={'slug': self.unpublished_product.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_product_filtering_by_category(self):
        """Test product filtering by category slug"""
        url = reverse('catalog:product-list')
        response = self.client.get(url, {'category': self.category.slug})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_product_filtering_by_price_range(self):
        """Test product filtering by price range"""
        url = reverse('catalog:product-list')
        response = self.client.get(url, {'min_price': '50.00', 'max_price': '100.00'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_product_ordering(self):
        """Test product ordering"""
        # Create another product with different price
        Product.objects.create(
            name="Cheap Product",
            description="Cheap product description",
            price=Decimal("49.99"),
            category=self.category,
            is_published=True,
            stock_quantity=20
        )

        url = reverse('catalog:product-list')
        response = self.client.get(url, {'ordering': 'price'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        # Check ordering (cheapest first)
        self.assertEqual(response.data['results'][0]['price'], '49.99')

    def test_product_properties_in_api(self):
        """Test that product properties are included in API responses"""
        # Create properties for the product
        ProductProperty.objects.create(
            product=self.product,
            key="Color",
            value="Red",
            order=1
        )
        ProductProperty.objects.create(
            product=self.product,
            key="Size",
            value="Large",
            order=2
        )
        
        url = reverse('catalog:product-detail', kwargs={'slug': self.product.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that properties are included
        self.assertIn('properties', response.data)
        self.assertEqual(len(response.data['properties']), 2)
        self.assertEqual(response.data['properties'][0]['key'], 'Color')
        self.assertEqual(response.data['properties'][0]['value'], 'Red')
        self.assertEqual(response.data['properties'][1]['key'], 'Size')
        self.assertEqual(response.data['properties'][1]['value'], 'Large')

    def test_health_endpoint(self):
        """Test health check endpoint"""
        url = reverse('catalog:product-health')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'healthy')
        self.assertEqual(response.data['total_products'], 1)  # Only published products
        self.assertEqual(response.data['total_categories'], 1)

    def test_pagination(self):
        """Test that pagination works correctly"""
        # Create more products to test pagination
        for i in range(15):
            Product.objects.create(
                name=f"Product {i}",
                description=f"Product {i} description",
                price=Decimal("99.99"),
                category=self.category,
                is_published=True,
                stock_quantity=10
            )

        url = reverse('catalog:product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 12)  # Default page size
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
