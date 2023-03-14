from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PasswordURL(models.Model):
    web_url = models.URLField(max_length=200)

    def __str__(self) -> str:
        return self.web_url

    class Meta:
        verbose_name = "Password URL"
        verbose_name_plural = "Password URLs"
    
class PasswordEntry(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    url = models.ForeignKey(PasswordURL, on_delete=models.PROTECT)
    userid_for_password = models.CharField(max_length=200) 
    password = models.CharField(max_length=50)
    note = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.userid_for_password} ({self.password})"
    
    class Meta:
        
        verbose_name = "Password Entry"
        verbose_name_plural = "Password Entries"
    
    
