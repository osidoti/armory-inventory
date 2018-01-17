"""
Orion Sidoti
inventory.py
Main module for the Flaming Blades Inventory
"""

import item
import sys
import time
import os
import errno

# add a single item, taking user input for each property
def addItem(invn):
	print("Type of item:\n1 - Clothing or Protective Gear\n2 - Weapon\n3 - Other (tools, expendable goods, etc.)")
	c = int(input("\nPlease choose the type of the item: "))
	if c == 1:	# clothing, items
		idNum = int(input("ID Number: "))
		idYear = int(input("Last two digits of catalogue year: "))
		article = str(input("Article of clothing ('Jacket', 'Lame, Foil', 'Knickers', etc.): "))
		size = str(input("Size: "))
		condition = str(input("Condition: "))
		c = str(input("Are there additional traits that you would like to note (y/n)? "))
		if c.lower() == "y":
			c = str(input("Is the " + article + " tailored for a specific gender (y/n)? "))
			if c.lower() == "y":
				gender = str(input("Gender: "))
			else:
				gender = None
			c = str(input("Is the " + article + " tailored for specific handedness (y/n)? "))
			if c.lower() == "y":
				hand = str(input("Hand: "))
			else:
				hand = None
			c = str(input("Is the " + article + " FIE quality (y/n)? "))
			if c.lower() == "y":
				fie = True
			else:
				fie = False
			c = str(input("Is the " + article + " in use or reserved for a specific fencer (y/n)? "))
			if c.lower() == "y":
				user = str(input("Fencer: "))
			else:
				user = None
			c = str(input("Do you have additional comments for this " + article + " (y/n)? "))
			if c.lower() == "y":
				comments = str(input("Comments: "))
			else:
				comments = ""
			newI = item.Clothing(idNum, idYear, article, condition, size, gender, hand, fie, comments, user)
		else:
			newI = item.Clothing(idNum, idYear, article, condition, size)
			
		invn['items'].append(newI)
		
	elif c == 2:	# weapon, items
		idNum = int(input("ID Number: "))
		idYear = int(input("Last two digits of catalogue year: "))
		article = str(input("Type of weapon (Foil, Epee, Sabre): "))
		condition = str(input("Condition: "))
		hand = str(input("Handedness of the " + article + ": "))
		bellCond = str(input("Bell Guard Condition: "))
		grip = str(input("Grip: "))
		if article.lower() != "sabre":
			wireCond = str(input("Condition of the wire(s): "))
		else:
			wireCond = "N/A"
		c = str(input("Are there additional traits that you would like to note (y/n)? "))
		if c.lower() == "y":
			c = str(input("Is the " + article + " FIE quality (y/n)? "))
			if c.lower() == "y":
				fie = True
			else:
				fie = False
			c = str(input("Is the " + article + " in use or reserved for a specific fencer (y/n)? "))
			if c.lower() == "y":
				user = str(input("Fencer: "))
			else:
				user = None
			c = str(input("Do you have additional comments for this " + article + " (y/n)? "))
			if c.lower() == "y":
				comments = str(input("Comments: "))
			else:
				comments = ""
			newI = item.Weapon(idNum, idYear, article, condition, hand, bellCond, grip, wireCond, fie, comments, user)
		else:
			newI = item.Weapon(idNum, idYear, article, condition, hand, bellCond, grip, wireCond)
			
		invn['items'].append(newI)
	elif c == 3:	# miscItem, misc
		name = str(input("Name the item (wire, saw, etc.): "))
		c = str(input("Are there more than 1 of this item or do you have comments for this item (y/n)? "))
		if c.lower() == "y":
			quantity = int(input("Quantity of the item: "))
			c = str(input("Do you have comments (y/n)? "))
			if c.lower() == "y":
				comments = str(input("Comments: "))
			else:
				comments = ""
			newM = item.MiscItem(name, quantity, comments)
		else:
			newM = item.MiscItem(name)
		
		invn['misc'].append(newM)
		
	else:
		pass	# substitute with error or loop until proper choice is picked

# delete a single item, identified by ID (idNum, idYear, idLetter)
def delItem(invn):
	pass

# search for all items matching search parameters (internal, system-use, helper function)
def helpSearch(invn):
	pass

# search for all items matching search parameters (user input in function)
def userSearch(invn):
	# choose search parameters
	s_param = 0
	in_use = False	# check if user wants to find clothes in use or not in use
	res_list = []
	if s_param == 0:	# idNum search
		# choose search number, search year (possibly parse text input of full id)
		s_num = 0
		s_year = 0
		s_letter = "A"
		for i in invn["items"]:
			if (i.getNum() == s_num) and (i.getYear() == s_year) and (i.getLetter() == s_letter):
				res_list.append(i)
	elif s_param == 1:	# size search
		# check if gender included
		pass

# load and initialize the inventory from a save file, if one exists
def loadInv(invn):
	pass

# save the inventory to a file (consider finding a way to compress size to ensure compactness of the file)
def saveInv(invn):
	fName = strftime("invn_%m-%d-%y_%X.sav")
	return 0

# keep the number of saves in check (maybe more features, like autosaving after x amount of time)
def maintainSaves(invn):
	pass

# add items in a batch, likely from csv file
def addBatch(invn):
	pass

# remove items in a batch, identified by ID (idNum, idYear, idLetter), likely read list either from text file (newline or csv) or user input, one after another
def delBatch(invn):
	pass

# list all items of a given type (i.e. Jackets, Plastra, Foils, etc.) or whole inventory
def listItems(invn):
	pass

# generate the next available ID number for a new item to add to the inventory (this will likely be a very involved method)
def genNextID(invn, article):
	pass

def main():
	exStat = False
	
	print("\nWelcome to the Oberlin College Flaming Blades Armory Inventory System (OCFBAIS)!\n")
	
	invn = {'items':[], 'misc':[]}	# each list in dictionary holds only corresponding type of object (from item.py)
	
	# open and load most recent inventory file
	
	while not exStat:	# user input loop
		print("\nOptions:\n1 - Add an Item\n2 - Remove an Item\n3 - Add a batch of Items\n4 - Remove a batch of Items\n5 - Search for an Item(s)\n6 - List Items\n7 - Save current inventory\n8 - Quit")	# detail available options for user
		c = int(input("\nPlease choose an option: "))
		if c == 1:	# add single item
			print("\nADD ITEM\n")
			addItem(invn)
		elif c == 2:	# remove single item
			print("\nREMOVE ITEM\n")
			delItem(invn)
		elif c == 3:	# add batch of items
			print("\nADD BATCH ITEMS\n")
			addBatch(invn)
		elif c == 4:	# remove batch of items
			print("\nREMOVE BATCH ITEMS\n")
			delBatch(invn)
		elif c == 5:	# search for item(s)
			print("\nSEARCH\n")
			userSearch(invn)
		elif c == 6:	# list items
			print("\nLIST ITEMS\n")
			listItems(invn)
		elif c == 7:	# save inventory
			print("\nSaving current inventory...\n")
			savStat = saveInv(invn)
			if savStat == 0:
				print("Inventory saved successfully!")
			else:	# include possible error messages with return values in saveInv() method
				print("Something went wrong, save aborted.")
		elif c == 8:	# exit
			v = False
			if v == True:	# perform some check for unsaved changes to inventory
				qC = str(input("There are unsaved changes to the inventory, are you sure you want to quit (y/n)? "))
				if qC.lower() == "y":
					exStat = True
			else:
				exStat = True
		else:
			print("\nSorry, that is not a valid option. Please try again.")
			time.sleep(1)
			
	print("Goodbye!")
	exit(0)

main()