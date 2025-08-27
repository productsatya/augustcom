'use client';

import { Suspense } from 'react';
import { useSearchParams } from 'next/navigation';
import { useQuery } from '@tanstack/react-query';
import { getCategories, getProducts, searchParamsToParams } from '@/lib/api';
import FiltersBar from '@/components/FiltersBar';
import ProductGrid from '@/components/ProductGrid';
import Pagination from '@/components/Pagination';
import ErrorState from '@/components/ErrorState';
import EmptyState from '@/components/EmptyState';

function HomePageContent() {
  const searchParams = useSearchParams();
  const params = searchParamsToParams(searchParams);
  
  // Set default values
  const page = params.page || 1;
  const pageSize = params.page_size || 12;
  const ordering = params.ordering || '-created_at';

  // Fetch categories
  const { data: categories = [], isLoading: categoriesLoading, error: categoriesError } = useQuery({
    queryKey: ['categories'],
    queryFn: getCategories,
  });

  // Fetch products with current filters
  const { data: productsData, isLoading: productsLoading, error: productsError } = useQuery({
    queryKey: ['products', { ...params, page, page_size: pageSize, ordering }],
    queryFn: () => getProducts({ ...params, page, page_size: pageSize, ordering }),
    enabled: !categoriesLoading,
  });

  // Debug logging
  console.log('Categories:', { categories, categoriesLoading, categoriesError });
  console.log('Products:', { productsData, productsLoading, productsError });
  console.log('Params:', { page, pageSize, ordering, params });

  if (productsError) {
    console.error('Products error:', productsError);
    return (
      <div className="max-w-7xl mx-auto px-4 py-8">
        <ErrorState 
          message="Failed to load products. Please try again."
          onRetry={() => window.location.reload()}
        />
      </div>
    );
  }

  if (categoriesError) {
    console.error('Categories error:', categoriesError);
  }

  const totalPages = productsData ? Math.ceil(productsData.count / pageSize) : 0;
  const products = productsData?.results || [];

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">
          Discover Amazing Products
        </h1>
        <p className="text-gray-600">
          Browse our collection of high-quality products at great prices
        </p>
      </div>

      <FiltersBar categories={categories} />

      {productsLoading ? (
        <ProductGrid products={[]} isLoading={true} />
      ) : products.length === 0 ? (
        <EmptyState />
      ) : (
        <>
          <ProductGrid products={products} isLoading={false} />
          
          <Pagination
            currentPage={page}
            totalPages={totalPages}
            totalCount={productsData?.count || 0}
            pageSize={pageSize}
          />
        </>
      )}
    </div>
  );
}

export default function HomePage() {
  return (
    <Suspense fallback={
      <div className="max-w-7xl mx-auto px-4 py-8">
        <div className="animate-pulse">
          <div className="h-8 bg-gray-200 rounded w-48 mb-2"></div>
          <div className="h-4 bg-gray-200 rounded w-32 mb-8"></div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[...Array(6)].map((_, i) => (
              <div key={i} className="bg-gray-200 rounded-lg h-80"></div>
            ))}
          </div>
        </div>
      </div>
    }>
      <HomePageContent />
    </Suspense>
  );
}

