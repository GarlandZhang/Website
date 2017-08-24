"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    #^ means beginng of string; $ means end
    #since there is no $, anything following 'admin/' will lead to same link
    #*Note: page 404 may occur if url in browser does not include admin/ or webapp/
    url(r'^admin/', admin.site.urls),
 #   url(r'^webapp/', include( 'webapp.urls' ) ), #second paramter appends
                                                #the 'include' function must be imported
    url(r'^_webapp/', include( '_webapp.urls' ) ) ,
	url(r'^', include( 'personal.urls' ) ) ,
	url(r'blog/', include( 'blog.urls' ) ),
	url(r'^polls/', include( 'polls.urls' ) ),
	url(r'^quizzes/', include( 'quizzes.urls' ) ),
]
 
