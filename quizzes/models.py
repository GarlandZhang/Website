from django.db import models

# Create your models here.
class Quiz( models.Model ):
	quiz_text = models.CharField( max_length = 200 )
	pub_date = models.DateTimeField( 'date published' )
	
	def __str__(self):
		return self.quiz_text	
	
	def was_published_recently( self ):
		return self.pub_date >= timezone.now() -datetime.timedelta(days=1)
		
class Question( models.Model ):
	question_text = models.CharField( max_length = 200 )
	quiz = models.ForeignKey( Quiz, on_delete = models.CASCADE )
	
	def __str__(self):
		return self.question_text

class Answer(models.Model):
	answer_text = models.CharField( max_length = 200 )
	question = models.ForeignKey( Question, on_delete = models.CASCADE )
	isCorrect = models.BooleanField( default = False )
	
	def __str__( self):
		return self.answer_text
