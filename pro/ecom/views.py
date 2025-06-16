
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Img

def first(request):
    return HttpResponse("Hello"
                        )
def demo(request):
    return render(request,"demo.html")

def style(request):
    return render(request,"style.html")

def show(request):
    Data=Student.objects.all()
    return render(request,"show.html",{"Student":Data})

def showimg(request):
    Dataimg=Img.objects.all()
    return render(request,"showimg.html",{"Dataimg":Dataimg})

def store(request):
    if request.method=="POST":
        store_data=
    return render(request,"store.html")