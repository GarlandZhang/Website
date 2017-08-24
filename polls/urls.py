from django.conf.urls import url, include
from . import views

app_name = 'polls'
urlpatterns = [
	#To get from a URL to a view, Django uses what are known as ‘URLconfs’. 
	#A URLconf maps URL patterns (described as regular expressions) to views.
	#ex: if url is .../34, this matches details view, which runs the url line
	#ex: /polls/
	url( r'^$', views.IndexView.as_view(), name = 'index' ),
	
	#ex: /polls/pineapples/5/
	url( r'^pineapples/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail' ),
	
	#exL /polls/5/results
	url( r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name = 'results' ),
	
	#ex: /polls/5/vote/
	url( r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = 'vote'),
]