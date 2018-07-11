from django.db import models


# Create your models here.
#models are essentially the objects that we want to represent our data
#we create the models first then run the django scripts so that it will create 
#the according table from the model, sqlite is default in django 

class Post(models.Model):
        #essentially our member variables will be our columns on the table 
        #these types are the same as the types in sqlite 
        author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


	#publish sets the publish date to the time now 
        def publish(self):
                #both these functions are from django's libraries 
                self.published_date = timezone.now()
                #save seems to be a form of an update method 
                self.save()
                
        #returns the title 
        def __str__(self):
                return self.title
