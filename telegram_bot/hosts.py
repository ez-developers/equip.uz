from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns('path.to',
    '',
    host(r'admin', settings.ROOT_URLCONF, name='admin'),
    host(r'api', 'api.urls', name='api'),
)