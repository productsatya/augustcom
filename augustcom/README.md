# ShopWeb - E-commerce Frontend

A modern, responsive e-commerce frontend built with Next.js 14, TypeScript, and Tailwind CSS, designed to work with the Django REST API backend.

## Features

- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Product Grid**: Responsive product grid with filtering and sorting
- **Advanced Filtering**: Category, price range, and search filters
- **Product Details**: Rich product pages with image galleries and specifications
- **Pagination**: Efficient pagination with URL state management
- **Real-time Updates**: React Query for efficient data fetching and caching
- **Accessibility**: ARIA labels, keyboard navigation, and semantic HTML
- **SEO Optimized**: Dynamic metadata and Open Graph tags

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: React Query (@tanstack/react-query)
- **Forms**: React Hook Form + Zod validation
- **HTTP Client**: Axios
- **Icons**: Lucide React
- **UI Components**: Custom component library with shadcn/ui patterns

## Project Structure

```
src/
├── app/                    # Next.js App Router
│   ├── layout.tsx         # Root layout with providers
│   ├── page.tsx           # Homepage with product grid
│   ├── product/[slug]/    # Product detail pages
│   └── globals.css        # Global styles and Tailwind
├── components/            # Reusable components
│   ├── ui/               # Base UI components
│   ├── ProductCard.tsx   # Product display card
│   ├── FiltersBar.tsx    # Filter and sort controls
│   ├── ProductGrid.tsx   # Product grid layout
│   ├── Pagination.tsx    # Page navigation
│   └── ...               # Other components
└── lib/                  # Utilities and configurations
    ├── api.ts            # API client and functions
    ├── types.ts          # TypeScript type definitions
    ├── utils.ts          # Utility functions
    └── schemas.ts        # Zod validation schemas
```

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Django backend running on http://localhost:8000

### Installation

1. **Clone and install dependencies:**
   ```bash
   npm install
   ```

2. **Set up environment variables:**
   ```bash
   # Create .env.local
   NEXT_PUBLIC_API_BASE=http://localhost:8000
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

## API Integration

The frontend integrates with the Django REST API endpoints:

- `GET /api/categories/` - Fetch product categories
- `GET /api/products/` - Fetch products with filtering
- `GET /api/products/{slug}/` - Fetch product details

### Filtering & Sorting

- **Category**: Filter by category slug
- **Price Range**: Min/max price filters
- **Sorting**: Newest, price (low/high), name (A-Z/Z-A)
- **Pagination**: Configurable page size (default: 12)

### URL State Management

All filters, sorting, and pagination are reflected in the URL, making them:
- Shareable via links
- Bookmarkable
- Refresh-safe
- SEO-friendly

## Components

### Core Components

- **ProductCard**: Displays product information in grid format
- **FiltersBar**: Category, price, and sorting controls
- **ProductGrid**: Responsive grid layout with loading states
- **Pagination**: Page navigation with smart ellipsis
- **ErrorState**: User-friendly error handling
- **EmptyState**: No results found messaging

### UI Components

Built with a consistent design system:
- **Button**: Multiple variants and sizes
- **Input**: Form inputs with validation
- **Select**: Dropdown selections
- **Card**: Content containers
- **Badge**: Status and category indicators
- **Skeleton**: Loading placeholders
- **Dialog**: Modal dialogs

## Features

### Homepage
- Hero section with product grid
- Advanced filtering system
- Responsive product cards
- Pagination controls
- Loading and error states

### Product Details
- Image gallery with thumbnails
- Product specifications
- Stock status indicators
- Buy Now functionality
- Breadcrumb navigation

### Filtering System
- Real-time filter application
- URL state synchronization
- Form validation with Zod
- Reset functionality
- Responsive filter layout

## Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

### Code Quality

- TypeScript for type safety
- ESLint for code quality
- Prettier for code formatting
- Component-based architecture
- Custom hooks for data fetching

### Performance

- React Query for efficient caching
- Image optimization with Next.js Image
- Lazy loading and code splitting
- Optimized bundle sizes
- Responsive image sizing

## Deployment

### Build for Production

```bash
npm run build
npm run start
```

### Environment Variables

- `NEXT_PUBLIC_API_BASE`: Backend API base URL
- Ensure backend is accessible from deployment domain

### Static Export (Optional)

```bash
npm run build
npm run export
```

## Backend Integration

This frontend is designed to work with the Django backend that provides:

- Product catalog management
- Category organization
- Image handling
- Product properties (key-value pairs)
- Admin interface for content management

## Contributing

1. Follow the existing code structure
2. Use TypeScript for all new code
3. Implement responsive design patterns
4. Add proper error handling
5. Include loading states
6. Test with different screen sizes

## License

This project is part of the ShopCore e-commerce platform.
