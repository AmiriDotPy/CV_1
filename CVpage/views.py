from django.shortcuts import render
from .models import *

About.Name = 'Mohyaldin'
About.LastName = 'Amiri'
About.Age = 28
About.Email = 'amiridotpy@gmail.com'
About.PhoneNumber = '0937-253-0857'
About.Address = 'Ardabil'

def Load_Index(request):
   
    all = {
        'name' : About.Name ,
        'lastname' : About.LastName,
        'age' : About.Age,
        'email' : About.Email,
        'phone' : About.PhoneNumber,
        'address' : About.Address,
    }
    return render(request , 'cvcontent/index.html' , {'all' : all})