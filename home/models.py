from datetime import datetime
from os import name
from django.db import models

# Create your models here.
class feeedback(models.Model):
    name = models.CharField(max_length=25)
    feedback = models.TextField(max_length=12222)
    datetime = models.DateTimeField()
