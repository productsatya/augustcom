'use client';

import { Package } from 'lucide-react';

export default function EmptyState() {
  return (
    <div className="flex flex-col items-center justify-center py-12 text-center">
      <Package className="w-16 h-16 text-gray-400 mb-4" />
      <h3 className="text-lg font-semibold text-gray-900 mb-2">
        No products found
      </h3>
      <p className="text-gray-600 max-w-md">
        Try adjusting your filters or search criteria. We might not have products matching your current selection.
      </p>
    </div>
  );
}

