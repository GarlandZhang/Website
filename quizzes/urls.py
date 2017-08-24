from django.conf.urls import url, include
from . import views

app_name = 'quizzes'
urlpatterns = [
		url( r'^$', views.IndexView.as_view(), name = 'index'),
		url( r'^quiz/(?P<pk>[0-9]+)/$', views.StartView.as_view(), name = 'start' ),
		url( r'^quiz/(?P<pk>[0-9]+)/question/(?P<pk2>[0-9]+)/$', views.QAView.as_view(), name = 'qa' ), #the values in the url are the quiz and question ids, respectively.
]
 
