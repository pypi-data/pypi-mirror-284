from pymongo import MongoClient
import os


class StaxDB:
	def __init__(self, uri):
		self.client = MongoClient(uri)
		self.db = self.client['db']
		self.clients = self.db['clients']
		self.users = self.db['users']
		self.projects = self.db['projects']
		self.tasks = self.db['tasks']
		self.teams = self.db['teams']
		self.plans = self.db['plans']
		self.automations = self.db['automations']
		self.templates = self.db['email_templates']
		self.contacts = self.db['contacts']
		self.fields = self.db['fields']
		

db = StaxDB(os.getenv('DB_URI', default="mongodb+srv://api:rCFojHAbs0o8MouH@cx-db.pewoo.mongodb.net/db"))