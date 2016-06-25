from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.CharField(max_length = 20)
    title = models.CharField(max_length = 40)
    body = models.TextField(blank=True)

    
