from django.shortcuts import render
#we need to import our model, the . infront of model indicates current directory
from .models import Post
from django.utils import timezone

# Create your views here.

'''

so essentially when a request is made to a url, it will go from
mysite.urls.py to blog.urls.py which then will call post_list()
which then will render the html to show

we are essentially directing the user to the according location 

'''
def post_list(request):

    #all the queries we were doing from our shell, we can call them in the views
    #python is pretty nice, since we dont need to worry about the typing
    #we get all the objects based on publish_date and order them by publishdate 
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


    '''
    The last parameter, {}, is a place in which we can add some things for
    the template to use. We need to give them names
    (we will stick to 'posts' right now). :)
    It should look like this: {'posts': posts}.
    Please note that the part before :
    is a string; you need to wrap it with quotes: ''.
    '''

    #to send the object data to the template (html) we need to fill in the {}
    #parameter we are essentially passing in a dictionary with key and object
    #(where the object is the result set)
    return render(request, 'blog/post_list.html', {'posts' : posts})
