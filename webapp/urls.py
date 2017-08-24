from django.conf.urls import url
from . import views #period means importing from the current package;
                    #this makes the code DYNAMIC

urlpatterns = [
    url(r'^$', views.index, name = 'index' ) ] #upon going to url, views.index is called
                                               #name is namespace; currently redundant but preliminary
