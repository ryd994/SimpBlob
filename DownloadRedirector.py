import os
import webapp2
import string
import re

from google.appengine.ext import blobstore

class DownloadRedirector(webapp2.RequestHandler):
  def get(self):
    keyword = self.request.get('keyword')
    keylen = len(keyword)
    if keyword[keylen-2:]=="==":
      blob_info = blobstore.get(blobstore.BlobKey(keyword))
      self.redirect('/download/%s/' % blob_info.key()+ blob_info.filename) #put the name of the blob at the end of the url, so the browser can recognize filename
      #if send file directly, use: blob serve hadler and self.send_blob(blob_info, save_as = blob_info.filename.replace('"', '\\"'))
    elif keyword[keylen-4:keylen-3]==".":
      query = blobstore.BlobInfo.all().filter("filename =",keyword)
      if query.count()==1:
        self.redirect('/download/%s/' % query.get().key()+ query.get().filename)
      else:
        self.redirect('/query?keyword='+keyword)
    else:
      self.redirect('/query?keyword='+keyword)


app = webapp2.WSGIApplication([('/download', DownloadRedirector)],
                              debug=True)
