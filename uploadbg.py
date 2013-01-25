import os
import webapp2

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import users

class Upload(blobstore_handlers.BlobstoreUploadHandler):
  def get(self):
    # the get() part displays the upload webpage
    user = users.get_current_user()
    upload_url = blobstore.create_upload_url('/uploadbg') #get blob upload url
    self.response.out.write('\n\
	<head><script src="upload.js">\n\
	</script></head>\n\
    <form action="1" id="imputform">\n\
      Upload File: <input type="file" name="file">\n\
      <br/>\n\
      <input type="button" value="Upload" onclick="upload('+"'"+str(upload_url)+"'"+')">\n\
    </form>\n')
  def post(self):
    # the post() part handles the file uploading process
    upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
    blob_info = upload_files[0]
    self.response.out.write('File Key:%s' % blob_info.key())


app = webapp2.WSGIApplication([('/uploadbg', Upload)],
                              debug=True)
