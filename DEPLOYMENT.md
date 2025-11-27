# Deploying Pixiee to Vercel

## Prerequisites
- Vercel account (free tier works!)
- Vercel CLI installed: `npm install -g vercel`

## Deployment Steps

### 1. Install Vercel CLI (if not already installed)
```bash
npm install -g vercel
```

### 2. Login to Vercel
```bash
vercel login
```

### 3. Deploy from your project directory
```bash
cd /Users/mihika/Documents/Projects/AI\ ZoomCamp\ Projects/1_to_do_app
vercel
```

### 4. Follow the prompts:
- Set up and deploy? **Y**
- Which scope? Select your account
- Link to existing project? **N**
- Project name? **pixiee** (or your preferred name)
- Directory? **./** (just press Enter)
- Override settings? **N**

### 5. For production deployment:
```bash
vercel --prod
```

## Important Notes

### Database Limitation
⚠️ **SQLite won't persist on Vercel** because the filesystem is ephemeral. Your todos will reset on each deployment.

**Solutions:**
1. **For demo purposes**: Current setup works, but data resets
2. **For production**: You'll need to switch to a cloud database:
   - Vercel Postgres (free tier available)
   - Supabase (free tier)
   - PlanetScale (free tier)
   - Railway Postgres (free tier)

### To add Vercel Postgres:
1. Go to your Vercel dashboard
2. Select your project
3. Go to Storage → Create Database → Postgres
4. Copy the connection string
5. Update `settings.py` to use PostgreSQL instead of SQLite

### Environment Variables
Set these in Vercel dashboard (Settings → Environment Variables):
- `DEBUG`: `False` (for production)
- `SECRET_KEY`: Generate a new one for production
- `DATABASE_URL`: Your database connection string (if using external DB)

## Troubleshooting

### Static files not loading?
Run locally first:
```bash
python manage.py collectstatic
```

### Build fails?
Check the Vercel build logs in the dashboard

### App not responding?
- Check Vercel function logs
- Verify `vercel.json` configuration
- Ensure all dependencies are in `requirements.txt`

## Alternative: Quick Deploy Button

You can also add this to your README for one-click deployment:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/mihikajadhav02/pixiee)

## Post-Deployment

After successful deployment, you'll get a URL like:
`https://pixiee-username.vercel.app`

Update `ALLOWED_HOSTS` in `settings.py` to include your Vercel domain for better security.
