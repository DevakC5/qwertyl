"""
Production-ready configuration management for BusinessAstra
"""
import os
from datetime import timedelta


class Config:
    """Base configuration class"""
    
    # Core Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///businessastra.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_timeout': 20,
        'pool_recycle': -1,
        'pool_pre_ping': True
    }
    
    # File upload settings
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'uploads_temp'
    
    # Security settings
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = 3600  # 1 hour
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    # API settings
    TOGETHER_API_KEY = os.environ.get('TOGETHER_API_KEY')
    TOGETHER_MODEL_NAME = os.environ.get('TOGETHER_MODEL_NAME') or 'meta-llama/Llama-3.3-70B-Instruct-Turbo-Free'
    
    # Rate limiting
    RATELIMIT_STORAGE_URL = os.environ.get('REDIS_URL') or 'memory://'
    RATELIMIT_DEFAULT = "100 per hour"
    
    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL') or 'INFO'
    LOG_FORMAT = '%(asctime)s %(levelname)s %(name)s %(message)s'
    
    # Performance
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(hours=12)
    
    # Monitoring
    HEALTH_CHECK_PATH = '/health'
    METRICS_PATH = '/metrics'


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False
    
    # Less strict security for development
    SESSION_COOKIE_SECURE = False
    WTF_CSRF_ENABLED = False
    
    # More verbose logging
    LOG_LEVEL = 'DEBUG'
    
    # SQLite for development
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///dev_businessastra.db'


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    
    # Strict security settings
    SESSION_COOKIE_SECURE = True
    FORCE_HTTPS = True
    
    # Production database (PostgreSQL recommended)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://username:password@localhost/businessastra_prod'
    
    # Connection pooling for production
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 10,
        'pool_timeout': 30,
        'pool_recycle': 3600,
        'pool_pre_ping': True,
        'max_overflow': 20
    }
    
    # Redis for rate limiting in production
    RATELIMIT_STORAGE_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    
    # Tighter rate limits for production
    RATELIMIT_DEFAULT = "50 per hour"
    
    # Production logging
    LOG_LEVEL = 'WARNING'


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    
    # In-memory database for testing
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    
    # Disable CSRF for testing
    WTF_CSRF_ENABLED = False
    
    # Fast sessions for testing
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)


# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config():
    """Get configuration based on environment"""
    env = os.environ.get('FLASK_ENV', 'development')
    return config.get(env, config['default'])
