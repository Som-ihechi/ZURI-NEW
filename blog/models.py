from cgitb import text
from webbrowser import get
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
#author = models.ForeignKey()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()