#typically when you use views.py file, in your defs, you will most likely be returning a render
from django.shortcuts import render

def index( request ):
	return render( request, 'personal/home.html' ) #2nd paramter is the template to use 

def contact( request ):
	return render( request, 'personal/basic.html', {'contentSSS' : [ 'If you wood like to contact me, don\'t. Please jump off a bridge instead, thanks...garland._zhang@hotmail.com' ] } ) #3rd parameter is dictionary
	#contentSSS is the dictionary variable which is referenced in basic.html