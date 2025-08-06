from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from datetime import datetime
from myapp.models import Contact
# Create your views here.
def homepage(request):
    data={
        'title' : 'home page',
        'coursename':['php','java','python'],
    }
    return render(request,"index.html",data)
def about(request):
     return render(request,"about.html")
def services(request):
     return render(request,"services.html")
def contact(request):
     if request.method =="POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          city=request.POST.get('city')
          state=request.POST.get('state')
          co= Contact(name=name,email=email,phone=phone,city=city,state=state,date=datetime.today())
          co.save()
     return render(request,"contact.html")