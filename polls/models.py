import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question( models.Model ):
	question_text = models.CharField( max_length = 200 )
	pub_date = models.DateTimeField( 'date published' )
	
	def __str__( self):
		return self.question_text
		
	def was_published_recently( self ):
		return self.pub_date >= timezone.now() - datetime.timedelta( days = 1)
	
class Choice( models.Model ):
	question = models.ForeignKey( Question, on_delete = models.CASCADE ) #linked to a single question
	choice_text = models.CharField( max_length = 200 )
	votes = models.IntegerField( default = 0 )
	
	def __str__(self):
		return self.choice_text
	
#three-step guide to making model changes: *migrations are a history of the previous database; migrate updates;
# *sqlmigrate DOES NOT run migrations, it just suggests what it thinks is required
#1. Change your models (in models.py).
#2. Run python manage.py makemigrations to create migrations for those changes
#3. Run python manage.py migrate to apply those changes to the database.