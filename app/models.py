from django.db import models

# Create your models here.
class College(models.Model):
    cname=models.CharField(max_length=100)
    cprincipal=models.CharField(max_length=100)
    clocation=models.CharField(max_length=100)
    
    