from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from home.models import Form
from home import models
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        desc = request.POST['desc']
        ins = Form( name=name,phone=phone,email=email,desc=desc)
        ins.save()
    return render(request, 'contact.html')