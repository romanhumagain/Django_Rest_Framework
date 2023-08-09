from django.urls import path , include
from APItest. views import *
from rest_framework.routers import DefaultRouter
from APItest.routers import *

urlpatterns =[
  path('routers/',include(routers.urls)),
  path('index/' , IndexView.as_view() , name="index"),
  path('person_view/' , PersonView.as_view() , name="person_view"),
  path('register_user/' , RegisterUser.as_view() , name="register_user"),
  path('login_user/' , LoginUser.as_view() , name="login_user"), 
]
