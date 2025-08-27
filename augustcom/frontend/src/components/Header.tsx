'use client';

import Link from 'next/link';
import { ShoppingCart, Home } from 'lucide-react';

export default function Header() {
  return (
    <header className="bg-white shadow-sm border-b">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <Link href="/" className="flex items-center space-x-2">
              <ShoppingCart className="h-8 w-8 text-blue-600" />
              <span className="text-xl font-bold text-gray-900">ShopCore</span>
            </Link>
          </div>
          
          <nav className="flex items-center space-x-8">
            <Link 
              href="/" 
              className="flex items-center space-x-2 text-gray-700 hover:text-blue-600 transition-colors"
            >
              <Home className="h-5 w-5" />
              <span>Home</span>
            </Link>
          </nav>
        </div>
      </div>
    </header>
  );
}
