
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
        store_data=Student()
        store_data.name=request.POST.get("uname")
        store_data.email=request.POST.get("email")
        store_data.save()
    return render(request,"store.html")

def store_get(request):
    if request.method == "GET":
        store_data = Student()
        store_data.name = request.GET.get("uname")
        store_data.email = request.GET.get("email")
        return render(request, "store_get.html", {"store_data": store_data})
