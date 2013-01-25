import os
import webapp2

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

class Upload(blobstore_handlers.BlobstoreUploadHandler):
  def get(self):
    # the get() part displays the upload webpage
    upload_url = blobstore.create_upload_url('/upload') #get blob upload url
    self.response.out.write('''<form action="%s" method="POST" enctype="multipart/form-data">''' % upload_url+'''Upload File: <input type="file" name="file"><br><input type="submit" name="submit" value="Upload"></form>''')
  def post(self):
    # the post() part handles the file uploading process
    upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
    blob_info = upload_files[0]
    self.response.out.write('File Key:%s' % blob_info.key())


app = webapp2.WSGIApplication([('/upload', Upload)],
                              debug=True)
