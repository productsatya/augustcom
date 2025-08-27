'use client';

import Image from 'next/image';
import Link from 'next/link';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { formatPrice, getFallbackImage } from '@/lib/utils';
import { ProductListItem } from '@/lib/types';
import { Eye } from 'lucide-react';

interface ProductCardProps {
  product: ProductListItem;
}

export default function ProductCard({ product }: ProductCardProps) {
  const imageUrl = product.primary_image?.image || getFallbackImage(product.slug);
  const imageAlt = product.primary_image?.alt_text || product.name;

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
      <div className="relative aspect-square overflow-hidden">
        <Image
          src={imageUrl}
          alt={imageAlt}
          fill
          className="object-cover hover:scale-105 transition-transform duration-300"
          sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
        />
        <Badge 
          variant="secondary" 
          className="absolute top-2 left-2"
        >
          {product.category.name}
        </Badge>
      </div>
      
      <div className="p-4">
        <h3 className="font-semibold text-lg mb-2 line-clamp-2">
          {product.name}
        </h3>
        <p className="text-2xl font-bold text-blue-600 mb-3">
          {formatPrice(product.price)}
        </p>
        
        <Link href={`/product/${product.slug}`} className="block">
          <Button className="w-full" size="lg">
            <Eye className="w-4 h-4 mr-2" />
            View Details
          </Button>
        </Link>
      </div>
    </div>
  );
}
