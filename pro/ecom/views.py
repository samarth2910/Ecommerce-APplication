from django.shortcuts import render , HttpResponse 
from .models import Student

# Create your views here.
def first(request):
    return HttpResponse("this is my first view")

def demo(request):
    return render(request,"demo.html")

def style(request):
    return render(request,'style.html')

def show(request):
    data=Student.objects.all()
    for i in data:
        print(i.name)
    return render(request,"show.html",{"Student":data})