'use client';

import * as React from "react"
import { cn } from "@/lib/utils"

interface DialogProps {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
  title?: string;
}

export function Dialog({ isOpen, onClose, children, title }: DialogProps) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      <div 
        className="fixed inset-0 bg-black/50" 
        onClick={onClose}
      />
      <div className="relative bg-white rounded-lg shadow-lg max-w-md w-full mx-4">
        {title && (
          <div className="px-6 py-4 border-b">
            <h3 className="text-lg font-semibold">{title}</h3>
          </div>
        )}
        <div className="px-6 py-4">
          {children}
        </div>
      </div>
    </div>
  );
}

