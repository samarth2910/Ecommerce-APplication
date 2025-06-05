from django.contrib import admin
from .models import Student
from .models import Img
# Register your models here.


class student_(admin.ModelAdmin):
    list_display=["id","name","email"]
    
class img_(admin.ModelAdmin):
    list_display=["name","img"]


admin.site.register(Student,student_)

admin.site.register(Img,img_)