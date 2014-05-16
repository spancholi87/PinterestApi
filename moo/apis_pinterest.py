import time
import sys
import socket
import json
import urllib
import urlparse
import os
import shutil
import encryption
enc= encryption


from bottle import request, response, route, run, template


from controller import Controller

control = None

def setup(base,conf_fn):
   print '\n**** service initialization ****\n'
   global control 
   control = Controller(base,conf_fn)
   

#
#Registration
#
@route('/v1/reg', method='POST')
def registration():
   fmt = __format(request)
   response.content_type = __response_format(fmt)
   name = request.forms.get('name')
   if name == None:
   	   name = "Unnamed User"
   user_id = request.forms.get('user_id')
   password = request.forms.get('password')
   encpassword= enc.set_password(password)
   #print encpassword
   return control.reg(fmt, name, user_id, encpassword)
   

#login
@route('/v1/login', method='POST')
def login():
   fmt = __format(request)   
   response.content_type = __response_format(fmt)   
   user_id = request.forms.get('user_id')
   password = request.forms.get('password')
   return control.login(fmt,user_id, password)
   

#Get Board
@route('/v1/boards/:board_id', method='GET')
def getBoard(board_id):
   fmt = __format(request)   
   response.content_type = __response_format(fmt)   
   return control.getBoard(fmt,board_id)
   

#Get All Boards
@route('/v1/boards', method='GET')
def getAllBoards():
   fmt = __format(request)   
   response.content_type = __response_format(fmt)   
   return control.getAllBoards(fmt)


#Get Pin   
@route('/v1/pin/:pinid',method='GET')
def getPin(pinid):
    # get pin path for the pin id
    print '--->moo.findPin:',pinid
    return control.findPin(pinid)
    

# get all pins
@route('/v1/pins',method='GET')
def getAllPins():
   print '->moo.getAllPins:'
   fmt = __format(request)
   response.content_type = __response_format(fmt)
   print "response = ",response
   return control.getAllPins(fmt)


#Create Board
@route('/v1/user/:user_id/board', method='POST')
def createBoard(user_id):
   fmt = __format(request)   
   response.content_type = __response_format(fmt)   
   boardname = request.forms.get('boardname')   
   return control.createBoard(fmt,boardname,user_id)
   
   
#add Comments
@route('/v1/user/:user_id/pin/:pin_id', method='POST')
def doComment(user_id,pin_id):
   fmt = __format(request)   
   response.content_type = __response_format(fmt)   
   comment = request.forms.get('comment')
   return control.comment(fmt,user_id,pin_id,comment)


#Delete Board
@route('/v1/user/:user_id/board/:board_id', method='DELETE')
def deleteBoard(user_id, board_id):
   fmt = __format(request)
   response.content_type = __response_format(fmt)
   
   #chkToken(user_id)
   return control.deleteBoard(fmt, board_id,user_id)


#Attach Pin
@route('/v1/user/:user_id/board/:board_id', method='PUT')
def attachPin(user_id, board_id):
   fmt = __format(request)
   response.content_type = __response_format(fmt)
   
   #chkToken(user_id)
   pin_id = request.forms.get('pin_id')
   print board_id, pin_id
   return control.attachPin(fmt, board_id, pin_id,user_id)


# Upload Pin from file
@route('/v2/user/:user_id/pin/uploadfile', method='POST')
def do_upload(user_id):
	print user_id
	fmt=__format(request)	
	response.content_type = __response_format(fmt)
	file1 = request.files.get('value')
	print request.get
	if not file1:
		return "Please Upload an Image"
      
    	cwd = os.getcwd()
    	dest = cwd + '/images'
    	dirList = os.listdir(dest)
    	i=1
    	for fname in dirList:
    		i=i+1
    
    	imagename = 'image' + str(i) + '.jpg'
    	pinname = imagename
     
    	if not os.path.exists(dest):
    		os.makedirs(dest)
    	file_path = "{path}/{file}".format(path=dest, file=imagename)
    
    	with open(file_path, 'w') as open_file:
    		open_file.write(file1.file.read())
        
    	pinpath=dest+'/'+imagename
    	return control.createPin(fmt,pinname,pinpath,user_id)
    
# Upload Pin from Url
@route('/v2/user/:user_id/pin/uploadurl', method='POST')
def do_upload(user_id):
    fmt=__format(request)
    response.content_type = __response_format(fmt)
    for k,v in request.forms.allitems():
      print "file:",k,"=",v

    url = request.forms.get('value')
    pinname = urlparse.urlparse(url).path.split('/')[-1]
    image=urllib.URLopener()
    cwd = os.getcwd()
   
    dest = cwd + '/images'
    dirList = os.listdir(dest)
    i=1
    for fname in dirList:
        i=i+1
    
    imagename = 'image' + str(i) + '.jpg'
    image.retrieve(url,imagename)
    src = cwd + '/' + imagename
 
    if not os.path.exists(dest):
        os.makedirs(dest)
    print src
    print dest
    
    shutil.move(src,dest)
    pinpath=dest+'/'+imagename
    return control.createPin(fmt,pinname,pinpath,user_id)
     

#Get All User Info
@route('/v1/user/:user_id', method='GET')
def getAllUserInfo(user_id):
   fmt = __format(request)
   #
   response.content_type = __response_format(fmt)
   #
   return control.getAllUserInfo(fmt,user_id)
   
   
#
# Determine the format to return data
#
def __format(request):
                                                                       
   types = request.headers.get("Accept",'')
   subtypes = types.split(",")
   for st in subtypes:
      sst = st.split(';')
      if sst[0] == "text/html":
         return Controller.html
      elif sst[0] == "text/plain":
         return Controller.text
      elif sst[0] == "application/json":
         return Controller.json
      elif sst[0] == "*/*":
         return Controller.json
         
   return Controller.html

#
# The content type on the reply
#
def __response_format(reqfmt):
      if reqfmt == Controller.html:
         return "text/html"
      elif reqfmt == Controller.text:
         return "text/plain"
      elif reqfmt == Controller.json:
         return "application/json"
      else:
         return "*/*"
