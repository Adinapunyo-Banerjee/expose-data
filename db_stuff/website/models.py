from django.db import models

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()

# In SQL we would define the type of data in the table here, Integer, Text, Null, whatever.
# We do the same here! A table named "Member" is created here.

    def __str__(self):
        return self.fname + ' ' + self.lname + ' - ' + self.email

# Doing this will allow the table in admin panel to not show "Member Model (i)" and instead give their name and email! (Changes object display name)

# This __str__ function returns the same thing when we are trying to access it in views.py