from django import forms

from .models import Post


'''
PostForm, as you probably suspect, is the name of our form. 
We need to tell Django that this form is a ModelForm 
(so Django will do some magic for us) – 
forms.ModelForm is responsible for that.

When we submit the form, we are brought back to the same view,
this is really good to know, because thats how we are going to implement search

'''

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)