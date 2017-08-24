from django.shortcuts import render
from django.views import generic
from .models import Post

class BlogListView( generic.ListView ):
	template_name = 'blog/blog.html'
	context_object_name = 'object_list'
	
	def get_queryset(self):
		return Post.objects.all().order_by( "-date" )[:25]

# Create your views here.
class DetailView( generic.DetailView ):
	model = Post
	template_name = 'blog/post.html'