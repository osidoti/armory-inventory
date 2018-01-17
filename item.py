"""
Orion Sidoti
item.py
Basic classes for items stored in a fencing armory
"""

"""
params:
int idNum: The number on the ID of the given item
int idYear: The last two digits of the year the item was first catalogued
str article: The type of item it is (i.e. Jacket, Plastron, etc.)
str condition: The condition of the item (ranging from excellent/new to very poor/broken)
str hand (default to None): If the item is tailored for right- or left-handedness, note it
bool fie (default to False): Boolean value for whether or not the item is marked as up to FIE competitive standards.
str comments (default to empty string): any comments about the specific item (i.e. condition notes, location in armory, etc.)
str user (default to None): Name of the fencer currently using the item

Function:
Generic superclass for a few shared types of functions and variables

Class Functions:
getArticle: returns str article property
getUser: returns str user property
addUser(newUser): replace str user property with str newUser
removeUser: empty the user property, return str, most recent user
getHand: returns str handedness of the item (None, if item has no handedness)
getCondition: returns str condition of the item
getNum: returns int idNum property
getYear: returns int idYear property
getLetter: returns str idLetter property
getID: returns str ID number for the item
updateCondition(condition): replaces current str condition property with new str condition parameter
isFie: returns boolean value of FIE competitive standard
getComments: returns str comments property
addComments(moreComments): appends str parameter moreComments on to str property comments after newline
replaceComments(replace): replaces str property comments with str replace parameter
delComments: removes all comments from item
areComments: returns boolean representation of presence of comments
newPrintForm(newP): replaces the int printForm property with int newP parameter
resetPrintForm: if property printForm != 10, sets it to 10. Returns 1 if changed, 0 if unchanged.
"""
class Item:
	def __init__(self, idNum, idYear, article, condition, hand=None, fie=False, comments="", user=None):
		self.idNum = idNum
		self.idYear = idYear
		self.article = article
		if article[0] == "M" or article[0] == "L":
			self.idLetter = article[0] + article[6]
		else:
			self.idLetter = article[0]
		self.user = user
		self.hand = hand
		self.condition = condition
		self.fie = fie
		self.comments = comments
		self.printForm = 10	# 20 for printing in block form, 21 for block form with comments, 11 for line form with comments, anything else for printing in line form (more options implementable later)
		
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
	
	def getNum(self):
		return self.idNum
	
	def getYear(self):
		return self.idYear
	
	def getLetter(self):
		return self.idLetter
	
	def getID(self):
		s = "OCFB" + str(self.idYear) + "-" + str(self.idLetter) + str(self.idNum)
		return s
	
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
		
	def newPrintForm(self, newP):
		self.printForm = newP
		
	def resetPrintForm(self):
		if self.printForm != 10:
			self.printForm = 10
			return 1
		else:
			return 0
		
		
"""
params:
int idNum: see superclass
int idYear: see superclass
str article: see superclass
str condition: see superclass
str size: The size of the piece of clothing (L, M, S, european or US measurements)
str gender (default to None): If the piece of clothing is tailored for a specific gender, note it
str hand (default to None): see superclass
bool fie (default to False): see superclass
str comments (default to empty string): see superclass
str user (default to None): see superclass

Function:
Class for clothing and protective type items (jackets, knickers, masks, etc.)
Contains a __str__ function for easy display with several options.
Inherits from Item class

Class Functions:
All superclass functions (Item)
getGender: retruns str gender the clothing item was tailored for
getSize: returns str size of the clothing item
__str__: converts item and properties to a printable format for a print statement. Has the following options (chosen by the int opt param, defaulting to 10):
	-(printForm=20) block print, where the item's properties are printed in block form with each property seaprated by a newline and title
	-(printForm=10) inline print, where the item's properties are printed without newline separation, but instead seaprated by " | "
	-(printForm=21) block print, with comments
	-(printForm=11) inline print, with comments
"""
class Clothing(Item):
	def __init__(self, idNum, idYear, article, condition, size, gender=None, hand=None, fie=False, comments="", user=None):
		Item.__init__(self, idNum, idYear, article, condition, hand, fie, comments, user)
		self.gender = gender
		self.size = size
		
	def getGender(self):
		return self.gender
	
	def getSize(self):
		return self.size

	def __str__(self):
		if self.printForm == 20:	# block print
			s = ("ID: " + self.getID() + "\nType: " + str(self.article) + "\nSize: " + str(self.size))
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
			s += "\n"
				
		elif self.printForm == 21:	# block print with comments
			s = ("ID: " + self.getID() + "\nType: " + str(self.article) + "\nSize: " + str(self.size))
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
			s += "\n"
				
		elif self.printForm == 11:	# line form with comments
			s = self.getID() + " | " + str(self.article) + " | " + str(self.size) + " | "
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
			s = self.getID() + " | " + str(self.article) + " | " + str(self.size) + " | "
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
int idNum: see superclass
int idYear: see superclass
str article: see superclass
str condition: see superclass
str hand: Note which hand the weapon is set up for (left or right)
str bellCond: The condition of the bell guard
str grip: The type of grip placed on the weapon
str wireCond: The condition of the wire laid in the blade (if applicable)
bool fie (default to False): see superclass
str comments (default to empty string): see superclass
str user (default to None): see superclass

Function:
Class for weapon type items (epees, foils, and sabres)
Contains a __str__ function for easy display with several options.
Inherits from Item class

Class Functions:
All superclass functions (Item)
getBellCond: returns str bellCond property, detailing the condition of the bell guard
getWireCond: returns str wireCond property, detailing the condition of the wire laid along the blade of the weapon
getGrip: returns str grip property, detailing the type of grip on the weapon
__str__: converts item and properties to a printable format for a print statement. Has the following options (chosen by the int opt param, defaulting to 10):
	-(printForm=20) block print, where the item's properties are printed in block form with each property seaprated by a newline and title
	-(printForm=10) inline print, where the item's properties are printed without newline separation, but instead seaprated by " | "
	-(printForm=21) block print, with comments
	-(printForm=11) inline print, with comments
"""
class Weapon(Item):
	def __init__(self, idNum, idYear, article, condition, hand, bellCond, grip, wireCond, fie=False, comments="", user=None):
		Item.__init__(self, idNum, idYear, article, condition, hand, fie, comments, user)
		self.bellCond = bellCond
		self.wireCond = wireCond
		self.grip = grip
		
	def getBellCond(self):
		return self.bellCond
	
	def getWireCond(self):
		return self.wireCond
	
	def getGrip(self):
		return self.grip
	
	def getID(self):
		s = "OC" + str(self.idYear) + "-W" + str(self.idNum)
		return s
	
	def __str__(self):
		if self.printForm == 20:	# block print
			s = ("ID: " + self.getID() + "\nType: " + str(self.article) + "\nHand: " + str(self.hand) + "\nGrip: " + str(self.grip) +
				"\nBlade Condition: " + str(self.condition) + "\nWire Condition: " + str(self.wireCond) + "\nBell Condition: " + str(self.bellCond))
			if self.user == None:
				s += "\nNot currently in use"
			else:
				s += "\nUser: " + str(self.user)
			if self.isFie():
				s += "\nFIE Quality"
			s += "\n"
				
		elif self.printForm == 21:		# block print with comments
			s = ("ID: " + self.getID() + "\nType: " + str(self.article) + "\nHand: " + str(self.hand) + "\nGrip: " + str(self.grip) +
				"\nBlade Condition: " + str(self.condition) + "\nWire Condition: " + str(self.wireCond) + "\nBell Condition: " + str(self.bellCond))
			if self.user == None:
				s += "\nNot currently in use"
			else:
				s += "\nUser: " + str(self.user)
			if self.isFie():
				s += "\nFIE Quality"
			if self.areComments():
				s += "\nComments: " + self.comments
			s += "\n"
				
		elif self.printForm == 11:		# line form with comments
			s = self.getID() + " | " + str(self.article) + " | " + str(self.hand) + " | " + str(self.grip) + " | " + self.condition + " | " + self.wireCond + " | " + self.bellCond
			if not (self.user == None):
				s += " | " + str(self.user)
			if self.isFie():
				s += " | FIE"
			if self.areComments():
				s += " | " + self.comments
				
		else:	# print in line form, for bulk items
			s = self.getID() + " | " + str(self.article) + " | " + str(self.hand) + " | " + str(self.grip) + " | " + self.condition + " | " + self.wireCond + " | " + self.bellCond
			if not (self.user == None):
				s += " | " + str(self.user)
			if self.isFie():
				s += " | FIE"
			
		return s
			
"""
params:
str name: name or type of item or tool or etc.
int quantity (defaults to 1): amount of specific item, if more than 1
str comments (default to empty string): any comments about the specific item (i.e. condition notes, location in armory, etc.)

Function:
Simple Class for miscellaneous other items found around the armory which it may be useful to catalog
Contains a __str__ function for easy display with several options:
	-block print, where the item's properties are printed in block form with each property seaprated by a newline and title
	-inline print, where the item's properties are printed without newline separation, but instead seaprated by " | "
	-block print, with comments
	-inline print, with comments
	
Class Functions:
getName: returns str name property, with name of the item
getQuantity: returns int quantity property, with quantity of the item
changeQuantity(newQ): replaces current int quantity property with int newQ parameter
addTo: increment quantity property
subFrom: decrement quantity property
getComments: returns str comments property
addComments(moreComments): appends str parameter moreComments on to str property comments after newline
replaceComments(replace): replaces str property comments with str replace parameter
delComments: removes all comments from item
areComments: returns boolean representation of presence of comments
newPrintForm(newP): replaces the int printForm property with int newP parameter
resetPrintForm: if property printForm != 10, sets it to 10. Returns 1 if changed, 0 if unchanged.
__str__: converts item and properties to a printable format for a print statement. Has the following options (chosen by the int opt param, defaulting to 10):
	-(printForm=20) block print, where the item's properties are printed in block form with each property seaprated by a newline and title
	-(printForm=10) inline print, where the item's properties are printed without newline separation, but instead seaprated by " | "
	-(printForm=21) block print, with comments
	-(printForm=11) inline print, with comments
"""
class MiscItem:
	def __init__(self, name, quantity=1, comments=""):
		self.name = name
		self.quantity = quantity
		self.comments = comments
		self.printForm = 10	# 20 for printing in block form, 21 for block form with comments, 11 for line form with comments, anything else for printing in line form (more options implementable later)
		
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
		
	def newPrintForm(self, newP):
		self.printForm = newP
		
	def resetPrintForm(self):
		if self.printForm != 10:
			self.printForm = 10
			return 1
		else:
			return 0
		
	def __str__(self):
		if self.printForm == 20:	# block print
			s = "Item: " + str(self.name) + "\nQuantity: " + str(self.quantity) + "\n"
				
		elif self.printForm == 21:		# block print with comments
			s = "Item: " + str(self.name) + "\nQuantity: " + str(self.quantity)
			if self.areComments():
				s += "\nComments: " + self.comments
			s += "\n"
				
		elif self.printForm == 11:		# line form with comments
			s = str(self.name) + " | " + str(self.quantity)
			if self.areComments():
				s += " | " + self.comments
				
		else:	# print in line form, for bulk items
			s = str(self.name) + " | " + str(self.quantity)
			
		return s
	
