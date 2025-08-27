# ShopCore Monorepo

A full-stack e-commerce application built with Django (backend) and Next.js (frontend).

## 🏗️ Project Structure

```
├── frontend/                 # Next.js application (public web)
│   ├── src/                 # React components and pages
│   ├── package.json         # Node.js dependencies
│   ├── next.config.js       # Next.js configuration
│   ├── tailwind.config.js   # Tailwind CSS configuration
│   └── env.example          # Frontend environment variables
│
├── backend/                  # Django application (API + Admin)
│   ├── manage.py            # Django management script
│   ├── shopcore/            # Django project settings
│   ├── catalog/             # Django app (products, categories)
│   ├── requirements.txt     # Python dependencies
│   ├── Procfile            # Heroku deployment configuration
│   └── env.example         # Backend environment variables
│
└── README_MONOREPO.md       # This file
```

## 🚀 Quick Start

### Backend (Django)

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server:**
   ```bash
   python manage.py runserver
   ```

### Frontend (Next.js)

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Set up environment variables:**
   ```bash
   cp env.example .env.local
   # Edit .env.local with your backend API URL
   ```

4. **Start development server:**
   ```bash
   npm run dev
   ```

## 🌐 Access Points

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000/api/
- **Django Admin**: http://localhost:8000/admin/

## 🚀 Production Deployment

### Backend Deployment

1. **Set environment variables:**
   - `SECRET_KEY`: Strong secret key
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: Your domain
   - `DATABASE_URL`: PostgreSQL connection string
   - `CORS_ALLOWED_ORIGINS`: Your frontend domain

2. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

3. **Deploy with Gunicorn:**
   ```bash
   gunicorn shopcore.wsgi:application
   ```

### Frontend Deployment

1. **Build for production:**
   ```bash
   npm run build
   npm start
   ```

2. **Update API base URL** in environment variables

## 🗄️ Database

- **Development**: SQLite (default)
- **Production**: PostgreSQL (recommended)

## 🔧 Key Features

- **Backend**: Django REST API, Admin interface, Product management
- **Frontend**: Next.js with TypeScript, Tailwind CSS, Responsive design
- **API**: RESTful endpoints for products, categories, and filtering
- **Admin**: Django admin for content management

## 📁 File Organization

- **No admin UI in frontend** - Admin access is through Django admin only
- **Public site only** in frontend - All admin functionality is backend-only
- **Clean separation** between frontend (public) and backend (admin + API)

## 🔒 Security

- CORS configured for production
- Environment-based configuration
- Production-ready security settings
- Separate admin and public interfaces

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Django REST Framework](https://www.django-rest-framework.org/)
