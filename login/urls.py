from django.urls import path
from .views import userLogin

urlpatterns=[

  path("",userLogin,name="login")   


]