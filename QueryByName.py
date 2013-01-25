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
    self.response.out.write('''<head>\n\r<title>Search Result</title>\n\r</head>\n\r<body>\n\r<table border="1" width="100%">\n\r<tr><th>Name</th><th>Create Time</th><th>Key</th></tr><br>\n\r''')
    count = 0
    for blob in query:
      if str(blob.filename).lower().find(name.lower())!=-1:
        self.response.out.write("<tr><th>"+str(blob.filename)+"</th><td>"+str(blob.creation)+'</td><td><textarea rows="1" cols="23" readonly="1" style="resize: none">'+str(blob.key())+'</textarea></td><td><a href="'+'../download/%s/' % blob.key()+ blob.filename+'">Download</a></td></tr><br>\n\r')
        count = count+1
    if count==0:
      self.response.out.write("<tr><td colspan='3'>No such file found!</td></tr>")
    self.response.out.write("</table>\n\r</body>")

    
app = webapp2.WSGIApplication([('/query', QueryByName)],
                              debug=True)
