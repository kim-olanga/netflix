from django.shortcuts import render
from . import views

# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')