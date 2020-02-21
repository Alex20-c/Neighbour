from django import forms
from .models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','location']
        
class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['user','location']