import string

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from autentification import template
from autentification.models import MyCr


# Create your views here.
def home(request):
    return render(request,"index.html")
def registrepage(request):
    return render(request, 'registration.html')

def logpage(request):
    return render(request,'lohin.html')

def registration(request):

    if request.method=='POST':
          name=request.POST.get('tbName')
          email=request.POST.get('tbEmail')
          mobile=request.POST.get('tbTel')
          password=request.POST.get('tbPass')
          new_instace=MyCr(name=name,email=email,mobile=mobile,password=password)
          new_instace.save()

    return render(request,'lohin.html')


def login(request):
    if request.method=='POST':
        email=request.POST['tbEmail']
        password=request.POST['tbPass']
        matchdata=MyCr.objects.filter(email=email,password=password)
        if matchdata.exists():
            return render(request,"succes.html")
        else:
            messages.error(request,'Ivalid details please enter details carefully')
            return render(request,'lohin.html')
