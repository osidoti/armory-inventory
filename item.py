"""
Orion Sidoti
item.py
Basic classes for items stored in a fencing armory
"""

"""
params:
int idNum
str article
str condition
str hand (default to None)
bool fie (default to False)
str comments (default to empty string)
str user (default to None)

Function:
Generic superclass for a few shared types of functions and variables
"""
class Item:
	def __init__(self, idNum, article, condition, hand=None, fie=False, comments="", user=None):
		self.idNum = idNum
		self.article = article
		self.user = user
		self.hand = hand
		self.condition = condition
		self.fie = fie
		self.comments = comments
		
	def getArticle(self):
		return self.article
	
	def getUser(self):
		return self.user
	
	def addUser(self, newUser):
		self.user = newUser
	
	def removeUser(self):
		u = self.user
		self.user = None
		return u
	
	def getHand(self):
		return self.hand
	
	def getCondition(self):
		return self.condition
	
	def getID(self):
		return self.idNum
	
	def updateCondition(self, condition):
		self.condition=condition
		
	def isFie(self):
		return self.fie
	
	def getComments(self):
		return self.comments
	
	def addComments(self, moreComments):
		if self.areComments():
			self.comments += "\n" + moreComments
		else:
			self.comments = moreComments
		
	def replaceComments(self, replace):
		self.comments = replace
		
	def delComments(self):
		self.comments = ""
	
	def areComments(self):
		if self.comments == "":
			return False
		else:
			return True
		
"""
params:
int idNum
str article
str condition
str size
str gender (default to None)
str hand (default to None)
bool fie (default to False)
str comments (default to empty string)
str user (default to None)

Function:
Class for clothing and protective type items (jackets, knickers, masks, etc.)
Contains a __str__ function for easy display with several options.
Inherits from Item class
"""
class Clothing(Item):
	def __init__(self, idNum, article, condition, size, gender=None, hand=None, fie=False, comments="", user=None):
		Item.__init__(idNum, article, condition, hand, fie, comments, user)
		self.gender = gender
		self.size = size
		
	def getGender(self):
		return self.gender
	
	def getSize(self):
		return self.size

	def __str__(self, opt=10):	# 20 for printing in block form, 21 for block form with comments, 11 for line form with comments, anything else for printing in line form (more options implementable later)
		if opt == 20:	# block print
			s = ("ID: " + str(self.idNum) + "\nType: " + str(self.article) + "\nSize: " + str(self.size))
			if not (self.gender == None):
				s += "\nGender: " + str(self.gender)
			if not (self.hand == None):
				s += "\nHand: " + str(self.hand)
			s += "\nCondition: " + str(self.condition)
			if self.user == None:
				s += "\nNot currently in use"
			else:
				s += "\nUser: " + str(self.user)
			if self.isFie():
				s += "\nFIE Quality"
				
		elif opt == 21:	# block print with comments
			s = ("ID: " + str(self.idNum) + "\nType: " + str(self.article) + "\nSize: " + str(self.size))
			if not (self.gender == None):
				s += "\nGender: " + str(self.gender)
			if not (self.hand == None):
				s += "\nHand: " + str(self.hand)
			s += "\nCondition: " + str(self.condition)
			if self.user == None:
				s += "\nNot currently in use"
			else:
				s += "\nUser: " + str(self.user)
			if self.isFie():
				s += "\nFIE Quality"
			if self.areComments():
				s += "\nComments: " + self.comments
				
		elif opt == 11:	# line form with comments
			s = str(self.idNum) + " | " + str(self.article) + " | " + str(self.size) + " | "
			if not (self.gender == None):
				s += str(self.gender) + " | "
			if not (self.hand == None):
				s += str(self.hand) + " | "
			s += str(self.condition)
			if not (self.user == None):
				s += " | " + str(self.user)
			if self.isFie():
				s += " | FIE"
			if self.areComments():
				s += " | " + self.comments
				
		else:	# print in line form, for bulk items
			s = str(self.idNum) + " | " + str(self.article) + " | " + str(self.size) + " | "
			if not (self.gender == None):
				s += str(self.gender) + " | "
			if not (self.hand == None):
				s += str(self.hand) + " | "
			s += str(self.condition)
			if not (self.user == None):
				s += " | " + str(self.user)
			if self.isFie():
				s += " | FIE"
				
		return s
			
"""
params:
int idNum
str article
str condition
str hand
str bellCond
str wireCond
str grip
bool fie (default to False)
str comments (default to empty string)
str user (default to None)

Function:
Class for weapon type items (epees, foils, and sabres)
Contains a __str__ function for easy display with several options.
Inherits from Item class
"""
class Weapon(Item):
	def __init__(self, idNum, article, condition, hand, bellCond, wireCond, grip, fie=False, comments="", user=None):
		Item.__init__(idNum, article, condition, hand, fie, comments, user)
		self.bellCond = bellCond
		self.wireCond = wireCond
		self.grip = grip
		
	def getBellCond(self):
		return self.bellCond
	
	def getWireCond(self):
		return self.wireCond
	
	def getGrip(self):
		return self.grip
	
	def __str__(self, opt=10):	# 20 for printing in block form, 21 for block form with comments, 11 for line form with comments, anything else for printing in line form (more options implementable later)
		if opt == 20:	# block print
			s = ("ID: " + str(self.idNum) + "\nType: " + str(self.article) + "\nHand: " + str(self.hand) + "\nGrip: " + str(self.grip) +
				"\nBlade Condition: " + str(self.condition) + "\nWire Condition: " + str(self.wireCond) + "\nBell Condition: " + str(self.bellCond))
			if self.user == None:
				s += "\nNot currently in use"
			else:
				s += "\nUser: " + str(self.user)
			if self.isFie():
				s += "\nFIE Quality"
				
		elif opt == 21:		# block print with comments
			s = ("ID: " + str(self.idNum) + "\nType: " + str(self.article) + "\nHand: " + str(self.hand) + "\nGrip: " + str(self.grip) +
				"\nBlade Condition: " + str(self.condition) + "\nWire Condition: " + str(self.wireCond) + "\nBell Condition: " + str(self.bellCond))
			if self.user == None:
				s += "\nNot currently in use"
			else:
				s += "\nUser: " + str(self.user)
			if self.isFie():
				s += "\nFIE Quality"
			if self.areComments():
				s += "\nComments: " + self.comments
				
		elif opt == 11:		# line form with comments
			s = str(self.idNum) + " | " + str(self.article) + " | " + str(self.hand) + " | " + str(self.grip) + " | " + self.condition + " | " + self.wireCond + " | " + self.bellCond
			if not (self.user == None):
				s += " | " + str(self.user)
			if self.isFie():
				s += " | FIE"
			if self.areComments():
				s += " | " + self.comments
				
		else:	# print in line form, for bulk items
			s = str(self.idNum) + " | " + str(self.article) + " | " + str(self.hand) + " | " + str(self.grip) + " | " + self.condition + " | " + self.wireCond + " | " + self.bellCond
			if not (self.user == None):
				s += " | " + str(self.user)
			if self.isFie():
				s += " | FIE"
			
		return s
			
"""
params:
str name
int quantity
str comments (default to empty string)

Function:
Simple Class for miscellaneous other items found around the armory which it may be useful to catalog
Contains a __str__ function for easy display with several options.
"""
class MiscItem:
	def __init__(self, name, quantity, comments=""):
		self.name = name
		self.quantity = quantity
		self.comments = comments
		
	def getName(self):
		return self.name
	
	def getQuantity(self):
		return self.quantity
	
	def changeQuantity(self, newQ):
		self.quantity = newQ
		
	def addTo(self):
		self.quantity += 1
		
	def subFrom(self):
		self.quantity -= 1
		
	def getComments(self):
		return self.comments
	
	def addComments(self, moreComments):
		if self.areComments():
			self.comments += "\n" + moreComments
		else:
			self.comments = moreComments
		
	def replaceComments(self, replace):
		self.comments = replace
		
	def delComments(self):
		self.comments = ""
	
	def areComments(self):
		if self.comments == "":
			return False
		else:
			return True
		
	def __str__(self, opt=10):	# 20 for printing in block form, 21 for block form with comments, 11 for line form with comments, anything else for printing in line form (more options implementable later)
		if opt == 20:	# block print
			s = "Item: " + str(self.name) + "\nQuantity: " + str(self.quantity)
				
		elif opt == 21:		# block print with comments
			s = "Item: " + str(self.name) + "\nQuantity: " + str(self.quantity)
			if self.areComments():
				s += "\nComments: " + self.comments
				
		elif opt == 11:		# line form with comments
			s = str(self.name) + " | " + str(self.quantity)
			if self.areComments():
				s += " | " + self.comments
				
		else:	# print in line form, for bulk items
			s = str(self.name) + " | " + str(self.quantity)
			
		return s
	
