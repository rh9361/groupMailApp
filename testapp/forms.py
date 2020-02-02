from django import forms
from . models import Student,Group


class PostForm(forms.ModelForm):


    class Meta():

        fields = ('name','email','groupName')

        widgets = {
            'name':forms.TextInput(attrs={'class':'textinputclass'}),
            'email':forms.TextInput(attrs={'class':'textinputclass'}),
            'groupName':forms.TextInput(attrs={'class':'textinputclass'}),

        }
