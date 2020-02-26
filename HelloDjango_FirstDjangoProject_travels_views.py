from django.shortcuts import render,redirect
from .models import Destination
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    if  request.user.is_authenticated:
        dests = Destination.objects.all()    
        isauth = User.is_authenticated
        return render(request,'index.html' ,{'dests':dests,'isauth':isauth})
    else:        
        return redirect('login')


def about(request):
    if  request.user.is_authenticated:
        return render(request,'about.html')
    else:
        return redirect('login')
