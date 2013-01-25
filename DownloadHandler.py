import os
import webapp2
import urllib

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

class DownloadHandler(blobstore_handlers.BlobstoreDownloadHandler):
  def get(self, blobkey, filename):#filname is not neccesary, added just to fit the pattern and indicate the right filename for browser
    #blobkey = str(urllib.unquote(blobkey))#do we really need unquoting? uncomment it if this script doesnt deal with specail chars well #check the url to find the key for the blob
    self.send_blob(blobstore.BlobInfo.get(blobkey),save_as=True)#save_as=True indicates that browser should save the file rather than open it when it's a picture or text, use save_as="str" to actively suggesting a filename.   


app = webapp2.WSGIApplication([('/download/([^/]+)?/([^/]+)?', DownloadHandler)],
                              debug=True)
