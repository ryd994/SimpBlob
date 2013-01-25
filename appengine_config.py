import re

def webapp_add_wsgi_middleware(app):
    from google.appengine.ext.appstats import recording
    app = recording.appstats_wsgi_middleware(app)
    return app

def appstats_extract_key(request):
    key = request.http_path()#Careful!appstats_normalize_path() is not used, so normalize_path function no longer effects!
    if re.match('/download/[^/]+/[^/]+',key):
        key = '%s %s' % (key[35:], key[10:32])
    if request.http_method() != 'GET':
        key = '%s %s' % (request.http_method(), key)
    return key
