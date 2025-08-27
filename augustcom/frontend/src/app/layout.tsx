import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import Providers from './providers';
import Header from '@/components/Header';
import Footer from '@/components/Footer';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'ShopCore - Your Online Store',
  description: 'Discover amazing products at great prices',
  openGraph: {
    title: 'ShopCore - Your Online Store',
    description: 'Discover amazing products at great prices',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'ShopCore - Your Online Store',
    description: 'Discover amazing products at great prices',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Providers>
          <div className="min-h-screen flex flex-col">
            <Header />
            <main className="flex-1">
              {children}
            </main>
            <Footer />
          </div>
        </Providers>
      </body>
    </html>
  );
}
