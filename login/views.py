from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from tuition.tools import encString

def userLogin(request):
     
     if request.method=="POST":
        name = request.POST.get("name")
        password = request.POST.get("pass")

        currUser = authenticate(username=name,password=password) 

        if currUser is not None:
            login(request,currUser)

            return redirect("/tuition/"+encString(currUser.username))
        else:
            messages.error(request,"Invalid user")






     return render(request,'login/login.html')


