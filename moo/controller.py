import sys
import os
import socket
import StringIO
import json


import database
store=database

sessionId ={}

class Controller(object):
   # very limited content negotiation support - our format choices 
   # for output. This also shows _a way_ of representing enums in python
   json, xml, html, text = range(1,5)
   
   
   #
   # setup the configuration for our service
   #
   def __init__(self,base,conf_fn):
      self.host = socket.gethostname()
      self.base = base
      self.conf = {}
      
      # should emit a failure (file not found) message
      if os.path.exists(conf_fn):
         with open(conf_fn) as cf:
            for line in cf:
               name, var = line.partition("=")[::2]
               self.conf[name.strip()] = var.strip()
      else:
         raise Exception("configuration file not found.")

   def dump_conf(self,format):
    	    if format == Controller.json:
    	    	    return self.__conf_as_json()
         
         
   def __conf_as_json(self):
        try:
        	all = {}
         	all["base.dir"] = self.base
         	all["conf"] = self.conf
         	return json.dumps(all)
        except:
         	return "error: unable to return configuration"
         	 	 
         	 	 
   def dump_msg(self,format,msg):
        	if format == Controller.json:
        		return self.__msg_as_json(msg)
        		
        
        #
   # reply the registration request in requested format
   #
   def reg(self,format, name, user_id, password):
      if format == Controller.json:
         return self.__reg_as_json(name, user_id, password)
      
   #      
   # reply the login request in requested format
   #     
   def login(self,format,user_id, password):
      if format == Controller.json:
         return self.__login_as_json(user_id, password)
       
       
   #  
   #Get Sigle Board by board_id 
   #    
   def getBoard(self, format, board_id):
   	   if format == Controller.json:
   	   	   return self.__getBoard_as_json(board_id)
   	    
   #  
   #Get All Boards wihout logging in
   #
   def getAllBoards(self, format):
   	   if format == Controller.json:
   	   	   return self.__getAllBoards_as_json()
   	
   #  
   #Get Pin wihout logging in
   #
   def findPin(self, pinid):
      obj1 = store.findPin(pinid)
      resp = { }
      resp['value'] = obj1
      return json.dumps(resp)
    

   #  
   #Get All Pins wihout logging in
   #
   def getAllPins(self, format):
    	if  format == Controller.json:
        	return self.__getAllPins_as_json()  
         
   #  
   #Create Pin wihout logging in
   #	
   def createPin(self, format,pinname,pinpath,user_id):
       if format == Controller.json:
      
       	       return self.__createPin_as_json(pinname,pinpath,user_id)
       else:
       	       return self.__msg_as_text()


   #  
   #Create Board request
   #	   	   
   def createBoard(self, format, boardname,user_id):
   	   if format == Controller.json:
   	   	   return self.__createBoard_as_json(boardname,user_id)
 
   #  
   #Create Comment request
   #		   
   def comment(self,format,user_id,pin_id,comment):
		if format == Controller.json:
         		return self.__comment_as_json(user_id, pin_id,comment)

   #  
   #Get User Info
   #
   def getAllUserInfo(self, format, user_id):
   	   	if format == Controller.json:
   	   	   	return self.__getAllUserInfo_as_json(user_id)
         		
  
   #reply for deleteBoard in json format		
   def deleteBoard(self, format, board_id,user_id):
   	   if format == Controller.json:
   	   	   return self.__deleteBoard_as_json(board_id,user_id)
   	   else:
   	   	   return self.__msg_as_text()	

   #reply for attachPin in json format		
   def attachPin(self, format, board_id, pin_id,user_id):
   	   if format == Controller.json:
   	   	   return self.__attachPin_as_json(board_id, pin_id,user_id)
   	   else:
   	   	   return self.__msg_as_text()
   	   

   #
   #format reply registration request as json
   #
   def __reg_as_json(self,name,user_id,password):
      try:
	  token = store.signup(name,user_id,password)
	  rsp = {}
	  if(token==None):
		rsp["Error Message"]="User already Exist"
	  else:
		rsp["token"] = token
		sessionId[token] = token
          return json.dumps(rsp)
      except:
          return "error: unable to return token"
  

   #  
   #format reply login request as json
   #
   def __login_as_json(self,user_id,password):
      try:
	  print user_id, password
	  token = store.login(user_id,password)
	  print token
	  rsp = {}
	  if(token==None):
		rsp["Error Message"]="UserName/Password is Incorrect."
	  else :
		rsp["token"] = token
		sessionId[token] = token
	  return json.dumps(rsp)
      except:
      	  return "error: unable to login"

   #  
   #get board request as json
   #
   def __getBoard_as_json(self, board_id):
   	   try:
   	   	   board = store.getBoard(board_id)
   	   	   rsp = {}
   	   	   rsp['board'] = board
   	   	   return json.dumps(rsp)
   	   except:
   	   	   return "Board does not exist"


   #  
   #format reply for 'Get All Board' request as json
   #   
   def __getAllBoards_as_json(self):
   	   try:
   	   	   boards = store.getAllBoards()
   	   	   rsp = {} 	   	   
   	   	   rsp['boards'] = boards
   	   	   return json.dumps(rsp)
   	   except:
   	   	   return "There are no boards in the database."
   

   #  
   #format reply for 'Get All Pins' request as json
   #
   def __getAllPins_as_json(self):
          try:
                pins = store.getAllPins()
                print pins
                rsp = {}
                rsp['pins'] = pins
                return json.dumps(rsp)
          except:
                return "unable to return val"
   
   #create pin as json
   def __createPin_as_json(self, pinname, pinpath,user_id):
   	   try:
   	   	   print "Hello first Line here"
   	   	   if not(sessionId.has_key(user_id)):
   	   	   	   return "Invalid User or Password"
   	   	   	   
		   pin_id = store.createPin(pinname,pinpath)
   	   	   rsp = {}
   	   	   rsp['pin_id'] = pin_id
   	   	   return json.dumps(rsp)
   	   except:
   	   	   return "Pin already exist"

   #delete pin as json
   def __deleteBoard_as_json(self,board_id,user_id):
      print "sessionId ",sessionId
      if(not(sessionId.has_key(user_id))):
	 return "Invalid User or Password"	
      try:
      	 rsp = store.deleteBoard(board_id)
	 return json.dumps(rsp)
      except:
         return "error: unable to delete board (hint : the board id might not be present)"
         
   #attach Pin
   def __attachPin_as_json(self,board_id,pin_id,user_id):
      print "sessionId ",sessionId
      if(not(sessionId.has_key(user_id))):
	 return "Invalid User or Password"	
      try:
      	 rsp = store.attachPin(board_id, pin_id)
	 return json.dumps(rsp)
      except:
         return "error: unable to attach pin(hint : either the board_id or pin_id might not be present)"



 
   #  
   #format reply for 'Create Board' request as json
   #  
   def __createBoard_as_json(self, boardname, user_id):
	  print "sessionId ",sessionId
	  if(not(sessionId.has_key(user_id))):
		return "Invalid User or Password"		
	  try:
		board_id = store.createBoard(boardname,user_id)
   	   	rsp = {}
   	   	rsp['board_id'] = board_id
   	   	return json.dumps(rsp)
   	  except:
   	   	return "Error : Unable to create board"
   	   	

  
   	   	   
   def __comment_as_json(self, user_id,pin_id,comment):
	   print "sessionId ",sessionId
	   if(not(sessionId.has_key(user_id))):
		return "Invalid User or Password"	
   	   try:
		   cmt = store.comment(user_id,pin_id,comment)
		   print cmt
   	   	   rsp = {}
   	   	   rsp['comment'] = cmt
   	   	   #return json.dumps(rsp)
   	   except:
   	   	   return "unable to comment"
   	   	   
   

   def __getAllUserInfo_as_json(self,user_id):
	   print "sessionId ",sessionId
	   if(not(sessionId.has_key(user_id))):
		return "Invalid User or Password"	
   	   try:
   	   	   user = store.getAllUserInfo(user_id)
   	   	   rsp = {}
   	   	   rsp['userInfo'] = user
   	   	   return json.dumps(rsp)
   	   except:
   	   	   return "Sorry, Could not find the user info"
         