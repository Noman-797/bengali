# WSGI configuration for PythonAnywhere
# Copy this content to your WSGI configuration file on PythonAnywhere

import sys
import os

# Add your project directory to the sys.path
path = '/home/yourusername/bengali'  # Replace 'yourusername' with your actual username
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'aiagent.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()