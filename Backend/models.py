from django.db import models

# Create your models here.

class category_db(models.Model):
    CategoryName=models.CharField(max_length=100,blank=True,null=True)
    Description=models.CharField(max_length=200,blank=True,null=True)
    CategoryPhoto=models.ImageField(upload_to="category_image", blank=True, null=True)
class Product_db(models.Model):
    CategorySelect=models.CharField(max_length=100,blank=True,null=True)
    ProductName=models.CharField(max_length=100,blank=True,null=True)
    ProductPrice=models.IntegerField(blank=True,null=True)
    Description=models.CharField(max_length=100,blank=True,null=True)
    ProductPhoto=models.ImageField(upload_to="category_image", blank=True, null=True)