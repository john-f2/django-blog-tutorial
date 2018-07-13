from django.shortcuts import render
#we need to import our model, the . infront of model indicates current directory
from .models import Post
from django.utils import timezone
#lets us render a 404 error
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
#redirect library
from django.shortcuts import redirect

# Create your views here.

'''

so essentially when a request is made to a url, it will go from
mysite.urls.py to blog.urls.py which then will call post_list()
which then will render the html to show

we are essentially directing the user to the according location 


how we can query for 1 item
Post.objects.get(pk=pk)
pk means primary key and the pk comes from url tranfer of pk 
so it goes HMTL -> Url.py -> view.py -> new hmtl 

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

def post_detail(request, pk):
    #either get the object and render the page or render a 404 error
    #remeber in the html we say {% url 'post_detail' pk=post.pk %}
    #thats how it knows that pk=pk because we get that object that was displayed
    #and assign pk to the object's primary key 
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# we need to incorperate in how to handle forms 
'''
in our view we have two separate situations to handle: first,
when we access the page for the first time and we want a blank form, 
and second, when we go back to the view with all form data we just typed. 
So we need to add a condition (we will use if for that):

in order to do a search, we probably need to rework this if statement
so that if there is a post then you do that search and then set the {objects_to_send}
to the query result which then will be displayed on the site

else would just be a full result set or no results 

'''
def post_new(request):
    #when we use forms, we are redirected back to the same page
    #thus requestion.method will be a post now if we submitted a form 
    if request.method == "POST":
        form = PostForm(request.POST)
    #checking if the form data submitted is valid and then commiting to the database 
        if form.is_valid():
            #we get the form data (.save is extended from a parent class, and we 
            #set commit to false because we want to add things first
            post = form.save(commit=False)

            #alittle testing for implementing search later!
            #forms is type PostForm from the forms.py
            #print(type(form))
            #this is how we can get the fields for the post
            #print(form.Meta.fields)

            #post is a post object 
            #print(type(post))
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #redirects when successful 
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})


#new function for post edits, it uses a different html 
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #this is for when we want to save the form
    if request.method == "POST":
        #this includes the instance of the post and sets it probably
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    #this is when we first open the form
    #having instance=post will set the forms 
    #REMEBER we are set to the post_edit.html and then when we hit send, are
    #are essentially sent back to this views.py (essentially if we didn't redirect
    #to anywhere else we would just back to the same page, the form enter doesnt go 
    #any where like how we do it in tomcat )        
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
