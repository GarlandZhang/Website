from django.conf.urls import url, include
from blog.models import Post #import the custom-made class Post from models
from . import views

urlpatterns = [

	url(r'^$', views.BlogListView.as_view() ), #template is blog/blog.html
		
	url(r'^(?P<pk>\d+)$', views.DetailView.as_view() ) #pk is primary key; the post id; \d means digit, with + sign being more than 1 digit is acceptable( this means 10, or 325 after blog/ is acceptable)
]
 