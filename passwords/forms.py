from django import forms
from .models import PasswordEntry, PasswordURL

class PasswordEntryForm(forms.ModelForm):
    class Meta:
        model = PasswordEntry
        exclude = ("user", "url",)
        
class PasswordURLForm(forms.ModelForm):

    class Meta:
        model = PasswordURL
        fields = ['web_url']
