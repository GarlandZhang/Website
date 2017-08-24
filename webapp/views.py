from django.shortcuts import render
from django.http import HttpResponse

def index( request ):
    return HttpResponse( "<h2>WHAT IS THISSS</h2>" )
