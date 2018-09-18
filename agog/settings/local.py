
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CORS_ORIGIN_ALLOW_ALL = True

CORS_URLS_REGEX = r'^/api/.*$'

CORS_ORIGIN_WHITELIST = (
    'localhost:4200',
    '127.0.0.1:4200'
)