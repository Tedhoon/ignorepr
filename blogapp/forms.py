from django import forms
from .models import Blog

class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog #이거 꼭 알려줘야함
        fields = ('title', 'body')