"""
WSGI entry point for production deployment
"""
import os
from main import app

# Set production environment
os.environ.setdefault('FLASK_ENV', 'production')

if __name__ == "__main__":
    app.run()
