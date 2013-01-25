import os
import webapp2
import urllib

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

class DownloadHandler(blobstore_handlers.BlobstoreDownloadHandler):
  def get(self, blobkey, filename):
    blobkey = str(urllib.unquote(blobkey))#find the key of the file
    self.send_blob(blobstore.BlobInfo.get(blobkey))# send the file(blob) with the key indicated to user


app = webapp2.WSGIApplication([('/download/([^/]+)?/([^/]+)?', DownloadHandler)],
                              debug=True)
