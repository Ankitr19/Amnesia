from django.db import models
from django.utils import timezone

class User(models.Model):
    phone_number = models.CharField( max_length=15 )
    created 	 = models.DateTimeField(auto_now_add=True)

class Error(models.Model):
    user        = models.ForeignKey( User, on_delete=models.CASCADE )
    start_time  = models.DateTimeField(auto_now_add=True, blank=True)