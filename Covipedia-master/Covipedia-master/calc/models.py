from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class blog(models.Model):
    full_name = models.CharField(max_length=100)
    place = models.CharField(max_length=50) 
    resource = models.TextField() 
    count = models.IntegerField(null=True, blank=True, default=0)
    upchek = models.BooleanField(default=True)
    downchek = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name + '|' + self.place

    
    
    
