from django import forms
from .models import PasswordEntry, PasswordURL

class PasswordEntryForm(forms.ModelForm):
    class Meta:
        model = PasswordEntry
        fields = ["user", "url", "userid_for_password", "password", "note"]
        exclude = ("user", "url")

class PasswordURLForm(forms.ModelForm):
    class Meta:
        model = PasswordURL
        fields = ['web_url']
