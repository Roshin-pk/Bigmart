from django.db import models

# Create your models here.
class contact_db(models.Model):
    Name=models.CharField(max_length=100,blank=True,null=True)
    Email=models.EmailField(max_length=100,blank=True,null=True)
    Subject=models.CharField(max_length=150,blank=True,null=True)
    Message=models.CharField(max_length=250,blank=True,null=True)
class Register_db(models.Model):
    UserName=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    CPassword=models.CharField(max_length=100,null=True,blank=True)
