from django import forms
from django.http import HttpRequest as request
#from django.contrib.auth.middleware.AuthenticationMiddleware import user

from .models import Category, Entry


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    #category = forms.ModelChoiceField(data=Category.objects.filter(owner=request.user)) #or should it be (queryset= ) or since it's the only required argument we may not even need to specify that?)

    class Meta:
        model = Entry
        fields = ['text', 'category', 'tags', 'resource_type', 'author', 'preferred_format', 'recommender', 'location', 'status', 'notes']
        #labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80}), 'notes': forms.Textarea(attrs={'cols':80})}
