from django.shortcuts import render
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
        return render(request, 'join.html', {})
        
    else:
        return render(request, 'join.html', {})