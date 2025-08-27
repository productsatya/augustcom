'use client';

import { useParams } from 'next/navigation';
import { useQuery } from '@tanstack/react-query';
import { useState } from 'react';
import Image from 'next/image';
import Link from 'next/link';
import { getProduct } from '@/lib/api';
import { formatPrice, getFallbackImage } from '@/lib/utils';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Dialog } from '@/components/ui/dialog';
import { Skeleton } from '@/components/ui/skeleton';
import ErrorState from '@/components/ErrorState';
import { ArrowLeft, ShoppingCart, Package, Calendar, Hash } from 'lucide-react';

export default function ProductDetailPage() {
  const params = useParams();
  const slug = params.slug as string;
  const [isOrderModalOpen, setIsOrderModalOpen] = useState(false);

  const { data: product, isLoading, error } = useQuery({
    queryKey: ['product', slug],
    queryFn: () => getProduct(slug),
  });

  const handleBuyNow = () => {
    setIsOrderModalOpen(true);
  };

  const handleMailtoOrder = () => {
    const subject = `Order: ${product?.name} (${product?.slug})`;
    const body = `Hi,\n\nI would like to order:\n\nProduct: ${product?.name}\nPrice: ${product?.price}\n\nPlease contact me to complete the order.\n\nThank you!`;
    
    window.location.href = `mailto:sales@shopcore.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  };

  if (error) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-8">
        <ErrorState 
          message="Failed to load product details. Please try again."
          onRetry={() => window.location.reload()}
        />
      </div>
    );
  }

  if (isLoading || !product) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-8">
        <div className="mb-6">
          <Skeleton className="h-8 w-48 mb-2" />
          <Skeleton className="h-4 w-32" />
        </div>
        
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <Skeleton className="aspect-square rounded-lg" />
          <div className="space-y-4">
            <Skeleton className="h-8 w-3/4" />
            <Skeleton className="h-6 w-1/2" />
            <Skeleton className="h-4 w-full" />
            <Skeleton className="h-4 w-2/3" />
            <Skeleton className="h-12 w-32" />
          </div>
        </div>
      </div>
    );
  }

  const primaryImage = product.images?.find(img => img.is_primary) || product.images?.[0];
  const imageUrl = primaryImage?.image || getFallbackImage(product.slug);
  const imageAlt = primaryImage?.alt_text || product.name;

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      {/* Breadcrumb */}
      <div className="mb-6">
        <Link 
          href="/" 
          className="inline-flex items-center text-blue-600 hover:text-blue-800 transition-colors"
        >
          <ArrowLeft className="w-4 h-4 mr-2" />
          Back to Products
        </Link>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Product Images */}
        <div className="space-y-4">
          <div className="relative aspect-square overflow-hidden rounded-lg border">
            <Image
              src={imageUrl}
              alt={imageAlt}
              fill
              className="object-cover"
              sizes="(max-width: 1024px) 100vw, 50vw"
            />
          </div>
          
          {/* Thumbnail strip for multiple images */}
          {product.images && product.images.length > 1 && (
            <div className="flex space-x-2 overflow-x-auto">
              {product.images.map((image) => (
                <div key={image.id} className="relative w-20 h-20 flex-shrink-0">
                  <Image
                    src={image.image}
                    alt={image.alt_text || product.name}
                    fill
                    className="object-cover rounded border cursor-pointer hover:opacity-80 transition-opacity"
                    sizes="80px"
                  />
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Product Info */}
        <div className="space-y-6">
          <div>
            <Badge variant="secondary" className="mb-3">
              {product.category.name}
            </Badge>
            <h1 className="text-3xl font-bold text-gray-900 mb-2">
              {product.name}
            </h1>
            <p className="text-2xl font-bold text-primary">
              {formatPrice(product.price)}
            </p>
          </div>

          {/* Stock Status */}
          <div className="flex items-center space-x-2">
            <Package className="w-5 h-5 text-gray-500" />
            <span className="text-gray-700">
              {product.stock_quantity > 0 ? (
                <span className="text-green-600 font-medium">In Stock ({product.stock_quantity} available)</span>
              ) : (
                <span className="text-red-600 font-medium">Out of Stock</span>
              )}
            </span>
          </div>

          {/* Description */}
          {product.description && (
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">Description</h3>
              <p className="text-gray-600 leading-relaxed">
                {product.description}
              </p>
            </div>
          )}

          {/* Product Properties */}
          {product.properties && product.properties.length > 0 && (
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-3">Specifications</h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {product.properties.slice(0, 6).map((prop) => (
                  <div key={prop.id} className="flex justify-between py-2 border-b border-gray-100">
                    <span className="font-medium text-gray-700">{prop.key}</span>
                    <span className="text-gray-600">{prop.value}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Buy Now Button */}
          <div className="pt-4">
            <Button 
              onClick={handleBuyNow}
              size="lg"
              className="w-full sm:w-auto"
              disabled={product.stock_quantity === 0}
            >
              <ShoppingCart className="w-5 h-5 mr-2" />
              Buy Now
            </Button>
          </div>

          {/* Additional Info */}
          <div className="pt-6 border-t border-gray-200">
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm text-gray-600">
              <div className="flex items-center space-x-2">
                <Calendar className="w-4 h-4" />
                <span>Added: {new Date(product.created_at).toLocaleDateString()}</span>
              </div>
              <div className="flex items-center space-x-2">
                <Hash className="w-4 h-4" />
                <span>SKU: {product.slug}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Order Success Modal */}
      <Dialog 
        isOpen={isOrderModalOpen} 
        onClose={() => setIsOrderModalOpen(false)}
        title="Order Placed Successfully!"
      >
        <div className="space-y-4">
          <p className="text-gray-600">
            Thank you for your order! This is a demo application. In a real scenario, you would be redirected to a checkout page.
          </p>
          
          <div className="flex space-x-3">
            <Button 
              onClick={handleMailtoOrder}
              className="flex-1"
            >
              Send Email Order
            </Button>
            <Button 
              variant="outline"
              onClick={() => setIsOrderModalOpen(false)}
              className="flex-1"
            >
              Close
            </Button>
          </div>
        </div>
      </Dialog>
    </div>
  );
}

