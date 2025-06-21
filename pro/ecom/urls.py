
from django.urls import path
from . import views
from .views import demo
from .views import style,first,show,showimg,store,store_get

urlpatterns = [
    path('first/',views.first,name='first'),
    path('demo/',views.demo,name="demo"),
    path('',views.style,name="style"),
    path("show/",views.show,name="show"),
    path("showimg/",views.showimg,name="showimg"),
    path("store/",views.store,name="store"),
    path("store_get/",views.store_get,name="store_get"),
]
