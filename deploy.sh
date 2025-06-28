#!/bin/bash
# Production deployment script for BusinessAstra

set -e  # Exit on any error

echo "🚀 Starting BusinessAstra Production Deployment"

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ .env file not found. Please copy .env.example to .env and configure it."
    exit 1
fi

# Load environment variables
source .env

# Validate required environment variables
required_vars=("SECRET_KEY" "TOGETHER_API_KEY" "DATABASE_URL")
for var in "${required_vars[@]}"; do
    if [ -z "${!var}" ]; then
        echo "❌ Required environment variable $var is not set in .env"
        exit 1
    fi
done

echo "✅ Environment variables validated"

# Install production dependencies
echo "📦 Installing production dependencies..."
pip install -r requirements_production.txt

# Run database migrations
echo "🗄️ Initializing database..."
python -c "
import os
os.environ['FLASK_ENV'] = 'production'
from main import app, init_database
with app.app_context():
    init_database()
print('Database initialized successfully')
"

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p uploads_temp
mkdir -p static/outputs/{images,documents,videos}
mkdir -p logs

# Set proper permissions
chmod 755 uploads_temp
chmod 755 static/outputs
chmod -R 755 static/outputs/*

# Test configuration
echo "🧪 Testing configuration..."
python -c "
import os
os.environ['FLASK_ENV'] = 'production'
from main import app
from config import get_config
config = get_config()
print(f'Environment: {os.environ.get(\"FLASK_ENV\")}')
print(f'Debug mode: {config.DEBUG}')
print(f'Database: {config.SQLALCHEMY_DATABASE_URI[:50]}...')
print('Configuration test passed')
"

# Test health check
echo "🏥 Testing health endpoint..."
python -c "
import os
os.environ['FLASK_ENV'] = 'production'
from main import app
with app.test_client() as client:
    response = client.get('/health')
    if response.status_code == 200:
        print('Health check passed')
    else:
        print(f'Health check failed: {response.status_code}')
        exit(1)
"

echo "✅ All tests passed!"

# Deployment options
echo ""
echo "🎯 Choose deployment method:"
echo "1) Run with Gunicorn (recommended for production)"
echo "2) Run with Docker Compose"
echo "3) Run development server (not recommended for production)"

read -p "Enter choice (1-3): " choice

case $choice in
    1)
        echo "🚀 Starting with Gunicorn..."
        echo "Access the application at: http://localhost:8000"
        echo "Health check: http://localhost:8000/health"
        echo "Metrics: http://localhost:8000/metrics"
        echo ""
        echo "To stop: Press Ctrl+C"
        echo ""
        exec gunicorn --config gunicorn.conf.py wsgi:app
        ;;
    2)
        echo "🐳 Starting with Docker Compose..."
        if ! command -v docker-compose &> /dev/null; then
            echo "❌ docker-compose not found. Please install Docker and Docker Compose."
            exit 1
        fi
        
        echo "Building and starting containers..."
        docker-compose up --build
        ;;
    3)
        echo "⚠️  Starting development server (NOT for production)..."
        FLASK_ENV=production python main.py
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac
