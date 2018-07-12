'''

Here we're importing Django's function url and all of our views from
the blog application

'''
from django.conf.urls import url
from . import views

'''

this is assigning a view called 'post_list' to the url that mathces r'^$'
^$ for regular expression means it is a beginging followed by an end,
meaning it is an empty url, hence sending it to 'http://127.0.0.1:8000/'
(essentially we are declaring our own pathing for urls, unlike what tomcat does
which already does it for you)

name="post_list" is also the name of the url that will be used to
identify the view

dont forget, we need to add post_list to views.py


'''
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
