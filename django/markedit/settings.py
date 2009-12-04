from django.conf import settings
media_url = getattr(settings, 'MEDIA_URL', '/media/')

# Default settings (as python dict)
MARKEDIT_DEFAULT_SETTINGS = { }

# Media
MARKEDIT_CSS = { 'all': (media_url + '/js/jquery-markedit/jquery.markedit.css',) }
MARKEDIT_JS = (
    media_url + '/js/jquery-markedit/showdown.js',
    media_url + '/js/jquery-markedit/jquery.markedit.js',
)