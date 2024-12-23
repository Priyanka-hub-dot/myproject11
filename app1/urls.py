from django.urls import path
from .views import *
app_name='app1'
urlpatterns=[
    path('',sheryians,name='sheryians'),
    path('home/',home,name='home'),
    path('courses/',courses,name='courses'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('request_callback/',request_callback,name='request_callback'),
    path('signin/',signin,name='signin'),
    path('email/',email,name='email'),

    

]
