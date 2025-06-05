
from django.urls import path
from . import views
from .views import demo
from .views import style,first,show

urlpatterns = [
    path('first/',views.first,name='first'),
    path('demo/',views.demo,name="demo"),
    path('',views.style,name="style"),
    path("show/",views.show,name="show")
]