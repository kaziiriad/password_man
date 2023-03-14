from django.contrib import admin
from . import models
# Register your models here.
my_models = [models.PasswordURL, models.PasswordEntry]
admin.site.register(my_models)