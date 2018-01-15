"""
Orion Sidoti
inventory.py
Main module for the Flaming Blades Inventory
"""

import item
import sys

# add a single item, taking user input for each property
def addItem():
	pass

# delete a single item, identified by ID (idNum, idYear, idLetter)
def delItem():
	pass

# search for all items matching search parameters (user input in function)
def search():
	pass

# load and initialize the inventory from a save file, if one exists
def loadInv():
	pass

# save the inventory to a file (consider finding a way to compress size to ensure compactness of the file)
def saveInv():
	pass

# keep the number of saves in check (maybe more features, like autosaving after x amount of time)
def maintainSaves():
	pass

# add items in a batch, likely from csv file
def addBatch():
	pass

# remove items in a batch, identified by ID (idNum, idYear, idLetter), likely read list either from text file (newline or csv) or user input, one after another
def delBatch():
	pass

# list all items of a given type (i.e. Jackets, Plastra, Foils, etc.) or whole inventory
def listItems():
	pass

def main():
	exStat = False
	
	print("Welcome to the Oberlin College Flaming Blades Armory Inventory System (OCFBAIS)!")
	
	# open and load most recent inventory file
	
	while not exStat:	# user input loop
		print("Options:\n1 - Add an Item\n2 - Remove an Item\n3 - Add a batch of Items\n4 - Remove a batch of Items\n5 - Search for an Item(s)\n6 - List Items\n7 - Save current inventory\n8 - Quit")	# detail available options for user
		c = int(input("\nPlease choose an option: "))
		if c == 1:	# add single item
			pass
		elif c == 2:	# remove single item
			pass
		elif c == 3:	# add batch of items
			pass
		elif c == 4:	# remove batch of items
			pass
		elif c == 5:	# search for item(s)
			pass
		elif c == 6:	# list items
			pass
		elif c == 7:	# save inventory
			pass
		elif c == 8:	# exit
			v = False
			if v == True:	# perform some check for unsaved changes to inventory
				qC = str(input("There are unsaved changes to the inventory, are you sure you want to quit (y/n)? "))
				if qC.lower() == "y":
					exStat = True
			else:
				exStat = True
		else:
			print("Sorry, that is not a valid option. Please try again.")
			
	print("Goodbye!")
	exit(0)

main()