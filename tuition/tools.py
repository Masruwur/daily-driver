import datetime
from cryptography.fernet import Fernet

def decrypt(daysBin):
    days=[]
    for i in range(7):
        temp = (daysBin>>i)&1;
        if temp:
            days.append(6-i)
    
    return days

def encrypt(days):
    dayBin=0;
    for i in range(7):
        temp = days[i]<<6-i
        dayBin = dayBin|temp

    return dayBin

    
def tuitionToday(dayBin,day):
    days=decrypt(dayBin)
    if (day%7) in days:
        return True
    else:
        return False  
    
def encData(key,name):
    fernet = Fernet(key)
    enc = fernet.encrypt(name.encode())

    return (enc)

def decData(key,enc):
   # x = bytes(enc,'utf-8')
    fernet = Fernet(key)
    dec = fernet.decrypt(enc).decode()

    return dec 


def encString(username):
    enc=''
    for i in range(len(username)):
        enc += chr(ord(username[i])+1)

    return enc[::-1]
    #username.reverse

def decString(enc):
    dec=''
    i=len(enc)-1
    while i>=0:
       dec += chr(ord(enc[i])-1)
       i = i-1;

    return dec