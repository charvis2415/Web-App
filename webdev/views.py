from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *





def hi(request):
    return render(request,'webdev/hi.html')



def signup(request):
    form = UserCreationForm()


    if request.method =='post':
        form = UserCreationForm(request.post)
        if form.is_valid():
            form.save()


    context = {'form': form}
    return render(request, 'webdev/signup.html',context)


