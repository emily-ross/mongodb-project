import pymongo
import pprint

from pymongo import MongoClient

client = MongoClient()
db = client.Broadway
collection = db.musicals


while True:
	print "What category would you like to search: a title, main_character, playwright, instrument, opening, voca_part, vocal_range, age, or gender?"
	category = raw_input()
	print "Enter your", category, "here."
	term = raw_input()

	pp = pprint.PrettyPrinter(indent = 4)
	for result in collection.find({category: term}):
	pp.pprint(result)
	