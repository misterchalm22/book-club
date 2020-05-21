"""This submodule contains form fields for use in the book-club project."""
from django import forms
from django.db import models


class NewReview(forms.Form):
    """Form fields for a book review."""
    
    title = forms.CharField(label='Book Name', max_length=200)
    author = forms.CharField(label='Author', max_length=200)
    illustrator = forms.CharField(
    	label='Book Name', max_length=200, required=False)
    funniest = forms.CharField(	
    	widget=forms.Textarea,
    	max_length=500,
    	label='Funniest part of the book', required=False)
    exciting = forms.CharField(
    	widget=forms.Textarea, max_length=500, 
    	label='Most exciting part of the book', required=False)
    saddest = forms.CharField(
    	widget=forms.Textarea, max_length=500,
    	label='Saddest part of the book', required=False)
    happiest = forms.CharField(
    	widget=forms.Textarea, max_length=500, 
    	label='Happiest part of the book', required=False)
    comments = forms.CharField(
        widget=forms.Textarea, max_length=1500,
        label=str("Any other comments? Think about how you liked the writing, "
        		  + "the characters, or anything else in the book. Or what you "
        		  + "didn't like!"),
        required=False)

# Consider rendering like this:
# <form action="/contact/" method="post">
#   {{ form.book_name }}
#   <div class="fieldWrapper">
#     {{ form.author }}
#     {{ form.illustrator }}
#     {{ form.funniest }}
#	  {{ form.etcetera }}
#   </div>
# </form>