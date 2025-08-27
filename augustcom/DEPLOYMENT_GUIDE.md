# 🚀 **Vercel + Render Deployment Guide**

## **Quick Deploy (30 minutes)**

### **1. Deploy Backend to Render**

1. **Go to [Render.com](https://render.com)** and sign up/login
2. **Click "New +" → "Web Service"**
3. **Connect your GitHub repository**
4. **Configure the service:**
   - **Name**: `shopcore-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn shopcore.wsgi:application`
   - **Plan**: Free

5. **Add Environment Variables:**
   ```
   SECRET_KEY: [Render will generate this]
   DEBUG: false
   ALLOWED_HOSTS: .onrender.com
   CORS_ALLOWED_ORIGINS: [Your Vercel frontend URL]
   DATABASE_URL: [Render will provide this]
   ```

6. **Click "Create Web Service"**
7. **Wait for deployment (5-10 minutes)**

### **2. Deploy Frontend to Vercel**

1. **Go to [Vercel.com](https://vercel.com)** and sign up/login
2. **Click "New Project"**
3. **Import your GitHub repository**
4. **Configure:**
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

5. **Add Environment Variables:**
   ```
   NEXT_PUBLIC_API_BASE: [Your Render backend URL]
   ```

6. **Click "Deploy"**
7. **Wait for deployment (2-3 minutes)**

### **3. Update CORS Settings**

1. **Go back to Render backend**
2. **Update CORS_ALLOWED_ORIGINS** with your Vercel URL
3. **Redeploy the backend**

## **🔧 Manual Deployment Steps**

### **Backend (Render)**

```bash
# 1. Push to GitHub
git add .
git commit -m "Ready for Render deployment"
git push origin main

# 2. Deploy on Render
# - Follow the web interface steps above
# - Render will auto-deploy on git push
```

### **Frontend (Vercel)**

```bash
# 1. Push to GitHub
git add .
git commit -m "Ready for Vercel deployment"
git push origin main

# 2. Deploy on Vercel
# - Follow the web interface steps above
# - Vercel will auto-deploy on git push
```

## **🌐 URLs After Deployment**

- **Frontend**: `https://your-project.vercel.app`
- **Backend**: `https://your-backend-name.onrender.com`
- **Admin**: `https://your-backend-name.onrender.com/admin`

## **📝 Important Notes**

1. **Database**: Render provides PostgreSQL automatically
2. **Static Files**: Served by Render (no CDN needed)
3. **Media Files**: Stored on Render (consider external storage for production)
4. **CORS**: Must be configured correctly for frontend-backend communication
5. **Environment Variables**: Update with actual URLs after deployment

## **🚨 Troubleshooting**

### **Common Issues:**

1. **CORS Errors**: Update `CORS_ALLOWED_ORIGINS` in Render
2. **Build Failures**: Check requirements.txt and package.json
3. **Database Connection**: Verify `DATABASE_URL` in Render
4. **Static Files**: Run `python manage.py collectstatic` if needed

### **Debug Commands:**

```bash
# Check backend logs in Render dashboard
# Check frontend build logs in Vercel dashboard
# Test API endpoints: https://your-backend.onrender.com/api/products/
```

## **🎯 Next Steps After Deployment**

1. **Test the application** on both URLs
2. **Create admin user**: `python manage.py createsuperuser`
3. **Add products** through Django admin
4. **Monitor performance** in both dashboards
5. **Set up custom domain** (optional)

---

**🎉 You're now live on Vercel + Render!**
