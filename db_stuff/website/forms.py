from django import forms
from .models import Member

class Memberform(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['fname', 'lname', 'email', 'passwd', 'age']

# Making this forms.py file and doing this will tell django what the model of the form is and how to put new data in the form!