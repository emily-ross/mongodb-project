import pymongo
import pprint

from pymongo import MongoClient

client = MongoClient()
db = client.Broadway
collection = db.musicals

def get_user_input():
	show = {}

	print "Please enter the title of a Broadway musical."
	title = raw_input()
	show["title"] = title

	print "Please enter the composer(s), lyricsist(s), and book writer(s) of", title, "with commas in between."
	writers = raw_input()
	show["playwrights"] = writers.split(", ")

	print "Please enter the year that", title, "opened on Broadway. If", title, "had a revival (or multiple), enter the opening years in order with commas in between."
	opening_year = raw_input()
	if opening_year.find(",") == True:
		show["openings"] = [opening_year.split(", ")]
	else:
		show["opening"] = opening_year

	print "Please enter the instruments for which", title, "is scored with commas in between."
	instruments = raw_input()
	show["instruments"] = instruments.split(", ")

	print "How many main characters does", title, "have?"
	character_num = int(raw_input())
	n = 0
	show["main_characters"] = []
	
	while n < character_num:
		if n == 0:
			print "Please enter the name of the first main character in", title,"."
		else:
			print "Please enter the name of the next main character."
		main_character = raw_input()
		character = {}
		character["name"] = main_character

		print "What vocal part is", main_character,"?"
		vox = raw_input()
		character["vocal_part"] = vox

		print "What is", main_character,"'s range?"
		vrange = raw_input()
		character["vocal_range"] = vrange

		print "How old is", main_character,"?"
		age = raw_input()
		character["age"] = age

		print "What gender is", main_character,"?"
		gender = raw_input()
		character["gender"] = gender
		show["main_characters"].append(character)
		n = n + 1
	return show

doc = get_user_input()
pp = pprint.PrettyPrinter(indent = 4)
pp.pprint(doc)
collection.insert(doc)