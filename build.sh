#!/bin/bash
# Build script for Render deployment

set -e  # Exit on any error

echo "🏗️ Starting Render build process..."

# Upgrade pip to latest version
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install system-level packages that might be needed
echo "🔧 Installing build dependencies..."
pip install --upgrade setuptools wheel

# Install production requirements
echo "📦 Installing production requirements..."
if [ -f requirements_render.txt ]; then
    echo "Using Render-specific requirements..."
    pip install -r requirements_render.txt
else
    echo "Using standard production requirements..."
    pip install -r requirements_production.txt
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p uploads_temp
mkdir -p static/outputs/{images,documents,videos}
mkdir -p logs

# Set executable permissions for deploy script
chmod +x deploy.sh || true

# Initialize database (will create tables on first run)
echo "🗄️ Preparing database initialization..."
python -c "
import os
print('Environment check:')
print(f'FLASK_ENV: {os.environ.get(\"FLASK_ENV\", \"not set\")}')
print(f'DATABASE_URL: {\"set\" if os.environ.get(\"DATABASE_URL\") else \"not set\"}')
print('Build completed successfully!')
"

echo "✅ Build completed successfully!"
