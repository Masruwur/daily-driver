from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    fees = models.IntegerField()
    days = models.IntegerField(default=0)
    stat = models.BooleanField(default=False)
    dayBin = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name
    



    
