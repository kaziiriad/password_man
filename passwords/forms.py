from django import forms
from .models import PasswordEntry, PasswordURL

class PasswordEntryForm(forms.ModelForm):
    url = forms.ModelChoiceField(queryset=PasswordURL.objects.all())
    class Meta:
        model = PasswordEntry
        field = ['user', 'url', 'user_id', 'password', 'note']
        