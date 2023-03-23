from django.db import models

# Create your models here.
class signup(models.Model):
    
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=12)
    state=models.CharField(max_length=10)
    zip=models.IntegerField(max_length=10)