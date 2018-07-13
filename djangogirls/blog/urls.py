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
identify the view, the name part also ties in the html to the url.py
just look at url(r'^post/new/$', views.post_new, name='post_new'), in our base.html
we define href which has  href="{% url 'post_new' %}", this post_new tells django which
view to go to in url.py 

dont forget, we need to add post_list to views.py

in url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
we use regular expression to create the url 


******
(?P<pk>\d+) means that Django will take everything that you place here 
and transfer it to a view as a variable called pk. 
(Note that this matches the name we gave the primary key variable back 
in blog/templates/blog/post_list.html!) 
\d also tells us that it can only be a digit, not a letter 
(so everything between 0 and 9).


'''
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
