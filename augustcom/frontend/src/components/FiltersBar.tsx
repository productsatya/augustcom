'use client';

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { useRouter, useSearchParams } from 'next/navigation';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Select } from '@/components/ui/select';
import { filterFormSchema, type FilterFormData } from '@/lib/schemas';
import { Category } from '@/lib/types';
import { Filter, RotateCcw } from 'lucide-react';

interface FiltersBarProps {
  categories: Category[];
}

export default function FiltersBar({ categories }: FiltersBarProps) {
  const router = useRouter();
  const searchParams = useSearchParams();
  
  const { register, handleSubmit, reset, formState: { errors } } = useForm<FilterFormData>({
    resolver: zodResolver(filterFormSchema),
    defaultValues: {
      category: searchParams.get('category') || '',
      min_price: searchParams.get('min_price') || '',
      max_price: searchParams.get('max_price') || '',
      ordering: searchParams.get('ordering') || '-created_at',
    },
  });

  const onSubmit = (data: FilterFormData) => {
    const params = new URLSearchParams();
    
    if (data.category) params.set('category', data.category);
    if (data.min_price) params.set('min_price', data.min_price);
    if (data.max_price) params.set('max_price', data.max_price);
    if (data.ordering) params.set('ordering', data.ordering);
    
    // Reset to first page when filters change
    params.set('page', '1');
    
    router.push(`/?${params.toString()}`);
  };

  const handleReset = () => {
    reset();
    router.push('/');
  };

  return (
    <div className="bg-white border rounded-lg p-6 mb-6">
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {/* Category Filter */}
          <div>
            <label htmlFor="category" className="block text-sm font-medium text-gray-700 mb-1">
              Category
            </label>
            <Select id="category" {...register('category')}>
              <option value="">All Categories</option>
              {categories.map((category) => (
                <option key={category.id} value={category.slug}>
                  {category.name}
                </option>
              ))}
            </Select>
          </div>

          {/* Min Price */}
          <div>
            <label htmlFor="min_price" className="block text-sm font-medium text-gray-700 mb-1">
              Min Price
            </label>
            <Input
              id="min_price"
              type="number"
              step="0.01"
              placeholder="0.00"
              {...register('min_price')}
            />
          </div>

          {/* Max Price */}
          <div>
            <label htmlFor="max_price" className="block text-sm font-medium text-gray-700 mb-1">
              Max Price
            </label>
            <Input
              id="max_price"
              type="number"
              step="0.01"
              placeholder="1000.00"
              {...register('max_price')}
            />
            {errors.max_price && (
              <p className="text-sm text-red-600 mt-1">{errors.max_price.message}</p>
            )}
          </div>

          {/* Sort Order */}
          <div>
            <label htmlFor="ordering" className="block text-sm font-medium text-gray-700 mb-1">
              Sort By
            </label>
            <Select id="ordering" {...register('ordering')}>
              <option value="-created_at">Newest First</option>
              <option value="created_at">Oldest First</option>
              <option value="price">Price: Low to High</option>
              <option value="-price">Price: High to Low</option>
              <option value="name">Name: A to Z</option>
              <option value="-name">Name: Z to A</option>
            </Select>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex justify-between items-center">
          <Button type="submit" className="flex items-center space-x-2">
            <Filter className="w-4 h-4" />
            <span>Apply Filters</span>
          </Button>
          
          <Button 
            type="button" 
            variant="outline" 
            onClick={handleReset}
            className="flex items-center space-x-2"
          >
            <RotateCcw className="w-4 h-4" />
            <span>Reset</span>
          </Button>
        </div>
      </form>
    </div>
  );
}
