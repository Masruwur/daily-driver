from django.urls import path
from .views import show,addStudent

urlpatterns=[

path("<str:encname>",show,name="current"),
path("<str:encname>/update",addStudent)

]