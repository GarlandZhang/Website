from django.db import models

class Post( models.Model ): #each class is a table in the database (database IS this file)
	#these are columns in the table
	title = models.CharField( max_length = 140 ) #like textfield but less space
	body = models.TextField()
	date = models.DateTimeField()

	#def is a method
	def __str__(self): #self refers to the object of the class
		return self.title