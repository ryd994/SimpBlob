import os
import cgi
import urllib
import webapp2

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

class MainHandler(webapp2.RequestHandler):
  def get(self):
    upload_url = blobstore.create_upload_url('/upload')
    self.response.out.write('''<html>
      <body>
        <form action="%s" method="POST" enctype="multipart/form-data">''' % upload_url+'''Upload File: <input type="file" name="file">
          <br> <input type="submit" name="submit" value="Upload">
        </form>
        <hr>
        <form action="/download" method="GET" enctype="multipart/form-data">
          Download File: <input type="text" name="filekey">
          <br> <input type="submit" name="submit" value="Download">
        </form>
      </body>
    </html>''')

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
  def post(self):
    upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
    blob_info = upload_files[0]
    self.response.out.write('File Key:%s' % blob_info.key())
#    self.redirect('/serve/%s/' % blob_info.key()+blob_info.filename)

class ServeRedirecter(webapp2.RequestHandler):
  def get(self):
    blob_info = blobstore.get(self.request.get('filekey'))
    self.redirect('/download/%s/' % blob_info.key()+ blob_info.filename)

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
  def get(self, resource, filename):
    resource = str(urllib.unquote(resource))
    blob_info = blobstore.BlobInfo.get(resource)
    self.send_blob(blob_info)

app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/upload', UploadHandler),
                               ('/download', ServeRedirecter),
                               ('/download/([^/]+)?', ServeHandler),
                               ('/download/([^/]+)?/([^/]+)?', ServeHandler)],
                              debug=True)
