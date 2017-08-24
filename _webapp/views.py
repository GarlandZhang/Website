from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def banana( request ):
	return render( request, '_webapp/basic.html' )
    
