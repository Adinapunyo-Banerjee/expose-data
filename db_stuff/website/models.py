from django.db import models

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField

# In SQL we would define the type of data in the table here, Integer, Text, Null, whatever. We do the same here! A table named "Member" is created here.