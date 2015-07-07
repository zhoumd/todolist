from django.db import models

# Create your models here.
class Mydata(models.Model):
    title=models.CharField(max_length=100,null=True,default='aaa')
