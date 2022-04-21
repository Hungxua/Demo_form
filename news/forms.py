from django import  forms
from .models import Post

class Post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at']

class Email_Form(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'title'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    cc = forms.BooleanField(required=False)