import os
import webapp2
import string

from google.appengine.ext import blobstore
from google.appengine.ext import db

class QueryByName(webapp2.RequestHandler):
  def get(self):
    name = self.request.get('keyword')
    query = blobstore.BlobInfo.all().order("-creation").order("filename") 
#use datastore queries to filter the result: (not using)
#if possible, try to use them to refine the result
#    length = len(name)
#    name2 = name[:length-1]+chr(ord(name[length-1:length])+1)
#    query.filter('filename >=',str(name)).filter('filename <',str(name2)).order("filename").order("-creation")
    self.response.out.write('\
<head>\
  <title>Search Result</title>\
</head>\
<body>\
  <table border="1" width="100%">\
    <tr>\
      <th>Name</th>\
      <th>Create Time</th>\
      <th>Key</th>\
    </tr>')
    count = 0
    for blob in query:
      if str(blob.filename).lower().find(name.lower())!=-1:
        count = count+1
        self.response.out.write('\
    <tr>\
      <th>%(filename)s</th>\
      <td>%(creation)s</td>\
      <td><textarea rows="1" cols="23" readonly="1" style="resize: none" onclick="this.select();">%(key)s</textarea></td>\
      <td><a href="../download/%(key)s/%(filename)s">Download</a></td>\
    </tr>'%{"filename": blob.filename,\
            "creation": blob.creation,\
            "key": blob.key(),\
            "count": count,\
           })
    if count==0:
      self.response.out.write('\
    <tr>\
      <td colspan="3">No such file found!</td>\
    </tr>')
    self.response.out.write('\
  </table>\
</body>')

    
app = webapp2.WSGIApplication([('/query', QueryByName)],
                              debug=True)
