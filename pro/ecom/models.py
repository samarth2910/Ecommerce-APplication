from django.db import models

# Create your models here.
class Student(models.Model):
    email=models.EmailField()
    name=models.CharField()
    
# class Employee(models.Model):
#     email=models.EmailField()
#     name=models.CharField()
#     mobile_no=models.CharField()
    
    def __str__(self):
        return self.name 

class Img(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="Image")
    
    def __str__(self):
        return self.name