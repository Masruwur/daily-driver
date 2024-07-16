from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Student
import datetime
from django.contrib.auth.models import User
#custom module
from .tools import decrypt,tuitionToday,encrypt,decString


def show(request,encname):
    username = decString(encname)
    currUser = User.objects.get(username=username)
    

    students = currUser.student_set.all()
        
    today = datetime.date.today().isoweekday()
    todayClass = []
    for student in students:
        if tuitionToday(student.dayBin,today):
            todayClass.append(student)

    
    
    if request.method=="POST":

       for student in students:
           if request.POST.get(student.name)=="add":
               student.days = (student.days + 1)%12;
               student.save()
               return redirect("current")
           
            


    return render(request,"tuition/table.html",{"students":students,
                                                "todayClass":todayClass,
                                                "current":encname})

def addStudent(request,encname):
    enc = encname
    username = decString(enc)

    if request.method=="POST":
       if request.POST.get("register")=="register":
           name = request.POST.get("name")
           fees = request.POST.get("fees")
           days=[]
           for i in range(7):
               curr = request.POST.get(str(i))
               if curr=="on":
                   days.append(1)
               else:
                   days.append(0)
               

           dayBin = encrypt(days)

           teacher = User.objects.get(username=username)

           new = Student(name=name,fees=fees,dayBin=dayBin,teacher=teacher)
           new.save()

           messages.success(request,f"Student {name} has been registered.")
           return redirect("/tuition/"+encname+"/update")




    return render(request,"tuition/update.html",{"current":encname})

    
