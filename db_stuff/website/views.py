from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Member
from .forms import Memberform

# Create your views here.

def home(request):
    all_members = Member.objects.all
    return render(request, 'index.html', {'all':all_members})

def join(request):
    if request.method == 'POST':
        form = Memberform(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            age = request.POST['age']
            email = request.POST['email']
            passwd = request.POST['passwd']

            messages.error(request, 'Given information is not valid! Check all fields.')
            return render(request, 'join.html', {fname:'fname', lname:'lname', age:'age', email:'email', passwd:'passwd'})

        messages.success(request, 'Thanks for Signing Up!')
        return redirect('home')
        
    else:
        return render(request, 'join.html', {})