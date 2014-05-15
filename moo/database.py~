import couchdb
import encryption
encry= encryption

couch = couchdb.Server() # Assuming localhost:5984
#couch = couchdb.Server('http://127.0.0.1:5984/')

def signup(name, user_id, password):
	db = couch['pinterest']

#create a document and insert it into the db:
	doc_id = 'UserInfo'
	doc = db[doc_id]
	users = doc['user']
	
	for item in users:
         	if user_id == item["user_id"]:
			print 'user already exist'
			return None

	user1 = {'name': name, 'user_id': user_id, 'password': password, 'boardlist':[ ] }
	print user1
	doc['user'].append(user1)
	db.save(doc)
	return user_id

#changes made for encryption password
def login(user_id, password):
	print password
	db = couch['pinterest']
	#print user_id, '**********************************'

	doc_id = 'UserInfo'
	doc = db[doc_id]
	users = doc['user']
	
	for item in users:
         	if user_id == item["user_id"] and encry.check_password(password,item["password"])== True: 		
			return user_id
         
#Get Board Details         
def getBoard(board_id):
	db = couch['pinterest']
	doc_id = 'boards'
	doc = db[doc_id]
	boards = doc['board']
	brd = []
	if boards.has_key(board_id):
		board = boards[board_id]
		pins = board['pin_id']
		for pin in pins:
			val = findPin(pin)
			brd.append(val)
		return brd
	else:
		return "Board does not exist"
		
# Get All Boards
def getAllBoards():
	db = couch['pinterest']
	
	doc_id = 'boards'
	doc = db[doc_id]
	boards = doc['board']
	allboards = []
	for key in boards:
		board = boards[key]
		print key
		boardVal = {'board_id': key, 'board_name': board['board_name']}
		allboards.append(boardVal)
		
	return allboards	

# Create a Board
def createBoard(boardName, user_id):
	db = couch['pinterest']

	doc_id = 'boards'
	doc = db[doc_id]
	boards = doc['board']
	length = str(len(boards))
	count = 0
	list1 = []
	board_id = 0
	if(length == 0):
		board_id = 0
	else:
		list1 = boards.keys()
		list1 = map(int, list1)
		board_id = str(max(list1) + 1)
	boards[board_id] = {'board_name': boardName, 'pin_id':[]}
	docid = 'UserInfo'
	doc1 = db[docid]
	users = doc1['user']
	flag = 0
	for item in users:
         	if user_id == item["user_id"]:
         		flag = 1
         		item["boardlist"].append(board_id)
         		db.save(doc1)
         
        if flag == 1:
        	db.save(doc)
        	return board_id
        	
        else:
        	return "Invalid User"
		
	
# Attach Pin	
def attachPin(boardId, pinId):
	db = couch['pinterest']
	print type(pinId)
	doc_id = 'boards'
	doc = db[doc_id]
	boards = doc['board']
	if boards.has_key(boardId):
			docid = 'pins'
			doc1 = db[docid]
			pins = doc1['allpins']
			board = boards[boardId]
			if pins.has_key(pinId):
				pins1 = board['pin_id']
				for i in pins1:
					if i == pinId:
						return "value already exists"
					
				board['pin_id'].append(pinId)
				db.save(doc)
				return True
	return False
	

# Create Pin
def createPin(pinname,pinpath):
	print '----->createPin'
	db = couch['pinterest']
	
	doc = db['pins']
	allpins = doc['allpins']
	list1 = allpins.keys()
	list1 = map(int, list1)
	pin_id = str(max(list1) + 1)
	
	newPin = {'pinname':pinname,'comments':[],'pinpath':pinpath}
	allpins[pin_id] = newPin
	db.save(doc)
	return pin_id
					
# Add Comment to a Pin				
def comment(user_id,pin_id,comment):
	db = couch['pinterest']
	#print "comment**********************************"

	doc_id = 'pins'
	doc = db[doc_id]
	pins = doc['allpins']
	if pins.has_key(pin_id):
		pin = pins[pin_id]
		newComment = {'userid': user_id, 'comment': comment}
		pin['comments'].append(newComment)
		db.save(doc)
		return True
	else:
		return False
			
# To get the Pin details of a particular Pin
def findPin(pin_id):
	db = couch['pinterest']
	doc_id = 'pins'
	doc = db[doc_id]
	pins = doc['allpins']
	if(pins.has_key(pin_id)):
			pin = pins[pin_id]
			pinVal = {'pin_id': pin_id, 'pin_name': pin['pinname'], 'pin_url': pin['pinpath']}
			return pinVal
	else:
		return "No such Pin Exist"
	
# Get All the Pins that are stored	
def getAllPins():
	db = couch['pinterest']
	doc_id = 'pins'
	doc = db[doc_id]
	pins = doc['allpins']
	allpins = []
	for key in pins:
		pin = pins[key]
		pinVal = {'pin_id': key, 'pin_name': pin['pinname'], 'pin_url': pin['pinpath']}
		allpins.append(pinVal)
		
	return allpins

# Delete the Board
def deleteBoard(boardId):
	db = couch['pinterest']
	doc_id = 'boards'
	doc = db[doc_id]
	boards = doc['board']
	if boards.has_key(boardId):
		del boards[boardId]
		db.save(doc)
		return "Board deleted "
		
	else: 
		print 'in Else********************************************************************'
		return "error: unable to delete board (hint : the board id might not be present)"
		

# Get the information of a User
def getAllUserInfo(user_id):
	
	db = couch['pinterest']
	
	doc_id1 = 'UserInfo'
	doc_id2 = 'boards'
	doc1 = db[doc_id1]
	doc2 = db[doc_id2]
	user = doc1['user']
	board = doc2['board']
	boards = []
	print user_id
        for item1 in user:
		if item1['user_id'] == user_id:
			name = item1['name']
			item2 = item1['boardlist']
			for board1 in item2:
				item = board[board1]
				val = {'board_id': board1, 'board_name': item['board_name']}
				boards.append(val)
			value = [name , boards]
			return value 
	

		
if __name__ == '__main__':
    main()  

	
