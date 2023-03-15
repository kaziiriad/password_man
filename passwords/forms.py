from django import forms
from .models import PasswordEntry, PasswordURL

class PasswordEntryForm(forms.ModelForm):
    url = forms.ModelChoiceField(queryset=PasswordURL.objects.all())
    class Meta:
        model = PasswordEntry
        fields = ['user', 'url', 'userid_for_password', 'password', 'note']

class PasswordURLForm(forms.ModelForm):

    class Meta:
        model = PasswordURL
        fields = ['web_url']
