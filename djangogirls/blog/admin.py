from django.contrib import admin
from .models import Post

# Register your models here.
#remember you need to import the model from model.py 

#this registers our model post 
admin.site.register(Post)

