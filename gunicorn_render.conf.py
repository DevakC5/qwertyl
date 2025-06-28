"""
Gunicorn configuration optimized for Render deployment
"""
import os

# Server socket - Render provides PORT environment variable
port = os.environ.get('PORT', 10000)
bind = f"0.0.0.0:{port}"

# Worker processes - optimized for Render's container limits
workers = int(os.environ.get('WEB_CONCURRENCY', 1))
worker_class = "sync"
worker_connections = 1000

# Memory management for Render's limits
max_requests = 1000
max_requests_jitter = 100
timeout = 30
keepalive = 2

# Security
limit_request_line = 4096
limit_request_fields = 100
limit_request_field_size = 8190

# Logging for Render
accesslog = '-'
errorlog = '-'
loglevel = 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming
proc_name = 'businessastra-render'

# Preload app for better memory usage
preload_app = True

# Render-specific optimizations
forwarded_allow_ips = '*'
secure_scheme_headers = {
    'X-FORWARDED-PROTOCOL': 'ssl',
    'X-FORWARDED-PROTO': 'https',
    'X-FORWARDED-SSL': 'on'
}

def when_ready(server):
    """Called just before the master process is initialized."""
    server.log.info("BusinessAstra ready on Render. Port: %s", port)
