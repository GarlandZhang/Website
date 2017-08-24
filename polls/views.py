from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

#all fields in the classes are SPECIFIC

class IndexView( generic.ListView ):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list' #latest_question_list is called in index.html
	
	def get_queryset(self): #this is overriden
		return Question.objects.order_by('-pub_date')[:25] #returns last 5 questions (minus sign means most recent)
		

#By default, the DetailView generic view uses a template 
#called <app name>/<model name>_detail.html. In our case, 
#it would use the template "polls/question_detail.html".

class DetailView(generic.DetailView): #DetailView is a premade class; just so happens we called ours DetailView too
	model = Question
	template_name = 'polls/detail.html' #overrides default template name: polls/question_detail.html
	
class ResultsView( generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
	
"""
# Create your views here.
def index( request ):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	
	#output = ', '.join([q.question_text for q in latest_question_list])
	#return HttpResponse( output ) #...OR
	
	context = {'latest_question_list': latest_question_list}
	
	#template = loader.get_template( 'polls/index.html' )
	#return HttpResponse( template.render( context, request ) )#....OR
	
	
	return render( request, 'polls/index.html', context ) #recall: 3rd parameter is dictionary
	
	
def detail( request, question_id ):

	#return HttpResponse( "You're looking at question %s." % question_id )
	
	question = get_object_or_404( Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})
	
def results( request, question_id ):
	question = get_object_or_404( Question, pk = question_id)
	return render(request, 'polls/results.html', {'question': question} )
	
"""

def vote( request, question_id ):
	question = get_object_or_404( Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get( pk = request.POST['choice']) #gets id since value of 'choice' was choice.id
	
	except( KeyError, Choice.DoesNotExist):
		#Redisplay the question voting form.
		return render( request, 'polls/detail.html', #shouldn't we make it dynamic?
		{
			'question': question,
			'error_message': "YOU DIDN'T CHOOSE. YOU DIE.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		
		return HttpResponseRedirect( reverse( 'polls:results', args = (question.id,))) #always return an
#		httpresponseredirect after successfully handling POST data to prevent data from being posted twice
#	    if user hits back button