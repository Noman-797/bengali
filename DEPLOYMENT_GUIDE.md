# PythonAnywhere Deployment Guide

## Files Ready for Deployment:
- ✅ Cleaned unnecessary files
- ✅ Updated settings.py
- ✅ Minimal requirements.txt
- ✅ WSGI configuration ready

## Deployment Steps:

### 1. Upload Files
- ZIP the entire `bengali` folder
- Upload to PythonAnywhere Files section
- Extract in your home directory

### 2. Install Requirements
```bash
pip3.10 install --user -r requirements.txt
```

### 3. Create Web App
- Go to Web tab
- Create new Django app
- Python version: 3.10

### 4. Configure WSGI
- Edit WSGI configuration file
- Copy content from `wsgi_config.py`
- Replace 'yourusername' with your actual username

### 5. Set Static Files
- Static URL: `/static/`
- Static directory: `/home/yourusername/bengali/staticfiles/`

### 6. Run Migrations (Optional)
```bash
python manage.py migrate
python manage.py collectstatic
```

### 7. Reload Web App
- Click "Reload" button in Web tab

## Your app will be live at:
`https://yourusername.pythonanywhere.com`

## Features:
- ✅ Bengali Translator
- ✅ Auto-translate
- ✅ Mobile responsive
- ✅ Dark/Light mode
- ✅ Copy functionality
- ✅ Hardcoded API key (no setup needed)