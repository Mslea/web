from django.shortcuts import render, HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import decorators
    # User is authenticated
# Create your views here.
def index(request):
    return render(request,'pages/home.html')
@decorators.login_required(login_url = '/home/login/')
def contact(request):
    return render(request,'pages/contact.html')

def register(request):
    form = RegistrationForm()
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    return render(request,'pages/register.html',{'form':form})
