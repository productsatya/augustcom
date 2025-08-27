from django.contrib import admin
from .models import Category, Product, ProductImage, ProductProperty


class ProductPropertyInline(admin.TabularInline):
    model = ProductProperty
    extra = 1
    fields = ['key', 'value', 'order']
    ordering = ['order', 'key']


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'alt_text', 'is_primary']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'is_published', 'stock_quantity', 'created_at']
    list_filter = ['is_published', 'category', 'created_at', 'price']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ProductPropertyInline, ProductImageInline]
    list_editable = ['is_published', 'price', 'stock_quantity']


@admin.register(ProductProperty)
class ProductPropertyAdmin(admin.ModelAdmin):
    list_display = ['product', 'key', 'value', 'order', 'created_at']
    list_filter = ['created_at', 'key']
    search_fields = ['product__name', 'key', 'value']
    ordering = ['product', 'order', 'key']
    readonly_fields = ['created_at']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'alt_text', 'is_primary', 'created_at']
    list_filter = ['is_primary', 'created_at']
    search_fields = ['product__name', 'alt_text']
    readonly_fields = ['created_at']
