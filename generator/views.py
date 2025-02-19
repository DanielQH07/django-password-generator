from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'abc'})

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    #12 is default length
    length = int(request.GET.get('length',12))
    #check if user wants uppercase
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    #check if user wants numbers
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    #check if user wants special characters
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    thepassword = ''
    for _ in range(length):
        thepassword += random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})
def about(request):
    return render(request,'generator/about.html')




