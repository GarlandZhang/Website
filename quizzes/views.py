from django.views import generic
from .models import Quiz, Question, Answer 

class IndexView( generic.ListView ):
	template_name = 'quizzes/home.html'
	context_object_name = 'latest_quizzes_list'
	
	def get_queryset(self):
		return Quiz.objects.order_by('-pub_date')[:25]
	
class StartView( generic.DetailView ): #unnecessary class? could fancy it up more
	model = Quiz
	template_name = 'quizzes/start.html'
	
class QAView ( generic.DetailView ):
	model = Question
	template_name = 'quizzes/qa.html'